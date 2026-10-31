"""CIM JSON-LD writer/reader tests: round trips, CIMXML equivalence, rules, tolerance, speed."""

from __future__ import annotations

import datetime as dt
import io
import json
import math
import time
from decimal import Decimal

import pytest

import cim_python_sdk
from cim_python_sdk.serialization import (
    CimJsonLdError,
    read_cimxml,
    read_jsonld,
    to_cimxml_string,
    to_jsonld_dict,
    to_jsonld_string,
    write_cimxml,
    write_jsonld,
)
from cim_python_sdk.serialization import _common as common
from tests.serialization.network import build_network, roots


def _read(text: str, **kw):
    return read_jsonld(io.BytesIO(text.encode()), **kw)


def _xml_doc(objs, **kw):
    return read_cimxml(io.BytesIO(to_cimxml_string(objs, **kw).encode()))


def _dump(doc):
    return common.canonical_dump(doc.objects, include_reachable=False)


def _node(d, ident):
    return next(n for n in d["@graph"] if n["@id"] == ident)


# --- round trip ------------------------------------------------------------------------


def test_roundtrip_canonical_dump():
    net = build_network()
    doc = _read(to_jsonld_string(roots(net)))
    assert doc.warnings == [] and doc.dangling == []
    orig = common.canonical_dump(roots(net))
    assert orig == _dump(doc)
    assert len(orig) == len(doc.objects) >= 25
    line = doc.by_id["line-1"]
    assert type(line) is cim_python_sdk.ACLineSegment and line.length == 12.5 and line.in_service is True
    assert [o.amount for o in doc.objects if isinstance(o, cim_python_sdk.Price)] == [Decimal("12.3400")]
    assert doc.by_id["tariff-1"].start_date == dt.date(2025, 1, 2)
    assert doc.by_id["shunt-1"].switch_on_date == dt.datetime(2024, 5, 6, 7, 8, 9)
    assert doc.by_id["shunt-1"].maximum_sections == 4
    assert doc.by_id["phase-1"].phase is cim_python_sdk.SinglePhaseKind.A
    assert doc.by_id["pte-1"].connection_kind is cim_python_sdk.WindingConnection.D
    addr = doc.by_id["loc-1"].main_address
    assert isinstance(addr, cim_python_sdk.StreetAddress) and addr.po_box == "Box <1> & 2"
    # N:M, 1:1 and self-association-style links
    assert doc.by_id["tx-1"].assets == (doc.by_id["asset-1"],)
    assert doc.by_id["pte-1"].ratio_tap_changer is doc.by_id["rtc-1"]
    loc = doc.by_id["loc-1"]
    assert len(loc.position_points) == 2 and all(p.location is loc for p in loc.position_points)


def _find_self_association():
    from cim_python_sdk._runtime import all_metas

    for name in sorted(dir(cim_python_sdk)):
        cls = getattr(cim_python_sdk, name, None)
        if not (isinstance(cls, type) and hasattr(cls, "_cim_meta") and hasattr(cls, "mrid")):
            continue
        for m in all_metas(cls):
            if m.cim_name != cls._cim_meta.cim_name:
                continue
            for e in m.ends:
                if getattr(cls, e.name).inverse.owner is cls:
                    return cls, e.name
    return None


def test_self_association_roundtrip():
    found = _find_self_association()
    assert found is not None
    cls, end = found
    x, y = cls(mrid="self-x"), cls(mrid="self-y")
    desc = getattr(cls, end)
    if desc.meta.many:
        desc.add(x, y)
    else:
        setattr(x, end, y)
    doc = _read(to_jsonld_string([x]))
    assert common.canonical_dump([x]) == _dump(doc) and len(doc.objects) == 2
    assert doc.warnings == []


def test_both_ends_restored_and_written_once():
    net = build_network()
    d = to_jsonld_dict(roots(net))
    text = json.dumps(d)
    assert (
        "cim:Terminal.ConductingEquipment" in text and "ConductingEquipment.Terminals" not in text
    )
    assert (
        "cim:RatioTapChanger.TransformerEnd" in text
        and "TransformerEnd.RatioTapChanger" not in text
    )
    assert text.count("Asset.PowerSystemResources") + text.count(
        "PowerSystemResource.Assets"
    ) == 2 or (("Asset.PowerSystemResources" in text) != ("PowerSystemResource.Assets" in text))
    assert "cim:IdentifiedObject.name" in text and "cim:ACLineSegment.name" not in text
    d2 = to_jsonld_dict(roots(net), write_both_ends=True)
    assert "ConductingEquipment.Terminals" in json.dumps(d2)
    doc = _read(json.dumps(d2))
    assert common.canonical_dump(roots(net)) == _dump(doc)
    assert len(doc.by_id["line-1"].terminals) == 2  # no duplicates from the two-sided links


