"""Fetch the pinned CGMES profile vocabularies (ENTSO-E RDFS) into build/profiles/.

Usage: fetch_profiles.py [--force] [--dest DIR] [--schema]
  --schema  also fetch the pinned CGMES EA model (.qea, ~50 MB) that tools/dump_eu_ir.py reads.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from codegen.profile_source import (
    DEFAULT_DEST,
    ProfileFetchError,
    ensure_profiles,
    ensure_schema,
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--force", action="store_true", help="re-download even if cached")
    ap.add_argument("--dest", type=Path, default=DEFAULT_DEST)
    ap.add_argument("--schema", action="store_true", help="also fetch the CGMES EA model")
    args = ap.parse_args()
    try:
        paths = ensure_profiles(args.dest, force=args.force)
        if args.schema:
            paths["schema"] = ensure_schema(args.dest, force=args.force)
    except ProfileFetchError as exc:
        print(f"error: could not fetch profiles: {exc}", file=sys.stderr)
        return 1
    for keyword, path in paths.items():
        print(f"{keyword:5} {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
