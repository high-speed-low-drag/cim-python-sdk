"""CGMES 3.0 per-profile writer (`cim_python_sdk.serialization.cgmes`)."""

from __future__ import annotations

import collections
import datetime as dt
import re
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import pytest

import cim_python_sdk as c
from cim_python_sdk.profiles import cgmes3, validate_profile
from cim_python_sdk.serialization import (
    CgmesHeader,
    CgmesWriteError,
    to_cgmes_strings,
    to_cimxml_string,
    write_cgmes,
)
from cim_python_sdk.serialization._common import CIM_NS, EU_NS
from tests.serialization.cgmes_network import build_cgmes, uid

RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
MD = "{http://iec.ch/TC57/61970-552/ModelDescription/1#}"
CIM = "{" + CIM_NS + "}"
EU = "{" + EU_NS + "}"
FIXTURE = Path(__file__).parent / "data" / "cgmes3_fixture"
KWS = ("EQ", "SSH", "TP", "SV")
MODEL_IDS = {kw: f"0000000{i}-1111-2222-3333-444444444444" for i, kw in enumerate(KWS)}
HEADER = CgmesHeader(
    scenario_time=dt.datetime(2026, 1, 1, 12, 30, tzinfo=dt.UTC),
    created=dt.datetime(2026, 1, 2, 3, 4, 5, 678),
    modeling_authority_set="http://example.com/tso",
    description="cim_python_sdk test",
    model_ids=MODEL_IDS,
)


@pytest.fixture(scope="module")
def net() -> dict[str, c.CimObject]:
    return build_cgmes()


@pytest.fixture(scope="module")
def docs(net: dict[str, c.CimObject]) -> dict[str, str]:
    return to_cgmes_strings(list(net.values()), header=HEADER)


@pytest.fixture(scope="module")
def roots(docs: dict[str, str]) -> dict[str, ET.Element]:
    return {kw: ET.fromstring(d) for kw, d in docs.items()}


def _id(el: ET.Element) -> str:
    return (el.get(f"{RDF}ID") or el.get(f"{RDF}about") or "").lstrip("#").removeprefix("_")


def _find(root: ET.Element, ident: str) -> ET.Element | None:
    return next((el for el in root[1:] if _id(el) == ident), None)


def _local(tag: str) -> str:
    return tag.rpartition("}")[2]


def _declared_ns(text: str) -> list[tuple[str, str]]:
    m = re.search(r"<rdf:RDF[^>]*>", text)
    assert m is not None
    return re.findall(r'xmlns:(\w+)="([^"]+)"', m.group())


# --------------------------------------------------------------------------------------
# files and headers
# --------------------------------------------------------------------------------------


def test_network_is_valid(net: dict[str, c.CimObject]) -> None:
    profiles = [cgmes3.by_keyword(k) for k in KWS]
    assert validate_profile(list(net.values()), profiles) == []


def test_one_document_per_profile(docs: dict[str, str]) -> None:
    assert list(docs) == list(KWS)
    for text in docs.values():
        assert _declared_ns(text) == [
            ("cim", CIM_NS),
            ("md", MD[1:-1]),
            ("rdf", RDF[1:-1]),
            ("eu", EU_NS),
        ]


def test_header(roots: dict[str, ET.Element]) -> None:
    deps = {"EQ": [], "SSH": ["EQ"], "TP": ["SSH"], "SV": ["TP"]}
    for kw, root in roots.items():
        fm = root[0]
        assert fm.tag == f"{MD}FullModel"
        assert fm.get(f"{RDF}about") == f"urn:uuid:{MODEL_IDS[kw]}"
        assert [_local(e.tag) for e in fm] == [
            "Model.created", "Model.scenarioTime", "Model.description",
            "Model.modelingAuthoritySet", "Model.profile", "Model.version",
        ] + ["Model.DependentOn"] * len(deps[kw])  # fmt: skip
        text = {_local(e.tag): e.text for e in fm}
        assert text["Model.created"] == "2026-01-02T03:04:05Z"
        assert text["Model.scenarioTime"] == "2026-01-01T12:30:00Z"
        assert text["Model.profile"] == cgmes3.by_keyword(kw).uri
        assert text["Model.version"] == "1"
        assert text["Model.modelingAuthoritySet"] == "http://example.com/tso"
        got = [e.get(f"{RDF}resource") for e in fm.findall(f"{MD}Model.DependentOn")]
        assert got == [f"urn:uuid:{MODEL_IDS[d]}" for d in deps[kw]]