def test_structure_context_arrays_compounds():
    net = build_network()
    d = to_jsonld_dict(roots(net))
    assert list(d) == ["@context", "@graph"]
    ctx = d["@context"]
    assert list(ctx) == ["cim", "rdf", "md", "xsd"] and ctx["cim"] == common.CIM_NS
    asset = _node(d, "#_asset-1")
    assert asset["@type"] == "cim:Asset"
    ends = [k for k in asset if k.endswith("PowerSystemResources")]
    if ends:  # N:M written on this side: an array even with one target
        assert isinstance(asset[ends[0]], list) and all(set(e) == {"@id"} for e in asset[ends[0]])
    else:
        tx = _node(d, "#_tx-1")
        assert isinstance(tx["cim:PowerSystemResource.Assets"], list)
    loc = _node(d, "#_loc-1")
    addr = loc["cim:Location.mainAddress"]
    assert "@id" not in addr and addr["@type"] == "cim:StreetAddress"
    assert addr["cim:StreetAddress.postalCode"] == "2000"
    phase = _node(d, "#_phase-1")
    assert phase["cim:ACLineSegmentPhase.phase"] == {"@id": "cim:SinglePhaseKind.A"}
    assert phase["cim:IdentifiedObject.mRID"] == "phase-1"
    line = _node(d, "#_line-1")
    assert line["cim:Conductor.length"] == 12.5 and line["cim:Equipment.inService"] is True
    assert line["cim:Equipment.EquipmentContainer"] == {"@id": "#_feeder-1"}
    shunt = _node(d, "#_shunt-1")
    assert shunt["cim:ShuntCompensator.switchOnDate"] == {
        "@value": "2024-05-06T07:08:09",
        "@type": "xsd:dateTime",
    }
    price = next(n for n in d["@graph"] if n["@type"] == "cim:Price")
    assert price["cim:Price.amount"] == "12.3400"  # Decimal is a string (DIGIN)
    assert price["@id"].startswith("_:gen")  # no mrid: blank node, no mRID property
    assert "cim:IdentifiedObject.mRID" not in price


def test_uuid_ids_use_urn():
    u = "123e4567-e89b-12d3-a456-426614174000"
    sub = cim_python_sdk.Substation(mrid=u)
    line = cim_python_sdk.ACLineSegment(mrid="l", equipment_container=sub)
    d = to_jsonld_dict([line])
    assert _node(d, f"urn:uuid:{u}")["@type"] == "cim:Substation"
    assert _node(d, "#_l")["cim:Equipment.EquipmentContainer"] == {"@id": f"urn:uuid:{u}"}
    assert sorted(_read(json.dumps(d)).by_id) == sorted([u, "l"])


def test_no_mrid_objects_get_generated_ids():
    net = build_network()
    text = to_jsonld_string(roots(net))
    assert '"_:gen0"' in text and '"_:gen1"' in text
    doc = _read(text)
    pts = [o for o in doc.objects if isinstance(o, cim_python_sdk.PositionPoint)]
    assert len(pts) == 2 and not hasattr(pts[0], "mrid")
    assert {i for i, o in doc.by_id.items() if isinstance(o, cim_python_sdk.PositionPoint)} == {
        "gen0",
        "gen1",
    }
    assert to_jsonld_string(roots(build_network())) == text  # independent of construction order


def test_float_special_values_decimal_datetime():
    seg = cim_python_sdk.ACLineSegment(
        mrid="s", length=float("inf"), r=float("nan"), x=-0.0, b0ch=-math.inf, in_service=False
    )
    text = to_jsonld_string([seg])
    d = json.loads(text)  # valid JSON: no bare NaN / Infinity
    assert "NaN," not in text.replace('"NaN"', "") and "Infinity" not in text
    n = d["@graph"][0]
    assert n["cim:Conductor.length"] == {"@value": "INF", "@type": "xsd:double"}
    assert n["cim:ACLineSegment.r"] == {"@value": "NaN", "@type": "xsd:double"}
    assert n["cim:ACLineSegment.b0ch"] == {"@value": "-INF", "@type": "xsd:double"}
    assert n["cim:ACLineSegment.x"] == 0.0 and math.copysign(1, n["cim:ACLineSegment.x"]) == -1
    back = _read(text).by_id["s"]
    assert back.length == math.inf and back.b0ch == -math.inf and math.isnan(back.r)
    assert math.copysign(1, back.x) == -1 and back.in_service is False
    # exact float and datetime/date/time/Decimal values
    t = cim_python_sdk.Tariff(mrid="t", start_date=dt.date(2025, 1, 2))
    sh = cim_python_sdk.LinearShuntCompensator(
        mrid="sh", b_per_section=1e-300, switch_on_date=dt.datetime(2024, 5, 6, 7, 8, 9, 123456)
    )
    p = cim_python_sdk.Price(amount=Decimal("0.1000000000000000000001"))
    doc = _read(to_jsonld_string([t, sh, p]))
    assert doc.by_id["sh"].b_per_section == 1e-300
    assert doc.by_id["sh"].switch_on_date == dt.datetime(2024, 5, 6, 7, 8, 9, 123456)
    assert doc.by_id["t"].start_date == dt.date(2025, 1, 2)
    assert next(o for o in doc.objects if isinstance(o, cim_python_sdk.Price)).amount == Decimal(
        "0.1000000000000000000001"
    )


