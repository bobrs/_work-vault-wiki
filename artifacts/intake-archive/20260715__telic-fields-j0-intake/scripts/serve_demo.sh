#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
PYTHONPATH="$ROOT/src" python3 -m telic_j0.cli serve --workdir "$ROOT/demo/web" --host 127.0.0.1 --port 8765