def test_header_defaults_and_overrides(net: dict[str, c.CimObject]) -> None:
    objs = list(net.values())
    h = CgmesHeader(
        dependent_on={"EQ": ["urn:uuid:aaaaaaaa-0000-0000-0000-000000000000"]},
        supersedes={"SSH": ["bbbbbbbb-0000-0000-0000-000000000000"]},
        profile_uris={"EQ": ["http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0"]},
        overrides={"SSH": {"version": 7, "description": "SSH only"}},
    )
    with pytest.warns(UserWarning, match="not written"):  # no SV: the island is dropped
        docs = to_cgmes_strings(objs, profiles=("EQ", "SSH", "TP"), header=h, validate=False)
    fms = {kw: ET.fromstring(d)[0] for kw, d in docs.items()}
    ids = {kw: fm.get(f"{RDF}about") for kw, fm in fms.items()}
    assert all(re.fullmatch(r"urn:uuid:[0-9a-f-]{36}", i) for i in ids.values())
    assert len(set(ids.values())) == 3

    def vals(kw: str, name: str) -> list[str | None]:
        return [e.get(f"{RDF}resource") or e.text for e in fms[kw].findall(f"{MD}Model.{name}")]

    assert vals("EQ", "DependentOn") == ["urn:uuid:aaaaaaaa-0000-0000-0000-000000000000"]
    assert vals("EQ", "profile") == [
        cgmes3.EQ.uri, "http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0"
    ]  # fmt: skip
    assert vals("SSH", "Supersedes") == ["urn:uuid:bbbbbbbb-0000-0000-0000-000000000000"]
    assert vals("SSH", "version") == ["7"] and vals("TP", "version") == ["1"]
    assert vals("SSH", "description") == ["SSH only"] and vals("TP", "description") == []
    assert vals("SSH", "DependentOn") == [ids["EQ"]]
    assert vals("TP", "DependentOn") == [ids["SSH"]]
    # created defaults to now, scenarioTime to created
    created = vals("EQ", "created")[0]
    assert created == vals("EQ", "scenarioTime")[0]
    assert created is not None and created.endswith("Z")
    with pytest.raises(TypeError, match="unknown header override"):
        to_cgmes_strings(objs, header=CgmesHeader(overrides={"EQ": {"colour": 1}}), validate=False)


def test_dependency_fallback(net: dict[str, c.CimObject]) -> None:
    objs = list(net.values())
    with pytest.warns(UserWarning, match="not written"):  # no SSH values
        docs = to_cgmes_strings(objs, profiles=("EQ", "TP", "SV"), header=HEADER, validate=False)
    fms = {kw: ET.fromstring(d)[0] for kw, d in docs.items()}

    def deps(kw: str) -> list[str | None]:
        return [e.get(f"{RDF}resource") for e in fms[kw].findall(f"{MD}Model.DependentOn")]

    assert deps("TP") == [f"urn:uuid:{MODEL_IDS['EQ']}"]
    assert deps("SV") == [f"urn:uuid:{MODEL_IDS['TP']}"]
    h = CgmesHeader(model_ids=MODEL_IDS, auto_dependencies=False)
    docs = to_cgmes_strings(objs, header=h, validate=False)
    assert all("DependentOn" not in d for d in docs.values())


# --------------------------------------------------------------------------------------
# ids, objects and properties
# --------------------------------------------------------------------------------------


