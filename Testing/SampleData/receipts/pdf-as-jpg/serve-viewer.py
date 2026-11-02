"""Serves this folder (key-viewer.html, the JPGs, the CSV) and forwards /api/... to the running StuffIt API, so the viewer's TEST THIS button
works without any change to the API (no CORS, one origin).

    python serve-viewer.py                      -> http://localhost:8765/key-viewer.html  (API at http://localhost:5259)
    python serve-viewer.py --port 8800 --api http://localhost:5259 --email someone@example.com
    python serve-viewer.py --no-login           -> no saved sign-in; the viewer asks in the browser instead

It starts listening at once, then asks for the app login of the test user (email defaults to stevewash123.test@gmail.com; the password is typed hidden, or taken from the
STUFFIT_PASSWORD environment variable). The login is kept only in this process's memory. The server signs in to the API on the first call that needs
it and adds the token to the viewer's /api requests, so nothing about the login ever reaches the browser. Anyone who can reach this port can act as
that user: it listens on 127.0.0.1 only, and a VS Code forwarded port is private to you by default. Use a test account.

Start the API first or at the same time (see HANDOFF.md: dotnet run --project src/StuffIt.Api --urls http://localhost:5259).
"""
import argparse, getpass, http.server, json, os, shutil, socketserver, subprocess, sys, threading, time, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
HOP = {'connection', 'keep-alive', 'proxy-authenticate', 'proxy-authorization', 'te', 'trailers', 'transfer-encoding', 'upgrade', 'host', 'content-length'}
DEFAULT_EMAIL = 'stevewash123.test@gmail.com'


class Session:
    """The saved sign-in. enabled is true when a password was given; the token is fetched lazily because the API may still be starting."""
    def __init__(self):
        self.email = ''; self.password = ''; self.token = None; self.error = None; self.lock = threading.Lock()

    @property
    def enabled(self): return bool(self.email and self.password)

    def login(self, api):
        with self.lock:
            try:
                req = urllib.request.Request(api + '/api/auth/login', data=json.dumps({'email': self.email, 'password': self.password}).encode(),
                                             headers={'Content-Type': 'application/json'}, method='POST')
                with urllib.request.urlopen(req, timeout=60) as r:
                    self.token = json.loads(r.read())['accessToken']; self.error = None
            except urllib.error.HTTPError as e:
                self.token = None
                self.error = 'The API refused the saved login (wrong password or no such account). Stop this server and start it again to retype it.' if e.code == 401 else f'The API answered {e.code} to the login.'
            except Exception as e:
                self.token = None; self.error = f'The API did not answer the login: {e}'
            return self.token


SESSION = Session()


