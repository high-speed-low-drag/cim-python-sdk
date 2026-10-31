"""CIMXML and JSON-LD with the CGMES European extensions (eu: classes, members and enum values)."""

from __future__ import annotations

import io
import json
import xml.etree.ElementTree as ET

import cim_python_sdk
from cim_python_sdk.serialization import _common as common
from cim_python_sdk.serialization import read_cimxml, read_jsonld, to_cimxml_string, to_jsonld_dict

CIM = "http://iec.ch/TC57/CIM100#"
EU = "http://iec.ch/TC57/CIM100-European#"


def _graph():
    cn = cim_python_sdk.ConnectivityNode(mrid="cn-1", name="CN1")
    bp = cim_python_sdk.BoundaryPoint(
        mrid="bp-1",
        name="BP1",
        short_name="BP1s",
        energy_ident_code_eic="10Y1001A1001A016",
        from_end_iso_code="NO",
        from_end_name="Sub A",
        from_end_name_tso="TSO A",
        to_end_iso_code="SE",
        to_end_name="Sub B",
        to_end_name_tso="TSO B",
        is_direct_current=False,
        is_excluded_from_area_interchange=True,
        connectivity_node=cn,
    )
    wpp = cim_python_sdk.WindPowerPlant(mrid="wpp-1", name="Wind")
    wgu = cim_python_sdk.WindGeneratingUnit(mrid="wgu-1", wind_power_plant=wpp)
    spp = cim_python_sdk.SolarPowerPlant(mrid="spp-1")
    sgu = cim_python_sdk.SolarGeneratingUnit(mrid="sgu-1", solar_power_plant=spp)
    olt = cim_python_sdk.OperationalLimitType(mrid="olt-1", kind=cim_python_sdk.LimitKind.tatl)
    line = cim_python_sdk.ACLineSegment(mrid="line-1", name="L1", short_name="L1s")
    return [bp, cn, wpp, wgu, spp, sgu, olt, line]


def _xml_roundtrip(objs):
    text = to_cimxml_string(objs)
    return text, read_cimxml(io.BytesIO(text.encode()), strict=True)


def test_cimxml_writes_eu_namespace():
    text, _ = _xml_roundtrip(_graph())
    root = ET.fromstring(text)
    tags = {el.tag for el in root.iter()}
    for local in ("BoundaryPoint", "WindPowerPlant", "SolarPowerPlant"):
        assert f"{{{EU}}}{local}" in tags and f"{{{CIM}}}{local}" not in tags
    for prop in (
        "IdentifiedObject.shortName",
        "IdentifiedObject.energyIdentCodeEic",
        "BoundaryPoint.fromEndIsoCode",
        "BoundaryPoint.ConnectivityNode",
        "WindGeneratingUnit.WindPowerPlant",
        "SolarGeneratingUnit.SolarPowerPlant",
        "OperationalLimitType.kind",
    ):
        assert f"{{{EU}}}{prop}" in tags, prop
    assert f"{{{CIM}}}IdentifiedObject.name" in tags and f"{{{CIM}}}ACLineSegment" in tags
    assert f'xmlns:cim="{CIM}" xmlns:eu="{EU}" xmlns:rdf=' in text
    assert f'<eu:OperationalLimitType.kind rdf:resource="{EU}LimitKind.tatl" />' in text
    assert "<eu:IdentifiedObject.shortName>L1s</eu:IdentifiedObject.shortName>" in text
    # associations are written from the side the profiles own
    assert "BoundaryPoint.ConnectivityNode" in text and "ConnectivityNode.BoundaryPoint" not in text
    assert "WindPowerPlant.WindGeneratingUnits" not in text


def test_cimxml_without_eu_members_has_no_eu_declaration():
    text = to_cimxml_string([cim_python_sdk.ACLineSegment(mrid="x", name="L")])
    assert "xmlns:eu" not in text and "CIM100-European" not in text


def test_cimxml_roundtrip():
    objs = _graph()
    _, doc = _xml_roundtrip(objs)
    assert doc.warnings == [] and doc.dangling == []
    assert common.canonical_dump(objs) == common.canonical_dump(doc.objects, False)
    bp = doc.by_id["bp-1"]
    assert type(bp) is cim_python_sdk.BoundaryPoint and bp.connectivity_node is doc.by_id["cn-1"]
    assert doc.by_id["cn-1"].boundary_point is bp
    assert bp.short_name == "BP1s" and bp.is_excluded_from_area_interchange is True
    assert doc.by_id["olt-1"].kind is cim_python_sdk.LimitKind.tatl
    assert doc.by_id["wgu-1"].wind_power_plant is doc.by_id["wpp-1"]
    assert doc.by_id["spp-1"].solar_generating_units == (doc.by_id["sgu-1"],)
    assert doc.by_id["line-1"].short_name == "L1s"


