"""CIMXML (IEC 61970-552) writer/reader tests: round trips, rules, tolerance, performance."""

from __future__ import annotations

import datetime as dt
import io
import time
import xml.etree.ElementTree as ET
from decimal import Decimal

import pytest

import cim_python_sdk
from cim_python_sdk.serialization import (
    CimXmlError,
    read_cimxml,
    to_cimxml_string,
    write_cimxml,
)
from cim_python_sdk.serialization import _common as common
from cim_python_sdk.serialization.cimxml import MD_NS, RDF_NS
from tests.serialization.network import build_network, roots

NS = (
    'xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"'
)


def test_roundtrip_canonical_dump():
    net = build_network()
    xml = to_cimxml_string(roots(net))
    doc = read_cimxml(io.BytesIO(xml.encode()))
    assert doc.warnings == [] and doc.dangling == []
    orig = common.canonical_dump(roots(net))
    back = common.canonical_dump(doc.objects, include_reachable=False)
    assert orig == back
    assert len(orig) == len(doc.objects) >= 25
    # types and a few spot values survived
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
    assert addr.postal_code == "2000"


def test_both_ends_restored_and_written_once():
    net = build_network()
    xml = to_cimxml_string(roots(net))
    # direction rule: written on the single-valued end only
    assert "Terminal.ConductingEquipment" in xml and "ConductingEquipment.Terminals" not in xml
    assert "Terminal.ConnectivityNode" in xml and "ConnectivityNode.Terminals" not in xml
    assert "PositionPoint.Location" in xml and "Location.PositionPoints" not in xml
    # 1:1 and N:M: the end whose <Owner>.<Role> sorts first
    assert "RatioTapChanger.TransformerEnd" in xml and "TransformerEnd.RatioTapChanger" not in xml
    assert xml.count("Asset.PowerSystemResources") + xml.count("PowerSystemResource.Assets") == 2
    assert ("Asset.PowerSystemResources" in xml) != ("PowerSystemResource.Assets" in xml)
    # declaring class names, not the object's class
    assert "<cim:IdentifiedObject.name>" in xml and "<cim:ACLineSegment.name>" not in xml
    assert "Equipment.EquipmentContainer" in xml and "mRID" not in xml
    # each association appears exactly once
    root = ET.fromstring(xml)
    seen = set()
    for el in root:
        for ch in el:
            ref = ch.get(f"{{{RDF_NS}}}resource")
            if ref and ref.startswith("#"):
                key = frozenset({el.get(f"{{{RDF_NS}}}ID"), ref[1:]})
                inv_ends = {ch.tag.split("}")[1]}
                assert (key, tuple(inv_ends)) not in seen
                seen.add((key, tuple(inv_ends)))
    doc = read_cimxml(io.StringIO(xml)) if False else read_cimxml(io.BytesIO(xml.encode()))
    line, t1 = doc.by_id["line-1"], doc.by_id["line-1"].terminals[0]
    assert t1.conducting_equipment is line and len(line.terminals) == 2
    assert doc.by_id["pte-1"].ratio_tap_changer is doc.by_id["rtc-1"]
    assert doc.by_id["rtc-1"].transformer_end is doc.by_id["pte-1"]
    assert doc.by_id["asset-1"].power_system_resources == tuple(
        sorted(doc.by_id["asset-1"].power_system_resources, key=lambda o: o.mrid)
    )
    assert doc.by_id["tx-1"].assets == (doc.by_id["asset-1"],)
    loc = doc.by_id["loc-1"]
    assert len(loc.position_points) == 2 and all(p.location is loc for p in loc.position_points)


def test_write_both_ends():
    net = build_network()
    xml = to_cimxml_string(roots(net), write_both_ends=True)
    assert "Terminal.ConductingEquipment" in xml and "ConductingEquipment.Terminals" in xml
    doc = read_cimxml(io.BytesIO(xml.encode()))
    assert common.canonical_dump(roots(net)) == common.canonical_dump(
        doc.objects, include_reachable=False
    )
    assert len(doc.by_id["line-1"].terminals) == 2  # no duplicates from the two-sided links