def test_unset_default_is_not_reintroduced():
    G = cim_python_sdk.GenericDataSetVersion
    default = G().major_version
    assert default is not None
    doc = _read(to_jsonld_string([G(major_version=None), G()]))
    assert sorted((o.major_version for o in doc.objects), key=str) == sorted(
        [None, default], key=str
    )


def test_control_characters_and_unicode_are_fine_in_jsonld():
    text = "a\x00b\x01\x1f￾\r\n\t é\U0001f600"
    obj = cim_python_sdk.ACLineSegment(mrid="s", name=text)
    s = to_jsonld_string([obj])
    json.loads(s)
    assert _read(s).by_id["s"].name == text


@pytest.mark.parametrize("mrid", ["a#b", "a b", "1abc", "x/y:z", "50%off", "é", "_lead", "a?b"])
def test_unusual_mrids_roundtrip(mrid):
    sub = cim_python_sdk.Substation(mrid=mrid)
    line = cim_python_sdk.ACLineSegment(mrid=mrid + "!", equipment_container=sub)
    cim_python_sdk.Terminal(mrid=mrid + "-t", conducting_equipment=line)
    doc = _read(to_jsonld_string([sub]))
    assert doc.warnings == [] and doc.dangling == []
    assert sorted(doc.by_id) == sorted([mrid, mrid + "!", mrid + "-t"])
    assert doc.by_id[mrid + "!"].equipment_container is doc.by_id[mrid]


# --- determinism and file objects --------------------------------------------------------


def test_deterministic_bytes_and_valid_json(tmp_path):
    net = build_network()
    a, b = tmp_path / "a.jsonld", tmp_path / "b.jsonld"
    write_jsonld(roots(net), a)
    write_jsonld(list(reversed(roots(net))), b)
    assert a.read_bytes() == b.read_bytes()
    data = a.read_bytes()
    assert json.loads(data)["@graph"]
    assert data.startswith(b'{\n  "@context"') and data.endswith(b"}\n")
    assert to_jsonld_string(roots(net)).encode() == data
    assert json.dumps(to_jsonld_dict(roots(net)), indent=2, ensure_ascii=False) + "\n" == (
        data.decode()
    )
    compact = to_jsonld_string(roots(net), indent=None)
    assert "\n" not in compact.rstrip("\n") and json.loads(compact) == json.loads(data)


def test_include_reachable_false_and_file_objects():
    net = build_network()
    text = to_jsonld_string([net["line"], net["t1"]], include_reachable=False)
    doc = _read(text)
    assert sorted(doc.by_id) == ["line-1", net["t1"].mrid]
    assert doc.dangling == []
    assert doc.by_id[net["t1"].mrid].conducting_equipment is doc.by_id["line-1"]
    buf, tbuf = io.BytesIO(), io.StringIO()
    write_jsonld([net["line"]], buf, include_reachable=False)
    write_jsonld([net["line"]], tbuf, include_reachable=False)
    assert buf.getvalue().decode() == tbuf.getvalue()
    assert read_jsonld(io.StringIO(tbuf.getvalue())).by_id["line-1"].length == 12.5


def test_custom_namespace():
    net = build_network()
    d = to_jsonld_dict([net["phase"]], namespace="http://example.org/cim#", include_reachable=False)
    assert d["@context"]["cim"] == "http://example.org/cim#"
    assert _read(json.dumps(d)).by_id["phase-1"].phase is cim_python_sdk.SinglePhaseKind.A


# --- header ------------------------------------------------------------------------------


HEADER = {
    "created": dt.datetime(2026, 1, 2, 3, 4, 5),
    "scenarioTime": "2026-01-02T03:00:00Z",
    "description": "Test model",
    "version": "3",
    "modelingAuthoritySet": "http://example.org/mas",
    "profile": ["http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0", "other"],
    "DependentOn": ["urn:uuid:1234", "urn:uuid:5678"],
}