def test_ids_and_mrid(roots: dict[str, ET.Element]) -> None:
    line, term, tn, island = uid("line"), uid("Line-t1"), uid("tn0"), uid("island")
    eq, ssh, tp, sv = (roots[k] for k in KWS)

    el = _find(eq, line)
    assert el is not None and el.tag == f"{CIM}ACLineSegment" and el.get(f"{RDF}ID") == f"_{line}"
    assert el.findtext(f"{CIM}IdentifiedObject.mRID") == line
    el = _find(eq, term)
    assert el is not None and el.get(f"{RDF}ID") == f"_{term}"
    # description profiles: rdf:about, no mRID
    for root in (ssh, tp):
        el = _find(root, term)
        assert el is not None and el.tag == f"{CIM}Terminal"
        assert el.get(f"{RDF}about") == f"#_{term}" and el.get(f"{RDF}ID") is None
        assert el.find(f"{CIM}IdentifiedObject.mRID") is None
    # SSH describes the line as cim:Equipment (ACLineSegment is not an SSH class)
    el = _find(ssh, line)
    assert el is not None and el.tag == f"{CIM}Equipment"
    assert [_local(e.tag) for e in el] == ["Equipment.inService"]
    # TP defines TopologicalNode, SV defines TopologicalIsland and the Sv* objects
    el = _find(tp, tn)
    assert el is not None and el.get(f"{RDF}ID") == f"_{tn}"
    assert el.findtext(f"{CIM}IdentifiedObject.mRID") == tn
    el = _find(sv, island)
    assert el is not None and el.get(f"{RDF}ID") == f"_{island}"
    assert el.findtext(f"{CIM}IdentifiedObject.mRID") == island
    svv = sv.findall(f"{CIM}SvVoltage")
    assert len(svv) == 2
    assert all(e.get(f"{RDF}ID", "").startswith("_gen") for e in svv)
    assert all(e.find(f"{CIM}IdentifiedObject.mRID") is None for e in svv)
    # SV does not describe TopologicalNodes or Terminals (nothing SV-specific to say)
    assert _find(sv, tn) is None and _find(sv, term) is None
    # every rdf:ID occurs once over the whole set
    defined = [el.get(f"{RDF}ID") for r in roots.values() for el in r[1:] if el.get(f"{RDF}ID")]
    assert len(defined) == len(set(defined))


def test_properties_restricted_to_profile(roots: dict[str, ET.Element]) -> None:
    seen: collections.Counter[tuple[str, str, str | None]] = collections.Counter()
    for kw, root in roots.items():
        p = cgmes3.by_keyword(kw)
        for el in root[1:]:
            listed = {
                f"{{{CIM_NS if i.namespace == 'cim' else EU_NS}}}{i.name}"
                for i in p.properties(_local(el.tag))
            }
            for child in el:
                assert child.tag in listed, (kw, el.tag, child.tag)
                seen[(_id(el), child.tag, child.get(f"{RDF}resource"))] += 1
    assert max(seen.values()) == 1  # every value once over the set


def test_profile_specific_values(roots: dict[str, ET.Element]) -> None:
    line = uid("line")
    eq_line = _find(roots["EQ"], line)
    assert eq_line is not None
    tags = {_local(e.tag) for e in eq_line}
    assert "ACLineSegment.r" in tags and "Equipment.inService" not in tags
    ssh_gen = _find(roots["SSH"], uid("gen"))
    assert ssh_gen is not None and ssh_gen.tag == f"{CIM}SynchronousMachine"
    assert ssh_gen.findtext(f"{CIM}RotatingMachine.p") == "-50.0"
    assert ssh_gen.find(f"{CIM}SynchronousMachine.operatingMode").get(f"{RDF}resource") == (
        CIM_NS + "SynchronousMachineOperatingMode.generator"
    )
    lim = _find(roots["SSH"], uid("lim"))
    assert lim is not None and [_local(e.tag) for e in lim] == ["CurrentLimit.value"]
    tp_term = _find(roots["TP"], uid("Line-t1"))
    assert tp_term is not None
    assert [_local(e.tag) for e in tp_term] == ["Terminal.TopologicalNode"]


def test_association_direction_follows_profile(roots: dict[str, ET.Element]) -> None:
    island = _find(roots["SV"], uid("island"))
    assert island is not None
    nodes = [
        e.get(f"{RDF}resource") for e in island.findall(f"{CIM}TopologicalIsland.TopologicalNodes")
    ]
    assert sorted(nodes) == sorted([f"#_{uid('tn0')}", f"#_{uid('tn1')}"])
    for root in roots.values():
        assert root.find(f".//{CIM}TopologicalNode.TopologicalIsland") is None
    # the generic writer writes this association from the other end
    generic = to_cimxml_string([island_obj := c.TopologicalIsland(mrid="i")])
    assert "TopologicalIsland.TopologicalNodes" not in generic and island_obj is not None
    cn = _find(roots["TP"], uid("cn0"))
    assert cn is not None and cn.get(f"{RDF}about") == f"#_{uid('cn0')}"
    assert [_local(e.tag) for e in cn] == ["ConnectivityNode.TopologicalNode"]


