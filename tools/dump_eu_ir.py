"""Read the CGMES European extensions from the pinned CGMES EA model into codegen/snapshot/eu_ir.json.

Usage: dump_eu_ir.py [--out PATH] [--check]
  --check  do not write; exit 1 if the snapshot on disk differs from a fresh read.

The EA model is profile-source.toml ``[schema]``, cached in build/profiles/ (fetched when
missing; ``tools/fetch_profiles.py --schema`` fetches it explicitly). External references are
checked against codegen/snapshot/cim100_ir.json. The snapshot has the IR shape of cim100_ir.json;
`codegen.ir.merge` adds it to the CIM100 IR before code generation (see codegen/eu_reader.py).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from codegen.eu_reader import read_eu_model
from codegen.normalize import EU_SNAPSHOT, load_snapshot
from codegen.profile_source import ensure_schema


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=EU_SNAPSHOT)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    model = read_eu_model(ensure_schema(), load_snapshot())
    text = model.to_json(indent=1)
    if args.check:
        same = args.out.is_file() and args.out.read_text(encoding="utf-8") == text
        print("snapshot up to date" if same else f"snapshot differs: {args.out}")
        return 0 if same else 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(text, encoding="utf-8")
    print(f"wrote {args.out} ({args.out.stat().st_size:,} bytes)")
    print("versions: " + ", ".join(f"{k}={v}" for k, v in model.versions.items()))
    for c in sorted(model.classifiers, key=lambda c: (c.package, c.name)):
        what = f"extends {c.extends}" if c.extends else c.kind
        members = [a.name for a in c.attributes] + [x.name for x in c.literals]
        print(f"  {c.package}/{c.name} ({what}): {', '.join(members)}")
    print(f"  associations: {len(model.associations)}; stats: {model.stats}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