def test_header():
    net = build_network()
    text = to_jsonld_string([net["sub"]], header=HEADER)
    d = json.loads(text)
    assert d["@type"] == "dcat:Dataset" and d["@id"].startswith("urn:uuid:")
    assert d["prov:generatedAtTime"] == {"@value": "2026-01-02T03:04:05", "@type": "xsd:dateTime"}
    assert d["dcterms:issued"] == {"@value": "2026-01-02", "@type": "xsd:date"}
    assert d["dcterms:description"] == [{"@value": "Test model", "@language": "en"}]
    assert d["dcterms:temporal"]["dcat:startDate"]["@value"] == "2026-01-02T03:00:00Z"
    assert d["dcterms:conformsTo"][1] == {"@id": "other"}
    assert d["dcterms:references"] == [{"@id": "urn:uuid:1234"}, {"@id": "urn:uuid:5678"}]
    assert d["dcat:isVersionOf"] == {"@id": "http://example.org/mas"}
    assert "dcterms" in d["@context"]
    assert "dcat:Dataset" not in to_jsonld_string([net["sub"]])
    doc = _read(text)
    assert doc.by_id["sub-1"].name == "Zone Sub" and len(doc.objects) == len(
        common.collect([net["sub"]])
    )
    # the same header read from CIMXML and from JSON-LD is equal (created is text in both)
    xml_h = _xml_doc([net["sub"]], header={**HEADER, "about": doc.header["about"]}).header
    assert doc.header == xml_h | {"created": "2026-01-02T03:04:05"}
    assert to_jsonld_string([net["sub"]], header=HEADER) == text


def test_header_keeps_unknown_terms_and_rewrites_them():
    text = """{
      "@context": {"cim": "http://iec.ch/TC57/CIM100#", "dcterms": "http://purl.org/dc/terms/"},
      "@id": "urn:uuid:abc", "@type": "dcat:Dataset",
      "dcterms:title": "My model",
      "dcterms:description": [{"@value": "hei", "@language": "nb"}, {"@value": "hello", "@language": "en"}],
      "@graph": []
    }"""
    doc = _read(text)
    assert doc.header == {
        "about": "urn:uuid:abc",
        "description": "hello",
        "dcterms:title": "My model",
    }
    out = json.loads(to_jsonld_string([], header=doc.header))
    assert out["dcterms:title"] == "My model" and out["@id"] == "urn:uuid:abc"


# --- equivalence with CIMXML -------------------------------------------------------------


def test_cimxml_and_jsonld_give_equal_canonical_dump():
    net = build_network()
    xml_doc = _xml_doc(roots(net))
    json_doc = _read(to_jsonld_string(roots(net)))
    assert xml_doc.warnings == [] and json_doc.warnings == []
    assert _dump(xml_doc) == _dump(json_doc) == common.canonical_dump(roots(net))
    assert sorted(xml_doc.by_id) == sorted(json_doc.by_id)


def test_cross_conversion_both_ways(tmp_path):
    net = build_network()
    write_cimxml(roots(net), tmp_path / "n.xml")
    d1 = read_cimxml(tmp_path / "n.xml")
    write_jsonld(d1.objects, tmp_path / "n.jsonld")
    d2 = read_jsonld(tmp_path / "n.jsonld")
    assert d2.warnings == [] and _dump(d1) == _dump(d2) == common.canonical_dump(roots(net))
    write_cimxml(d2.objects, tmp_path / "m.xml")
    d3 = read_cimxml(tmp_path / "m.xml")
    assert _dump(d3) == _dump(d1)
    # mrid-less objects keep their generated ids in both formats
    assert (tmp_path / "n.xml").read_bytes() == (tmp_path / "m.xml").read_bytes()


# --- hand-written documents --------------------------------------------------------------

