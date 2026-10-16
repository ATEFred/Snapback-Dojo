#!/usr/bin/env python3
"""Snap Back Dojo — tiny stdlib server.

Serves the app, proxies the private AI (chat / TTS / STT) so the browser
never deals with CORS, caches taunt audio, and stores progress + custom
scenarios in snapback-data.json.

Run:  python3 server.py [port]        (default 8081)
Env:  HALO_BASE        default http://halo-server:8080
      HALO_CHAT_MODEL  default "Qwen3.8 Flash Next"
      HALO_TTS_MODEL   default "qwen3-tts"
      HALO_ASR_MODEL   default "qwen3-asr"
"""
import json
import os
import sys
import threading
import time
import urllib.error
import urllib.request
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIO_DIR = HERE / "audio"
DATA_FILE = HERE / "snapback-data.json"
UPSTREAM = os.environ.get("HALO_BASE", "http://halo-server:8080").rstrip("/")
CHAT_MODEL = os.environ.get("HALO_CHAT_MODEL", "Qwen3.8 Flash Next")
TTS_MODEL = os.environ.get("HALO_TTS_MODEL", "qwen3-tts")
ASR_MODEL = os.environ.get("HALO_ASR_MODEL", "qwen3-asr")

_data_lock = threading.Lock()
_cap_lock = threading.Lock()
_cap_cache = {"t": 0.0, "caps": {"chat": False, "tts": False, "stt": False}}


def _http(url, data=None, headers=None, method=None, timeout=90):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read(), dict(resp.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read(), dict(e.headers)
    except Exception:
        return 0, b"", {}


def capabilities():
    with _cap_lock:
        if time.time() - _cap_cache["t"] < 30:
            return _cap_cache["caps"]
        caps = {"chat": False, "tts": False, "stt": False}
        status, body, _ = _http(UPSTREAM + "/v1/models", timeout=5)
        caps["chat"] = status == 200
        # Unconfigured audio routes answer with a "not configured" error body.
        status, body, _ = _http(UPSTREAM + "/v1/audio/speech", timeout=5)
        caps["tts"] = status not in (0,) and b"not configured" not in body and status != 404
        status, body, _ = _http(UPSTREAM + "/v1/audio/transcriptions", timeout=5)
        caps["stt"] = status not in (0,) and b"not configured" not in body and status != 404
        _cap_cache.update(t=time.time(), caps=caps)
        return caps


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(HERE), **kwargs)

    # ---------------- helpers ----------------
    def log_message(self, fmt, *args):
        if not self.path.startswith("/api/"):
            super().log_message(fmt, *args)

    def _send(self, code, body, ctype="application/json"):
        if isinstance(body, str):
            body = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(n) if n else b""

    # ---------------- GET ----------------
    def do_GET(self):
        if self.path.startswith("/api/capabilities"):
            if "refresh" in self.path:
                _cap_cache["t"] = 0
            return self._send(200, json.dumps(capabilities()))
        if self.path == "/api/data":
            with _data_lock:
                if DATA_FILE.exists():
                    return self._send(200, DATA_FILE.read_bytes())
                return self._send(200, "{}")
        if self.path.startswith("/api/tts/audio/"):
            key = self.path.rsplit("/", 1)[-1]
            for ext in ("wav", "mp3", "ogg", "opus", "m4a"):
                f = AUDIO_DIR / f"{key}.{ext}"
                if f.exists():
                    ctype = {"wav": "audio/wav", "mp3": "audio/mpeg",
                             "ogg": "audio/ogg", "opus": "audio/ogg",
                             "m4a": "audio/mp4"}[ext]
                    return self._send(200, f.read_bytes(), ctype)
            return self._send(404, json.dumps({"error": "not cached"}))
        return super().do_GET()

    # ---------------- POST ----------------
    def do_POST(self):
        if self.path == "/api/chat":
            return self._proxy_chat()
        if self.path == "/api/tts":
            return self._proxy_tts()
        if self.path == "/api/stt":
            return self._proxy_raw(UPSTREAM + "/v1/audio/transcriptions")
        return self._send(404, json.dumps({"error": "no route"}))

    def do_PUT(self):
        if self.path == "/api/data":
            raw = self._body()
            try:
                obj = json.loads(raw or b"{}")
            except Exception:
                return self._send(400, json.dumps({"error": "bad json"}))
            with _data_lock:
                if DATA_FILE.exists():
                    DATA_FILE.with_suffix(".json.bak").write_bytes(DATA_FILE.read_bytes())
                tmp = DATA_FILE.with_suffix(".json.tmp")
                tmp.write_bytes(json.dumps(obj).encode())
                os.replace(tmp, DATA_FILE)
            return self._send(200, json.dumps({"ok": True}))
        return self._send(404, json.dumps({"error": "no route"}))

    # ---------------- proxies ----------------
    def _proxy_chat(self):
        try:
            payload = json.loads(self._body() or b"{}")
        except Exception:
            return self._send(400, json.dumps({"error": "bad json"}))
        payload.setdefault("model", CHAT_MODEL)
        payload.setdefault("thinking", {"type": "disabled"})
        payload["stream"] = False
        status, body, _ = _http(UPSTREAM + "/v1/chat/completions",
                                data=json.dumps(payload).encode(),
                                headers={"Content-Type": "application/json"})
        return self._send(status or 502, body)

    def _proxy_tts(self):
        try:
            payload = json.loads(self._body() or b"{}")
        except Exception:
            return self._send(400, json.dumps({"error": "bad json"}))
        text = payload.get("text", "")
        voice = payload.get("voice", "default")
        if not text:
            return self._send(400, json.dumps({"error": "no text"}))
        AUDIO_DIR.mkdir(exist_ok=True)
        key = hashlib.sha1(f"{voice}|{text}".encode()).hexdigest()
        for ext in ("wav", "mp3", "ogg", "opus", "m4a"):
            if (AUDIO_DIR / f"{key}.{ext}").exists():
                return self._send(200, json.dumps({"cached": True, "key": key}))
        up = {"model": payload.get("model", TTS_MODEL), "input": text,
              "voice": voice, "response_format": "wav"}
        status, body, _ = _http(UPSTREAM + "/v1/audio/speech",
                                data=json.dumps(up).encode(),
                                headers={"Content-Type": "application/json"},
                                timeout=60)
        if status != 200 or not body:
            return self._send(503, body or json.dumps({"error": "tts unavailable"}))
        (AUDIO_DIR / f"{key}.wav").write_bytes(body)
        return self._send(200, json.dumps({"cached": True, "key": key}))

    def _proxy_raw(self, url):
        raw = self._body()
        ctype = self.headers.get("Content-Type", "application/octet-stream")
        status, body, hdrs = _http(url, data=raw, headers={"Content-Type": ctype})
        if status == 0:
            return self._send(502, json.dumps({"error": "upstream unreachable"}))
        return self._send(status, body)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get("PORT", 8081))
    srv = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"Snap Back Dojo on http://0.0.0.0:{port}  (AI: {UPSTREAM})")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
