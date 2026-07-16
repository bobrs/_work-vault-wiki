#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
PYTHONPATH="$ROOT/src" python3 -m telic_j0.cli demo \
  --workdir "$ROOT/demo/run" \
  --export "$ROOT/exports/tf-mvi-1-witness.zip"
