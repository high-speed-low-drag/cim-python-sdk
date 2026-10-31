"""CGMES 3.0 multi-file reader (`cim_python_sdk.serialization.cgmes.read_cgmes`)."""

from __future__ import annotations

import datetime as dt
import hashlib
import io
import json
import os
import random
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from importlib import resources
from pathlib import Path

import pytest

import cim_python_sdk as c
from cim_python_sdk.profiles import ProfileSet, cgmes3
from cim_python_sdk.serialization import (
    CgmesDocument,
    CgmesHeader,
    CgmesReadError,
    CimXmlError,
    read_cgmes,
    read_cimxml,
    to_cgmes_strings,
    write_cgmes,
)
from cim_python_sdk.serialization._common import canonical_dump
from tests.serialization.cgmes_network import build_cgmes, uid

FIXTURE = Path(__file__).parent / "data" / "cgmes3_fixture"
KWS = ("EQ", "SSH", "TP", "SV")
MODEL_IDS = {kw: f"0000000{i}-1111-2222-3333-444444444444" for i, kw in enumerate(KWS)}
HEADER = CgmesHeader(
    scenario_time=dt.datetime(2026, 1, 1, 12, 30, tzinfo=dt.UTC),
    created=dt.datetime(2026, 1, 2, 3, 4, 5),
    modeling_authority_set="http://example.com/tso",
    description="cim_python_sdk reader test",
    version="3",
    model_ids=MODEL_IDS,
)


@pytest.fixture(scope="module")
def net() -> dict[str, c.CimObject]:
    return build_cgmes()


@pytest.fixture(scope="module")
def docs(net: dict[str, c.CimObject]) -> dict[str, str]:
    return to_cgmes_strings(list(net.values()), header=HEADER)


def dump(objects: list[c.CimObject]) -> list[dict]:  # type: ignore[type-arg]
    return canonical_dump(objects, include_reachable=False)


# --------------------------------------------------------------------------------------
# round trip of the writer's output
# --------------------------------------------------------------------------------------


def test_roundtrip_in_memory_shuffled(net: dict[str, c.CimObject], docs: dict[str, str]) -> None:
    orig = canonical_dump(list(net.values()))
    for seed in range(4):
        items = [(f"{kw}.xml", d) for kw, d in docs.items()]
        random.Random(seed).shuffle(items)
        doc = read_cgmes(items)
        assert doc.warnings == [] and doc.dangling == []
        assert dump(doc.objects) == orig
        assert doc.profiles == KWS
    mapping = {f"{kw}.xml": d.encode() for kw, d in reversed(docs.items())}  # bytes, reversed
    assert dump(read_cgmes(mapping).objects) == orig


def test_roundtrip_directory_and_zip(net: dict[str, c.CimObject], tmp_path: Path) -> None:
    orig = canonical_dump(list(net.values()))
    out = tmp_path / "set"
    report = write_cgmes(list(net.values()), out, name="grid", header=HEADER)
    doc = read_cgmes(out)
    assert doc.warnings == [] and dump(doc.objects) == orig
    assert sorted(doc.headers) == sorted(report.files.values())

    zpath = tmp_path / "set.zip"
    write_cgmes(list(net.values()), zpath, name="grid", header=HEADER)
    doc = read_cgmes(zpath)
    assert doc.warnings == [] and dump(doc.objects) == orig
    paths = sorted(out.iterdir(), reverse=True)  # an iterable of paths, any order
    assert dump(read_cgmes(paths).objects) == orig
    assert dump(read_cgmes(str(paths[0:1][0])).objects) != orig  # one file is not the set


def test_object_properties_survive(net: dict[str, c.CimObject], docs: dict[str, str]) -> None:
    doc = read_cgmes(docs)
    line = doc.by_id[uid("line")]
    assert isinstance(line, c.ACLineSegment) and line.mrid == uid("line")
    assert line.short_name == net["line"].short_name  # type: ignore[attr-defined]
    assert line.in_service is True  # from SSH, described as cim:Equipment
    assert type(doc.by_id[uid("Line-t1")]) is c.Terminal
    assert not any(type(o) is c.Equipment for o in doc.objects)
    sv = [o for o in doc.objects if isinstance(o, c.SvVoltage)]
    assert len(sv) == 2 and all(not hasattr(o, "mrid") for o in sv)


def test_headers_and_rewrite(docs: dict[str, str]) -> None:
    doc = read_cgmes(docs)
    assert isinstance(doc, CgmesDocument) and list(doc.headers) == list(docs)
    for kw in KWS:
        h = doc.headers[kw]  # the name is the key given by the mapping
        assert h.about == f"urn:uuid:{MODEL_IDS[kw]}" and h.model_id == h.about
        assert h.profile_uris == (cgmes3.by_keyword(kw).uri,) and h.profiles == (kw,)
        assert h.created == dt.datetime(2026, 1, 2, 3, 4, 5, tzinfo=dt.UTC)
        assert h.scenario_time == dt.datetime(2026, 1, 1, 12, 30, tzinfo=dt.UTC)
        assert h.description == "cim_python_sdk reader test" and h.version == "3"
        assert h.modeling_authority_set == "http://example.com/tso"
    deps = {"EQ": (), "SSH": ("EQ",), "TP": ("SSH",), "SV": ("TP",)}
    for kw, d in deps.items():
        assert doc.headers[kw].dependent_on == tuple(f"urn:uuid:{MODEL_IDS[x]}" for x in d)
    by_profile = doc.headers_by_profile
    assert list(by_profile) == list(KWS) and by_profile["TP"] == [doc.headers["TP"]]

    again = to_cgmes_strings(doc.objects, header=doc.header_for_rewrite())
    for kw in KWS:
        assert ET.tostring(ET.fromstring(again[kw])[0]) == ET.tostring(ET.fromstring(docs[kw])[0])
    assert dump(read_cgmes(again).objects) == dump(doc.objects)