DIGIN = """
{
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "cim": "https://cim.ucaiug.io/ns#",
        "eu": "https://cim.ucaiug.io/ns/eu#",
        "dcterms": "http://purl.org/dc/terms/",
        "dcat": "http://www.w3.org/ns/dcat#",
        "prov": "http://www.w3.org/ns/prov#",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "@id": "urn:uuid:c47d4310-b8ee-480d-9cf3-e53a81630981",
    "@type": "dcat:Dataset",
    "prov:generatedAtTime": {"@value": "2023-10-26T10:35:31Z", "@type": "xsd:dateTime"},
    "dcterms:issued": {"@value": "2022-03-30T16:26:37.958Z", "@type": "xsd:date"},
    "dcterms:title": "Telemark-120-LV1_EQ",
    "dcterms:description": [{"@value": "Core Equipment model", "@language": "en"}],
    "dcat:isVersionOf": {"@id": "https://digin.no/baseprofile/Telemark-120-LV1_EQ"},
    "dcterms:conformsTo": [{"@id": "http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0"}],
    "dcterms:references": [{"@id": "urn:uuid:e766c722-d2db-41cc-93e4-74b1f161c13a"}],
    "@graph": [
        {
            "@id": "urn:uuid:9d58e5bb-834c-4faa-928c-7da0bb1497d9",
            "@type": "cim:ACLineSegment",
            "cim:IdentifiedObject.mRID": "9d58e5bb-834c-4faa-928c-7da0bb1497d9",
            "cim:IdentifiedObject.description": "400V line",
            "cim:IdentifiedObject.name": "04 TELEMA2 ACLS1",
            "cim:Equipment.aggregate": false,
            "cim:Equipment.normallyInService": true,
            "cim:Conductor.length": 0.050,
            "cim:ACLineSegment.bch": 0,
            "cim:ACLineSegment.r": 0.015999999945951,
            "cim:ACLineSegment.x": 0.003769911221053,
            "eu:Equipment.networkAnalysisEnabled": true,
            "cim:PowerSystemResource.AssetDatasheet": {"@id": "urn:uuid:d25f35ca-69fb-4c06-905b-67ec532e5f14"},
            "cim:Equipment.EquipmentContainer": {"@id": "urn:uuid:64e21d95-8b55-b941-a923-b74087410a66"}
        },
        {
            "@id": "urn:uuid:64e21d95-8b55-b941-a923-b74087410a66",
            "@type": "cim:Feeder",
            "cim:IdentifiedObject.name": "Feeder 1"
        },
        {
            "@id": "urn:uuid:a1a1a1a1-b8ee-480d-9cf3-e53a81630981",
            "@type": "cim:Terminal",
            "cim:ACDCTerminal.sequenceNumber": 2,
            "cim:Terminal.phases": {"@id": "cim:PhaseCode.ABCN"},
            "cim:Terminal.ConductingEquipment": {"@id": "urn:uuid:9d58e5bb-834c-4faa-928c-7da0bb1497d9"}
        }
    ]
}
"""


def test_digin_style_snippet():
    doc = _read(DIGIN)
    line = doc.by_id["9d58e5bb-834c-4faa-928c-7da0bb1497d9"]
    assert type(line) is cim_python_sdk.ACLineSegment
    assert line.name == "04 TELEMA2 ACLS1" and line.length == 0.05 and line.bch == 0.0
    assert isinstance(line.bch, float) and line.r == 0.015999999945951
    assert line.equipment_container is doc.by_id["64e21d95-8b55-b941-a923-b74087410a66"]
    term = doc.by_id["a1a1a1a1-b8ee-480d-9cf3-e53a81630981"]
    assert term.phases is cim_python_sdk.PhaseCode.ABCN and term.sequence_number == 2
    assert term.conducting_equipment is line and line.terminals == (term,)
    assert doc.header == {
        "created": "2023-10-26T10:35:31Z",
        "about": "urn:uuid:c47d4310-b8ee-480d-9cf3-e53a81630981",
        "modelingAuthoritySet": "https://digin.no/baseprofile/Telemark-120-LV1_EQ",
        "description": "Core Equipment model",
        "profile": "http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0",
        "DependentOn": "urn:uuid:e766c722-d2db-41cc-93e4-74b1f161c13a",
        "dcterms:title": "Telemark-120-LV1_EQ",
    }
    # eu: is read as CIM vocabulary by local name (C2), so DIGIN's eu:Equipment.networkAnalysisEnabled
    # lands on the CIM100 attribute; the asset datasheet is not in the document
    assert line.network_analysis_enabled is True
    assert not any("networkAnalysisEnabled" in w for w in doc.warnings)
    assert any(
        "dangling reference in PowerSystemResource.AssetDatasheet" in w for w in doc.warnings
    )
    assert [d[1] for d in doc.dangling] == ["PowerSystemResource.AssetDatasheet"]