def test_no_mrid_objects_get_generated_ids():
    net = build_network()
    xml = to_cimxml_string(roots(net))
    assert 'rdf:ID="_gen0"' in xml and 'rdf:ID="_gen1"' in xml
    doc = read_cimxml(io.BytesIO(xml.encode()))
    pts = [o for o in doc.objects if isinstance(o, cim_python_sdk.PositionPoint)]
    assert len(pts) == 2 and not hasattr(pts[0], "mrid")
    assert {id_ for id_, o in doc.by_id.items() if isinstance(o, cim_python_sdk.PositionPoint)} == {
        "gen0",
        "gen1",
    }
    # ids do not depend on construction order
    net2 = build_network()
    assert to_cimxml_string(roots(net2)) == xml


def test_deterministic_bytes(tmp_path):
    net = build_network()
    a, b = tmp_path / "a.xml", tmp_path / "b.xml"
    write_cimxml(roots(net), a)
    write_cimxml(list(reversed(roots(net))), b)
    assert a.read_bytes() == b.read_bytes()
    data = a.read_bytes()
    assert data.startswith(b"<?xml version='1.0' encoding='utf-8'?>\n<rdf:RDF")
    assert b"\n  <cim:" in data  # pretty-printed
    assert to_cimxml_string(roots(net)).encode() == data


def test_include_reachable_false_and_file_objects():
    net = build_network()
    xml = to_cimxml_string([net["line"], net["t1"]], include_reachable=False)
    doc = read_cimxml(io.BytesIO(xml.encode()))
    assert sorted(doc.by_id) == ["line-1", net["t1"].mrid]
    assert doc.dangling == []  # references to unwritten objects are not written
    assert doc.by_id[net["t1"].mrid].conducting_equipment is doc.by_id["line-1"]
    buf = io.BytesIO()
    write_cimxml([net["line"]], buf, include_reachable=False)
    tbuf = io.StringIO()
    write_cimxml([net["line"]], tbuf, include_reachable=False)
    assert buf.getvalue().decode() == tbuf.getvalue()


def test_header():
    net = build_network()
    header = {
        "created": dt.datetime(2026, 1, 2, 3, 4, 5),
        "description": "Test model",
        "version": "3",
        "profile": ["http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0", "other"],
        "DependentOn": "urn:uuid:1234",
    }
    xml = to_cimxml_string([net["sub"]], header=header)
    assert f'xmlns:md="{MD_NS}"' in xml
    assert "<md:Model.created>2026-01-02T03:04:05</md:Model.created>" in xml
    assert 'md:Model.DependentOn rdf:resource="urn:uuid:1234"' in xml
    assert "md:FullModel" not in to_cimxml_string([net["sub"]])
    doc = read_cimxml(io.BytesIO(xml.encode()))
    assert doc.header["description"] == "Test model"
    assert doc.header["profile"] == header["profile"]
    assert doc.header["DependentOn"] == "urn:uuid:1234"
    assert doc.header["about"].startswith("urn:uuid:")
    assert doc.by_id["sub-1"].name == "Zone Sub"  # header is not an object
    assert to_cimxml_string([net["sub"]], header=header) == xml


def test_enum_resource_and_custom_namespace():
    net = build_network()
    xml = to_cimxml_string(
        [net["phase"]], namespace="http://example.org/cim#", include_reachable=False
    )
    assert 'rdf:resource="http://example.org/cim#SinglePhaseKind.A"' in xml
    assert 'xmlns:cim="http://example.org/cim#"' in xml
    doc = read_cimxml(io.BytesIO(xml.encode()))
    assert doc.by_id["phase-1"].phase is cim_python_sdk.SinglePhaseKind.A


def test_float_special_values_and_bool():
    seg = cim_python_sdk.ACLineSegment(
        mrid="s", length=float("inf"), r=float("nan"), x=-0.0, in_service=False
    )
    xml = to_cimxml_string([seg])
    assert ">INF<" in xml and ">NaN<" in xml and ">false<" in xml and ">-0.0<" in xml
    back = read_cimxml(io.BytesIO(xml.encode())).by_id["s"]
    assert back.length == float("inf") and back.r != back.r and back.in_service is False