# --------------------------------------------------------------------------------------
# the committed hand-written fixture (the CGMES 3.0 file conventions, made-up content)
# --------------------------------------------------------------------------------------


def test_fixture_file_set() -> None:
    doc = read_cgmes(FIXTURE)
    assert len(doc.headers) == 4
    eq, ssh, tp, sv = (doc.headers[f"fixture_{k}.xml"] for k in KWS)
    assert eq.profiles == ("EQ", "SC") and len(eq.profile_uris) == 2
    assert eq.profile_uris[0] == cgmes3.EQ.uri and eq.profile_uris[1] == cgmes3.SC.uri
    assert eq.about == f"urn:uuid:{uid('fx-eq-model')}"
    assert eq.dependent_on == (f"urn:uuid:{uid('fx-bd-model')}",)
    assert ssh.dependent_on == (eq.about,) and tp.dependent_on == (ssh.about,)
    assert sv.dependent_on == (tp.about,)
    assert eq.version == "001"
    assert eq.modeling_authority_set == "http://example.com/cgmes-fixture"
    assert eq.scenario_time == dt.datetime(2026, 2, 10, 9, 30, tzinfo=dt.UTC)
    assert eq.created == dt.datetime(2026, 2, 10, 11, 5, 12, tzinfo=dt.UTC)
    assert eq.description == "cim-python-sdk hand-written CGMES 3.0 fixture"
    assert doc.profiles == ("EQ", "SSH", "TP", "SV", "SC")
    assert doc.headers_by_profile["SC"] == [eq]

    # merged across files: EQ defines the terminal, TP describes it
    term = doc.by_id[uid("fx-term")]
    assert isinstance(term, c.Terminal)
    tn = doc.by_id[uid("fx-tn")]
    assert isinstance(tn, c.TopologicalNode) and term.topological_node is tn
    cn = doc.by_id[uid("fx-cn")]
    assert isinstance(cn, c.ConnectivityNode) and cn.topological_node is tn  # TP rdf:about
    line = doc.by_id[uid("fx-line")]
    assert isinstance(line, c.ACLineSegment) and line.mrid == uid("fx-line")  # EQ rdf:ID
    assert line.b0ch is not None  # ShortCircuit property in the EQ file
    assert line.length == 42500.0  # km -> m
    # SSH-only descriptions: created once, as the class seen, with a warning
    sm = doc.by_id[uid("fx-gen")]
    assert type(sm) is c.SynchronousMachine and sm.in_service is True and sm.p == -85.5e6  # MW -> W
    eqp = doc.by_id[uid("fx-busbar")]
    assert type(eqp) is c.Equipment and eqp.in_service is True
    assert any("only described" in w and "Equipment" in w for w in doc.warnings)
    # the terminal's equipment is a plain Equipment: not a ConductingEquipment
    assert any("cannot link Terminal.ConductingEquipment" in w for w in doc.warnings)
    # the fixture has a few elements only: references to everything else dangle
    assert doc.dangling and {d[1] for d in doc.dangling} >= {"TopologicalNode.BaseVoltage"}
    assert not any("unknown" in w or "not in profile" in w for w in doc.warnings)
    with pytest.raises(CgmesReadError):
        read_cgmes(FIXTURE, strict=True)


# --------------------------------------------------------------------------------------
# merging rules
# --------------------------------------------------------------------------------------

NS = (
    'xmlns:cim="http://iec.ch/TC57/CIM100#" '
    'xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#" '
    'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" '
    'xmlns:eu="http://iec.ch/TC57/CIM100-European#"'
)
LINE = "11111111-aaaa-bbbb-cccc-000000000001"
TERM = "11111111-aaaa-bbbb-cccc-000000000002"
TNODE = "11111111-aaaa-bbbb-cccc-000000000003"


def xml(profiles: list[str], body: str, header: bool = True) -> str:
    hdr = ""
    if header:
        uris = "".join(f"<md:Model.profile>{u}</md:Model.profile>" for u in profiles)
        hdr = (
            '<md:FullModel rdf:about="urn:uuid:99999999-0000-0000-0000-000000000000">'
            f"<md:Model.version>1</md:Model.version>{uris}</md:FullModel>"
        )
    return f'<?xml version="1.0" encoding="utf-8"?><rdf:RDF {NS}>{hdr}{body}</rdf:RDF>'


