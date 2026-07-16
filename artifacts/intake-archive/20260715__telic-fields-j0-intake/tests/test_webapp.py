from __future__ import annotations

import io
import json
import tempfile
import unittest
from pathlib import Path

from telic_j0.webapp import PilotWebApp


ROOT = Path(__file__).resolve().parents[1]


def call_wsgi(app, path: str, method: str = "GET"):
    captured = {}
    def start_response(status, headers):
        captured["status"] = status
        captured["headers"] = headers
    environ = {
        "REQUEST_METHOD": method,
        "PATH_INFO": path,
        "wsgi.input": io.BytesIO(b""),
        "CONTENT_LENGTH": "0",
    }
    body = b"".join(app(environ, start_response))
    return captured["status"], dict(captured["headers"]), body


class WebAppTests(unittest.TestCase):
    def test_status_and_full_demo_endpoints(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            app = PilotWebApp(Path(name), ROOT / "schemas")
            status, _, body = call_wsgi(app, "/")
            self.assertTrue(status.startswith("200"))
            self.assertIn(b"J.0", body)
            status, _, body = call_wsgi(app, "/api/status")
            self.assertTrue(status.startswith("200"))
            self.assertEqual(json.loads(body)["step"], "new")
            status, headers, _ = call_wsgi(app, "/step/full", "POST")
            self.assertTrue(status.startswith("303"))
            status, _, body = call_wsgi(app, "/api/status")
            self.assertEqual(json.loads(body)["step"], "retired")


if __name__ == "__main__":
    unittest.main()
