"""`codegen.rdfs_reader` on a small hand-written vocabulary, and on the pinned files when cached."""

import pytest

from codegen import profile_source
from codegen.rdfs_reader import RdfsError, read_rdfs

CIM = "http://iec.ch/TC57/CIM100#"
EU = "http://iec.ch/TC57/CIM100-European#"
UML = "http://iec.ch/TC57/NonStandard/UML#"
M = "http://iec.ch/TC57/1999/rdf-schema-extensions-19990926#M:"


def doc(body: str, header: bool = True) -> bytes:
    head = """
<rdf:Description rdf:about="http://iec.ch/TC57/ns/CIM/Test-EU#Ontology">
  <dcat:keyword>TST</dcat:keyword>
  <owl:versionIRI rdf:resource="http://iec.ch/TC57/ns/CIM/Test-EU/3.0"/>
  <owl:versionInfo xml:lang="en">3.0.0</owl:versionInfo>
  <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Ontology"/>
</rdf:Description>
<rdf:Description rdf:about="http://iec.ch/TC57/ns/CIM/Test-EU#Package_TestProfile">
  <rdfs:comment>A test profile.</rdfs:comment>
  <rdf:type rdf:resource="http://iec.ch/TC57/1999/rdf-schema-extensions-19990926#ClassCategory"/>
</rdf:Description>"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xmlns:owl="http://www.w3.org/2002/07/owl#"
  xmlns:cims="http://iec.ch/TC57/1999/rdf-schema-extensions-19990926#"
  xmlns:dcat="http://www.w3.org/ns/dcat#" xml:base="http://iec.ch/TC57/CIM100">
{head if header else ""}
{body}
</rdf:RDF>""".encode()


def cls(name: str, *stereo: str, sup: str | None = None, about: str | None = None) -> str:
    s = "".join(
        f'<cims:stereotype rdf:resource="{UML}{x}"/>' if x == "concrete" else
        f"<cims:stereotype>{x}</cims:stereotype>"
        for x in stereo
    )  # fmt: skip
    sup_el = f'<rdfs:subClassOf rdf:resource="#{sup}"/>' if sup else ""
    return (
        f'<rdf:Description rdf:about="{about or "#" + name}">{sup_el}{s}'
        '<rdf:type rdf:resource="http://www.w3.org/2000/01/rdf-schema#Class"/></rdf:Description>'
    )


def prop(name: str, domain: str, mult: str, *, dt: str = "", rng: str = "", extra: str = "",
         about: str | None = None) -> str:  # fmt: skip
    t = f'<cims:dataType rdf:resource="#{dt}"/>' if dt else ""
    t += f'<rdfs:range rdf:resource="#{rng}"/>' if rng else ""
    dom = domain if domain.startswith("http") else "#" + domain
    return (
        f'<rdf:Description rdf:about="{about or "#" + name}">'
        f'<rdfs:domain rdf:resource="{dom}"/>{t}'
        f'<cims:multiplicity rdf:resource="{M}{mult}"/>{extra}'
        '<rdf:type rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"/>'
        "</rdf:Description>"
    )


def fixed(dt: str, mult: str, unit: str) -> str:
    return "".join(
        f'<rdf:Description rdf:about="#{dt}.{m}"><rdfs:domain rdf:resource="#{dt}"/>'
        f'<cims:dataType rdf:resource="#String"/><cims:isFixed>{v}</cims:isFixed>'
        f'<cims:multiplicity rdf:resource="{M}0..1"/>'
        '<rdf:type rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"/>'
        "</rdf:Description>"
        for m, v in (("multiplier", mult), ("unit", unit))
    )