EQ_BODY = f"""
<cim:ACLineSegment rdf:ID="_{LINE}">
  <cim:IdentifiedObject.mRID>{LINE}</cim:IdentifiedObject.mRID>
  <cim:IdentifiedObject.name>L</cim:IdentifiedObject.name>
  <cim:ACLineSegment.r>1.5</cim:ACLineSegment.r>
</cim:ACLineSegment>
<cim:Terminal rdf:ID="_{TERM}">
  <cim:IdentifiedObject.mRID>{TERM}</cim:IdentifiedObject.mRID>
  <cim:Terminal.ConductingEquipment rdf:resource="#_{LINE}"/>
</cim:Terminal>"""
SSH_BODY = f"""
<cim:Equipment rdf:about="#_{LINE}"><cim:Equipment.inService>false</cim:Equipment.inService></cim:Equipment>
<cim:Terminal rdf:about="#_{TERM}"><cim:ACDCTerminal.connected>true</cim:ACDCTerminal.connected></cim:Terminal>"""
TP_BODY = f"""
<cim:TopologicalNode rdf:ID="_{TNODE}">
  <cim:IdentifiedObject.mRID>{TNODE}</cim:IdentifiedObject.mRID>
</cim:TopologicalNode>
<cim:Terminal rdf:about="#_{TERM}"><cim:Terminal.TopologicalNode rdf:resource="#_{TNODE}"/></cim:Terminal>"""


def _three() -> dict[str, str]:
    return {
        "eq.xml": xml([cgmes3.EQ.uri], EQ_BODY),
        "ssh.xml": xml([cgmes3.SSH.uri], SSH_BODY),
        "tp.xml": xml([cgmes3.TP.uri], TP_BODY),
    }


@pytest.mark.parametrize("order", [(0, 1, 2), (2, 1, 0), (1, 2, 0), (1, 0, 2)])
def test_description_before_or_after_definition(order: tuple[int, ...]) -> None:
    files = list(_three().items())
    doc = read_cgmes([files[i] for i in order])
    assert doc.warnings == [] and doc.dangling == []
    line = doc.by_id[LINE]
    assert type(line) is c.ACLineSegment  # not overridden by the SSH cim:Equipment element
    assert line.in_service is False and line.r == 1.5 and line.mrid == LINE
    assert [type(o).__name__ for o in doc.objects if type(o) is c.Equipment] == []
    assert len(doc.objects) == 3
    term = doc.by_id[TERM]
    assert isinstance(term, c.Terminal) and term.connected is True
    assert term.conducting_equipment is line and term.topological_node is doc.by_id[TNODE]
    assert set(doc.profiles) == {"EQ", "SSH", "TP"}


def test_only_described_gets_the_most_specific_class() -> None:
    body = (
        f'<cim:Equipment rdf:about="#_{LINE}"><cim:Equipment.inService>true</cim:Equipment.inService></cim:Equipment>'
        f'<cim:ACLineSegment rdf:about="#_{LINE}"/>'
    )
    doc = read_cgmes({"ssh.xml": xml([cgmes3.SSH.uri], body)})
    assert type(doc.by_id[LINE]) is c.ACLineSegment and doc.by_id[LINE].in_service is True  # type: ignore[attr-defined]
    assert doc.warnings == [
        "class 'ACLineSegment' is not in profile(s) SSH",
        "object only described (no definition): created as ACLineSegment",
    ]
    # a description with a class that is not an ancestor of the defined one is reported
    files = {
        "eq.xml": xml([cgmes3.EQ.uri], EQ_BODY),
        "x.xml": xml([cgmes3.SSH.uri], f'<cim:Terminal rdf:about="#_{LINE}"/>'),
    }
    doc = read_cgmes(files)
    assert type(doc.by_id[LINE]) is c.ACLineSegment
    assert any("describes it as Terminal" in w for w in doc.warnings)


def test_mrid_rules() -> None:
    body = (
        f'<cim:Substation rdf:ID="_{LINE}"/>'  # no mRID element: the id without "_"
        f'<cim:Substation rdf:ID="_{TERM}"><cim:IdentifiedObject.mRID>other</cim:IdentifiedObject.mRID></cim:Substation>'
        f'<cim:Substation rdf:ID="_{TNODE}"><cim:IdentifiedObject.mRID>{LINE}</cim:IdentifiedObject.mRID></cim:Substation>'
    )
    doc = read_cgmes({"eq.xml": xml([cgmes3.EQ.uri], body)})
    assert doc.by_id[LINE].mrid == LINE  # type: ignore[attr-defined]
    assert doc.by_id[TERM].mrid == "other"  # type: ignore[attr-defined]
    assert doc.by_id[TNODE].mrid == TNODE  # type: ignore[attr-defined]  # duplicate: id kept
    assert len(doc.warnings) == 2
    assert any("differs from the id" in w for w in doc.warnings)
    assert any("kept the id as mRID" in w for w in doc.warnings)


def test_duplicate_definitions_and_class_conflict() -> None:
    a = xml([cgmes3.EQ.uri], f'<cim:Substation rdf:ID="_{LINE}"/>')
    b = xml([cgmes3.EQ.uri], f'<cim:Substation rdf:ID="_{LINE}"/><cim:Terminal rdf:ID="_{LINE}"/>')
    doc = read_cgmes({"a.xml": a, "b.xml": b})
    assert len(doc.objects) == 1 and type(doc.objects[0]) is c.Substation
    assert any("defined more than once" in w for w in doc.warnings)
    assert any("defined as Substation and Terminal" in w for w in doc.warnings)