def test_identifier_forms_and_top_level_shapes():
    items = [
        {"@id": "_a", "@type": "cim:ACLineSegment", "cim:IdentifiedObject.name": "A"},
        {"@id": "#_b", "@type": "cim:ACLineSegment"},
        {"@id": "urn:uuid:ccc", "@type": "cim:ACLineSegment"},
        {"@id": "_:d", "@type": "cim:ACLineSegment"},
        {"@id": "http://ex.org/data.jsonld#_e", "@type": "cim:ACLineSegment"},
        {"@id": "ex:f", "@type": "cim:ACLineSegment"},
        {"@id": "t1", "@type": "cim:Terminal", "cim:Terminal.ConductingEquipment": {"@id": "_a"}},
        {"@id": "t2", "@type": "cim:Terminal", "cim:Terminal.ConductingEquipment": "#b"},
        {
            "@id": "t3",
            "@type": "cim:Terminal",
            "cim:Terminal.ConductingEquipment": {"@id": "urn:uuid:ccc"},
        },
        {"@id": "t4", "@type": "cim:Terminal", "cim:Terminal.ConductingEquipment": {"@id": "ex:f"}},
    ]
    ctx = {"cim": "http://iec.ch/TC57/CIM100#", "ex": "http://example.org/"}
    for text in (
        json.dumps({"@context": ctx, "@graph": items}),
        json.dumps({"@context": [ctx], "@graph": items}),
        json.dumps([{"@context": ctx}, *items]),
        json.dumps({"@context": ctx, "@graph": items[:0] or items}),
    ):
        doc = _read(text)
        assert doc.warnings == [], doc.warnings
        assert sorted(doc.by_id) == ["a", "b", "ccc", "d", "e", "f", "t1", "t2", "t3", "t4"]
        assert doc.by_id["a"].name == "A"
        assert doc.by_id["t1"].conducting_equipment is doc.by_id["a"]
        assert doc.by_id["t2"].conducting_equipment is doc.by_id["b"]
        assert doc.by_id["t3"].conducting_equipment is doc.by_id["ccc"]
        assert doc.by_id["t4"].conducting_equipment is doc.by_id["f"]
    single = _read(json.dumps({"@id": "x", "@type": "cim:Substation"}))
    assert list(single.by_id) == ["x"] and single.warnings == []
    assert (
        _read("[]").objects == [] and _read('{"@graph": {"@id": "y", "@type": "cim:Feeder"}}').by_id
    )


def test_vocab_aliases_and_unprefixed_properties():
    text = json.dumps(
        {
            "@context": {
                "@vocab": "http://iec.ch/TC57/CIM100#",
                "label": "cim:IdentifiedObject.name",
                "len": {"@id": "Conductor.length"},
            },
            "@graph": [
                {
                    "@id": "l",
                    "@type": "ACLineSegment",
                    "IdentifiedObject.description": "d",
                    "label": "named",
                    "len": 3,
                    "Equipment.EquipmentContainer": {"@id": "f"},
                },
                {"@id": "f", "@type": ["Feeder"]},
                {
                    "@id": "p",
                    "@type": "http://iec.ch/TC57/CIM100#Terminal",
                    "http://iec.ch/TC57/CIM100#Terminal.phases": {
                        "@id": "http://iec.ch/TC57/CIM100#PhaseCode.AB"
                    },
                },
            ],
        }
    )
    doc = _read(text)
    assert doc.warnings == []
    line = doc.by_id["l"]
    assert (line.name, line.description, line.length) == ("named", "d", 3.0)
    assert isinstance(line.length, float) and line.equipment_container is doc.by_id["f"]
    assert doc.by_id["p"].phases is cim_python_sdk.PhaseCode.AB
    # without @vocab an unprefixed property is unknown
    bad = _read('{"@graph": [{"@id": "l", "@type": "cim:ACLineSegment", "name": "x"}]}')
    assert bad.warnings == ["unknown property 'name' on ACLineSegment"] or any(
        "unknown property" in w for w in bad.warnings
    )


def test_association_on_wrong_end_and_scalar_forms():
    doc = _read(
        json.dumps(
            {
                "@context": {"cim": "http://iec.ch/TC57/CIM100#"},
                "@graph": [
                    {
                        "@id": "l",
                        "@type": "cim:ACLineSegment",
                        "cim:ConductingEquipment.Terminals": [{"@id": "t1"}, {"@id": "t2"}],
                        "cim:Conductor.length": "12.5",
                        "cim:ACLineSegment.r": {"@value": "3", "@type": "xsd:double"},
                    },
                    {"@id": "t1", "@type": "cim:Terminal", "cim:ACDCTerminal.sequenceNumber": 4.0},
                    {
                        "@id": "t2",
                        "@type": "cim:Terminal",
                        "cim:Terminal.ConductingEquipment": [{"@id": "l"}],
                        "cim:ACDCTerminal.connected": "true",
                    },
                ],
            }
        )
    )
    assert doc.warnings == []
    line = doc.by_id["l"]
    assert set(line.terminals) == {doc.by_id["t1"], doc.by_id["t2"]} and len(line.terminals) == 2
    assert line.length == 12.5 and line.r == 3.0
    assert doc.by_id["t1"].sequence_number == 4 and doc.by_id["t2"].connected is True


