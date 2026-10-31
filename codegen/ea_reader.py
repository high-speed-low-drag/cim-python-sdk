"""Read an Enterprise Architect 16 `.qea` (SQLite) model into the IR.

Scope is the `Model/TC57CIM` package subtree. See docs/PLAN.md "Model facts"
for the verified data conventions this reader relies on.

EA connector convention (verified on Terminal/ConductingEquipment and
Contingency/ContingencyElement):
  * Generalization: Start_Object_ID is the subclass, End_Object_ID the superclass.
  * Association: DestRole/DestCard describe the property owned by the START class
    that points at the END class; SourceRole/SourceCard describe the property
    owned by the END class that points back at the START class.
"""

from __future__ import annotations

import html
import re
import sqlite3
from collections import defaultdict
from pathlib import Path

from codegen.ir import (
    Association,
    AssociationEnd,
    Attribute,
    Classifier,
    EnumLiteral,
    Model,
    Package,
    UnresolvedType,
)

SCOPE = ("Model", "TC57CIM")

STEREOTYPE_KIND = {
    None: "class",
    "enumeration": "enumeration",
    "cimdatatype": "cimdatatype",
    "compound": "compound",
    "primitive": "primitive",
}

AGGREGATION = {0: "none", 1: "shared", 2: "composite"}


class EAReadError(RuntimeError):
    pass


# --------------------------------------------------------------------------- helpers

_CARD_RE = re.compile(r"^(\d+)(?:\.\.(\d+|\*|n)?)?$")


def parse_cardinality(text: str | None) -> tuple[int, int | None]:
    """Parse an EA cardinality string into (lower, upper); upper None = unbounded.

    Accepted forms: `N`, `*`, `n`, `N..M`, `N..*`, `N..n`, `N..` (open upper).
    Anything else raises EAReadError.
    """
    if text is None:
        raise EAReadError("missing cardinality")
    s = text.strip()
    if s in ("*", "n"):
        return 0, None
    m = _CARD_RE.match(s)
    if not m:
        raise EAReadError(f"unknown cardinality form {text!r}")
    lower = int(m.group(1))
    if ".." not in s:
        return lower, lower
    up = m.group(2)
    if up is None or up in ("*", "n"):
        return lower, None
    upper = int(up)
    if upper < lower or upper == 0:
        raise EAReadError(f"invalid cardinality bounds {text!r}")
    return lower, upper


def _bound(text: str | None, default: int) -> int | None:
    if text is None or text.strip() == "":
        return default
    s = text.strip()
    if s in ("*", "n"):
        return None
    if not s.isdigit():
        raise EAReadError(f"unknown attribute bound {text!r}")
    return int(s)


# EA rich-text notes use a small HTML subset. Only these tags are stripped:
# notes also contain literal pseudo-tags such as "<was Switch data.>" or
# "<type>.<domain>" which are real text and must be kept.
_TAGS = "a|b|i|u|s|em|strong|strike|sub|sup|font|ul|ol|li|img|br|p|span"
_LI_RE = re.compile(r"<li\b[^>]*>", re.IGNORECASE)
_BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
_TAG_RE = re.compile(rf"</?(?:{_TAGS})\b[^<>]*>", re.IGNORECASE)


def clean_notes(text: str | None) -> str:
    if not text:
        return ""
    s = text.replace("\r\n", "\n").replace("\r", "\n")
    s = _LI_RE.sub("- ", s)
    s = _BR_RE.sub("\n", s)
    s = _TAG_RE.sub("", s)
    s = html.unescape(s)
    lines = [ln.rstrip() for ln in s.split("\n")]
    # "\t- item" left over from <ul>\n\t<li> -> "- item"
    lines = [ln.lstrip("\t") for ln in lines]
    return "\n".join(lines).strip()


_STEREO_RE = re.compile(r"@STEREO;Name=([^;]+);")


def _blank(s: str | None) -> str | None:
    if s is None:
        return None
    s = s.strip()
    return s or None


# --------------------------------------------------------------------------- reader


def read_model(path: str | Path) -> Model:
    uri = f"file:{Path(path)}?mode=ro"
    con = sqlite3.connect(uri, uri=True)
    con.row_factory = sqlite3.Row
    try:
        return _read(con)
    finally:
        con.close()


