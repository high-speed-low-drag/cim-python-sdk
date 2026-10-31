"""``mvlv-cim`` command line: export, verify, summary."""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

from mvlv_cim import cgmes
from mvlv_cim.builder import build_network
from mvlv_cim.export import DEFAULT_SOURCE, FORMATS, export_network, find_workbooks

MAIN_CLASSES = (
    "ACLineSegment",
    "Terminal",
    "ConnectivityNode",
    "PowerTransformer",
    "PowerTransformerEnd",
    "RatioTapChanger",
    "EquivalentInjection",
    "LinearShuntCompensator",
    "Substation",
    "VoltageLevel",
    "PositionPoint",
    "Name",
)


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mvlv-cim", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp: argparse.ArgumentParser) -> None:
        sp.add_argument("--network", "-n", type=int, action="append", metavar="N")
        sp.add_argument("--all", action="store_true", help="all networks (default if none given)")
        sp.add_argument("--source", type=Path, default=DEFAULT_SOURCE)

    e = sub.add_parser("export", help="write CIMXML, JSON-LD and/or a CGMES 3.0 file set")
    common(e)
    e.add_argument(
        "--format",
        choices=["cimxml", "jsonld", "both", "cgmes", "all"],
        default="both",
        help="both = cimxml + jsonld; cgmes = EQ/SSH/TP files per network; all = all three",
    )
    e.add_argument("--out", type=Path, default=Path("out"))
    e.add_argument("--created", help="header timestamp (default: source file mtime)")
    _cgmes_args(e)
    v = sub.add_parser("verify", help="round-trip check against a fresh build")
    common(v)
    v.add_argument("--out", type=Path, default=Path("out"))
    v.add_argument("--created")
    v.add_argument(
        "--cgmes", action="store_true", help="also validate and round-trip the CGMES set"
    )
    _cgmes_args(v, zip_option=False)
    s = sub.add_parser("summary", help="object counts per class")
    common(s)
    return p


def _cgmes_args(sp: argparse.ArgumentParser, zip_option: bool = True) -> None:
    sp.add_argument(
        "--gl",
        action="store_true",
        help="CGMES: also write the GL profile (Location, PositionPoint, CoordinateSystem)",
    )
    if zip_option:
        sp.add_argument("--zip", action="store_true", help="CGMES: one .zip per network")


def _profiles(args: argparse.Namespace) -> tuple[str, ...]:
    return cgmes.GL_PROFILES if args.gl else cgmes.PROFILES


def _select(args: argparse.Namespace):
    return find_workbooks(args.source, None if args.all or not args.network else args.network)


def _cmd_export(args: argparse.Namespace) -> int:
    plain = {
        "both": list(FORMATS),
        "all": list(FORMATS),
        "cimxml": ["cimxml"],
        "jsonld": ["jsonld"],
    }
    formats = plain.get(args.format, [])
    for wb in _select(args):
        for f, p in export_network(wb, args.out, formats, args.created).items() if formats else ():
            print(f"{wb.stem} [{f}] -> {p} ({p.stat().st_size / 1e6:.1f} MB)")
        if args.format in ("cgmes", "all"):
            res = cgmes.export_cgmes(
                wb, args.out, profiles=_profiles(args), zip_file=args.zip, created=args.created
            )
            sizes = ", ".join(f"{kw} {n / 1e6:.1f} MB" for kw, n in res.sizes.items())
            print(f"{wb.stem} [cgmes] -> {res.target} ({sizes})")
            print(
                f"  {res.n_objects} objects, validate_profile: {len(res.errors)} errors, "
                f"{len(res.warnings)} warnings; not carried: {sum(res.dropped.values())} "
                f"values/objects ({len(res.dropped)} kinds, see docs/EXPORT_REPORT.md)"
            )
            for issue in res.errors[:5]:
                print(f"  error: {issue}")
    return 0


def _cmd_verify(args: argparse.Namespace) -> int:
    from mvlv_cim.verify import verify_network

    bad = 0
    for wb in _select(args):
        r = verify_network(
            wb,
            args.out,
            created=args.created,
            cgmes_profiles=_profiles(args) if args.cgmes else None,
        )
        print(f"{wb.stem}: {r.n_objects} objects, cross-format equal: {r.cross_equal}")
        for f, fr in r.formats.items():
            print(
                f"  {f:7} {fr.size / 1e6:6.1f} MB write {fr.write_s:5.1f}s read {fr.read_s:5.1f}s "
                f"equal={fr.equal} deterministic={fr.deterministic} "
                f"warnings={len(fr.warnings)} dangling={fr.dangling}"
            )
            for w in fr.warnings[:5]:
                print(f"    warning: {w}")
            if fr.diff:
                print("    " + fr.diff.replace("\n", "\n    "))
        if r.cgmes:
            c = r.cgmes
            print(
                f"  cgmes   {'+'.join(c.profiles)} {sum(c.sizes.values()) / 1e6:6.1f} MB "
                f"write {c.write_s:5.1f}s read {c.read_s:5.1f}s equal={c.equal} "
                f"deterministic={c.deterministic} errors={len(c.errors)} "
                f"warnings={len(c.read_warnings)} dangling={c.dangling}"
            )
            for msg in [*c.errors[:5], *c.read_warnings[:5]]:
                print(f"    {msg}")
            if c.diff:
                print("    " + c.diff.replace("\n", "\n    "))
        print(f"  {'OK' if r.ok else 'FAILED'}")
        bad += not r.ok
    return 1 if bad else 0


def _cmd_summary(args: argparse.Namespace) -> int:
    nets = [(wb, build_network(wb.path).counts) for wb in _select(args)]
    classes = [c for c in MAIN_CLASSES if any(c in n for _, n in nets)]
    rest = Counter()
    for _, n in nets:
        rest.update({k: v for k, v in n.items() if k not in classes})
    classes += sorted(rest)
    w = max(len(c) for c in classes)
    print(f"{'class':{w}}" + "".join(f" {'N' + str(wb.number):>8}" for wb, _ in nets))
    for c in classes:
        print(f"{c:{w}}" + "".join(f" {n.get(c, 0):>8}" for _, n in nets))
    print(f"{'TOTAL':{w}}" + "".join(f" {sum(n.values()):>8}" for _, n in nets))
    return 0


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        return {"export": _cmd_export, "verify": _cmd_verify, "summary": _cmd_summary}[args.cmd](
            args
        )
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