def test_ids_in_other_forms() -> None:
    odd = "a#b c"
    body = (
        '<cim:Substation rdf:about="#_a%23b%20c"><cim:IdentifiedObject.name>x</cim:IdentifiedObject.name></cim:Substation>'
        f'<cim:VoltageLevel rdf:ID="_{LINE}"><cim:VoltageLevel.Substation rdf:resource="#_a%23b%20c"/></cim:VoltageLevel>'
    )
    doc = read_cgmes({"eq.xml": xml([cgmes3.EQ.uri], body)})
    sub = doc.by_id[odd]
    assert type(sub) is c.Substation and sub.name == "x" and sub.mrid == odd
    assert doc.warnings == [] and doc.by_id[LINE].substation is sub  # type: ignore[attr-defined]


# --------------------------------------------------------------------------------------
# warnings
# --------------------------------------------------------------------------------------


def test_unknown_profile_uri_and_missing_header() -> None:
    cim16 = "http://entsoe.eu/CIM/EquipmentCore/3/1"
    doc = read_cgmes({"old.xml": xml([cim16], EQ_BODY)})
    assert [w for w in doc.warnings] == [f"old.xml: unknown profile URI {cim16!r}"]
    assert doc.profiles == () and doc.headers["old.xml"].profile_uris == (cim16,)
    assert type(doc.by_id[LINE]) is c.ACLineSegment  # still read, generic classification

    doc = read_cgmes({"x.xml": xml([], EQ_BODY, header=False)})
    assert len(doc.warnings) == 1 and "no md:FullModel header" in doc.warnings[0]
    assert doc.headers["x.xml"].about is None and len(doc.objects) == 2

    known = xml([cgmes3.EQ.uri, "urn:example:other"], EQ_BODY)
    doc = read_cgmes({"k.xml": known})
    assert doc.profiles == ("EQ",) and len(doc.warnings) == 1
    with pytest.raises(CgmesReadError, match="unknown profile URI"):
        read_cgmes({"old.xml": xml([cim16], EQ_BODY)}, strict=True)


def test_dangling_reference_across_files() -> None:
    files = _three()
    only_tp = {"tp.xml": files["tp.xml"]}  # Terminal.TopologicalNode is fine, the terminal is not
    doc = read_cgmes(only_tp)
    assert doc.dangling == []  # the TP file describes the terminal itself, no dangling references
    without_tp = {k: v for k, v in files.items() if k != "tp.xml"}
    assert read_cgmes(without_tp).dangling == []
    broken = dict(files)
    missing = "22222222-0000-0000-0000-000000000009"
    body = TP_BODY.replace(f'rdf:resource="#_{TNODE}"', f'rdf:resource="#_{missing}"')
    broken["tp.xml"] = xml([cgmes3.TP.uri], body)
    doc = read_cgmes(broken)
    assert doc.dangling == [(TERM, "Terminal.TopologicalNode", f"#_{missing}")]
    assert doc.warnings == ["dangling reference in Terminal.TopologicalNode"]
    with pytest.raises(CgmesReadError, match="dangling"):
        read_cgmes(broken, strict=True)
    # strict passes for a complete set
    assert read_cgmes(files, strict=True).warnings == []


def test_property_checks_against_the_profile() -> None:
    # ACDCTerminal.sequenceNumber is an EQ property, not an SSH one: applied, but reported
    body = (
        f'<cim:Terminal rdf:about="#_{TERM}">'
        "<cim:ACDCTerminal.sequenceNumber>2</cim:ACDCTerminal.sequenceNumber></cim:Terminal>"
    )
    files = {"eq.xml": xml([cgmes3.EQ.uri], EQ_BODY), "ssh.xml": xml([cgmes3.SSH.uri], body)}
    doc = read_cgmes(files)
    assert doc.by_id[TERM].sequence_number == 2  # type: ignore[attr-defined]
    assert doc.warnings == [
        "property 'ACDCTerminal.sequenceNumber' of Terminal is not in profile(s) SSH"
    ]
    # unknown class / property, unparsable literal
    body = (
        f'<cim:ACLineSegment rdf:about="#_{LINE}"><cim:ACLineSegment.nope>1</cim:ACLineSegment.nope>'
        "<cim:ACLineSegment.x>abc</cim:ACLineSegment.x></cim:ACLineSegment>"
        '<cim:NoSuchClass rdf:ID="_zzz"/>'
    )
    doc = read_cgmes({"eq.xml": xml([cgmes3.EQ.uri], EQ_BODY + body)})
    text = "\n".join(doc.warnings)
    assert "unknown class 'NoSuchClass'" in text
    assert "unknown property 'ACLineSegment.nope' on ACLineSegment" in text
    assert "cannot parse 'abc'" in text
    # a class outside the file's profiles
    doc = read_cgmes({"tp.xml": xml([cgmes3.TP.uri], f'<cim:ACLineSegment rdf:ID="_{LINE}"/>')})
    assert doc.warnings == ["class 'ACLineSegment' is not in profile(s) TP"]


def _snapshot() -> dict:
    text = resources.files("cim_python_sdk.profiles").joinpath("data/cgmes_3_0.json").read_text("utf-8")
    return json.loads(text)  # type: ignore[no-any-return]


VSC_UF = "".join(
    f'<cim:VsConverter rdf:about="#_{i}"><cim:VsConverter.uf>1.0</cim:VsConverter.uf></cim:VsConverter>'
    for i in ("v1", "v2")
)
VSC_EQ = "".join(f'<cim:VsConverter rdf:ID="_{i}"/>' for i in ("v1", "v2"))