SAMPLE = doc(
    cls("IdentifiedObject")
    + cls("Equipment", sup="IdentifiedObject")
    + cls("Terminal", "concrete", "Description", sup="IdentifiedObject")
    + cls("ACLineSegment", "concrete", sup="Equipment")
    + cls("BoundaryPoint", "concrete", "European", sup="IdentifiedObject", about=EU + "BoundaryPoint")
    + cls("String", "Primitive")
    + cls("Voltage", "CIMDatatype")
    + fixed("Voltage", "k", "V")
    + cls("StreetAddress", "Compound")
    + cls("PhaseCode", "enumeration")
    + '<rdf:Description rdf:about="#PhaseCode.ABC"><rdf:type rdf:resource="#PhaseCode"/></rdf:Description>'
    + '<rdf:Description rdf:about="#PhaseCode.AN"><rdf:type rdf:resource="#PhaseCode"/></rdf:Description>'
    + prop("IdentifiedObject.name", "IdentifiedObject", "0..1", dt="String")
    + prop("ACLineSegment.ratedU", "ACLineSegment", "1..1", dt="Voltage")
    + prop("Terminal.phases", "Terminal", "0..1", rng="PhaseCode")
    + prop("Terminal.ConductingEquipment", "Terminal", "1", rng="Equipment",
           extra="<cims:AssociationUsed>Yes</cims:AssociationUsed>")
    + prop("Equipment.Terminals", "Equipment", "0..n", rng="Terminal",
           extra="<cims:AssociationUsed>No</cims:AssociationUsed>")
    + prop("Terminal.Location", "Terminal", "1..n", rng="Location",
           extra="<cims:AssociationUsed>Yes</cims:AssociationUsed>")
    + prop("BoundaryPoint.address", EU + "BoundaryPoint", "0..1", dt="StreetAddress",
           about=EU + "BoundaryPoint.address", extra="<cims:stereotype>European</cims:stereotype>")
)  # fmt: skip


def test_header_classes_and_units():
    p = read_rdfs(SAMPLE)
    assert (p.keyword, p.uri, p.version, p.name) == (
        "TST", "http://iec.ch/TC57/ns/CIM/Test-EU/3.0", "3.0.0", "Test",
    )  # fmt: skip
    assert p.namespace == "http://iec.ch/TC57/ns/CIM/Test-EU#" and p.comment == "A test profile."
    # value types (Primitive, CIMDatatype) are not profile classes; compounds and enums are
    assert [c.name for c in p.classes] == [
        "ACLineSegment", "BoundaryPoint", "Equipment", "IdentifiedObject", "PhaseCode",
        "StreetAddress", "Terminal",
    ]  # fmt: skip
    assert p.units == {"Voltage": ("k", "V")}
    term = p.get("Terminal")
    assert term.concrete and term.stereotypes == ("concrete", "description")
    assert term.superclass == "IdentifiedObject" and term.namespace == CIM
    bp = p.get("BoundaryPoint")
    assert bp.namespace == EU and "european" in bp.stereotypes
    assert p.get("PhaseCode").literals == ("ABC", "AN") and p.get("PhaseCode").enumeration
    assert p.get("Equipment").literals is None and not p.get("Equipment").concrete


def test_properties():
    p = read_rdfs(SAMPLE)
    props = {q.name: q for c in p.classes for q in c.properties}
    assert "Equipment.Terminals" not in props  # AssociationUsed No: the other end is written
    name = props["IdentifiedObject.name"]
    assert (name.kind, name.min, name.max, name.range, name.range_kind) == (
        "attribute", 0, 1, "http://www.w3.org/2001/XMLSchema#string", "datatype",
    )  # fmt: skip
    u = props["ACLineSegment.ratedU"]
    assert (u.min, u.max, u.range, u.range_kind) == (1, 1, CIM + "Voltage", "datatype")
    ph = props["Terminal.phases"]
    assert (ph.kind, ph.range_kind, ph.targets) == ("attribute", "enumeration", ("PhaseCode",))
    ce = props["Terminal.ConductingEquipment"]
    assert (ce.kind, ce.min, ce.max, ce.targets) == ("association", 1, 1, ("Equipment",))
    loc = props["Terminal.Location"]
    assert (loc.min, loc.max, loc.targets) == (1, None, ())  # range outside the profile
    addr = props["BoundaryPoint.address"]
    assert addr.namespace == EU and addr.range_kind == "compound" and "european" in addr.stereotypes


@pytest.mark.parametrize(
    ("body", "header", "match"),
    [
        ("", False, "one owl:Ontology"),
        (cls("A") + prop("A.x", "A", "0..q", dt="String"), True, "multiplicity"),
        (prop("B.x", "B", "0..1", dt="String"), True, "not a class"),
        (cls("A") + prop("A.x", "A", "0..1"), True, "neither"),
    ],
)
def test_errors(body, header, match):
    with pytest.raises(RdfsError, match=match):
        read_rdfs(doc(body, header))


def test_pinned_vocabularies():
    paths = profile_source.cached_profiles()
    if paths is None:
        pytest.skip("vocabularies not cached; run tools/fetch_profiles.py")
    for kw, path in paths.items():
        p = read_rdfs(path)
        assert p.keyword == kw and p.uri.startswith("http://iec.ch/TC57/ns/CIM/")
        for c in p.classes:
            for q in c.properties:
                assert q.name.split(".")[0] == c.name or c.name in q.name, (kw, q.name)
