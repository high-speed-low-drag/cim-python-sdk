"""The CGMES European extension IR (codegen/snapshot/eu_ir.json), its merge and its source pin.

Snapshot tests run offline; the live tests read the pinned CGMES EA model and skip when it is
not cached in build/profiles/ (``uv run python tools/fetch_profiles.py --schema``).
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

import pytest

from codegen import profile_source as ps
from codegen.ir import MergeError, merge
from codegen.normalize import (
    NormalizeError,
    load_eu_snapshot,
    load_model,
    load_snapshot,
    normalize,
)

ROOT = Path(__file__).resolve().parent.parent
IDENTIFIED_OBJECT = "{055C5806-E9D8-4a7a-9307-DAF7C31763C7}"
OPERATIONAL_LIMIT_TYPE = "{B5E14C75-6C8D-4e7e-9FAF-D49F3BE177B9}"
POWER_SYSTEM_RESOURCE = "{0340C084-3759-40cc-AAF2-386101DE842F}"


@pytest.fixture(scope="module")
def eu():
    return load_eu_snapshot()


@pytest.fixture(scope="module")
def base():
    return load_snapshot()


def _one(model, name):
    (c,) = [c for c in model.classifiers if c.name == name]
    return c


# ---------------------------------------------------------------- snapshot facts


def test_snapshot_contents(eu):
    assert eu.versions == {"ExtIEC61970Version": "3.0"}
    assert {c.namespace for c in eu.classifiers} == {"eu"}
    assert {a.namespace for c in eu.classifiers for a in c.attributes} == {"eu"}
    assert {a.namespace for a in eu.associations} == {"eu"}
    summary = {
        c.name: (c.kind, c.extends, [a.name for a in c.attributes] or [x.name for x in c.literals])
        for c in eu.classifiers
    }
    assert summary == {
        "BoundaryPoint": (
            "class",
            None,
            [
                "fromEndIsoCode",
                "fromEndName",
                "fromEndNameTso",
                "toEndIsoCode",
                "toEndName",
                "toEndNameTso",
                "isDirectCurrent",
                "isExcludedFromAreaInterchange",
            ],
        ),
        "ExtEuIdentifiedObject": ("class", IDENTIFIED_OBJECT, ["energyIdentCodeEic", "shortName"]),
        "ExtEuOperationalLimitType": ("class", OPERATIONAL_LIMIT_TYPE, ["kind"]),
        "LimitKind": (
            "enumeration",
            None,
            [
                "patl",
                "patlt",
                "tatl",
                "tc",
                "tct",
                "highVoltage",
                "lowVoltage",
                "operationalVoltageLimit",
                "alarmVoltage",
                "warningVoltage",
                "stability",
            ],
        ),
        "SolarPowerPlant": ("class", None, []),
        "WindPowerPlant": ("class", None, []),
    }
    for name in ("BoundaryPoint", "SolarPowerPlant", "WindPowerPlant"):
        assert _one(eu, name).superclass == POWER_SYSTEM_RESOURCE
    assert all(p.path.startswith("EuropeanCIMExtensions") for p in eu.packages)
    assert eu.stats["generalizations_skipped_out_of_scope"] == 1  # the NC ExtOperationalLimitType


def test_association_roles(eu, base):
    names = {c.guid: c.name for c in (*base.classifiers, *eu.classifiers)}
    ends = {
        (names[e.owner], e.role): (names[e.target], e.lower, e.upper)
        for a in eu.associations
        for e in a.ends
    }
    assert ends == {
        ("BoundaryPoint", "ConnectivityNode"): ("ConnectivityNode", 1, 1),
        ("ConnectivityNode", "BoundaryPoint"): ("BoundaryPoint", 0, 1),
        ("SolarPowerPlant", "SolarGeneratingUnits"): ("SolarGeneratingUnit", 0, None),
        ("SolarGeneratingUnit", "SolarPowerPlant"): ("SolarPowerPlant", 0, 1),
        ("WindPowerPlant", "WindGeneratingUnits"): ("WindGeneratingUnit", 0, None),
        ("WindGeneratingUnit", "WindPowerPlant"): ("WindPowerPlant", 0, 1),
    }


def test_merge(base, eu):
    m = load_model()
    assert m == merge(base, eu)
    assert len(m.classifiers) == len(base.classifiers) + 4  # extension classes are folded in
    assert not any(c.name.startswith("ExtEu") for c in m.classifiers)
    io = _one(m, "IdentifiedObject")
    assert [(a.name, a.namespace) for a in io.attributes][-2:] == [
        ("energyIdentCodeEic", "eu"),
        ("shortName", "eu"),
    ]
    assert io.namespace == "cim" and _one(m, "BoundaryPoint").namespace == "eu"
    assert m.versions["ExtIEC61970Version"] == "3.0"
    assert m.versions["IEC61970CIMVersion"] == "IEC61970CIM17v40"


def test_merge_rejects_conflicts(base, eu):
    with pytest.raises(MergeError, match="exists"):
        merge(base, base)
    bad = replace(_one(eu, "ExtEuIdentifiedObject"), extends="{nope}")
    others = tuple(c for c in eu.classifiers if c.name != "ExtEuIdentifiedObject")
    with pytest.raises(MergeError, match="unknown class"):
        merge(base, replace(eu, classifiers=(*others, bad)))


def test_normalize_rejects_a_name_in_two_namespaces(base, eu):
    bp = _one(eu, "BoundaryPoint")
    clash = replace(bp, name="ACLineSegment")
    others = tuple(c for c in eu.classifiers if c.name != "BoundaryPoint")
    with pytest.raises(NormalizeError, match="namespaces"):
        normalize(merge(base, replace(eu, classifiers=(*others, clash))))


def test_eu_modules():
    rm = normalize(load_model())
    mods = {c.cim_name: c.module for c in (*rm.classes, *rm.enums) if c.namespace == "eu"}
    assert mods == {
        "BoundaryPoint": "cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_core."
        "boundary_point",
        "LimitKind": "cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_operational_limits."
        "limit_kind",
        "SolarPowerPlant": "cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_generation."
        "ext_eu_production.solar_power_plant",
        "WindPowerPlant": "cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_generation."
        "ext_eu_production.wind_power_plant",
    }


# ---------------------------------------------------------------- source pin


def test_schema_pin():
    cfg = ps.load_source_config()
    s = cfg["schema"]
    assert s["file"] == "CIM17-2_CGMES31v01_PROF-20v02_NC23v66_MS10v01_DES10v01.qea"
    assert len(s["sha256"]) == 64 and s["size"] == 50151424
    assert ps.schema_url(cfg) == (
        "https://raw.githubusercontent.com/cimug-org/CGMES-CIM17/"
        "1c7708f5d3bde53e154201707f31961573868cf2/CGMES-CIM17/Schema/" + s["file"]
    )


def test_schema_download_verifies(tmp_path, monkeypatch):
    good = b"SQLite format 3\x00" + b"x" * 32
    cfg = {
        "schema": {
            "commit": "c0ffee",
            "file": "m.qea",
            "url": "https://example.invalid/{commit}/{file}",
            "sha256": hashlib.sha256(good).hexdigest(),
            "size": len(good),
        },
    }
    calls = []

    def fake(payload):
        def dl(url, out_path):
            calls.append(url)
            out_path.write_bytes(payload)

        return dl

    assert ps.cached_schema(tmp_path, cfg) is None
    monkeypatch.setattr(ps, "download", fake(b"<html>nope</html>"))
    with pytest.raises(ps.ProfileFetchError, match="not a SQLite"):
        ps.ensure_schema(tmp_path, config=cfg)
    monkeypatch.setattr(ps, "download", fake(good))
    path = ps.ensure_schema(tmp_path, config=cfg)
    assert path == tmp_path / "m.qea" and ps.cached_schema(tmp_path, cfg) == path
    ps.ensure_schema(tmp_path, config=cfg)
    assert calls == ["https://example.invalid/c0ffee/m.qea"] * 2  # second call was a cache hit
    assert not list(tmp_path.glob("*.part"))


# ---------------------------------------------------------------- live model


@pytest.mark.skipif(ps.cached_schema() is None, reason="CGMES EA model not in build/profiles/")
def test_dump_eu_ir_check_is_clean():
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "dump_eu_ir.py"), "--check"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stdout + r.stderr
