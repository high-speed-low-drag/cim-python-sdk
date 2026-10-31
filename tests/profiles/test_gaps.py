"""Every snapshot member is modelled by the SDK (see PLAN.md Phase 3 facts).

A snapshot member counts as modelled only when the SDK has it in the same namespace (``cim`` or
``eu``, from ``ClassMeta``/``AttrMeta``/``EndMeta.namespace``). The European extensions (C2) are
modelled; with the ENTSO-E vocabularies as the source nothing else is missing (the CIMTool OWL
used before listed ``VsConverter.uf``, ``Simple_Float`` and stale CIM15 members)."""

import importlib
import json
from importlib import resources

from cim_python_sdk._registry import BY_NAME
from cim_python_sdk._runtime.meta import cim_attributes, cim_ends

PRIMITIVES = {
    "Boolean",
    "Date",
    "DateTime",
    "Decimal",
    "Duration",
    "Float",
    "Integer",
    "MonthDay",
    "String",
    "Time",
}

# European extensions: modelled since C2 (test_eu_members_modelled checks them in detail).
EU_CLASSES = {
    "eu:BoundaryPoint": ["EQ", "EQBD"],
    "eu:LimitKind": ["EQ"],
    "eu:SolarPowerPlant": ["EQ"],
    "eu:WindPowerPlant": ["EQ"],
}
EU_PROPERTIES = {
    **{
        f"eu:BoundaryPoint.{p}": ["EQ", "EQBD"]
        for p in (
            "ConnectivityNode",
            "fromEndIsoCode",
            "fromEndName",
            "fromEndNameTso",
            "isDirectCurrent",
            "isExcludedFromAreaInterchange",
            "toEndIsoCode",
            "toEndName",
            "toEndNameTso",
        )
    },
    "eu:IdentifiedObject.energyIdentCodeEic": ["EQ", "EQBD", "TP"],
    "eu:IdentifiedObject.shortName": ["EQ", "EQBD", "TP"],
    "eu:OperationalLimitType.kind": ["EQ"],
    "eu:SolarGeneratingUnit.SolarPowerPlant": ["EQ"],
    "eu:WindGeneratingUnit.WindPowerPlant": ["EQ"],
}
EU_RANGES = {"eu:LimitKind": ["EQ"], "eu:SolarPowerPlant": ["EQ"], "eu:WindPowerPlant": ["EQ"]}

def _cls(name):
    module, cls = BY_NAME[name].split(":")
    return getattr(importlib.import_module(module), cls)


def _member(qname: str):
    """The AttrMeta or EndMeta for ``Class.prop`` (inherited ones included), or None."""
    cls, prop = qname.split(".", 1)
    if cls not in BY_NAME:
        return None
    k = _cls(cls)
    found = [a for a in cim_attributes(k) if a.cim_name == prop]
    found += [e for e in cim_ends(k) if e.cim_role == prop]
    return found[0] if found else None


def _in_sdk(qname: str, ns: str = "cim") -> bool:
    m = _member(qname)
    return m is not None and m.namespace == ns


def _class_in_sdk(name: str, ns: str) -> bool:
    return name in BY_NAME and _cls(name)._cim_meta.namespace == ns


def _gaps():
    snap = json.loads(
        resources.files("cim_python_sdk.profiles").joinpath("data/cgmes_3_0.json").read_text("utf-8")
    )
    gaps: dict[str, dict[str, set]] = {k: {} for k in ("class", "property", "range")}

    def add(kind, key, kw):
        gaps[kind].setdefault(key, set()).add(kw)

    for kw, p in snap["profiles"].items():
        for cname, c in p["classes"].items():
            if not _class_in_sdk(cname, c["ns"]):
                add("class", f"{c['ns']}:{cname}", kw)
            for pname, prop in c["properties"].items():
                if not _in_sdk(pname, prop["ns"]):
                    add("property", f"{prop['ns']}:{pname}", kw)
                rng = prop["range"]
                if rng and not rng.startswith("xsd:"):
                    pre, local = rng.split(":", 1)
                    if not (_class_in_sdk(local, pre) or (pre == "cim" and local in PRIMITIVES)):
                        add("range", rng, kw)
    return {k: {n: sorted(v) for n, v in d.items()} for k, d in gaps.items()}


def test_no_gaps():
    assert _gaps() == {"class": {}, "property": {}, "range": {}}


XSD_PY = {"xsd:string": "str", "xsd:boolean": "bool"}


def test_eu_members_modelled():
    """Every eu: class, property and range of the snapshot is in the SDK, in the eu namespace,
    with a matching kind, type and a UML multiplicity the profile narrows (never widens)."""
    snap = json.loads(
        resources.files("cim_python_sdk.profiles").joinpath("data/cgmes_3_0.json").read_text("utf-8")
    )
    classes: dict[str, list[str]] = {}
    props: dict[str, list[str]] = {}
    ranges: dict[str, list[str]] = {}
    for kw, p in snap["profiles"].items():
        for cname, c in p["classes"].items():
            if c["ns"] == "eu":
                classes.setdefault(f"eu:{cname}", []).append(kw)
                k = _cls(cname)
                assert k._cim_meta.namespace == "eu"
                if c["super"]:
                    assert k.__mro__[1].__name__ == c["super"]
            for pname, prop in c["properties"].items():
                if prop["ns"] != "eu":
                    continue
                props.setdefault(f"eu:{pname}", []).append(kw)
                m = _member(pname)
                assert m is not None and m.namespace == "eu", pname
                rng = prop["range"]
                if rng.startswith("eu:"):
                    ranges.setdefault(rng, []).append(kw)
                if prop["kind"] == "attribute":
                    want = XSD_PY.get(rng, rng.partition(":")[2])
                    assert m.py_type == want, pname
                else:
                    assert m.target.rpartition(":")[2] == rng.partition(":")[2], pname
                assert m.lower <= prop["min"], pname
                assert prop["max"] is None or m.upper is None or prop["max"] <= m.upper
    assert classes == EU_CLASSES
    assert props == EU_PROPERTIES
    assert ranges == EU_RANGES


def test_every_cim_class_and_in_profile_target_exists():
    snap = json.loads(
        resources.files("cim_python_sdk.profiles").joinpath("data/cgmes_3_0.json").read_text("utf-8")
    )
    for p in snap["profiles"].values():
        for cname, c in p["classes"].items():
            if c["ns"] == "cim":
                assert cname in BY_NAME
            for prop in c["properties"].values():
                if prop["kind"] == "association" and prop["range"].startswith("cim:"):
                    assert prop["range"][4:] in BY_NAME
