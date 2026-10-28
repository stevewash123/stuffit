"""Local receiver for StuffIt Page Saver. Run:  python receiver.py [folder]
Writes each page to <folder>/<host>/pagesource/<timestamp>_<title>.html and each PDF to <folder>/<host>/<name>.pdf. Listens on 127.0.0.1 only."""
import json, re, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / "OfficialDocs")
safe = lambda s: re.sub(r"[^A-Za-z0-9._-]+", "_", str(s or "")).strip("_")[:120] or "page"

class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type, x-host, x-name")

    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()

    def do_POST(self):
        if self.path not in ("/save", "/save-file"):
            self.send_response(404); self.end_headers(); return
        try:
            raw = self.rfile.read(int(self.headers.get("content-length", 0)))
            if self.path == "/save-file":   # a PDF: skip if the same file is already there
                folder = ROOT / safe(self.headers.get("x-host"))
                folder.mkdir(parents=True, exist_ok=True)
                fp = folder / (safe(self.headers.get("x-name")).removesuffix(".pdf") + ".pdf")
                if not (fp.exists() and fp.stat().st_size == len(raw)):
                    fp.write_bytes(raw)
            else:
                body = json.loads(raw)
                folder = ROOT / safe(body.get("host")) / "pagesource"   # scratch: whole pages to be read later
                folder.mkdir(parents=True, exist_ok=True)
                fp = folder / (safe(body.get("name")).removesuffix(".html") + ".html")
                fp.write_text(body.get("html", ""), encoding="utf-8")
            out, code = {"path": str(fp), "bytes": fp.stat().st_size}, 200
            print("saved", fp)
        except Exception as e:
            out, code = {"error": str(e)}, 400
        self.send_response(code); self._cors()
        self.send_header("content-type", "application/json"); self.end_headers()
        self.wfile.write(json.dumps(out).encode())

if __name__ == "__main__":
    ROOT.mkdir(parents=True, exist_ok=True)
    print("Saving to", ROOT, "- listening on http://127.0.0.1:8765")
    HTTPServer(("127.0.0.1", 8765), H).serve_forever()