def test_cimxml_reads_cgmes_style_input():
    text = f"""<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="{CIM}" xmlns:eu="{EU}"
         xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <cim:ConnectivityNode rdf:ID="_cn"/>
  <eu:BoundaryPoint rdf:ID="_bp">
    <cim:IdentifiedObject.name>XB</cim:IdentifiedObject.name>
    <eu:IdentifiedObject.energyIdentCodeEic>10X</eu:IdentifiedObject.energyIdentCodeEic>
    <eu:BoundaryPoint.isDirectCurrent>true</eu:BoundaryPoint.isDirectCurrent>
    <eu:BoundaryPoint.ConnectivityNode rdf:resource="#_cn"/>
  </eu:BoundaryPoint>
  <cim:OperationalLimitType rdf:ID="_olt">
    <eu:OperationalLimitType.kind rdf:resource="{EU}LimitKind.patl"/>
  </cim:OperationalLimitType>
</rdf:RDF>
"""
    doc = read_cimxml(io.BytesIO(text.encode()), strict=True)
    bp = doc.by_id["bp"]
    assert bp.name == "XB" and bp.energy_ident_code_eic == "10X" and bp.is_direct_current is True
    assert bp.connectivity_node is doc.by_id["cn"]
    assert doc.by_id["olt"].kind is cim_python_sdk.LimitKind.patl


def test_jsonld_writes_eu_prefix_and_roundtrips():
    objs = _graph()
    d = to_jsonld_dict(objs)
    assert list(d["@context"])[:2] == ["cim", "eu"] and d["@context"]["eu"] == EU
    nodes = {n["@id"]: n for n in d["@graph"]}
    bp = nodes["#_bp-1"]
    assert bp["@type"] == "eu:BoundaryPoint"
    assert bp["eu:BoundaryPoint.fromEndIsoCode"] == "NO"
    assert (
        bp["eu:IdentifiedObject.shortName"] == "BP1s" and bp["cim:IdentifiedObject.name"] == "BP1"
    )
    assert bp["eu:BoundaryPoint.ConnectivityNode"] == {"@id": "#_cn-1"}
    assert nodes["#_olt-1"]["eu:OperationalLimitType.kind"] == {"@id": "eu:LimitKind.tatl"}
    assert nodes["#_wgu-1"]["eu:WindGeneratingUnit.WindPowerPlant"] == {"@id": "#_wpp-1"}
    assert nodes["#_line-1"]["@type"] == "cim:ACLineSegment"
    doc = read_jsonld(io.BytesIO(json.dumps(d).encode()), strict=True)
    assert doc.warnings == []
    assert common.canonical_dump(objs) == common.canonical_dump(doc.objects, False)
    assert doc.by_id["olt-1"].kind is cim_python_sdk.LimitKind.tatl


def test_jsonld_without_eu_members_has_no_eu_context():
    d = to_jsonld_dict([cim_python_sdk.ACLineSegment(mrid="x", name="L")])
    assert "eu" not in d["@context"]


def test_jsonld_reads_eu_without_context_entry():
    items = [
        {"@id": "_bp", "@type": "eu:BoundaryPoint", "eu:BoundaryPoint.toEndIsoCode": "DE"},
        {
            "@id": "_olt",
            "@type": "cim:OperationalLimitType",
            "eu:OperationalLimitType.kind": {"@id": f"{EU}LimitKind.tc"},
        },
    ]
    doc = read_jsonld(io.BytesIO(json.dumps(items).encode()), strict=True)
    assert doc.by_id["bp"].to_end_iso_code == "DE"
    assert doc.by_id["olt"].kind is cim_python_sdk.LimitKind.tc


def test_cimxml_jsonld_equivalent():
    objs = _graph()
    xdoc = read_cimxml(io.BytesIO(to_cimxml_string(objs).encode()))
    jdoc = read_jsonld(io.BytesIO(json.dumps(to_jsonld_dict(objs)).encode()))
    assert common.canonical_dump(xdoc.objects, False) == common.canonical_dump(jdoc.objects, False)
