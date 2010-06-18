#!/bin/sh
# glow.sh — friendly wrapper so cron does not need to remember python paths
# Usage: ./glow.sh [--plain]

DIR=`dirname "$0"`
cd "$DIR" || exit 1

# Prefer python2 if the OS is being modern and weird
if command -v python2 >/dev/null 2>&1; then
  PY=python2
elif command -v python >/dev/null 2>&1; then
  PY=python
else
  echo "No python found. The octo cannot glow without a brain." >&2
  exit 127
fi

exec "$PY" ./glow.py "$@"