def test_property_outside_profile_and_sdk_warns() -> None:
    # VsConverter.uf: in the CIMTool OWL of SV, not in the ENTSO-E vocabulary nor in CIM17
    files = {"eq.xml": xml([cgmes3.EQ.uri], VSC_EQ), "sv.xml": xml([cgmes3.SV.uri], VSC_UF)}
    doc = read_cgmes(files)
    assert doc.warnings == ["unknown property 'VsConverter.uf' on VsConverter (x2)"]


def test_known_sdk_gap_is_warned_once() -> None:
    # a profile property the SDK does not have (none in CGMES 3.0: a made-up profile set)
    snap = _snapshot()
    snap["profiles"]["SV"]["classes"]["VsConverter"]["properties"]["VsConverter.uf"] = {
        "ns": "cim", "kind": "attribute", "min": 1, "max": 1, "range": "cim:Voltage",
        "range_kind": "datatype", "targets": [], "stereotypes": ["attribute"],
    }  # fmt: skip
    pset = ProfileSet.from_snapshot(snap, "with gap")
    files = {"eq.xml": xml([pset.EQ.uri], VSC_EQ), "sv.xml": xml([pset.SV.uri], VSC_UF)}
    doc = read_cgmes(files, profile_set=pset)
    assert doc.warnings == ["known SDK gap: cim:VsConverter.uf has no SDK member"]
    with pytest.raises(CgmesReadError, match="known SDK gap"):
        read_cgmes(files, strict=True, profile_set=pset)


def test_dynamics_file_reads_without_warnings() -> None:
    body = (
        '<cim:GovHydro1 rdf:ID="_g"><cim:IdentifiedObject.name>G</cim:IdentifiedObject.name>'
        "<cim:GovHydro1.mwbase>120</cim:GovHydro1.mwbase></cim:GovHydro1>"
    )
    doc = read_cgmes({"dy.xml": xml([cgmes3.DY.uri], body)})
    g = doc.by_id["g"]
    assert doc.warnings == [] and g.name == "G"  # type: ignore[attr-defined]
    assert g.mwbase == 120e6  # type: ignore[attr-defined]  # MW -> W


def test_profile_without_classes_is_not_checked() -> None:
    snap = _snapshot()
    snap["profiles"]["DY"]["classes"] = {}
    pset = ProfileSet.from_snapshot(snap, "empty DY")
    body = '<cim:GovHydro1 rdf:ID="_g"><cim:IdentifiedObject.name>G</cim:IdentifiedObject.name></cim:GovHydro1>'
    doc = read_cgmes({"dy.xml": xml([pset.DY.uri], body)}, profile_set=pset)
    assert len(doc.warnings) == 1 and "have no classes" in doc.warnings[0]
    assert doc.by_id["g"].name == "G"  # type: ignore[attr-defined]


# --------------------------------------------------------------------------------------
# sources
# --------------------------------------------------------------------------------------


def test_source_forms(tmp_path: Path, docs: dict[str, str]) -> None:
    orig = dump(read_cgmes(docs).objects)
    # a zip holding a nested zip and noise
    inner = io.BytesIO()
    with zipfile.ZipFile(inner, "w") as zf:
        zf.writestr("TP.xml", docs["TP"])
        zf.writestr("SV.xml", docs["SV"])
    outer = tmp_path / "outer.zip"
    with zipfile.ZipFile(outer, "w") as zf:
        zf.writestr("EQ.xml", docs["EQ"])
        zf.writestr("readme.txt", "ignored")
        zf.writestr("dir/", "")
        zf.writestr("inner.zip", inner.getvalue())
        zf.writestr("SSH.XML", docs["SSH"])
    doc = read_cgmes(outer)
    assert sorted(doc.headers) == ["EQ.xml", "SSH.XML", "SV.xml", "TP.xml"]
    assert dump(doc.objects) == orig
    # a directory with xml and zip files side by side
    d = tmp_path / "mix"
    d.mkdir()
    (d / "EQ.xml").write_text(docs["EQ"], encoding="utf-8")
    (d / "rest.zip").write_bytes(outer.read_bytes())
    (d / "notes.txt").write_text("x")
    assert read_cgmes(d).warnings  # EQ is read twice: duplicate definitions
    assert min(read_cgmes(d).headers) == "EQ.xml"
    # file objects, equal names stay distinct
    doc = read_cgmes([("a.xml", io.BytesIO(docs["EQ"].encode())), ("a.xml", docs["SSH"])])
    assert sorted(doc.headers) == ["a.xml", "a.xml (2)"]
    # profile_set as the cgmes3 facade module or a ProfileSet
    assert read_cgmes(docs, profile_set=cgmes3).profiles == KWS
    assert read_cgmes(docs, profile_set=cgmes3.profile_set).profiles == KWS


def test_errors(tmp_path: Path) -> None:
    with pytest.raises(CgmesReadError, match="not well-formed"):
        read_cgmes({"bad.xml": "<rdf:RDF"})
    with pytest.raises(CimXmlError):  # CgmesReadError is a CimXmlError
        read_cgmes({"bad.xml": "<root/>"})
    with pytest.raises(CgmesReadError, match="not a zip"):
        bad = tmp_path / "bad.zip"
        bad.write_bytes(b"nope")
        read_cgmes(bad)
    with pytest.raises(FileNotFoundError):
        read_cgmes(tmp_path / "missing.xml")
    with pytest.raises(TypeError):
        read_cgmes([1])
    assert read_cgmes([]).objects == []


