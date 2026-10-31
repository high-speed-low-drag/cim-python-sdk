"""Read the CGMES European extensions (namespace ``eu``) from the CGMES-CIM17 EA model into the IR.

Source: ``CGMES-CIM17/Schema/CIM17-2_CGMES31v01_PROF-20v02_NC23v66_MS10v01_DES10v01.qea``
(pinned in profile-source.toml ``[schema]``). Scope is the package
``Model/EuropeanCIMExtensions/ExtIEC61970/ExtEuBase``: the European extensions of the IEC 61970
Base package (``ExtIEC61970Version.version`` = 3.0), which are the ``eu:`` members of the CGMES
3.0 profiles. The network-code (ExtNetworkCodes) and header (ExtHeaderMetadata) extensions in the
same model are out of scope.

The EA conventions are those of `codegen.ea_reader` (roles, cardinalities, notes, stereotypes).
In addition:

* Extension classes follow the CIMTool pattern: a CIM class that *generalizes* a scope class
  (``IdentifiedObject`` -> ``ExtEuIdentifiedObject``) gains that class's attributes. The scope
  class is read as a classifier with ``extends`` = the CIM class GUID; `codegen.ir.merge` moves
  its attributes into the CIM class.
* Classes outside the scope are resolved by GUID against the base (CIM100) IR and their names must
  agree (the CGMES model reuses the CIM GUIDs). A generalization of a scope class to a class in
  neither (``ExtEuOperationalLimitType`` -> the NC ``ExtOperationalLimitType``) is skipped and
  counted in ``stats``; any other unresolved reference raises `EAReadError`.
* Every classifier, attribute and association read gets namespace ``eu``.
"""

from __future__ import annotations

import sqlite3
from collections import defaultdict
from pathlib import Path

from codegen.ea_reader import (
    _STEREO_RE,
    AGGREGATION,
    STEREOTYPE_KIND,
    EAReadError,
    _blank,
    _bound,
    clean_notes,
    parse_cardinality,
)
from codegen.ir import (
    Association,
    AssociationEnd,
    Attribute,
    Classifier,
    EnumLiteral,
    Model,
    Package,
)

NAMESPACE = "eu"
CHAIN = ("Model", "EuropeanCIMExtensions", "ExtIEC61970", "ExtEuBase")
VERSION_CLASS = "ExtIEC61970Version"  # in ExtIEC61970


