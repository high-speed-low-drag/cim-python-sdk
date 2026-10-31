"""Association direction: the profile snapshot against the generic serializer rule.

A profile writes an association on the class that owns the property (the snapshot key
``Class.Role``); no profile lists both ends. The generic CIMXML/JSON-LD writers pick the written
end with `association_write_end` (single-valued end first, else the name that sorts first). Of the
233 profile associations, the generic rule picks the other end for the nine below and for 45 of the
Dynamics profile. A profile (CGMES) writer must use the snapshot's owner, not `is_write_end`.
"""

import json
from importlib import resources

import cim_python_sdk
from cim_python_sdk.serialization._common import _end_key, resolve_property

DIFFERENT_FROM_GENERIC_RULE = {
    ("DL", "VisibilityLayer.VisibleObjects"),
    ("EQ", "PowerElectronicsConnection.PowerElectronicsUnit"),
    ("EQ", "ThermalGeneratingUnit.CAESPlant"),
    ("GL", "Location.PowerSystemResources"),
    ("OP", "AccumulatorLimitSet.Measurements"),
    ("OP", "AnalogLimitSet.Measurements"),
    ("OP", "MeasurementValueQuality.MeasurementValue"),
    ("SV", "DCTopologicalIsland.DCTopologicalNodes"),
    ("SV", "TopologicalIsland.TopologicalNodes"),
}


def _snapshot():
    text = resources.files("cim_python_sdk.profiles").joinpath("data/cgmes_3_0.json").read_text("utf-8")
    return json.loads(text)


def test_profile_association_direction_vs_generic_rule():
    snap = _snapshot()
    total = 0
    different = set()
    for kw, prof in snap["profiles"].items():
        owned = {
            pn
            for c in prof["classes"].values()
            for pn, v in c["properties"].items()
            if v["kind"] == "association"
        }
        for cname, c in prof["classes"].items():
            for pn, v in c["properties"].items():
                if v["kind"] != "association":
                    continue
                total += 1
                spec = resolve_property(getattr(cim_python_sdk, cname), pn)
                assert spec is not None, (kw, pn)
                assert _end_key(spec.desc.inverse) not in owned, f"{kw}: both ends of {pn}"
                if not spec.writes:
                    different.add((kw, pn))
    assert total == 233
    assert {d for d in different if d[0] != "DY"} == DIFFERENT_FROM_GENERIC_RULE
    assert sum(d[0] == "DY" for d in different) == 45