def test_unset_default_is_not_reintroduced():
    G = cim_python_sdk.GenericDataSetVersion
    default = G().major_version
    assert default is not None
    objs = [G(major_version=None), G()]
    doc = read_cimxml(io.BytesIO(to_cimxml_string(objs).encode()))
    assert sorted((o.major_version for o in doc.objects), key=str) == sorted(
        [None, default], key=str
    )


# --- hand-written documents ------------------------------------------------------------


def _doc(body: str, **kw):
    xml = f'<?xml version="1.0"?><rdf:RDF {NS}>{body}</rdf:RDF>'
    return read_cimxml(io.BytesIO(xml.encode()), **kw)


def test_identifier_forms():
    doc = _doc(
        """
        <cim:ACLineSegment rdf:ID="_a"><cim:IdentifiedObject.name>A</cim:IdentifiedObject.name></cim:ACLineSegment>
        <cim:ACLineSegment rdf:about="#_b"/>
        <cim:ACLineSegment rdf:about="urn:uuid:ccc"/>
        <cim:Terminal rdf:ID="t1"><cim:Terminal.ConductingEquipment rdf:resource="#_a"/></cim:Terminal>
        <cim:Terminal rdf:ID="t2"><cim:Terminal.ConductingEquipment rdf:resource="#b"/></cim:Terminal>
        <cim:Terminal rdf:ID="t3"><cim:Terminal.ConductingEquipment rdf:resource="urn:uuid:ccc"/></cim:Terminal>
        """
    )
    assert doc.warnings == []
    assert [o.mrid for o in doc.objects] == ["a", "b", "ccc", "t1", "t2", "t3"]
    assert doc.by_id["a"].name == "A"
    assert doc.by_id["t1"].conducting_equipment is doc.by_id["a"]
    assert doc.by_id["t2"].conducting_equipment is doc.by_id["b"]
    assert doc.by_id["t3"].conducting_equipment is doc.by_id["ccc"]


def test_association_on_wrong_end_and_both_ends():
    doc = _doc(
        """
        <cim:ACLineSegment rdf:ID="_l">
          <cim:ConductingEquipment.Terminals rdf:resource="#_t1"/>
          <cim:ConductingEquipment.Terminals rdf:resource="#_t2"/>
        </cim:ACLineSegment>
        <cim:Terminal rdf:ID="_t1"/>
        <cim:Terminal rdf:ID="_t2"><cim:Terminal.ConductingEquipment rdf:resource="#_l"/></cim:Terminal>
        """
    )
    assert doc.warnings == []
    line = doc.by_id["l"]
    assert set(line.terminals) == {doc.by_id["t1"], doc.by_id["t2"]} and len(line.terminals) == 2
    assert doc.by_id["t1"].conducting_equipment is line


def test_unknown_class_property_and_bad_literal():
    doc = _doc(
        """
        <cim:Spaceship rdf:ID="_x"/>
        <cim:Spaceship rdf:ID="_y"/>
        <cim:ACLineSegment rdf:ID="_l">
          <cim:ACLineSegment.warpDrive>9</cim:ACLineSegment.warpDrive>
          <cim:Conductor.length>12.5</cim:Conductor.length>
          <cim:ACLineSegment.r>not-a-number</cim:ACLineSegment.r>
          <cim:IdentifiedObject.name>ok</cim:IdentifiedObject.name>
        </cim:ACLineSegment>
        """
    )
    assert [o.mrid for o in doc.objects] == ["l"]
    assert doc.by_id["l"].name == "ok" and doc.by_id["l"].length == 12.5
    assert doc.by_id["l"].r is None
    text = "\n".join(doc.warnings)
    assert "unknown class 'Spaceship'" in text and "(x2)" in text
    assert "unknown property 'ACLineSegment.warpDrive'" in text
    assert "cannot parse" in text


def test_dangling_reference_and_type_mismatch():
    doc = _doc(
        """
        <cim:Terminal rdf:ID="_t"><cim:Terminal.ConductingEquipment rdf:resource="#_missing"/></cim:Terminal>
        <cim:Substation rdf:ID="_s"/>
        <cim:Terminal rdf:ID="_u"><cim:Terminal.ConductingEquipment rdf:resource="#_s"/></cim:Terminal>
        """
    )
    assert doc.dangling == [("t", "Terminal.ConductingEquipment", "#_missing")]
    assert doc.by_id["t"].conducting_equipment is None
    assert any("dangling" in w for w in doc.warnings)
    assert any("cannot link" in w for w in doc.warnings)  # Substation is not ConductingEquipment


