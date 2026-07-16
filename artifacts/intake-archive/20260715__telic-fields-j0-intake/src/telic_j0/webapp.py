from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

from .scenario import ReferencePilot


HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Telic Fields J.0 Pilot</title>
<style>
body{font-family:system-ui,sans-serif;max-width:980px;margin:2rem auto;padding:0 1rem;line-height:1.45}
button{padding:.55rem .9rem;margin:.2rem}pre{background:#f3f3f3;padding:1rem;overflow:auto}code{font-family:ui-monospace,monospace}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem}.card{border:1px solid #bbb;border-radius:8px;padding:1rem}
</style>
</head>
<body>
<h1>J.0 — Bounded Model-Assisted Scheduling</h1>
<p>The model may summarize and generate candidate schedules. The external gate controls execution.</p>
<div class="grid">
<div class="card"><h2>Scenario steps</h2>
<form method="post" action="/step/seed"><button>1. Seed field</button></form>
<form method="post" action="/step/summarize"><button>2. Generate summary</button></form>
<form method="post" action="/step/correct"><button>3. Apply participant correction</button></form>
<form method="post" action="/step/gate"><button>4. Generate and gate routes</button></form>
<form method="post" action="/step/execute"><button>5. Execute authorized route</button></form>
<form method="post" action="/step/consequence"><button>6. Observe consequence</button></form>
<form method="post" action="/step/retire"><button>7. Retire pilot</button></form>
<form method="post" action="/step/full"><button>Run full demonstration</button></form>
</div>
<div class="card"><h2>Inspection</h2>
<p><a href="/api/status">Status JSON</a></p>
<p><a href="/api/events">Event chain JSON</a></p>
<p><a href="/api/objects">Objects JSON</a></p>
<p><a href="/api/witness">Witness JSON</a></p>
</div>
</div>
<h2>Current status</h2><pre>{status}</pre>
<h2>Last result</h2><pre>{result}</pre>
</body></html>"""


class PilotWebApp:
    def __init__(self, workdir: Path, schema_dir: Path):
        self.pilot = ReferencePilot(workdir, schema_dir)
        self.last_result = {"message": "Ready"}

    def _json_response(self, start_response, payload, status="200 OK"):
        body = json.dumps(payload, indent=2).encode("utf-8")
        start_response(status, [("Content-Type", "application/json"), ("Content-Length", str(len(body)))])
        return [body]

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "/")
        method = environ.get("REQUEST_METHOD", "GET")
        try:
            if path == "/api/status":
                return self._json_response(start_response, self.pilot.status())
            if path == "/api/events":
                return self._json_response(start_response, {"events": self.pilot.store.list_events()})
            if path == "/api/objects":
                return self._json_response(start_response, {"objects": self.pilot.store.list_objects()})
            if path == "/api/witness":
                return self._json_response(start_response, self.pilot.witness_summary())
            if method == "POST" and path.startswith("/step/"):
                step = path.rsplit("/", 1)[-1]
                actions = {
                    "seed": self.pilot.seed,
                    "summarize": self.pilot.summarize,
                    "correct": self.pilot.correct_participant_b,
                    "gate": self.pilot.plan_and_gate,
                    "execute": self.pilot.execute_approved,
                    "consequence": self.pilot.observe_consequence,
                    "retire": self.pilot.retire,
                    "full": self.pilot.run_full,
                }
                if step not in actions:
                    return self._json_response(start_response, {"error": "unknown step"}, "404 Not Found")
                self.last_result = actions[step]()
                start_response("303 See Other", [("Location", "/")])
                return [b""]
            status = json.dumps(self.pilot.status(), indent=2)
            result = json.dumps(self.last_result, indent=2, default=str)
            body = HTML.replace("{status}", status).replace("{result}", result).encode("utf-8")
            start_response("200 OK", [("Content-Type", "text/html; charset=utf-8"), ("Content-Length", str(len(body)))])
            return [body]
        except Exception as exc:  # noqa: BLE001
            return self._json_response(start_response, {"error": type(exc).__name__, "detail": str(exc)}, "500 Internal Server Error")


def serve(workdir: Path, schema_dir: Path, host: str = "127.0.0.1", port: int = 8765) -> None:
    app = PilotWebApp(workdir, schema_dir)
    with make_server(host, port, app) as server:
        print(f"J.0 pilot server: http://{host}:{port}")
        server.serve_forever()