def read_eu_model(path: str | Path, base: Model) -> Model:
    """The ``eu`` extension IR; external references are checked against `base`."""
    con = sqlite3.connect(f"file:{Path(path)}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        return _read(con, base)
    finally:
        con.close()


def _read(con: sqlite3.Connection, base: Model) -> Model:
    stats: dict[str, int] = defaultdict(int)
    base_cls = base.classifier_by_guid()

    # ---- packages: the chain down to ExtEuBase, then its subtree --------------------
    pkg_rows = {r["Package_ID"]: r for r in con.execute("SELECT * FROM t_package")}
    children: dict[int, list[int]] = defaultdict(list)
    for pid, r in pkg_rows.items():
        children[r["Parent_ID"]].append(pid)
    parent, chain_ids = 0, []
    for name in CHAIN:
        found = [c for c in children[parent] if pkg_rows[c]["Name"] == name]
        if len(found) != 1:
            raise EAReadError(f"expected one package {name!r} under {parent}, found {len(found)}")
        parent = found[0]
        chain_ids.append(parent)
    pkg_path: dict[int, str] = {}
    for i, pid in enumerate(chain_ids[1:], start=1):
        pkg_path[pid] = "/".join(CHAIN[1 : i + 1])
    scope_root = chain_ids[-1]
    scope: set[int] = {scope_root}
    stack = [scope_root]
    while stack:
        pid = stack.pop()
        for cid in children[pid]:
            pkg_path[cid] = f"{pkg_path[pid]}/{pkg_rows[cid]['Name']}"
            scope.add(cid)
            stack.append(cid)
    packages = [
        Package(
            pid,
            pkg_rows[pid]["ea_guid"],
            pkg_rows[pid]["Name"],
            path,
            path.rpartition("/")[0] or None,
            clean_notes(pkg_rows[pid]["Notes"]),
        )
        for pid, path in pkg_path.items()
    ]

    # ---- stereotypes ---------------------------------------------------------------
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

    # ---- objects: scope classifiers, and every object by id for external lookups ----
    all_objs = {
        r["Object_ID"]: r
        for r in con.execute("SELECT * FROM t_object WHERE Object_Type IN ('Class','Enumeration')")
    }
    objs = {oid: r for oid, r in all_objs.items() if r["Package_ID"] in scope}

    def external(oid: int) -> str | None:
        """Base-IR GUID of an object outside the scope, or None if the base lacks it."""
        r = all_objs.get(oid)
        if r is None:
            return None
        c = base_cls.get(r["ea_guid"])
        if c is None:
            return None
        if c.name != r["Name"]:
            raise EAReadError(f"GUID {r['ea_guid']}: {r['Name']!r} here, {c.name!r} in the base")
        return c.guid

    def ref(oid: int) -> str | None:
        return objs[oid]["ea_guid"] if oid in objs else external(oid)

    def kind_of(r: sqlite3.Row) -> str:
        if r["Object_Type"] == "Enumeration":
            return "enumeration"
        key = (r["Stereotype"] or "").lower() or None
        if key == "european":
            return "class"
        if key not in STEREOTYPE_KIND:
            raise EAReadError(f"unknown classifier stereotype {r['Stereotype']!r} on {r['Name']}")
        return STEREOTYPE_KIND[key]

    # ---- generalizations -------------------------------------------------------------
    superclass: dict[int, str] = {}
    extends: dict[int, str] = {}
    for r in con.execute(
        "SELECT Start_Object_ID s, End_Object_ID e FROM t_connector "
        "WHERE Connector_Type='Generalization' ORDER BY Connector_ID"
    ):
        s, e = r["s"], r["e"]
        if s in objs:
            sup = ref(e)
            if sup is None:
                stats["generalizations_skipped_out_of_scope"] += 1
                continue
            if s in superclass:
                raise EAReadError(f"multiple inheritance on {objs[s]['Name']}")
            superclass[s] = sup
            stats["generalizations"] += 1
        elif e in objs:
            sub = external(s)
            if sub is None:
                stats["generalizations_skipped_out_of_scope"] += 1
                continue
            if e in extends:
                raise EAReadError(f"{objs[e]['Name']} extends two classes")
            extends[e] = sub
            stats["extensions"] += 1

    # ---- attributes and classifiers -----------------------------------------------------
    attrs_by_obj: dict[int, list[sqlite3.Row]] = defaultdict(list)
    for r in con.execute("SELECT * FROM t_attribute ORDER BY Object_ID, Pos, ID"):
        if r["Object_ID"] in objs:
            attrs_by_obj[r["Object_ID"]].append(r)

    def attr_type(a: sqlite3.Row, owner: str) -> str:
        cid = (a["Classifier"] or "0").strip()
        target = int(cid) if cid.isdigit() else 0
        tname = (a["Type"] or "").strip()
        guid = ref(target) if target else None
        if guid is None or all_objs[target]["Name"] != tname:
            raise EAReadError(f"{owner}.{a['Name']}: cannot resolve type {tname!r} ({cid})")
        return guid

    classifiers = []
    versions: dict[str, str] = {}
    for oid, r in objs.items():
        kind = kind_of(r)
        if oid in extends and oid in superclass:
            del superclass[oid]  # an extension class only donates its attributes
        attributes: list[Attribute] = []
        literals: list[EnumLiteral] = []
        for a in attrs_by_obj.get(oid, ()):
            name = (a["Name"] or "").strip()
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
                    type_guid=attr_type(a, r["Name"]),
                    lower=_bound(a["LowerBound"], 0),
                    upper=_bound(a["UpperBound"], 1),
                    default=a["Default"],
                    is_static=bool(a["IsStatic"]),
                    is_const=bool(a["Const"]),
                    stereotypes=asts,
                    deprecated="deprecated" in asts,
                    notes=clean_notes(a["Notes"]),
                    namespace=NAMESPACE,
                )
            )
        sts = stereotypes(r["ea_guid"], r["Stereotype"])
        classifiers.append(
            Classifier(
                ea_id=oid,
                guid=r["ea_guid"],
                name=r["Name"],
                package=pkg_path[r["Package_ID"]],
                kind=kind,
                stereotypes=sts,
                abstract=(r["Abstract"] or "0") == "1",
                deprecated="deprecated" in sts,
                superclass=superclass.get(oid),
                attributes=tuple(attributes),
                literals=tuple(literals),
                notes=clean_notes(r["Note"]),
                namespace=NAMESPACE,
                extends=extends.get(oid),
            )
        )

    # version of the extensions: ExtIEC61970Version.version (a class in the chain, not in scope)
    for r in con.execute(
        'SELECT a."Default" v FROM t_attribute a JOIN t_object o ON o.Object_ID = a.Object_ID '
        "WHERE o.Name = ? AND o.Package_ID = ? AND a.Name = 'version'",
        (VERSION_CLASS, chain_ids[2]),
    ):
        versions[VERSION_CLASS] = r["v"]
    if VERSION_CLASS not in versions:
        raise EAReadError(f"{VERSION_CLASS}.version not found")

    # ---- associations ---------------------------------------------------------------
    associations = []
    for r in con.execute(
        "SELECT * FROM t_connector WHERE Connector_Type IN ('Association','Aggregation') "
        "ORDER BY Connector_ID"
    ):
        s, e = r["Start_Object_ID"], r["End_Object_ID"]
        if s not in objs and e not in objs:
            continue
        gs, ge = ref(s), ref(e)
        if gs is None or ge is None:
            raise EAReadError(f"association {r['ea_guid']} references a class outside the IR")
        if s in extends or e in extends:
            raise EAReadError(f"association {r['ea_guid']} references an extension class")
        d_lo, d_up = parse_cardinality(r["DestCard"])
        s_lo, s_up = parse_cardinality(r["SourceCard"])
        start_end = AssociationEnd(
            owner=gs,
            target=ge,
            role=_blank(r["DestRole"]),
            lower=d_lo,
            upper=d_up,
            cardinality=r["DestCard"].strip(),
            owner_aggregation=AGGREGATION[r["SourceIsAggregate"] or 0],
            navigable=bool(r["DestIsNavigable"]),
            notes=clean_notes(r["DestRoleNote"]),
        )
        end_end = AssociationEnd(
            owner=ge,
            target=gs,
            role=_blank(r["SourceRole"]),
            lower=s_lo,
            upper=s_up,
            cardinality=r["SourceCard"].strip(),
            owner_aggregation=AGGREGATION[r["DestIsAggregate"] or 0],
            navigable=bool(r["SourceIsNavigable"]),
            notes=clean_notes(r["SourceRoleNote"]),
        )
        stats[f"connectors_{r['Connector_Type'].lower()}"] += 1
        associations.append(
            Association(
                guid=r["ea_guid"],
                type=r["Connector_Type"],
                ends=(start_end, end_end),
                name=_blank(r["Name"]),
                stereotypes=stereotypes(r["ea_guid"], r["Stereotype"]),
                notes=clean_notes(r["Notes"]),
                namespace=NAMESPACE,
            )
        )

    return Model(
        versions=versions,
        packages=tuple(packages),
        classifiers=tuple(classifiers),
        associations=tuple(associations),
        stats=dict(stats),
    ).sorted()