def test_read_cimxml_unchanged_by_the_refactor() -> None:
    doc = read_cimxml(FIXTURE / "fixture_SSH.xml")
    # one file alone: the SSH rdf:about elements are stubs of the element's class
    assert {type(o).__name__ for o in doc.objects} == {
        "Terminal",
        "SynchronousMachine",
        "Equipment",
    }
    assert doc.header is not None and doc.header["version"] == "001"


# --------------------------------------------------------------------------------------
# opt-in: the full ENTSO-E CGMES 3.0.2 MicroGrid BaseCase (BE, NL, boundary)
# --------------------------------------------------------------------------------------

COMMIT = "f6749ad368fba8dd3776099c040fed07023a1ba3"
BASE = (
    f"https://raw.githubusercontent.com/powsybl/powsybl-core/{COMMIT}/cgmes/cgmes-conformity/"
    "src/main/resources/conformity/cas-3-data-3.0.2/MicroGrid/BaseCase"
)
FILES = {  # path under BASE -> sha256
    **{
        f"MicroGrid-BE-MAS/20210325T1530Z_1D_BE_{k}_001.xml": h
        for k, h in {
            "DL": "ed28b60d930d5e526cfc1b9e3560a4126793574030e65e5af088806f799bb077",
            "EQ": "2b9c3417c0acca1ba8389c6f9be66dc3fcc327523f9a67c2be09ab1e03df41eb",
            "GL": "7541f764cce1cc104b5535b326dcf05c90f28b72304883e7418d23e4dbd35098",
            "SSH": "d419d61f88126fa00663de0b5bb4ff233960a67f1784bae9547ef04c39ba3dde",
            "SV": "2b6286e288cba0f97692d06622b71e52de697baf854fd6df520a831bcf59d6d9",
            "TP": "f6d2342aefad2bd49a663fa34f263dfea46f88bb15091f30fce35a7d17483631",
        }.items()
    },
    **{
        f"MicroGrid-NL-MAS/20210325T1530Z_1D_NL_{k}_001.xml": h
        for k, h in {
            "DL": "bbb5f30ff5f44c48bd0e2188983be5d815f74f17527e033d09797e26300ba942",
            "EQ": "ce7ee39a5ae589659050ead2a320c6b59d8ebd05326dc14a2b9ef1e86f54deaf",
            "GL": "a309ce726848adc0a182dc9717c8508f9ebcbb928b75fa70c10e3ef6012c5e2e",
            "SSH": "2f8eab76dc76e93ba146e700a64272bdbb728491c1434b1f6077ae18078c50b7",
            "SV": "cbfaaf22ffbe9b7cde236c12c0884991ec83943ac98e33a3dda7ea65645bb971",
            "TP": "4710abbeba54ebd4334f0ac1eea1211cca3fcb6218570b388a314910a914c0e0",
        }.items()
    },
    "MicroGrid-BD-MAS/20171002T0930Z_ENTSO-E_EQ_BD_2.xml": (
        "d5a59aabb8554098f7c0185426991f411c3a940f290c600de2b454149e0d6696"
    ),
}


@pytest.fixture(scope="module")
def full_samples(tmp_path_factory: pytest.TempPathFactory) -> dict[str, Path]:
    """BE, NL and BD file lists. ``CIM_PYTHON_SDK_CGMES_SAMPLES`` names a directory holding the files
    (any layout); ``CIM_PYTHON_SDK_CGMES_DOWNLOAD=1`` fetches the pinned commit instead."""
    env = os.environ.get("CIM_PYTHON_SDK_CGMES_SAMPLES")
    if env:
        found = {p.name: p for p in Path(env).rglob("*.xml")}
    elif os.environ.get("CIM_PYTHON_SDK_CGMES_DOWNLOAD") == "1":
        root = tmp_path_factory.mktemp("microgrid")
        found = {}
        for rel, sha in FILES.items():
            try:
                with urllib.request.urlopen(f"{BASE}/{rel}", timeout=30) as r:
                    data = r.read()
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                pytest.skip(f"offline: {e}")
            assert hashlib.sha256(data).hexdigest() == sha, rel
            dest = root / rel.rpartition("/")[2]
            dest.write_bytes(data)
            found[dest.name] = dest
    else:
        pytest.skip("set CIM_PYTHON_SDK_CGMES_SAMPLES=<dir> or CIM_PYTHON_SDK_CGMES_DOWNLOAD=1")
    out: dict[str, Path] = {"BE": [], "NL": [], "BD": []}  # type: ignore[dict-item]
    for rel in FILES:
        name = rel.rpartition("/")[2]
        if name not in found:
            pytest.skip(f"{name} not in CIM_PYTHON_SDK_CGMES_SAMPLES")
        out["BD" if "_BD_" in name else name.split("_")[2]].append(found[name])  # type: ignore[attr-defined]
    return out


def _total(samples: dict[str, Path], *parts: str) -> list[Path]:
    return [p for k in parts for p in samples[k]]  # type: ignore[union-attr]