def test_eu_namespace(roots: dict[str, ET.Element]) -> None:
    line = _find(roots["EQ"], uid("line"))
    assert line is not None and line.findtext(f"{EU}IdentifiedObject.shortName") == "L1"
    olt = _find(roots["EQ"], uid("olt"))
    assert olt is not None
    kind = olt.find(f"{EU}OperationalLimitType.kind")
    assert kind is not None and kind.get(f"{RDF}resource") == EU_NS + "LimitKind.patl"


def test_deterministic(net: dict[str, c.CimObject], docs: dict[str, str], tmp_path: Path) -> None:
    again = to_cgmes_strings(list(build_cgmes().values()), header=HEADER)
    assert again == docs
    a = write_cgmes(list(net.values()), tmp_path / "a.zip", header=HEADER)
    b = write_cgmes(list(net.values()), tmp_path / "b.zip", header=HEADER)
    assert (tmp_path / "a.zip").read_bytes() == (tmp_path / "b.zip").read_bytes()
    assert a.model_ids == b.model_ids


# --------------------------------------------------------------------------------------
# output targets and reporting
# --------------------------------------------------------------------------------------


def test_write_directory_and_zip(
    net: dict[str, c.CimObject], docs: dict[str, str], tmp_path: Path
) -> None:
    objs = list(net.values())
    rep = write_cgmes(objs, tmp_path / "out", name="grid", header=HEADER)
    assert rep.files == {kw: f"grid_{kw}.xml" for kw in KWS}
    assert rep.model_ids == {kw: f"urn:uuid:{i}" for kw, i in MODEL_IDS.items()}
    assert rep.issues == [] and rep.dropped == []
    for kw in KWS:
        assert (tmp_path / "out" / f"grid_{kw}.xml").read_text("utf-8") == docs[kw]
    rep = write_cgmes(
        objs, tmp_path / "set.zip", header=HEADER, name="BE",
        file_name="{scenario}_1D_{name}_{keyword}_{version:0>3}.xml",
    )  # fmt: skip
    with zipfile.ZipFile(tmp_path / "set.zip") as zf:
        assert sorted(zf.namelist()) == sorted(f"20260101T1230Z_1D_BE_{kw}_001.xml" for kw in KWS)
        assert zf.read(rep.files["SV"]).decode("utf-8") == docs["SV"]
    write_cgmes(objs, tmp_path / "new" / "dir" / "set.zip", header=HEADER)  # parents are created
    assert (tmp_path / "new" / "dir" / "set.zip").is_file()


def test_dropped_values_are_reported(net: dict[str, c.CimObject]) -> None:
    objs = list(net.values())
    with pytest.warns(UserWarning, match="not written"):
        docs = to_cgmes_strings(objs, profiles=("EQ",), header=HEADER, validate=False)
    assert list(docs) == ["EQ"]
    with pytest.raises(CgmesWriteError, match="Equipment.inService is not written"):
        to_cgmes_strings(objs, profiles=("EQ",), header=HEADER, validate=False, strict=True)
    with pytest.raises(CgmesWriteError, match="TopologicalIsland .* in none of the written"):
        to_cgmes_strings(objs, profiles=("EQ", "SSH", "TP"), validate=False, strict=True)


def test_class_outside_profiles_is_not_written(tmp_path: Path) -> None:
    feeder = c.Feeder(mrid=uid("feeder"), name="F")
    bv = c.BaseVoltage(mrid=uid("bv2"), name="BV", nominal_voltage=11e3)
    with pytest.warns(UserWarning):
        rep = write_cgmes([feeder, bv], tmp_path, header=HEADER)
    assert [str(i.message) for i in rep.dropped] == [
        f"Feeder {uid('feeder')!r} is in none of the written files"
    ]
    assert any(i.severity == "error" for i in rep.issues)  # validate_profile: not in profiles
    text = (tmp_path / "model_EQ.xml").read_text("utf-8")
    assert "Feeder" not in text and uid("bv2") in text
    with pytest.raises(CgmesWriteError):
        write_cgmes([feeder], tmp_path / "strict", header=HEADER, strict=True)
    assert not (tmp_path / "strict").exists()


