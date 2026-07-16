#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
PYTHONPATH="$ROOT/src" python3 "$ROOT/tests/run_all.py"
PYTHONPATH="$ROOT/src" python3 -m telic_j0.cli threats --workdir "$ROOT/demo/threats"
PYTHONPATH="$ROOT/src" python3 -m telic_j0.cli verify "$ROOT/exports/tf-mvi-1-witness.zip"
