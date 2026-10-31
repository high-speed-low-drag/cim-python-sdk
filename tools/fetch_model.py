"""Fetch the pinned CIM100 model into build/model/. Usage: fetch_model.py [--force] [--dest DIR]"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from codegen.model_source import DEFAULT_DEST, ModelFetchError, ensure_model


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--force", action="store_true", help="re-download even if cached")
    ap.add_argument("--dest", type=Path, default=DEFAULT_DEST)
    args = ap.parse_args()
    try:
        path = ensure_model(args.dest, force=args.force)
    except ModelFetchError as exc:
        print(f"error: could not fetch model: {exc}", file=sys.stderr)
        return 1
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