def test_strict_raises():
    with pytest.raises(CimXmlError, match="Spaceship"):
        _doc('<cim:Spaceship rdf:ID="_x"/>', strict=True)
    with pytest.raises(CimXmlError, match="unknown property"):
        _doc(
            '<cim:Terminal rdf:ID="_x"><cim:Terminal.nope>1</cim:Terminal.nope></cim:Terminal>',
            strict=True,
        )
    with pytest.raises(CimXmlError, match="dangling"):
        _doc(
            '<cim:Terminal rdf:ID="_x"><cim:Terminal.ConductingEquipment rdf:resource="#_q"/></cim:Terminal>',
            strict=True,
        )
    with pytest.raises(CimXmlError):
        read_cimxml(io.BytesIO(b"<not-xml"))
    with pytest.raises(CimXmlError, match="rdf:RDF"):
        read_cimxml(io.BytesIO(b"<a/>"))


def test_compound_wrapper_form_and_enum_forms():
    doc = _doc(
        """
        <cim:Location rdf:ID="_l">
          <cim:Location.mainAddress>
            <cim:StreetAddress><cim:StreetAddress.postalCode>3000</cim:StreetAddress.postalCode></cim:StreetAddress>
          </cim:Location.mainAddress>
        </cim:Location>
        <cim:Terminal rdf:ID="_t">
          <cim:ACDCTerminal.connected>true</cim:ACDCTerminal.connected>
          <cim:Terminal.phases rdf:resource="http://other.example/ns#PhaseCode.AB"/>
        </cim:Terminal>
        <cim:Terminal rdf:ID="_u"><cim:Terminal.phases rdf:resource="#PhaseCode.Nope"/></cim:Terminal>
        """
    )
    assert doc.by_id["l"].main_address.postal_code == "3000"
    assert doc.by_id["t"].phases is cim_python_sdk.PhaseCode.AB and doc.by_id["t"].connected is True
    assert doc.by_id["u"].phases is None and any("unknown enum value" in w for w in doc.warnings)


# --- class-name ambiguity ---------------------------------------------------------------


def test_duplicate_cim_names_resolve_to_canonical():
    # 4 CIM names occur twice in the model; BY_NAME holds one canonical class for each
    for name in ("IEC61968CIMVersion", "TroubleReportingKind", "Profile", "ResourceCertification"):
        cands = common.class_candidates(name)
        assert len(cands) >= 2 and all(c._cim_meta.cim_name == name for c in cands)
        assert common.resolve_class(name) is cands[0] is getattr(cim_python_sdk, name)
    from cim_python_sdk.model.iec61968.customers.trouble_reporting_kind_2 import (
        TroubleReportingKind_2,
    )

    assert common.resolve_class("TroubleReportingKind_2") is None  # the safe-name is not a CIM name
    # names with characters that are not valid in Python identifiers resolve via _cim_meta
    assert common.resolve_class("MeasurementKind-Old") is cim_python_sdk.MeasurementKind_Old
    assert common.resolve_class("TroubleSymptomsTree Kind") is cim_python_sdk.TroubleSymptomsTree_Kind
    assert common.resolve_class("NoSuchThing") is None
    # a non-canonical duplicate class is written under the shared CIM name and reads back as
    # the canonical class; its enum literal is found through the alternate enum
    from cim_python_sdk.model.iec61968.doc_iec61968.iec61968_cim_version_2 import (
        IEC61968CIMVersion_2,
    )

    obj = IEC61968CIMVersion_2()
    xml = to_cimxml_string([obj])
    assert "<cim:IEC61968CIMVersion " in xml
    assert type(read_cimxml(io.BytesIO(xml.encode())).objects[0]) is cim_python_sdk.IEC61968CIMVersion
    alt = common.class_candidates("TroubleReportingKind")[1]
    member = next(iter(alt))
    assert (
        common.decode_enum(
            common.enum_resource(member), common.class_candidates("TroubleReportingKind")
        )
        is not None
    )
    assert TroubleReportingKind_2 is alt