def test_validation_errors_warn(tmp_path: Path) -> None:
    line = c.ACLineSegment(mrid=uid("bare"), name="bare")  # r, x, bch missing
    with pytest.warns(UserWarning, match="validation error"):
        rep = to_cgmes_strings([line], profiles=("EQ",), header=HEADER)
    assert "EQ" in rep
    with pytest.raises(CgmesWriteError, match="ACLineSegment.r"):
        to_cgmes_strings([line], profiles=("EQ",), header=HEADER, strict=True)


def test_reference_outside_written_set() -> None:
    # a boundary node defined in another model is referenced by its mrid
    bv = c.BaseVoltage(mrid=uid("bv3"), name="BV", nominal_voltage=11e3)
    vl = c.VoltageLevel(mrid=uid("vl3"), name="VL", base_voltage=bv)
    docs = to_cgmes_strings([vl], profiles=("EQ",), header=HEADER, include_reachable=False,
                            validate=False)  # fmt: skip
    el = _find(ET.fromstring(docs["EQ"]), uid("vl3"))
    assert el is not None
    assert el.find(f"{CIM}VoltageLevel.BaseVoltage").get(f"{RDF}resource") == f"#_{uid('bv3')}"


def test_element_class_and_validation_via_ancestor(net: dict[str, c.CimObject]) -> None:
    assert cgmes3.SSH.element_class(c.ACLineSegment) is c.Equipment
    assert cgmes3.SSH.element_class(c.Terminal) is c.Terminal
    assert cgmes3.EQ.element_class(c.ACLineSegment) is c.ACLineSegment
    assert cgmes3.SV.element_class(c.Feeder) is c.IdentifiedObject
    # Equipment.inService of a line is listed in SSH (through Equipment), so not reported
    issues = validate_profile([net["line"]], [cgmes3.EQ, cgmes3.SSH], include_reachable=False)
    assert not [i for i in issues if i.property == "Equipment.inService"]


# --------------------------------------------------------------------------------------
# conformance with the hand-written CGMES 3.0 fixture (the sample file conventions)
# --------------------------------------------------------------------------------------


def _sample(kw: str) -> tuple[str, ET.Element]:
    path = FIXTURE / f"fixture_{kw}.xml"
    text = path.read_text("utf-8")
    return text, ET.fromstring(text)


def _id_style(el: ET.Element) -> tuple[str, bool]:
    return (
        "ID" if el.get(f"{RDF}ID") else "about",
        el.find(f"{CIM}IdentifiedObject.mRID") is not None,
    )


@pytest.mark.parametrize("kw", KWS)
def test_conforms_to_sample_structure(kw: str, docs: dict[str, str]) -> None:
    sample_text, sample = _sample(kw)
    ours = ET.fromstring(docs[kw])
    # namespaces and header shape
    assert dict(_declared_ns(docs[kw])) == dict(_declared_ns(sample_text))
    assert ours[0].tag == sample[0].tag == f"{MD}FullModel"
    assert ours[0].get(f"{RDF}about", "").startswith("urn:uuid:")
    assert sample[0].get(f"{RDF}about", "").startswith("urn:uuid:")

    def order(fm: ET.Element) -> list[str]:
        return list(dict.fromkeys(_local(e.tag) for e in fm))

    if kw == "EQ":  # the sample EQ adds the ShortCircuit profile after DependentOn
        assert set(order(ours[0])) <= set(order(sample[0]))
    else:
        assert order(ours[0]) == order(sample[0])
    assert ours[0].findtext(f"{MD}Model.profile") == sample[0].findtext(f"{MD}Model.profile")
    # the same id style (rdf:ID + mRID vs rdf:about) per class
    sample_style = {el.tag: _id_style(el) for el in sample[1:]}
    our_style = {el.tag: _id_style(el) for el in ours[1:]}
    common = set(sample_style) & set(our_style)
    assert common  # the fixture and our network share classes
    for tag in common:
        assert our_style[tag] == sample_style[tag], tag
    # every sample property is a property of the profiles the sample header names for that
    # element's class (the sample EQ also carries ShortCircuit data, e.g. ACLineSegment.b0ch)
    profs = [cgmes3.by_uri(e.text or "") for e in sample[0].findall(f"{MD}Model.profile")]
    for el in sample[1:]:
        listed = {i.name for p in profs for i in p.properties(_local(el.tag))}
        for child in el:
            assert _local(child.tag) in listed, (kw, el.tag, child.tag)
        # references use the #_ form, as ours do
        for child in el:
            r = child.get(f"{RDF}resource")
            if r is not None and not r.startswith("http"):
                assert r.startswith("#_")


