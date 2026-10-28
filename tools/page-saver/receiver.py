"""Local receiver for StuffIt Page Saver. Run:  python receiver.py [folder]
Writes each page to <folder>/<host>/pagesource/<timestamp>_<title>.html and each PDF or Word file to <folder>/<host>/<name>. Listens on 127.0.0.1 only."""
import json, os, re, sys, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / "OfficialDocs")
JOBS = {}   # host folder -> {"state": running|done|error, "log": [...], "result": {...}}
safe = lambda s: re.sub(r"[^A-Za-z0-9._-]+", "_", str(s or "")).strip("_")[:120] or "page"

class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type, x-host, x-name, x-url")

    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()

    def do_GET(self):
        u = urlparse(self.path)
        if u.path != "/process-status":
            self.send_response(404); self.end_headers(); return
        job = JOBS.get(safe(parse_qs(u.query).get("host", [""])[0]))
        self.send_response(200); self._cors()
        self.send_header("content-type", "application/json"); self.end_headers()
        self.wfile.write(json.dumps(job or {"state": "none"}).encode())

    def do_POST(self):
        if self.path == "/process":
            return self._process()
        if self.path not in ("/save", "/save-file"):
            self.send_response(404); self.end_headers(); return
        try:
            raw = self.rfile.read(int(self.headers.get("content-length", 0)))
            if self.path == "/save-file":   # a PDF or Word file: skip if the same file is already there
                folder = ROOT / safe(self.headers.get("x-host"))
                folder.mkdir(parents=True, exist_ok=True)
                fp = folder / safe(self.headers.get("x-name"))
                if fp.suffix.lower() not in (".pdf", ".doc", ".docx", ".rtf"):
                    fp = fp.with_name(fp.name + ".pdf")
                if not (fp.exists() and fp.stat().st_size == len(raw)):
                    fp.write_bytes(raw)
                src = self.headers.get("x-url")
                if src:   # where the file came from: the evidence for anything read out of it
                    from urllib.parse import unquote
                    fp.with_name(fp.name + ".source.txt").write_text(unquote(src) + chr(10), encoding="utf-8")
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

def _run_job(site: Path, host: str):
    job = JOBS[host]
    try:
        import analyze_pages as ap
        key = os.environ.get("ANTHROPIC_API_KEY", "")
        if not key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set where the receiver runs. Set it, then restart the receiver.")
        ap.analyze_site(site, ap.DEFAULT_MODEL, key, log=job["log"].append)
        job["result"] = ap.candidates(site)
        job["state"] = "done"
    except Exception as e:
        job["log"].append(str(e)); job["state"] = "error"


def _process(self):
    try:
        host = safe(json.loads(self.rfile.read(int(self.headers.get("content-length", 0)))).get("host"))
        site = ROOT / host
        if not site.is_dir():
            raise RuntimeError(f"Nothing saved for {host} yet: save its pages first.")
        if JOBS.get(host, {}).get("state") != "running":
            JOBS[host] = {"state": "running", "log": [], "result": None, "started": time.time()}
            threading.Thread(target=_run_job, args=(site, host), daemon=True).start()
        out, code = {"state": "running"}, 200
    except Exception as e:
        out, code = {"error": str(e)}, 400
    self.send_response(code); self._cors()
    self.send_header("content-type", "application/json"); self.end_headers()
    self.wfile.write(json.dumps(out).encode())


H._process = _process

if __name__ == "__main__":
    try:
        ROOT.mkdir(parents=True, exist_ok=True)
        probe = ROOT / ".write-test"
        probe.write_text("ok"); probe.unlink()
    except OSError as e:
        sys.exit(f"Cannot write to {ROOT}: {e}" + chr(10) + "If it is a shared folder, open it in Explorer first so Windows asks for the sign-in.")
    print("Saving to", ROOT, "- listening on http://127.0.0.1:8791")
    ThreadingHTTPServer(("127.0.0.1", 8791), H).serve_forever()
