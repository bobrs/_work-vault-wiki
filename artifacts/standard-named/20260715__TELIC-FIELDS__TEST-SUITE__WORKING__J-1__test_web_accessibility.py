from __future__ import annotations

import io
import tempfile
import unittest
from pathlib import Path

from telic_j1.webapp import PilotWebApp

ROOT = Path(__file__).resolve().parents[1]


def call(app, path: str, method: str = "GET"):
    captured = {}
    def start_response(status, headers):
        captured["status"] = status
        captured["headers"] = headers
    environ = {"REQUEST_METHOD":method,"PATH_INFO":path,"wsgi.input":io.BytesIO(b""),"CONTENT_LENGTH":"0"}
    body = b"".join(app(environ, start_response))
    return captured["status"], dict(captured["headers"]), body.decode("utf-8")


class WebAccessibilityTests(unittest.TestCase):
    def test_semantic_keyboard_and_status_features_present(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            app = PilotWebApp(Path(name), ROOT/"schemas")
            status, _, body = call(app, "/")
            self.assertTrue(status.startswith("200"))
            for marker in ['lang="en"','class="skip-link"','id="main"','aria-live="polite"','type="submit"','prefers-reduced-motion','forced-colors']:
                self.assertIn(marker, body)
            status, _, accessibility = call(app, "/accessibility")
            self.assertTrue(status.startswith("200"))
            self.assertIn("Accessibility statement", accessibility)