def test_unknown_class_property_and_bad_literal():
    doc = _read(
        json.dumps(
            {
                "@context": {"cim": "http://iec.ch/TC57/CIM100#"},
                "@graph": [
                    {"@id": "x", "@type": "cim:Spaceship"},
                    {"@id": "y", "@type": "cim:Spaceship"},
                    {"@type": "cim:Substation"},
                    {"@id": "nt"},
                    "stray",
                    {
                        "@id": "l",
                        "@type": "cim:ACLineSegment",
                        "cim:ACLineSegment.warpDrive": 9,
                        "cim:Conductor.length": 12.5,
                        "cim:ACLineSegment.r": "not-a-number",
                        "cim:ACLineSegment.x": [1, 2],
                        "cim:IdentifiedObject.name": "ok",
                    },
                ],
            }
        )
    )
    assert [o.mrid for o in doc.objects] == ["l"]
    assert doc.by_id["l"].name == "ok" and doc.by_id["l"].length == 12.5
    assert doc.by_id["l"].r is None and doc.by_id["l"].x is None
    text = "\n".join(doc.warnings)
    assert "unknown class 'cim:Spaceship'" in text and "(x2)" in text
    assert "unknown property 'ACLineSegment.warpDrive'" in text
    assert "ACLineSegment: ACLineSegment.r: cannot parse 'not-a-number' as Resistance" in text
    assert "without @id" in text and "not an object" in text and "several values" in text


def test_dangling_type_mismatch_and_enum_and_compound_forms():
    doc = _read(
        json.dumps(
            {
                "@context": {"cim": "http://iec.ch/TC57/CIM100#"},
                "@graph": [
                    {
                        "@id": "t",
                        "@type": "cim:Terminal",
                        "cim:Terminal.ConductingEquipment": {"@id": "missing"},
                    },
                    {"@id": "s", "@type": "cim:Substation"},
                    {
                        "@id": "u",
                        "@type": "cim:Terminal",
                        "cim:Terminal.ConductingEquipment": {"@id": "s"},
                    },
                    {
                        "@id": "e1",
                        "@type": "cim:Terminal",
                        "cim:Terminal.phases": "cim:PhaseCode.AB",
                    },
                    {
                        "@id": "e2",
                        "@type": "cim:Terminal",
                        "cim:Terminal.phases": {"@id": "cim:PhaseCode.Nope"},
                    },
                    {
                        "@id": "loc",
                        "@type": "cim:Location",
                        "cim:Location.mainAddress": {"cim:StreetAddress.postalCode": "3000"},
                    },
                ],
            }
        )
    )
    assert doc.dangling == [("t", "Terminal.ConductingEquipment", "missing")]
    assert doc.by_id["t"].conducting_equipment is None
    assert any("cannot link" in w for w in doc.warnings)
    assert doc.by_id["e1"].phases is cim_python_sdk.PhaseCode.AB
    assert doc.by_id["e2"].phases is None and any("unknown enum value" in w for w in doc.warnings)
    assert doc.by_id["loc"].main_address.postal_code == "3000"


def test_strict_and_malformed():
    ctx = '"@context": {"cim": "http://iec.ch/TC57/CIM100#"}'
    with pytest.raises(CimJsonLdError, match="Spaceship"):
        _read(f'{{{ctx}, "@graph": [{{"@id": "x", "@type": "cim:Spaceship"}}]}}', strict=True)
    with pytest.raises(CimJsonLdError, match="unknown property"):
        _read(
            f'{{{ctx}, "@graph": [{{"@id": "x", "@type": "cim:Terminal", "cim:Terminal.nope": 1}}]}}',
            strict=True,
        )
    with pytest.raises(CimJsonLdError, match="dangling"):
        _read(
            f'{{{ctx}, "@graph": [{{"@id": "x", "@type": "cim:Terminal", '
            '"cim:Terminal.ConductingEquipment": {"@id": "q"}}]}',
            strict=True,
        )
    with pytest.raises(CimJsonLdError, match="not valid JSON"):
        _read("{not json")
    with pytest.raises(CimJsonLdError, match="expected object or array"):
        _read("3")
    with pytest.raises(CimJsonLdError, match="@graph must be an array"):
        _read('{"@graph": 3}')
    assert isinstance(CimJsonLdError("x"), ValueError)


def test_duplicate_cim_names_resolve_to_canonical():
    from cim_python_sdk.model.iec61968.doc_iec61968.iec61968_cim_version_2 import (
        IEC61968CIMVersion_2,
    )

    text = to_jsonld_string([IEC61968CIMVersion_2()])
    assert '"cim:IEC61968CIMVersion"' in text
    assert type(_read(text).objects[0]) is cim_python_sdk.IEC61968CIMVersion


