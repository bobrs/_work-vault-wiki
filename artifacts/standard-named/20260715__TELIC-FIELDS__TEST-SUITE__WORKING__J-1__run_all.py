#!/usr/bin/env python3
from __future__ import annotations

import unittest

loader = unittest.TestLoader()
suite = loader.discover(start_dir=str(__import__('pathlib').Path(__file__).parent), pattern='test_*.py')
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
