#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
export PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}"
python -m telic_j2 serve --workdir "$ROOT/demo/web" --host 127.0.0.1 --port 8767