def _read(con: sqlite3.Connection) -> Model:
    stats: dict[str, int] = defaultdict(int)

    # ---- packages -------------------------------------------------------
    pkg_rows = {r["Package_ID"]: r for r in con.execute("SELECT * FROM t_package")}
    root_id = None
    roots = [r for r in pkg_rows.values() if r["Name"] == SCOPE[0] and r["Parent_ID"] == 0]
    if len(roots) != 1:
        raise EAReadError(f"expected one root package {SCOPE[0]!r}, found {len(roots)}")
    tops = [
        r
        for r in pkg_rows.values()
        if r["Name"] == SCOPE[1] and r["Parent_ID"] == roots[0]["Package_ID"]
    ]
    if len(tops) != 1:
        raise EAReadError(f"expected one {'/'.join(SCOPE)} package, found {len(tops)}")
    root_id = tops[0]["Package_ID"]

    children: dict[int, list[int]] = defaultdict(list)
    for pid, r in pkg_rows.items():
        children[r["Parent_ID"]].append(pid)

    pkg_path: dict[int, str] = {root_id: SCOPE[1]}
    stack = [root_id]
    while stack:
        pid = stack.pop()
        for cid in children[pid]:
            pkg_path[cid] = f"{pkg_path[pid]}/{pkg_rows[cid]['Name']}"
            stack.append(cid)
    packages = []
    for pid, p in pkg_path.items():
        r = pkg_rows[pid]
        parent = None if pid == root_id else pkg_path[r["Parent_ID"]]
        packages.append(Package(pid, r["ea_guid"], r["Name"], p, parent, clean_notes(r["Notes"])))
    if len({p.path for p in packages}) != len(packages):
        raise EAReadError("duplicate package paths")

    # ---- stereotypes from t_xref (complete list; t_object.Stereotype is the first) ----
    xstereo: dict[str, list[str]] = defaultdict(list)
    for r in con.execute(
        "SELECT Client, Description FROM t_xref WHERE Name='Stereotypes' "
        "AND Type IN ('element property','attribute property','connector property') "
        "ORDER BY XrefID"
    ):
        for name in _STEREO_RE.findall(r["Description"] or ""):
            if name not in xstereo[r["Client"]]:
                xstereo[r["Client"]].append(name)

    def stereotypes(guid: str, primary: str | None) -> tuple[str, ...]:
        out = list(xstereo.get(guid, ()))
        if primary and primary not in out:
            out.insert(0, primary)
        return tuple(out)

    # ---- classifier objects -------------------------------------------------
    obj_rows = {
        r["Object_ID"]: r
        for r in con.execute(
            "SELECT * FROM t_object WHERE Object_Type IN ('Class','Enumeration')"
        )
        if r["Package_ID"] in pkg_path
    }
    stats["objects_outside_scope"] = con.execute(
        "SELECT count(*) FROM t_object WHERE Object_Type IN ('Class','Enumeration')"
    ).fetchone()[0] - len(obj_rows)
    guid_of = {oid: r["ea_guid"] for oid, r in obj_rows.items()}
    by_name: dict[str, list[int]] = defaultdict(list)
    for oid, r in obj_rows.items():
        by_name[r["Name"]].append(oid)

    def kind_of(r: sqlite3.Row) -> str:
        st = r["Stereotype"]
        if r["Object_Type"] == "Enumeration":
            return "enumeration"
        key = st.lower() if st else None
        if key not in STEREOTYPE_KIND:
            raise EAReadError(f"unknown classifier stereotype {st!r} on {r['Name']}")
        return STEREOTYPE_KIND[key]

    kinds = {oid: kind_of(r) for oid, r in obj_rows.items()}

    # ---- generalizations ----------------------------------------------------
    supers: dict[int, list[int]] = defaultdict(list)
    for r in con.execute(
        "SELECT Start_Object_ID s, End_Object_ID e FROM t_connector "
        "WHERE Connector_Type='Generalization' ORDER BY Connector_ID"
    ):
        if r["s"] in obj_rows and r["e"] in obj_rows:
            supers[r["s"]].append(r["e"])
            stats["generalizations"] += 1
    multi = {obj_rows[k]["Name"]: v for k, v in supers.items() if len(v) > 1}
    if multi:
        raise EAReadError(f"multiple inheritance not supported: {sorted(multi)}")

    # ---- attributes ---------------------------------------------------------
    attrs_by_obj: dict[int, list[sqlite3.Row]] = defaultdict(list)
    seen: set[tuple] = set()
    for r in con.execute('SELECT * FROM t_attribute ORDER BY Object_ID, Pos, ID'):
        if r["Object_ID"] not in obj_rows:
            continue
        # Exact (case-sensitive) duplicate rows. Note the columns are COLLATE NOCASE,
        # so this must not be done in SQL: UnitSymbol has both "m" and "M".
        key = (r["Object_ID"], r["Name"], r["Type"], r["Default"])
        if key in seen:
            stats["duplicate_attributes_removed"] += 1
            continue
        seen.add(key)
        attrs_by_obj[r["Object_ID"]].append(r)
    stats.setdefault("duplicate_attributes_removed", 0)

    unresolved: list[UnresolvedType] = []

    def resolve(r: sqlite3.Row, owner: int) -> str | None:
        cid = (r["Classifier"] or "0").strip()
        if cid.isdigit() and int(cid) != 0:
            target = int(cid)
            if target in obj_rows and obj_rows[target]["Name"] == (r["Type"] or "").strip():
                stats["types_resolved_by_id"] += 1
                return guid_of[target]
            stats["types_bad_classifier_id"] += 1
        tname = (r["Type"] or "").strip()
        cands = by_name.get(tname, [])
        if len(cands) > 1:
            # prefer a candidate in the owner's own package
            same = [c for c in cands if obj_rows[c]["Package_ID"] == obj_rows[owner]["Package_ID"]]
            cands = same if len(same) == 1 else cands
        if len(cands) == 1:
            stats["types_resolved_by_name"] += 1
            return guid_of[cands[0]]
        unresolved.append(UnresolvedType(guid_of[owner], (r["Name"] or "").strip(), tname))
        return None

    # ---- build classifiers --------------------------------------------------
    classifiers = []
    versions: dict[str, str] = {}
    for oid, r in obj_rows.items():
        guid = r["ea_guid"]
        kind = kinds[oid]
        sts = stereotypes(guid, r["Stereotype"])
        attributes: list[Attribute] = []
        literals: list[EnumLiteral] = []
        for a in attrs_by_obj.get(oid, ()):
            name = (a["Name"] or "").strip()
            if name != a["Name"]:
                stats["names_stripped"] += 1
            if kind == "enumeration":
                literals.append(
                    EnumLiteral(a["ID"], a["ea_guid"], name, a["Default"], clean_notes(a["Notes"]))
                )
                continue
            asts = stereotypes(a["ea_guid"], a["Stereotype"])
            attributes.append(
                Attribute(
                    ea_id=a["ID"],
                    guid=a["ea_guid"],
                    name=name,
                    type_name=(a["Type"] or "").strip(),
                    type_guid=resolve(a, oid),
                    lower=_bound(a["LowerBound"], 0),
                    upper=_bound(a["UpperBound"], 1),
                    default=a["Default"],
                    is_static=bool(a["IsStatic"]),
                    is_const=bool(a["Const"]),
                    stereotypes=asts,
                    deprecated="deprecated" in asts,
                    notes=clean_notes(a["Notes"]),
                )
            )
        if r["Name"].endswith("CIMVersion"):
            vs = [a.default for a in attributes if a.name == "version"]
            if vs:
                prev = versions.setdefault(r["Name"], vs[0])
                if prev != vs[0]:
                    raise EAReadError(f"conflicting versions for {r['Name']}: {prev} / {vs[0]}")
        sup = supers.get(oid)
        classifiers.append(
            Classifier(
                ea_id=oid,
                guid=guid,
                name=r["Name"],
                package=pkg_path[r["Package_ID"]],
                kind=kind,
                stereotypes=sts,
                abstract=(r["Abstract"] or "0") == "1",
                deprecated="deprecated" in sts,
                superclass=guid_of[sup[0]] if sup else None,
                attributes=tuple(attributes),
                literals=tuple(literals),
                notes=clean_notes(r["Note"]),
            )
        )

    # ---- associations -------------------------------------------------------
    associations = []
    for r in con.execute(
        "SELECT * FROM t_connector WHERE Connector_Type IN ('Association','Aggregation') "
        "ORDER BY Connector_ID"
    ):
        s, e = r["Start_Object_ID"], r["End_Object_ID"]
        if s not in obj_rows or e not in obj_rows:
            stats["connectors_skipped_out_of_scope"] += 1
            continue
        for col in ("SourceRole", "DestRole"):
            if r[col] is not None and r[col] != r[col].strip():
                stats["names_stripped"] += 1
        d_lo, d_up = parse_cardinality(r["DestCard"])
        s_lo, s_up = parse_cardinality(r["SourceCard"])
        start_end = AssociationEnd(
            owner=guid_of[s],
            target=guid_of[e],
            role=_blank(r["DestRole"]),
            lower=d_lo,
            upper=d_up,
            cardinality=r["DestCard"].strip(),
            owner_aggregation=AGGREGATION[r["SourceIsAggregate"] or 0],
            navigable=bool(r["DestIsNavigable"]),
            notes=clean_notes(r["DestRoleNote"]),
        )
        end_end = AssociationEnd(
            owner=guid_of[e],
            target=guid_of[s],
            role=_blank(r["SourceRole"]),
            lower=s_lo,
            upper=s_up,
            cardinality=r["SourceCard"].strip(),
            owner_aggregation=AGGREGATION[r["DestIsAggregate"] or 0],
            navigable=bool(r["SourceIsNavigable"]),
            notes=clean_notes(r["SourceRoleNote"]),
        )
        stats[f"connectors_{r['Connector_Type'].lower()}"] += 1
        if start_end.role is None and end_end.role is None:
            stats["associations_without_roles"] += 1
        elif start_end.role is None or end_end.role is None:
            stats["associations_one_role_missing"] += 1
        associations.append(
            Association(
                guid=r["ea_guid"],
                type=r["Connector_Type"],
                ends=(start_end, end_end),
                name=_blank(r["Name"]),
                stereotypes=stereotypes(r["ea_guid"], r["Stereotype"]),
                notes=clean_notes(r["Notes"]),
            )
        )

    stats["unresolved_types"] = len(unresolved)
    return Model(
        versions=versions,
        packages=tuple(packages),
        classifiers=tuple(classifiers),
        associations=tuple(associations),
        unresolved_types=tuple(unresolved),
        stats=dict(stats),
    ).sorted()