def test_roleless_end_warns_once_per_end_per_call():
    objs = []
    for i in range(3):
        a = cim_python_sdk.AssemblyManifest(mrid=f"am{i}")
        a.add_model_part_version(cim_python_sdk.ModelPartVersion(mrid=f"mpv{i}"))
        objs.append(a)
    with pytest.warns(UserWarning) as rec:
        text = to_jsonld_string(objs)
    msgs = [str(w.message) for w in rec if "AssemblyManifest.model_part_versions" in str(w.message)]
    assert len(msgs) == 1 and "no CIM role" in msgs[0]
    doc = _read(text)
    assert common.canonical_dump(objs) == _dump(doc)


# --- optional: prove the output is valid JSON-LD with pyld -------------------------------


def test_pyld_expands_output():
    jsonld = pytest.importorskip("pyld.jsonld")
    net = build_network()
    ns = common.CIM_NS
    opts = {"base": "http://example.org/data"}

    def check(nodes):
        assert len(nodes) >= 25
        line = next(n for n in nodes if n["@id"].endswith("#_line-1"))
        assert line["@type"] == [ns + "ACLineSegment"]
        assert line[ns + "Conductor.length"][0]["@value"] == 12.5
        phase = next(n for n in nodes if n["@id"].endswith("#_phase-1"))
        assert phase[ns + "ACLineSegmentPhase.phase"][0]["@id"] == ns + "SinglePhaseKind.A"
        sh = next(n for n in nodes if n["@id"].endswith("#_shunt-1"))
        dtv = sh[ns + "ShuntCompensator.switchOnDate"][0]
        assert dtv["@type"] == "http://www.w3.org/2001/XMLSchema#dateTime"
        assert any(n["@id"].startswith("_:") for n in nodes)  # the mrid-less objects

    check(jsonld.expand(to_jsonld_dict(roots(net)), opts))
    # with a header the dataset node carries the objects as its named graph
    expanded = jsonld.expand(to_jsonld_dict(roots(net), header=HEADER), opts)
    assert len(expanded) == 1 and "http://www.w3.org/ns/dcat#Dataset" in expanded[0]["@type"][0]
    check(expanded[0]["@graph"])
    # the typed NaN literal survives expansion
    seg = cim_python_sdk.ACLineSegment(mrid="s", r=float("nan"))
    (node,) = jsonld.expand(to_jsonld_dict([seg]), opts)
    assert node[ns + "ACLineSegment.r"][0] == {
        "@value": "NaN",
        "@type": "http://www.w3.org/2001/XMLSchema#double",
    }


# --- performance -------------------------------------------------------------------------


def test_performance_50k_objects(tmp_path, capsys):
    sub = cim_python_sdk.Substation(name="S")
    bv = cim_python_sdk.BaseVoltage(nominal_voltage=11000.0)
    nodes = [cim_python_sdk.ConnectivityNode(name=f"n{i}") for i in range(8000)]
    n_objs = 2 + len(nodes)
    for i in range(8000):
        line = cim_python_sdk.ACLineSegment(
            name=f"l{i}", length=float(i), equipment_container=sub, base_voltage=bv
        )
        for seq, j in ((1, i), (2, (i + 1) % 8000)):
            cim_python_sdk.Terminal(
                sequence_number=seq,
                phases=cim_python_sdk.PhaseCode.ABC,
                conducting_equipment=line,
                connectivity_node=nodes[j],
            )
        loc = cim_python_sdk.Location(type="x", main_address=cim_python_sdk.StreetAddress(postal_code="1"))
        line.location = loc
        cim_python_sdk.PositionPoint(sequence_number=1, location=loc)
        cim_python_sdk.PositionPoint(sequence_number=2, location=loc)
        n_objs += 6
    path = tmp_path / "big.jsonld"
    xml_path = tmp_path / "big.xml"
    t0 = time.perf_counter()
    write_jsonld([sub], path)
    t1 = time.perf_counter()
    doc = read_jsonld(path)
    t2 = time.perf_counter()
    write_cimxml([sub], xml_path)
    t3 = time.perf_counter()
    xdoc = read_cimxml(xml_path)
    t4 = time.perf_counter()
    with capsys.disabled():
        print(
            f"\nperf JSON-LD: {len(doc.objects)} objects, {path.stat().st_size / 1e6:.1f} MB; "
            f"write {t1 - t0:.1f}s, read {t2 - t1:.1f}s"
            f"  (CIMXML: {xml_path.stat().st_size / 1e6:.1f} MB; "
            f"write {t3 - t2:.1f}s, read {t4 - t3:.1f}s)"
        )
    assert len(doc.objects) == len(xdoc.objects) == n_objs > 50_000
    assert doc.warnings == []
    assert t1 - t0 < 60 and t2 - t1 < 60
