from __future__ import annotations

import html
import json
from pathlib import Path
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

from .trial import ReleaseCandidateTrial
from .witness import verify_export


CSS = """
:root { font-family: system-ui, sans-serif; line-height: 1.55; }
body { max-width: 74rem; margin: 0 auto; padding: 1rem; }
a { text-decoration-thickness: .12em; text-underline-offset: .18em; }
.skip-link { position: absolute; left: -9999px; }
.skip-link:focus { left: 1rem; top: 1rem; background: Canvas; color: CanvasText; padding: .75rem; border: 2px solid; }
nav ul { display: flex; gap: 1rem; flex-wrap: wrap; padding-left: 1.25rem; }
section, fieldset { border: 1px solid; padding: 1rem; margin: 1rem 0; }
button { font: inherit; padding: .65rem 1rem; min-height: 2.75rem; }
pre { white-space: pre-wrap; overflow-wrap: anywhere; border: 1px solid; padding: 1rem; }
.status { border-left: .4rem solid; padding-left: 1rem; }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { scroll-behavior: auto !important; transition: none !important; animation: none !important; } }
@media (forced-colors: active) { button, section, fieldset, pre { border: 1px solid ButtonText; } }
"""


class PilotWebApp:
    def __init__(self, workdir: Path, schema_dir: Path):
        self.workdir = Path(workdir)
        self.schema_dir = Path(schema_dir)
        self.pilot = ReleaseCandidateTrial(self.workdir, self.schema_dir)

    def _json(self, start_response, payload, status="200 OK"):
        body = json.dumps(payload, indent=2, default=str).encode("utf-8")
        start_response(status, [("Content-Type","application/json; charset=utf-8"),("Content-Length",str(len(body)))])
        return [body]

    def _redirect(self, start_response, location="/"):
        start_response("303 See Other", [("Location",location),("Content-Length","0")])
        return [b""]

    def _page(self) -> bytes:
        status = self.pilot.status()
        safe = html.escape(json.dumps(status, indent=2, default=str))
        return f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Telic Fields J.2 Release Candidate Trial</title><style>{CSS}</style></head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<header><h1>Telic Fields J.2</h1><p>Authenticated multi-party trial and release-candidate readiness.</p></header>
<nav aria-label="Pilot navigation"><ul><li><a href="#controls">Controls</a></li><li><a href="#status">Status</a></li><li><a href="/accessibility">Accessibility</a></li><li><a href="/api/status">JSON status</a></li></ul></nav>
<main id="main">
<section id="controls" aria-labelledby="controls-heading"><h2 id="controls-heading">Pilot controls</h2>
<p>Each control is keyboard-operable and works without JavaScript.</p>
<form method="post" action="/step/full"><button type="submit">Run full multi-party trial</button></form>
<form method="post" action="/step/seed"><button type="submit">Seed records only</button></form>
<form method="post" action="/step/correct"><button type="submit">Apply two participant corrections and policy migration</button></form>
<form method="post" action="/step/retire"><button type="submit">Retire pilot and revoke tool authority</button></form>
</section>
<section id="status" aria-labelledby="status-heading"><h2 id="status-heading">Current status</h2><div class="status" role="status" aria-live="polite"><pre>{safe}</pre></div></section>
<section aria-labelledby="privacy-heading"><h2 id="privacy-heading">Runtime data choices</h2><dl><dt>Service use</dt><dd>Allowed</dd><dt>Cross-session memory</dt><dd>Denied</dd><dt>Evaluation use</dt><dd>Denied</dd><dt>Training reuse</dt><dd>Denied</dd></dl></section>
</main>
<footer><p>Reference pilot only. No production personal data.</p></footer>
</body></html>""".encode("utf-8")

    def __call__(self, environ, start_response):
        method = environ.get("REQUEST_METHOD", "GET")
        path = environ.get("PATH_INFO", "/")
        if path == "/" and method == "GET":
            body = self._page()
            start_response("200 OK", [("Content-Type","text/html; charset=utf-8"),("Content-Length",str(len(body)))])
            return [body]
        if path == "/accessibility" and method == "GET":
            body = ("<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Accessibility</title></head>"
                    "<body><main><h1>Accessibility statement</h1><p>The pilot supports keyboard operation, semantic headings, visible focus, reduced-motion preferences, forced-colors mode, plain-language status, and non-JavaScript controls.</p><p><a href='/'>Return to pilot</a></p></main></body></html>").encode()
            start_response("200 OK", [("Content-Type","text/html; charset=utf-8"),("Content-Length",str(len(body)))])
            return [body]
        if path == "/api/status" and method == "GET":
            return self._json(start_response, self.pilot.status())
        if path == "/api/objects" and method == "GET":
            return self._json(start_response, self.pilot.store.list_objects())
        if path == "/step/seed" and method == "POST":
            self.pilot.seed(); return self._redirect(start_response)
        if path == "/step/correct" and method == "POST":
            self.pilot.apply_multi_party_corrections(); self.pilot.migrate_policy_with_rollback(); return self._redirect(start_response)
        if path == "/step/retire" and method == "POST":
            self.pilot.retire(); return self._redirect(start_response)
        if path == "/step/full" and method == "POST":
            self.pilot.run_full(self.workdir / "tf-mvi-1-j2-witness.zip"); return self._redirect(start_response)
        return self._json(start_response, {"error":"not found"}, "404 Not Found")


def serve(workdir: Path, schema_dir: Path, host: str, port: int) -> None:
    app = PilotWebApp(workdir, schema_dir)
    with make_server(host, port, app) as server:
        print(f"Serving J.2 pilot at http://{host}:{port}")
        server.serve_forever()