# --------------------------------------------------------------------------------------
# R2: one defining file per object (EQ / EQBD), several profiles in one file
# --------------------------------------------------------------------------------------


def _count_defs(root: ET.Element, ident: str) -> int:
    return sum(1 for el in root[1:] if _id(el) == ident and el.get(f"{RDF}ID") is not None)


@pytest.mark.filterwarnings("ignore:CGMES export")
def test_eq_and_eqbd_define_each_object_once(net: dict[str, c.CimObject]) -> None:
    objs = list(net.values())
    bv = net["bv"]
    docs = to_cgmes_strings(objs, profiles=("EQBD", "EQ", "SSH", "TP", "SV"), header=HEADER)
    eq, bd = ET.fromstring(docs["EQ"]), ET.fromstring(docs["EQBD"])
    assert _count_defs(eq, bv.mrid) == 1 and _find(bd, bv.mrid) is None  # type: ignore[attr-defined]
    assert len(bd) == 1  # header only: nothing is a boundary object unless the caller says so
    for cls in ("BaseVoltage", "VoltageLevel", "Terminal", "ConnectivityNode"):
        ids_eq = {_id(e) for e in eq[1:] if e.tag == CIM + cls and e.get(f"{RDF}ID")}
        ids_bd = {_id(e) for e in bd[1:] if e.tag == CIM + cls and e.get(f"{RDF}ID")}
        assert not ids_eq & ids_bd

    # the caller says which objects are boundary objects: they are defined in EQBD only
    cn = net["cn0"]
    docs = to_cgmes_strings(objs, profiles=("EQ", "EQBD"), header=HEADER, boundary=[bv, cn],
                            validate=False)  # fmt: skip
    eq, bd = ET.fromstring(docs["EQ"]), ET.fromstring(docs["EQBD"])
    for o in (bv, cn):
        assert _count_defs(bd, o.mrid) == 1 and _find(eq, o.mrid) is None  # type: ignore[attr-defined]
    el = _find(bd, bv.mrid)  # type: ignore[attr-defined]
    assert el is not None and el.find(f"{CIM}BaseVoltage.nominalVoltage") is not None
    assert el.find(f"{CIM}IdentifiedObject.mRID") is not None
    # others stay in EQ; references to the boundary objects are unchanged
    assert _count_defs(eq, net["vl"].mrid) == 1  # type: ignore[attr-defined]
    ref = _find(eq, net["vl"].mrid).find(f"{CIM}VoltageLevel.BaseVoltage")  # type: ignore[union-attr]
    assert ref.get(f"{RDF}resource") == f"#_{bv.mrid}"  # type: ignore[attr-defined,union-attr]
    # EQBD alone defines everything it can
    only = to_cgmes_strings(objs, profiles=("EQBD",), header=HEADER, validate=False)
    assert _count_defs(ET.fromstring(only["EQBD"]), bv.mrid) == 1  # type: ignore[attr-defined]