class Handler(http.server.SimpleHTTPRequestHandler):
    api = 'http://localhost:5259'

    def __init__(self, *a, **kw):
        super().__init__(*a, directory=HERE, **kw)

    def _send(self, status, body, ctype='text/plain'):
        self.send_response(status); self.send_header('Content-Type', ctype); self.send_header('Content-Length', str(len(body))); self.end_headers()
        if self.command != 'HEAD': self.wfile.write(body)

    def _forward(self, body, token):
        req = urllib.request.Request(self.api + self.path, data=body, method=self.command)
        for k, v in self.headers.items():
            if k.lower() not in HOP and not (token and k.lower() == 'authorization'): req.add_header(k, v)
        if token: req.add_header('Authorization', 'Bearer ' + token)
        try:
            return urllib.request.urlopen(req, timeout=300)
        except urllib.error.HTTPError as e:
            return e

    def _proxy(self):
        body = self.rfile.read(int(self.headers.get('Content-Length') or 0)) if self.command in ('POST', 'PUT', 'PATCH', 'DELETE') else None
        # the saved sign-in is added only to calls that carry no token of their own (never to /api/auth/*)
        inject = SESSION.enabled and 'authorization' not in {k.lower() for k in self.headers.keys()} and not self.path.startswith('/api/auth/')
        try:
            token = (SESSION.token or SESSION.login(self.api)) if inject else None
            if inject and not token:
                return self._send(401, (SESSION.error or 'No saved sign-in.').encode())
            resp = self._forward(body, token)
            if inject and getattr(resp, 'code', 200) == 401:   # token expired: sign in again once
                token = SESSION.login(self.api)
                if token: resp = self._forward(body, token)
        except Exception as e:  # API not running, refused, timed out
            return self._send(502, f'The API at {self.api} did not answer: {e}'.encode())
        data = resp.read()
        self.send_response(getattr(resp, 'status', None) or resp.code)
        for k, v in resp.headers.items():
            if k.lower() not in HOP: self.send_header(k, v)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        if self.command != 'HEAD': self.wfile.write(data)

    def _is_api(self): return self.path.startswith('/api/')

    def do_GET(self):
        if self.path.startswith('/viewer/issues'):
            from urllib.parse import parse_qs, urlparse
            return self._json(200, {'issues': self._issues_for((parse_qs(urlparse(self.path).query).get('file') or [''])[0])})
        if self.path == '/viewer/status':
            path = os.path.join(HERE, 'review-status.json')
            try:
                with open(path, encoding='utf-8') as f: return self._json(200, json.load(f))
            except FileNotFoundError: return self._json(200, {})
            except ValueError: return self._json(500, {'error': 'review-status.json is not valid JSON'})
        if self.path == '/viewer/session':
            return self._send(200, json.dumps({'enabled': SESSION.enabled, 'email': SESSION.email if SESSION.enabled else None, 'error': SESSION.error}).encode(), 'application/json')
        self._proxy() if self._is_api() else super().do_GET()

    def do_HEAD(self): self._proxy() if self._is_api() else super().do_HEAD()
    def _json(self, status, obj): self._send(status, json.dumps(obj).encode(), 'application/json')

    def _issues_for(self, file):
        """The notes in issues.md about one receipt, oldest first. Each entry starts with '### <file> · line <n> · <time>'; the comment is the '> ' lines."""
        path = os.path.join(HERE, 'issues.md')
        if not os.path.exists(path): return []
        found, cur = [], None
        with open(path, encoding='utf-8') as f:
            for raw in f:
                line = raw.rstrip('\r\n')
                if line.startswith('### '):
                    parts = line[4:].split(' \u00b7 ')
                    cur = {'file': parts[0].strip(), 'line_no': parts[1].replace('line', '').strip() if len(parts) > 1 else '', 'time': parts[2].strip() if len(parts) > 2 else '', 'comment': '', 'test': ''}
                    found.append(cur)
                elif cur is not None:
                    if line.startswith('> '): cur['comment'] += ('\n' if cur['comment'] else '') + line[2:]
                    elif line == '>': cur['comment'] += '\n'
                    elif line.startswith('Test: '): cur['test'] = line[6:]
        return [e for e in found if e['file'] == file]

    def _add_issue(self):
        """Appends one comment to issues.md (created on first use). The comment is written as '> ' lines so nothing in it can be mistaken for an entry heading."""
        n = int(self.headers.get('Content-Length') or 0)
        if n <= 0 or n > 200_000: return self._json(400, {'error': 'The body is empty or too large.'})
        try: d = json.loads(self.rfile.read(n).decode('utf-8'))
        except ValueError: return self._json(400, {'error': 'Not valid JSON.'})
        one = lambda s: ' '.join(str(s or '').split())
        file, comment = one(d.get('file')), str(d.get('comment') or '').strip()
        if not file.lower().endswith('.jpg') or '/' in file or '\\' in file: return self._json(400, {'error': 'That is not a receipt file name.'})
        if not comment or len(comment) > 5000: return self._json(400, {'error': 'The comment is empty or longer than 5000 characters.'})
        entry = f"\n### {file} \u00b7 line {one(d.get('line_no')) or '?'} \u00b7 {time.strftime('%Y-%m-%d %H:%M')}\n"
        if one(d.get('line')): entry += f"Line: {one(d.get('line'))[:200]}\n"
        entry += '\n' + '\n'.join(('> ' + l) if l.strip() else '>' for l in comment.splitlines()) + '\n'
        if one(d.get('test')): entry += f"\nTest: {one(d.get('test'))[:3000]}\n"
        path = os.path.join(HERE, 'issues.md')
        try:
            new = not os.path.exists(path)
            with open(path, 'a', encoding='utf-8', newline='\n') as f:
                if new: f.write('# Answer key issues\n\nOne entry per comment, added from the viewer (Note issue). Newest last.\n')
                f.write(entry)
        except OSError as e:
            return self._json(500, {'error': str(e)})
        self._json(200, {'ok': True, 'count': len(self._issues_for(file))})

    def _save_status(self):
        """Keeps which receipts passed, failed or need a retest: the whole map, written atomically so a crash never leaves half a file."""
        n = int(self.headers.get('Content-Length') or 0)
        try: data = json.loads(self.rfile.read(n) or b'{}')
        except ValueError: return self._json(400, {'error': 'That was not JSON.'})
        if not isinstance(data, dict): return self._json(400, {'error': 'Expected an object of receipt statuses.'})
        path = os.path.join(HERE, 'review-status.json'); tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f: json.dump(data, f, indent=1, sort_keys=True)
        os.replace(tmp, path)
        return self._json(200, {'saved': len(data)})

    def _save_key(self):
        """Writes the edited answer key back to answer-key-by-item.csv (the previous file is kept as .bak), then refreshes truth.draft.json."""
        n = int(self.headers.get('Content-Length') or 0)
        if n <= 0 or n > 20_000_000: return self._json(400, {'error': 'The body is empty or too large.'})
        text = self.rfile.read(n).decode('utf-8')
        path = os.path.join(HERE, 'answer-key-by-item.csv')
        try:
            with open(path, encoding='utf-8-sig') as f: current = f.readline().strip()
        except OSError:
            current = None
        first = (text.lstrip('﻿').splitlines() or [''])[0].strip()
        if current is not None and first != current:
            return self._json(400, {'error': 'The header row differs from the file on disk; nothing was written.'})
        tmp = path + '.tmp'
        try:
            if os.path.exists(path): shutil.copyfile(path, path + '.bak')
            with open(tmp, 'w', encoding='utf-8-sig', newline='') as f: f.write(text)
            os.replace(tmp, path)
        except PermissionError:
            try: os.remove(tmp)
            except OSError: pass
            return self._json(409, {'error': 'The CSV is locked, probably open in Excel. Close it there, then save again.'})
        except OSError as e:
            return self._json(500, {'error': str(e)})
        draft = 'regenerated'
        try:
            r = subprocess.run([sys.executable, '-I', os.path.join(HERE, 'make-truth.py')], cwd=HERE, capture_output=True, text=True, timeout=60)
            if r.returncode != 0: draft = 'truth.draft.json not refreshed: ' + (r.stderr.strip().splitlines() or ['error'])[-1]
        except Exception as e:
            draft = f'truth.draft.json not refreshed: {e}'
        self._json(200, {'ok': True, 'draft': draft})

    def do_POST(self):
        if self.path == '/viewer/save-key': return self._save_key()
        if self.path == '/viewer/issue': return self._add_issue()
        if self.path == '/viewer/status': return self._save_status()
        self._proxy() if self._is_api() else self.send_error(404)
    def do_PUT(self): self._proxy() if self._is_api() else self.send_error(404)
    def do_PATCH(self): self._proxy() if self._is_api() else self.send_error(404)
    def do_DELETE(self): self._proxy() if self._is_api() else self.send_error(404)

    def log_message(self, fmt, *args):
        if self._is_api(): sys.stderr.write('api  ' + fmt % args + '\n')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--port', type=int, default=8765)
    ap.add_argument('--api', default='http://localhost:5259')
    ap.add_argument('--email', default=DEFAULT_EMAIL, help='the test user to sign in as')
    ap.add_argument('--no-login', action='store_true', help='do not save a sign-in; the viewer asks in the browser')
    a = ap.parse_args()
    Handler.api = a.api.rstrip('/')
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(('127.0.0.1', a.port), Handler)
    # Listen FIRST, so the page loads even while the password prompt is waiting; the login is saved as soon as it is typed.
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    print(f'Viewer: http://localhost:{a.port}/key-viewer.html   (API {Handler.api})   Ctrl+C to stop', flush=True)
    if not a.no_login:
        env_pw = os.environ.get('STUFFIT_PASSWORD')
        try:
            if env_pw:   # non-interactive: no prompts
                SESSION.email, SESSION.password = os.environ.get('STUFFIT_EMAIL') or a.email, env_pw
            else:
                email = input(f'App login email [{a.email}]: ').strip() or a.email
                password = getpass.getpass(f'Password for {email} (hidden; blank = ask in the browser instead): ')
                if password: SESSION.email, SESSION.password = email, password
        except (EOFError, KeyboardInterrupt):
            pass
    print(f'Signed in as: {SESSION.email or "nobody (the browser will ask)"}', flush=True)
    try:
        while True: time.sleep(3600)
    except KeyboardInterrupt:
        srv.shutdown()