# BE, NL and BD each hold known data quirks; everything else reads without a warning
EXPECTED_WARNINGS = [
    # EQ_BD_2: Line ...caa3 repeats the mRID of Line ...caa2
    (
        "Line '54a2e470-ef70-443f-ae81-bcf2d117caa3': mRID '54a2e470-ef70-443f-ae81-bcf2d117caa2' "
        "is also the mRID of '54a2e470-ef70-443f-ae81-bcf2d117caa2'; kept the id as mRID"
    )
]


def test_full_microgrid(full_samples: dict[str, Path], tmp_path: Path) -> None:
    files = _total(full_samples, "BE", "NL", "BD")
    doc = read_cgmes(files)
    assert len(doc.headers) == 13
    assert len(doc.objects) == 957 and doc.dangling == []
    assert doc.warnings == EXPECTED_WARNINGS
    assert doc.profiles == ("EQ", "SSH", "TP", "SV", "DL", "GL", "SC", "EQBD")
    # every element of the files landed on an object: compare with the number of rdf:ID
    ids = set()
    for f in files:
        for el in ET.parse(f).getroot()[1:]:
            ids.add(el.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID"))
    ids.discard(None)
    assert len(ids) == len(doc.objects)
    assert doc.by_id["17086487-56ba-4979-b8de-064025a6b4da"].b0ch is not None  # type: ignore[attr-defined]
    # shuffled order gives the same graph
    shuffled = list(files)
    random.Random(1).shuffle(shuffled)
    assert dump(read_cgmes(shuffled).objects) == dump(doc.objects)

    # BE alone: the boundary objects it references are missing
    be = read_cgmes(_total(full_samples, "BE"))
    assert len(be.objects) == 514 and len(be.dangling) == 49
    assert all("dangling" in w for w in be.warnings)
    # BE + boundary: complete
    be_bd = read_cgmes(_total(full_samples, "BE", "BD"))
    assert len(be_bd.objects) == 542 and be_bd.dangling == []

    # write back, read again
    profiles = ["EQ", "SSH", "TP", "SV", "DL", "GL", "SC"]
    for sel, label in ((_total(full_samples, "BE"), "BE"), (files, "all")):
        src = read_cgmes(sel)
        out = tmp_path / label
        with pytest.warns(UserWarning, match="CGMES export"):  # sample data violates the profiles
            write_cgmes(
                src.objects, out, profiles=profiles, header=src.header_for_rewrite(),
                include_reachable=False,
            )  # fmt: skip
        back = read_cgmes(out)
        assert dump(back.objects) == dump(src.objects), label
        assert back.dangling == []  # a reference to an unknown object cannot be written
        assert all("dangling" in w or w.startswith("Line '54a2") for w in back.warnings)

    # the boundary set is written back as its own EQBD file, each object defined exactly once
    bd_ids = {
        el.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
        for f in full_samples["BD"]  # type: ignore[union-attr]
        for el in ET.parse(f).getroot()[1:]
    }
    src = read_cgmes(_total(full_samples, "BE", "BD"))
    assert {"_" + o.mrid for o in src.boundary_objects} == bd_ids  # type: ignore[attr-defined]
    out = tmp_path / "bd"
    with pytest.warns(UserWarning, match="CGMES export"):
        write_cgmes(
            src.objects, out, profiles=[*profiles, "EQBD"], header=src.header_for_rewrite(),
            boundary=src.boundary_objects, include_reachable=False,
        )  # fmt: skip
    back = read_cgmes(out)
    assert dump(back.objects) == dump(src.objects)
    assert {"_" + o.mrid for o in back.boundary_objects} == bd_ids  # type: ignore[attr-defined]
    assert all(w.startswith("Line '54a2") for w in back.warnings), back.warnings


# --------------------------------------------------------------------------------------
# R2: boundary objects, files with several profiles, conflicting values
# --------------------------------------------------------------------------------------


@pytest.mark.filterwarnings("ignore:CGMES export")
def test_boundary_objects_round_trip(tmp_path: Path) -> None:
    net = build_cgmes()
    bv, cn = net["bv"], net["cn0"]
    objs = list(net.values())
    profiles = ("EQ", "EQBD", "SSH", "TP", "SV")
    write_cgmes(objs, tmp_path, profiles=profiles, header=HEADER, boundary=[bv, cn])
    doc = read_cgmes(tmp_path)
    assert doc.warnings == [], doc.warnings  # no "defined more than once"
    assert doc.boundary_objects == [doc.by_id[bv.mrid], doc.by_id[cn.mrid]]  # type: ignore[attr-defined]
    assert "EQBD" in doc.profiles
    # and back again: same files
    again = tmp_path / "again"
    write_cgmes(doc.objects, again, profiles=profiles, header=doc.header_for_rewrite(),
                boundary=doc.boundary_objects, include_reachable=False)  # fmt: skip
    for f in tmp_path.glob("*.xml"):
        assert (again / f.name).read_text("utf-8") == f.read_text("utf-8"), f.name


@pytest.mark.filterwarnings("ignore:CGMES export")
def test_file_with_two_profiles_survives_rewrite(tmp_path: Path) -> None:
    net = build_cgmes()
    line = net["line"]
    assert isinstance(line, c.ACLineSegment)
    line.r0, line.x0 = 3.0, 30.0
    hdr = CgmesHeader(**{**HEADER.__dict__, "combine": {"EQ": ["SC"]}})
    write_cgmes(list(net.values()), tmp_path, profiles=("EQ", "SC", "SSH", "TP", "SV"), header=hdr)
    assert sorted(p.name for p in tmp_path.iterdir()) == sorted(f"model_{k}.xml" for k in KWS)
    doc = read_cgmes(tmp_path)
    assert doc.warnings == [] and "SC" in doc.profiles
    assert doc.by_id[line.mrid].r0 == 3.0  # type: ignore[attr-defined]
    assert doc.header_for_rewrite().combine == {"EQ": ["SC"]}
    again = tmp_path / "again"
    write_cgmes(doc.objects, again, profiles=("EQ", "SC", "SSH", "TP", "SV"), include_reachable=False,
                header=doc.header_for_rewrite())  # fmt: skip
    assert sorted(p.name for p in again.iterdir()) == sorted(f"model_{k}.xml" for k in KWS)
    assert dump(read_cgmes(again).objects) == dump(doc.objects)
    for f in tmp_path.glob("*.xml"):
        assert (again / f.name).read_text("utf-8") == f.read_text("utf-8"), f.name


def test_conflicting_values_across_files_warn() -> None:
    ssh2 = xml(
        [cgmes3.SSH.uri],
        f'<cim:Equipment rdf:about="#_{LINE}"><cim:Equipment.inService>true</cim:Equipment.inService></cim:Equipment>',
    )
    files = {**_three(), "ssh2.xml": ssh2}
    doc = read_cgmes(files)
    assert len(doc.warnings) == 1
    assert "ssh2.xml" in doc.warnings[0] and "Equipment.inService" in doc.warnings[0]
    assert doc.by_id[LINE].in_service is True  # type: ignore[attr-defined]  # the later file wins
    with pytest.raises(CgmesReadError, match="Equipment.inService"):
        read_cgmes(files, strict=True)
    # the same value twice is not a conflict, and neither is a repeated reference
    same = xml(
        [cgmes3.SSH.uri],
        f'<cim:Equipment rdf:about="#_{LINE}"><cim:Equipment.inService>false</cim:Equipment.inService></cim:Equipment>',
    )
    assert read_cgmes({**_three(), "ssh2.xml": same}).warnings == []
    eq2 = xml([cgmes3.EQ.uri], f'<cim:Terminal rdf:about="#_{TERM}"><cim:Terminal.ConductingEquipment rdf:resource="#_{LINE}"/></cim:Terminal>')
    doc = read_cgmes({**_three(), "eq2.xml": eq2})
    assert not any("earlier element" in w for w in doc.warnings)

    # a single-valued reference and the single-valued opposite end of a many end
    other = "bbbbbbbb-0000-0000-0000-000000000099"
    eq3 = xml([cgmes3.EQ.uri], f'<cim:ACLineSegment rdf:ID="_{other}"/>'
              f'<cim:Terminal rdf:about="#_{TERM}"><cim:Terminal.ConductingEquipment rdf:resource="#_{other}"/></cim:Terminal>')
    doc = read_cgmes({**_three(), "eq3.xml": eq3})
    assert any("Terminal.ConductingEquipment" in w for w in doc.warnings), doc.warnings
    assert doc.by_id[TERM].conducting_equipment is doc.by_id[other]  # type: ignore[attr-defined]


def test_empty_source_warns(tmp_path: Path) -> None:
    doc = read_cgmes(tmp_path)  # an empty directory
    assert doc.objects == [] and doc.warnings == ["no XML files found in the source"]
    with pytest.raises(CgmesReadError, match="no XML files"):
        read_cgmes([], strict=True)


def test_units_round_trip_without_float_noise() -> None:
    # 1.1 * 1000 is 1100.0000000000002 in float; the decimal shift keeps 1100.0 and 1.1
    bv = c.BaseVoltage(mrid=uid("bv5"), name="BV", nominal_voltage=1100.0)
    line = c.ACLineSegment(
        mrid=uid("line5"), name="L", r=0.1, x=0.3, bch=0.0, length=2.3e3, base_voltage=bv
    )
    docs = to_cgmes_strings([bv, line], profiles=("EQ",), header=HEADER)
    assert ">1.1<" in docs["EQ"] and ">2.3<" in docs["EQ"]
    doc = read_cgmes(docs)
    bv2, line2 = doc.by_id[uid("bv5")], doc.by_id[uid("line5")]
    assert bv2.nominal_voltage == 1100.0 and line2.length == 2300.0 and line2.r == 0.1
    # ``units="cgmes"`` keeps the numbers of the file
    raw = read_cgmes(docs, units="cgmes")
    assert raw.by_id[uid("bv5")].nominal_voltage == 1.1
    assert raw.by_id[uid("line5")].length == 2.3
    assert to_cgmes_strings([bv, line], profiles=("EQ",), header=HEADER) == docs
    # a value with float noise keeps every digit in the file and reads back as the same float
    line.length = 0.033605 * 1000  # 33.605000000000004
    docs = to_cgmes_strings([bv, line], profiles=("EQ",), header=HEADER)
    assert ">0.033605000000000004<" in docs["EQ"]
    assert read_cgmes(docs).by_id[uid("line5")].length == line.length