@pytest.mark.filterwarnings("ignore:CGMES export")
def test_combine_writes_profiles_into_one_file() -> None:
    net = build_cgmes()  # not the shared fixture: it is modified
    line = net["line"]
    assert isinstance(line, c.ACLineSegment)
    line.r0, line.x0, line.b0ch = 3.0, 30.0, 2e-5
    if True:
        sep = to_cgmes_strings(list(net.values()), profiles=("EQ", "SC", "SSH"), header=HEADER)
        assert set(sep) == {"EQ", "SC", "SSH"}
        one = to_cgmes_strings(
            list(net.values()), profiles=("EQ", "SC", "SSH"),
            header=CgmesHeader(**{**HEADER.__dict__, "combine": {"EQ": ["SC"]}}),
        )  # fmt: skip
        assert set(one) == {"EQ", "SSH"}
        root = ET.fromstring(one["EQ"])
        uris = [e.text for e in root[0].findall(f"{MD}Model.profile")]
        assert uris == [cgmes3.EQ.uri, cgmes3.SC.uri]
        el = _find(root, line.mrid)  # type: ignore[attr-defined]
        assert el is not None and el.get(f"{RDF}ID")
        assert [e for e in root[1:] if _id(e) == line.mrid] == [el]  # type: ignore[attr-defined]
        assert el.find(f"{CIM}ACLineSegment.r0").text == "3.0"  # type: ignore[union-attr]
        assert el.find(f"{CIM}ACLineSegment.r") is not None and el.find(f"{CIM}IdentifiedObject.mRID") is not None
        # every value of the separate files is in the combined file
        def values(roots: list[ET.Element]) -> collections.Counter[tuple[str, str]]:
            return collections.Counter(
                (_id(e), c_.tag + (c_.text or c_.get(f"{RDF}resource") or ""))
                for r in roots for e in r[1:] for c_ in e
            )  # fmt: skip
        assert values([ET.fromstring(sep[k]) for k in sep]) == values(
            [ET.fromstring(one[k]) for k in one]
        )
        # SSH depends on EQ as before; a guest that is not selected is ignored
        assert ET.fromstring(one["SSH"])[0].find(f"{MD}Model.DependentOn").get(f"{RDF}resource") == (  # type: ignore[union-attr]
            ET.fromstring(one["EQ"])[0].get(f"{RDF}about")
        )
        plain = to_cgmes_strings(list(net.values()), profiles=("EQ",), validate=False,
                                 header=CgmesHeader(combine={"EQ": ["SC"]}))  # fmt: skip
        assert list(plain) == ["EQ"]
        with pytest.raises(ValueError, match="combine"):
            to_cgmes_strings(list(net.values()), profiles=("SC",), header=CgmesHeader(combine={"EQ": ["SC"]}))


def test_file_names_must_differ(net: dict[str, c.CimObject], tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="same name"):
        write_cgmes(list(net.values()), tmp_path, header=HEADER, file_name="{name}.xml")
    assert list(tmp_path.iterdir()) == []


def test_units_are_scaled_to_cgmes(roots: dict[str, ET.Element]) -> None:
    # SI in the objects; kV, MW, MVAr, MVA and km in the files; ohm, S and A unchanged
    eq, ssh, sv = roots["EQ"], roots["SSH"], roots["SV"]
    assert _find(eq, uid("bv")).findtext(f"{CIM}BaseVoltage.nominalVoltage") == "110.0"
    line = _find(eq, uid("line"))
    assert line.findtext(f"{CIM}Conductor.length") == "10.0"
    assert line.findtext(f"{CIM}ACLineSegment.r") == "1.0"
    gen = _find(eq, uid("gen"))
    assert gen.findtext(f"{CIM}RotatingMachine.ratedS") == "250.0"
    assert gen.findtext(f"{CIM}SynchronousMachine.minQ") == "-100.0"
    assert _find(eq, uid("lim")).findtext(f"{CIM}CurrentLimit.normalValue") == "500.0"
    assert _find(ssh, uid("load")).findtext(f"{CIM}EnergyConsumer.q") == "10.0"
    assert {e.text for e in sv.iter(f"{CIM}SvVoltage.v")} == {"110.0", "109.5"}


def test_units_cgmes_writes_values_as_held() -> None:
    bv = c.BaseVoltage(mrid=uid("bv4"), name="BV", nominal_voltage=22.0)
    docs = to_cgmes_strings([bv], profiles=("EQ",), header=HEADER, units="cgmes")
    text = _find(ET.fromstring(docs["EQ"]), uid("bv4")).findtext(f"{CIM}BaseVoltage.nominalVoltage")
    assert text == "22.0"
    with pytest.raises(ValueError, match="units must be one of"):
        to_cgmes_strings([bv], profiles=("EQ",), header=HEADER, units="kV")
