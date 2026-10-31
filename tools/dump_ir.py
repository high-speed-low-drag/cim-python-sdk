"""Read the cached EA model and write codegen/snapshot/cim100_ir.json, then print a summary.

Usage: dump_ir.py [--out PATH] [--check]
  --check  do not write; exit 1 if the snapshot on disk differs from a fresh read.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from codegen.ea_reader import read_model
from codegen.ir import Model
from codegen.model_source import ensure_model

SNAPSHOT = ROOT / "codegen" / "snapshot" / "cim100_ir.json"


def summary(model: Model) -> dict[str, int]:
    kinds = Counter(c.kind for c in model.classifiers)
    types = Counter(a.type for a in model.associations)
    out = {"classifiers": len(model.classifiers)}
    out.update({f"kind_{k}": kinds[k] for k in sorted(kinds)})
    out["attributes"] = sum(len(c.attributes) for c in model.classifiers)
    out["literals"] = sum(len(c.literals) for c in model.classifiers)
    out["associations"] = types["Association"]
    out["aggregations"] = types["Aggregation"]
    out["generalizations"] = sum(c.superclass is not None for c in model.classifiers)
    out["packages"] = len(model.packages)
    out["duplicate_attributes_removed"] = model.stats.get("duplicate_attributes_removed", 0)
    out["unresolved_types"] = len(model.unresolved_types)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=SNAPSHOT)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    model = read_model(ensure_model())
    text = model.to_json(indent=1)
    if args.check:
        same = args.out.is_file() and args.out.read_text(encoding="utf-8") == text
        print("snapshot up to date" if same else f"snapshot differs: {args.out}")
        return 0 if same else 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(text, encoding="utf-8")
    print(f"wrote {args.out} ({args.out.stat().st_size:,} bytes)")
    print("versions: " + ", ".join(f"{k}={v}" for k, v in model.versions.items()))
    for k, v in summary(model).items():
        print(f"  {k:30} {v:>6}")
    for u in model.unresolved_types:
        print(f"  unresolved: {u.classifier} {u.attribute}: {u.type_name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
