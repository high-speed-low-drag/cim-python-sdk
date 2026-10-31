"""Read an ENTSO-E CGMES RDFS2020 vocabulary (RDF/XML) into plain frozen dataclasses.

Conventions of the CGMES 3.0 vocabularies (entsoe/CGMES-AP, ``CGMES/RDFS/61970-600-2_<Name>-AP-
Voc-RDFS2020.rdf``, checked on all 10 files):

- Flat RDF/XML: every node is an ``rdf:Description`` with ``rdf:about``. ``xml:base`` is
  ``http://iec.ch/TC57/CIM100``, so ``#Terminal`` is ``cim:Terminal``; European members are
  written with the full ``http://iec.ch/TC57/CIM100-European#`` URI.
- The ontology node (``rdf:type owl:Ontology``) carries the profile keyword (``dcat:keyword``), URI
  (``owl:versionIRI``, also ``md:Model.profile`` of an instance file) and version
  (``owl:versionInfo``). The profile package (``rdf:type cims:ClassCategory``; Dynamics has one
  per sub-package) holds the profile description as ``rdfs:comment``.
- A class is ``rdf:type rdfs:Class`` with at most one ``rdfs:subClassOf`` (the profile superclass).
  ``cims:stereotype`` (a ``UML#`` resource or a literal): ``concrete`` (instantiable),
  ``Description`` (instances describe objects defined in another profile: ``rdf:about``),
  ``enumeration``, ``Compound``, ``CIMDatatype``, ``Primitive``, ``European``, ``deprecated``.
  CIMDatatype and Primitive classes are value types, not profile classes; a datatype's
  ``multiplier`` and ``unit`` members carry the fixed values as ``cims:isFixed``.
- Enumeration literals are nodes ``#Kind.literal`` with ``rdf:type #Kind``; the list is what the
  profile allows.
- A property is ``rdf:type rdf:Property`` named ``Class.prop`` with ``rdfs:domain`` (the class
  that lists it), ``cims:multiplicity`` (``M:1``, ``M:1..1``, ``M:0..1``, ``M:0..n``, ``M:1..n``) and
  either ``cims:dataType`` (a datatype, primitive or compound: an attribute) or ``rdfs:range`` (an
  enumeration: an attribute; a class: an association). Of an association's two ends, the one with
  ``cims:AssociationUsed`` ``Yes`` is written in instance files; ``No`` ends are skipped.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
RDFS = "http://www.w3.org/2000/01/rdf-schema#"
OWL = "http://www.w3.org/2002/07/owl#"
CIMS = "http://iec.ch/TC57/1999/rdf-schema-extensions-19990926#"
DCAT = "http://www.w3.org/ns/dcat#"
CIM_NS = "http://iec.ch/TC57/CIM100#"
XSD = "http://www.w3.org/2001/XMLSchema#"
XML_BASE = "{http://www.w3.org/XML/1998/namespace}base"

#: CIM primitives -> XSD types (the range of a primitive attribute in the snapshot)
PRIMITIVES = {
    "String": "string",
    "Boolean": "boolean",
    "Float": "float",
    "Integer": "integer",
    "Decimal": "decimal",
    "DateTime": "dateTime",
    "Date": "date",
    "Time": "time",
    "Duration": "duration",
    "MonthDay": "gMonthDay",
}
# stereotype spellings of the vocabularies -> the snapshot's
_STEREO = {"Description": "description", "European": "european", "Compound": "compound"}
_VALUE_TYPES = {"cimdatatype", "primitive"}


@dataclass(frozen=True)
class RdfsProperty:
    name: str  # CIM local name "Class.prop"
    namespace: str  # e.g. "http://iec.ch/TC57/CIM100#"
    kind: str  # "attribute" / "association"
    min: int
    max: int | None  # None = unbounded
    range: str  # full URI: xsd type, CIM datatype, enumeration, compound or target class
    range_kind: str  # "datatype" / "enumeration" / "compound" / "class"
    targets: tuple[str, ...] = ()  # the range class when the profile lists it
    stereotypes: tuple[str, ...] = ()  # sorted


@dataclass(frozen=True)
class RdfsClass:
    name: str  # CIM local name
    namespace: str
    superclass: str | None  # profile superclass (local name)
    stereotypes: tuple[str, ...] = ()
    literals: tuple[str, ...] | None = None  # enumerations: the literals the profile allows
    properties: tuple[RdfsProperty, ...] = ()

    @property
    def concrete(self) -> bool:
        return "concrete" in self.stereotypes

    @property
    def enumeration(self) -> bool:
        return "enumeration" in self.stereotypes


@dataclass(frozen=True)
class RdfsProfile:
    keyword: str  # dcat:keyword
    uri: str  # owl:versionIRI
    version: str  # owl:versionInfo
    name: str  # the URI's profile name, e.g. "CoreEquipment"
    namespace: str  # profile namespace, e.g. "http://iec.ch/TC57/ns/CIM/CoreEquipment-EU#"
    comment: str
    classes: tuple[RdfsClass, ...]
    units: dict[str, tuple[str, str | None]]  # datatype -> (fixed multiplier, fixed unit)

    def get(self, name: str) -> RdfsClass | None:
        return next((c for c in self.classes if c.name == name), None)


class RdfsError(ValueError):
    pass


def split_uri(uri: str) -> tuple[str, str]:
    """('http://ns#', 'Local') for 'http://ns#Local'."""
    ns, sep, local = uri.rpartition("#")
    if not sep:
        raise RdfsError(f"URI without '#': {uri}")
    return ns + "#", local


Graph = dict[str, dict[str, list[str]]]


def parse_triples(source: str | Path | bytes) -> Graph:
    """Parse flat RDF/XML into {subject: {predicate: [object, ...]}} with absolute URIs."""
    root = ET.fromstring(source) if isinstance(source, bytes) else ET.parse(source).getroot()
    if root.tag != f"{{{RDF}}}RDF":
        raise RdfsError(f"not RDF/XML: root element {root.tag}")
    base = root.get(XML_BASE, "").strip()

    def absolute(ref: str) -> str:
        return base + ref if ref.startswith("#") else ref

    graph: defaultdict[str, defaultdict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for el in root:
        about = el.get(f"{{{RDF}}}about")
        if about is None or el.tag != f"{{{RDF}}}Description":
            raise RdfsError(f"unexpected node {el.tag} {el.attrib}")
        node = graph[absolute(about.strip())]
        for child in el:
            if len(child):
                raise RdfsError(f"nested RDF/XML not supported under {about}")
            pred = child.tag[1:].replace("}", "")
            res = child.get(f"{{{RDF}}}resource")
            node[pred].append(absolute(res.strip()) if res is not None else (child.text or ""))
    return {k: dict(v) for k, v in graph.items()}


def _one(values: list[str], what: str) -> str | None:
    if len(values) > 1:
        raise RdfsError(f"more than one {what}: {values}")
    return values[0] if values else None


def _stereotypes(node: dict[str, list[str]]) -> tuple[str, ...]:
    out = set()
    for s in node.get(CIMS + "stereotype", ()):
        s = s.rsplit("#", 1)[-1].strip()
        out.add(_STEREO.get(s, s))
    return tuple(sorted(out))


def _multiplicity(value: str | None, name: str) -> tuple[int, int | None]:
    if value is None:
        raise RdfsError(f"{name}: no cims:multiplicity")
    m = value.rsplit("#M:", 1)[-1]
    lo, _, hi = m.partition("..")
    hi = hi or lo
    try:
        return int(lo), None if hi == "n" else int(hi)
    except ValueError:
        raise RdfsError(f"{name}: multiplicity {value!r}") from None


def read_rdfs(source: str | Path | bytes) -> RdfsProfile:
    """Read one CGMES RDFS2020 vocabulary file."""
    graph = parse_triples(source)
    types = {s: set(n.get(RDF + "type", ())) for s, n in graph.items()}
    onto = [s for s, t in types.items() if OWL + "Ontology" in t]
    if len(onto) != 1:
        raise RdfsError(f"expected one owl:Ontology node, found {len(onto)}")
    head = graph[onto[0]]
    keyword = _one(head.get(DCAT + "keyword", []), "dcat:keyword")
    uri = _one(head.get(OWL + "versionIRI", []), "owl:versionIRI")
    version = _one(head.get(OWL + "versionInfo", []), "owl:versionInfo")
    if not (keyword and uri and version):
        raise RdfsError("ontology without keyword, versionIRI or versionInfo")
    packages = sorted(s for s, t in types.items() if CIMS + "ClassCategory" in t)
    comment = next(
        (c for p in packages for c in graph[p].get(RDFS + "comment", ()) if c.strip()), ""
    )

    cls_nodes = {s: n for s, n in graph.items() if RDFS + "Class" in types[s]}
    kinds = {s: {x.lower() for x in _stereotypes(n)} for s, n in cls_nodes.items()}
    value_types = {s for s, k in kinds.items() if k & _VALUE_TYPES}

    # fixed units of the datatypes
    units: dict[str, tuple[str, str | None]] = {}
    for dt in sorted(value_types):
        if "cimdatatype" not in kinds[dt]:
            continue
        fixed = {
            m: _one(graph.get(f"{dt}.{m}", {}).get(CIMS + "isFixed", []), f"{dt}.{m} isFixed")
            for m in ("multiplier", "unit")
        }
        if fixed["multiplier"] is not None:
            units[split_uri(dt)[1]] = (fixed["multiplier"].strip(), fixed["unit"])

    literals: defaultdict[str, list[str]] = defaultdict(list)
    for s, t in types.items():
        for typ in t:
            if typ in cls_nodes and "enumeration" in kinds[typ]:
                literals[typ].append(split_uri(s)[1].split(".", 1)[1])

    def _targets(rng: str) -> tuple[str, ...]:
        return (split_uri(rng)[1],) if rng in cls_nodes else ()

    props: defaultdict[str, list[RdfsProperty]] = defaultdict(list)
    for s, node in graph.items():
        if RDF + "Property" not in types[s]:
            continue
        domain = _one(node.get(RDFS + "domain", []), f"domain of {s}")
        if domain is None or domain in value_types:
            continue  # datatype members (value, unit, multiplier)
        if _one(node.get(CIMS + "AssociationUsed", []), f"AssociationUsed of {s}") == "No":
            continue
        ns, name = split_uri(s)
        lo, hi = _multiplicity(_one(node.get(CIMS + "multiplicity", []), name), name)
        stereo = _stereotypes(node)
        dtype = _one(node.get(CIMS + "dataType", []), f"dataType of {name}")
        rng = _one(node.get(RDFS + "range", []), f"range of {name}")
        if dtype is not None:
            local = split_uri(dtype)[1]
            k = kinds.get(dtype, set())
            if "primitive" in k or (dtype not in cls_nodes and local in PRIMITIVES):
                p = RdfsProperty(name, ns, "attribute", lo, hi, XSD + PRIMITIVES[local], "datatype",
                                 (), stereo)  # fmt: skip
            elif "compound" in k:
                p = RdfsProperty(name, ns, "attribute", lo, hi, dtype, "compound",
                                 _targets(dtype), tuple(sorted({*stereo, "compound"})))  # fmt: skip
            else:
                p = RdfsProperty(name, ns, "attribute", lo, hi, dtype, "datatype", (), stereo)
        elif rng is not None and "enumeration" in kinds.get(rng, set()):
            p = RdfsProperty(name, ns, "attribute", lo, hi, rng, "enumeration", _targets(rng),
                             tuple(sorted({*stereo, "enumeration"})))  # fmt: skip
        elif rng is not None:
            p = RdfsProperty(name, ns, "association", lo, hi, rng, "class", _targets(rng), stereo)
        else:
            raise RdfsError(f"{name}: neither cims:dataType nor rdfs:range")
        if domain not in cls_nodes:
            raise RdfsError(f"{name}: domain {domain} is not a class of the profile")
        props[domain].append(p)

    classes: list[RdfsClass] = []
    for s, node in cls_nodes.items():
        if s in value_types:
            continue
        ns, name = split_uri(s)
        sup = _one(node.get(RDFS + "subClassOf", []), f"superclass of {name}")
        own = sorted(props.get(s, ()), key=lambda p: p.name)
        if len({p.name for p in own}) != len(own):
            raise RdfsError(f"{name}: one local property name in two namespaces")
        classes.append(
            RdfsClass(
                name=name,
                namespace=ns,
                superclass=split_uri(sup)[1] if sup else None,
                stereotypes=_stereotypes(node),
                literals=tuple(literals[s]) if "enumeration" in kinds[s] else None,
                properties=tuple(own),
            )
        )
    profile_ns = onto[0].rsplit("#", 1)[0] + "#"
    return RdfsProfile(
        keyword=keyword.strip(),
        uri=uri.strip(),
        version=version.strip(),
        name=uri.rstrip("/").split("/")[-2].removesuffix("-EU"),
        namespace=profile_ns,
        comment=comment.strip(),
        classes=tuple(sorted(classes, key=lambda c: c.name)),
        units=units,
    )