def test_property_resolution_and_write_end_helpers():
    plan = common.class_plan(cim_python_sdk.ACLineSegment)
    assert common.resolve_property(cim_python_sdk.ACLineSegment, "IdentifiedObject.name").name == "name"
    assert common.resolve_property(cim_python_sdk.ACLineSegment, "Conductor.length").name == "length"
    assert common.resolve_property(cim_python_sdk.ACLineSegment, "ConductingEquipment.Terminals").many
    assert common.resolve_property(cim_python_sdk.ACLineSegment, "ACLineSegment.name") is None
    assert "Terminal.ConductingEquipment" in common.class_plan(cim_python_sdk.Terminal).by_prop
    # generated role names are used when the model has no role (documented)
    gen = common.resolve_property(
        cim_python_sdk.ACLineSegment, "Equipment.equipment_unavailability_schedules"
    )
    assert gen is not None and plan.cim_name == "ACLineSegment"
    end = cim_python_sdk.Terminal.conducting_equipment
    assert common.association_write_end(end) is end
    assert common.association_write_end(end.inverse) is end
    assert common.association_write_end(end.meta, cim_python_sdk.Terminal) is end
    # N:M and 1:1 pick the end whose "<Owner>.<Role>" sorts first, from either side
    nm = cim_python_sdk.Asset.power_system_resources
    assert common.association_write_end(nm) is common.association_write_end(nm.inverse)
    one = cim_python_sdk.RatioTapChanger.transformer_end
    assert common.association_write_end(one.inverse) is one


# --- performance -------------------------------------------------------------------------


def test_performance_50k_objects(tmp_path, capsys):
    sub = cim_python_sdk.Substation(name="S")
    bv = cim_python_sdk.BaseVoltage(nominal_voltage=11000.0)
    nodes = [cim_python_sdk.ConnectivityNode(name=f"n{i}") for i in range(8000)]
    objs = [sub, bv, *nodes]
    for i in range(8000):
        line = cim_python_sdk.ACLineSegment(
            name=f"l{i}", length=float(i), equipment_container=sub, base_voltage=bv
        )
        objs.append(line)
        objs.append(
            cim_python_sdk.Terminal(
                sequence_number=1,
                phases=cim_python_sdk.PhaseCode.ABC,
                conducting_equipment=line,
                connectivity_node=nodes[i],
            )
        )
        objs.append(
            cim_python_sdk.Terminal(
                sequence_number=2,
                phases=cim_python_sdk.PhaseCode.ABC,
                conducting_equipment=line,
                connectivity_node=nodes[(i + 1) % 8000],
            )
        )
        loc = cim_python_sdk.Location(type="x", main_address=cim_python_sdk.StreetAddress(postal_code="1"))
        line.location = loc
        objs.append(loc)
        objs.append(cim_python_sdk.PositionPoint(sequence_number=1, location=loc))
        objs.append(cim_python_sdk.PositionPoint(sequence_number=2, location=loc))
    path = tmp_path / "big.xml"
    t0 = time.perf_counter()
    write_cimxml([sub], path)
    t1 = time.perf_counter()
    doc = read_cimxml(path)
    t2 = time.perf_counter()
    n = len(doc.objects)
    with capsys.disabled():
        print(
            f"\nperf: {n} objects, {path.stat().st_size / 1e6:.1f} MB; "
            f"write {t1 - t0:.1f}s, read {t2 - t1:.1f}s"
        )
    assert n == len(objs) > 50_000
    assert doc.warnings == []
    assert t1 - t0 < 60 and t2 - t1 < 60


# --- S1 review fixes ---------------------------------------------------------------------


@pytest.mark.parametrize("bad", ["a\x00b", "x\x01", "\x0b", "\x1f", "￾", "￿", "\ud800"])
def test_xml_invalid_characters_raise(bad):
    obj = cim_python_sdk.ACLineSegment(mrid="seg-1", name=f"n{bad}")
    with pytest.raises(ValueError, match=r"ACLineSegment 'seg-1': IdentifiedObject\.name"):
        to_cimxml_string([obj])
    # inside a compound the nested property is named too
    loc = cim_python_sdk.Location(mrid="loc", main_address=cim_python_sdk.StreetAddress(po_box=bad))
    with pytest.raises(ValueError, match=r"Location 'loc': Location\.mainAddress/StreetAddress"):
        to_cimxml_string([loc])
    with pytest.raises(ValueError, match="header"):
        to_cimxml_string([], header={"description": bad})


