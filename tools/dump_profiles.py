"""Read the pinned CGMES 3.0 vocabularies (ENTSO-E RDFS) and write
src/cim_python_sdk/profiles/data/cgmes_3_0.json.

Usage: dump_profiles.py [--out PATH] [--check]
  --check  do not write; exit 1 if the snapshot on disk differs from a fresh read.

Snapshot schema (keys sorted; URIs compacted to `prefix:Local` with the `namespaces` table):
  source: {repo, commit, license}
  namespaces: {prefix: namespace URI}
  units: {datatype: {multiplier, unit}}   (cims:isFixed of the datatypes; unit absent for Money)
  profiles: {keyword: {keyword, name, file, uri, version, base, comment,
                       classes: {CIM name: class}}}
  class: {ns, super, concrete, enumeration, stereotypes, literals (list; null if not an enum),
          properties: {"Class.prop": property}}
  property: {ns, kind ("attribute"/"association"), min, max (null = unbounded), range,
             range_kind ("datatype"/"enumeration"/"compound"/"class"),
             targets (the range class when the profile lists it), stereotypes}
A property sits under the class that owns it in the profile (its rdfs:domain; for an
association the end with cims:AssociationUsed "Yes"), which is the side written in CIMXML.
The `[[corrections]]` of profile-source.toml (known errors of the vocabularies) are applied.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from codegen.profile_source import ensure_profiles, load_source_config
from codegen.rdfs_reader import RdfsClass, RdfsProfile, RdfsProperty, read_rdfs, split_uri

SNAPSHOT = ROOT / "src" / "cim_python_sdk" / "profiles" / "data" / "cgmes_3_0.json"
NAMESPACES = {
    "cim": "http://iec.ch/TC57/CIM100#",
    "eu": "http://iec.ch/TC57/CIM100-European#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}
_PREFIX = {v: k for k, v in NAMESPACES.items()}


def prefix(ns: str) -> str:
    return _PREFIX.get(ns, ns)


def compact(uri: str) -> str:
    ns, local = split_uri(uri)
    p = _PREFIX.get(ns)
    return f"{p}:{local}" if p else uri


def _prop(p: RdfsProperty) -> dict:
    return {
        "ns": prefix(p.namespace),
        "kind": p.kind,
        "min": p.min,
        "max": p.max,
        "range": compact(p.range),
        "range_kind": p.range_kind,
        "targets": list(p.targets),
        "stereotypes": list(p.stereotypes),
    }


def _cls(c: RdfsClass) -> dict:
    return {
        "ns": prefix(c.namespace),
        "super": c.superclass,
        "concrete": c.concrete,
        "enumeration": c.enumeration,
        "stereotypes": list(c.stereotypes),
        "literals": None if c.literals is None else list(c.literals),
        "properties": {p.name: _prop(p) for p in c.properties},
    }


def profile_entry(entry: dict, prof: RdfsProfile) -> dict:
    if prof.keyword != entry["keyword"]:
        raise ValueError(
            f"{entry['file']}: keyword {prof.keyword!r}, pinned as {entry['keyword']!r}"
        )
    return {
        "keyword": prof.keyword,
        "name": prof.name,
        "file": entry["file"],
        "uri": prof.uri,
        "version": prof.version,
        "base": prof.namespace,
        "comment": prof.comment,
        "classes": {c.name: _cls(c) for c in prof.classes},
    }


def merged_units(profiles: list[RdfsProfile]) -> dict[str, dict[str, str]]:
    """The fixed units over all profiles; a datatype fixed differently in two profiles raises."""
    out: dict[str, tuple[str, str | None]] = {}
    for prof in profiles:
        for dt, unit in prof.units.items():
            if out.setdefault(dt, unit) != unit:
                raise ValueError(f"{dt}: fixed as {out[dt]} and as {unit} ({prof.keyword})")
    return {
        dt: {"multiplier": m} | ({"unit": u} if u is not None else {})
        for dt, (m, u) in sorted(out.items())
    }


def apply_corrections(profiles: dict[str, dict], corrections: list[dict]) -> None:
    """Apply the `[[corrections]]` of profile-source.toml; one that no longer applies raises."""
    for c in corrections:
        cls = profiles[c["profile"]]["classes"].get(c["class"])
        if cls is None:
            raise ValueError(f"correction: no class {c['class']} in {c['profile']}")
        stereo = c["add_stereotype"]
        if stereo in cls["stereotypes"]:
            raise ValueError(
                f"correction: {c['profile']} {c['class']} already has {stereo!r}; remove the entry"
            )
        cls["stereotypes"] = sorted([*cls["stereotypes"], stereo])


def build_snapshot(config: dict, paths: dict[str, Path]) -> dict:
    read = {e["keyword"]: read_rdfs(paths[e["keyword"]]) for e in config["profiles"]}
    profiles = {e["keyword"]: profile_entry(e, read[e["keyword"]]) for e in config["profiles"]}
    apply_corrections(profiles, config.get("corrections", []))
    return {
        "source": {k: config[k] for k in ("repo", "commit", "license")},
        "namespaces": NAMESPACES,
        "units": merged_units(list(read.values())),
        "profiles": profiles,
    }


def snapshot_text(snapshot: dict) -> str:
    return json.dumps(snapshot, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--out", type=Path, default=SNAPSHOT)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    config = load_source_config()
    snap = build_snapshot(config, ensure_profiles(config=config))
    text = snapshot_text(snap)
    if args.check:
        same = args.out.is_file() and args.out.read_text(encoding="utf-8") == text
        print("snapshot up to date" if same else f"snapshot differs: {args.out}")
        return 0 if same else 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(text, encoding="utf-8")
    print(f"wrote {args.out} ({args.out.stat().st_size:,} bytes)")
    for kw, p in snap["profiles"].items():
        props = sum(len(c["properties"]) for c in p["classes"].values())
        print(f"  {kw:5} {p['name']:22} classes {len(p['classes']):4}  properties {props:5}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