def test_xml_allowed_whitespace_controls_and_cr_roundtrip():
    text = "a\tb\nc\r\nd\re é\U0001f600"
    obj = cim_python_sdk.ACLineSegment(mrid="s", name=text, description="\r")
    xml = to_cimxml_string([obj])
    assert "&#13;" in xml and "\r" not in xml and "\x00" not in xml
    back = read_cimxml(io.BytesIO(xml.encode())).by_id["s"]
    assert back.name == text and back.description == "\r"


@pytest.mark.parametrize("mrid", ["a#b", "a b", "1abc", "x/y:z", "50%off", "é", "_lead", "-x", "a?b"])
def test_unusual_mrids_roundtrip(mrid):
    sub = cim_python_sdk.Substation(mrid=mrid)
    line = cim_python_sdk.ACLineSegment(mrid=mrid + "!", equipment_container=sub)
    term = cim_python_sdk.Terminal(mrid=mrid + "-t", conducting_equipment=line)
    xml = to_cimxml_string([sub])
    ET.fromstring(xml)  # well-formed
    doc = read_cimxml(io.BytesIO(xml.encode()))
    assert doc.warnings == [] and doc.dangling == []
    assert sorted(doc.by_id) == sorted([mrid, mrid + "!", mrid + "-t"])
    assert doc.by_id[mrid + "!"].equipment_container is doc.by_id[mrid]
    assert doc.by_id[mrid + "-t"].conducting_equipment is doc.by_id[mrid + "!"]
    assert term.mrid == mrid + "-t"


def test_non_ncname_mrid_wire_form():
    sub = cim_python_sdk.Substation(mrid="a#b c")
    xml = to_cimxml_string([sub])
    assert 'rdf:about="#_a%23b%20c"' in xml and "rdf:ID" not in xml
    uuid = "123e4567-e89b-12d3-a456-426614174000"
    assert f'rdf:ID="_{uuid}"' in to_cimxml_string([cim_python_sdk.Substation(mrid=uuid)])
    assert common.normalize_id("a#b") == "a#b"
    assert common.normalize_id("#_a#b") == "a#b"
    assert common.normalize_id("model.xml#_x") == "x"
    assert common.normalize_id("urn:uuid:" + uuid) == uuid
    assert common.normalize_id("_:gen0") == "gen0"
    assert common.normalize_id("#_a%23b") == "a#b"


def test_roleless_end_warns_once_per_end_per_call():
    # AssemblyManifest.model_part_versions has no CIM role and is the end it is written from
    objs = []
    for i in range(3):
        a = cim_python_sdk.AssemblyManifest(mrid=f"am{i}")
        a.add_model_part_version(cim_python_sdk.ModelPartVersion(mrid=f"mpv{i}"))
        objs.append(a)
    with pytest.warns(UserWarning) as rec:
        xml = to_cimxml_string(objs)
    msgs = [str(w.message) for w in rec if "AssemblyManifest.model_part_versions" in str(w.message)]
    assert len(msgs) == 1 and "no CIM role" in msgs[0]
    assert "AssemblyManifest.model_part_versions" in xml
    with pytest.warns(UserWarning):  # a new call warns again
        to_cimxml_string(objs)


def test_value_warning_text_names_class_once():
    doc = _doc(
        '<cim:Terminal rdf:ID="_u"><cim:ACDCTerminal.sequenceNumber>x</cim:ACDCTerminal.sequenceNumber></cim:Terminal>'
    )
    assert doc.warnings == ["Terminal: ACDCTerminal.sequenceNumber: cannot parse 'x' as int"]


def test_common_docstring_counts():
    assert "66 ends without a CIM" in " ".join(common.__doc__.split())
    assert "33 of them" in common.__doc__ and "200" not in common.__doc__
