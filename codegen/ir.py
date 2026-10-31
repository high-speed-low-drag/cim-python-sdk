"""Intermediate representation (IR) of the CIM UML model.

Plain frozen dataclasses with tuples, so an IR value is hashable and immutable.
`Model.to_json()` is deterministic: collections are sorted (packages by path,
classifiers and associations by GUID) and dict keys are emitted in sorted order.
Member order inside a classifier (attributes, literals) follows the EA `Pos`
order, which is itself deterministic.

Namespaces: classifiers, attributes and associations carry the RDF namespace prefix of their
names (`namespace`, default ``"cim"``; the CGMES European extensions use ``"eu"``). An
extension classifier (`extends` = a CIM class GUID) only carries attributes that `merge` adds
to that class. Both fields are left out of the JSON when they have their default, so the
CIM100 snapshot does not spell them out.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field, fields, replace
from typing import Any

KINDS = ("class", "enumeration", "cimdatatype", "compound", "primitive")
ASSOCIATION_TYPES = ("Association", "Aggregation")
DEFAULT_NAMESPACE = "cim"
AGGREGATION_KINDS = ("none", "shared", "composite")


@dataclass(frozen=True)
class Package:
    ea_id: int
    guid: str
    name: str
    path: str  # e.g. "TC57CIM/IEC61970/Base/Wires"
    parent: str | None  # parent path, None for the scope root
    notes: str = ""


@dataclass(frozen=True)
class Attribute:
    ea_id: int
    guid: str
    name: str
    type_name: str
    type_guid: str | None  # resolved classifier GUID, None if unresolved
    lower: int
    upper: int | None  # None = unbounded
    default: str | None = None
    is_static: bool = False
    is_const: bool = False
    stereotypes: tuple[str, ...] = ()
    deprecated: bool = False
    notes: str = ""
    namespace: str = DEFAULT_NAMESPACE


@dataclass(frozen=True)
class EnumLiteral:
    ea_id: int
    guid: str
    name: str
    value: str | None = None  # EA "Default" column, e.g. ISO 4217 code for Currency
    notes: str = ""


@dataclass(frozen=True)
class Classifier:
    ea_id: int
    guid: str
    name: str
    package: str  # package path
    kind: str  # one of KINDS
    stereotypes: tuple[str, ...] = ()
    abstract: bool = False
    deprecated: bool = False
    superclass: str | None = None  # superclass GUID
    attributes: tuple[Attribute, ...] = ()
    literals: tuple[EnumLiteral, ...] = ()
    notes: str = ""
    namespace: str = DEFAULT_NAMESPACE
    extends: str | None = None  # extension classifier: GUID of the class it adds attributes to

    def __post_init__(self) -> None:
        if self.kind not in KINDS:
            raise ValueError(f"unknown classifier kind {self.kind!r} for {self.name}")


@dataclass(frozen=True)
class AssociationEnd:
    """A property owned by `owner` (the class that HAS it) pointing at `target`."""

    owner: str  # owner class GUID
    target: str  # target class GUID
    role: str | None  # property name; None when EA has no role name
    lower: int
    upper: int | None  # None = unbounded
    cardinality: str  # raw EA text, e.g. "0..*"
    owner_aggregation: str = "none"  # owner is the whole: none / shared / composite
    navigable: bool = False  # explicitly marked navigable in EA (mostly unspecified)
    notes: str = ""

    def __post_init__(self) -> None:
        if self.owner_aggregation not in AGGREGATION_KINDS:
            raise ValueError(f"bad aggregation {self.owner_aggregation!r}")


@dataclass(frozen=True)
class Association:
    """EA connector between two classes.

    ends[0] is owned by the connector's Start class (EA Dest* columns),
    ends[1] is owned by the connector's End class (EA Source* columns).
    """

    guid: str
    type: str  # "Association" or "Aggregation"
    ends: tuple[AssociationEnd, AssociationEnd]
    name: str | None = None
    stereotypes: tuple[str, ...] = ()
    notes: str = ""
    namespace: str = DEFAULT_NAMESPACE  # of both ends

    def __post_init__(self) -> None:
        if self.type not in ASSOCIATION_TYPES:
            raise ValueError(f"bad association type {self.type!r}")
        if len(self.ends) != 2:
            raise ValueError("association needs exactly two ends")


@dataclass(frozen=True)
class UnresolvedType:
    classifier: str  # owning classifier GUID
    attribute: str
    type_name: str


@dataclass(frozen=True)
class Model:
    versions: dict[str, str] = field(default_factory=dict)  # e.g. IEC61970CIMVersion -> ...
    packages: tuple[Package, ...] = ()
    classifiers: tuple[Classifier, ...] = ()
    associations: tuple[Association, ...] = ()
    unresolved_types: tuple[UnresolvedType, ...] = ()
    stats: dict[str, int] = field(default_factory=dict)  # reader bookkeeping

    # --- canonical form -------------------------------------------------
    def sorted(self) -> Model:
        return replace(
            self,
            versions=dict(sorted(self.versions.items())),
            packages=tuple(sorted(self.packages, key=lambda p: p.path)),
            classifiers=tuple(sorted(self.classifiers, key=lambda c: c.guid)),
            associations=tuple(sorted(self.associations, key=lambda a: a.guid)),
            unresolved_types=tuple(
                sorted(
                    self.unresolved_types,
                    key=lambda u: (u.classifier, u.attribute, u.type_name),
                )
            ),
            stats=dict(sorted(self.stats.items())),
        )

    # --- lookups --------------------------------------------------------
    def classifier_by_guid(self) -> dict[str, Classifier]:
        return {c.guid: c for c in self.classifiers}

    def classifiers_named(self, name: str) -> list[Classifier]:
        return [c for c in self.classifiers if c.name == name]

    # --- JSON -----------------------------------------------------------
    def to_dict(self) -> dict[str, Any]:
        d = asdict(self.sorted())
        for c in d["classifiers"]:
            _drop_defaults(c)
            for a in c["attributes"]:
                _drop_defaults(a)
        for a in d["associations"]:
            _drop_defaults(a)
        return d

    def to_json(self, indent: int | None = 1) -> str:
        return json.dumps(self.to_dict(), indent=indent, sort_keys=True, ensure_ascii=False) + "\n"

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Model:
        return cls(
            versions=dict(d["versions"]),
            packages=tuple(_build(Package, p) for p in d["packages"]),
            classifiers=tuple(_classifier(c) for c in d["classifiers"]),
            associations=tuple(_association(a) for a in d["associations"]),
            unresolved_types=tuple(_build(UnresolvedType, u) for u in d["unresolved_types"]),
            stats=dict(d.get("stats", {})),
        )

    @classmethod
    def from_json(cls, text: str) -> Model:
        return cls.from_dict(json.loads(text))


def _drop_defaults(d: dict[str, Any]) -> None:
    if d.get("namespace") == DEFAULT_NAMESPACE:
        del d["namespace"]
    if "extends" in d and d["extends"] is None:
        del d["extends"]


class MergeError(ValueError):
    pass


def merge(base: Model, ext: Model) -> Model:
    """`base` plus the extension model `ext` (e.g. the CGMES European extensions).

    Packages, classifiers, associations and versions of `ext` are added; GUIDs, package paths
    and version keys must be new. An extension classifier (`extends` set) is not added: its
    attributes are appended to the classifier it extends, keeping their own namespace. Any
    reference to an extension classifier or to an unknown GUID raises `MergeError`. `stats`
    stay those of `base`.
    """
    errors: list[str] = []
    classes = {c.guid: c for c in base.classifiers}
    paths = {p.path for p in base.packages}
    errors += [f"package {p.path} exists" for p in ext.packages if p.path in paths]
    errors += [f"version {k} exists" for k in ext.versions if k in base.versions]
    extensions = {c.guid: c for c in ext.classifiers if c.extends is not None}
    added = [c for c in ext.classifiers if c.extends is None]
    for c in added:
        if c.guid in classes:
            errors.append(f"classifier {c.name} {c.guid} exists")
        classes[c.guid] = c
    extra: dict[str, list[Attribute]] = {}
    for x in sorted(extensions.values(), key=lambda c: c.guid):
        if x.extends not in classes or x.extends in extensions:
            errors.append(f"extension {x.name} extends unknown class {x.extends}")
            continue
        if x.superclass is not None or x.literals:
            errors.append(f"extension {x.name} has a superclass or literals")
        extra.setdefault(x.extends, []).extend(x.attributes)
    known = set(classes)
    for c in added:
        if c.superclass is not None and c.superclass not in known:
            errors.append(f"{c.name}: unknown superclass {c.superclass}")
        for a in c.attributes:
            if a.type_guid is not None and a.type_guid not in known:
                errors.append(f"{c.name}.{a.name}: unknown type {a.type_guid}")
    for g, attrs in extra.items():
        for a in attrs:
            if a.type_guid is not None and a.type_guid not in known:
                errors.append(f"{classes[g].name}.{a.name}: unknown type {a.type_guid}")
            if any(b.name == a.name for b in classes[g].attributes):
                errors.append(f"{classes[g].name}.{a.name} exists")
    assoc_guids = {a.guid for a in base.associations}
    for assoc in ext.associations:
        if assoc.guid in assoc_guids:
            errors.append(f"association {assoc.guid} exists")
        for e in assoc.ends:
            if e.owner not in known or e.target not in known:
                errors.append(f"association {assoc.guid} references an unknown class")
    if errors:
        raise MergeError("\n".join(errors))
    merged = [
        replace(c, attributes=c.attributes + tuple(extra[c.guid])) if c.guid in extra else c
        for c in (*base.classifiers, *added)
    ]
    return replace(
        base,
        versions={**base.versions, **ext.versions},
        packages=base.packages + ext.packages,
        classifiers=tuple(merged),
        associations=base.associations + ext.associations,
        unresolved_types=base.unresolved_types + ext.unresolved_types,
    ).sorted()


def _build(dc: type, d: dict[str, Any]) -> Any:
    kwargs = {}
    for f in fields(dc):
        if f.name not in d:
            continue
        v = d[f.name]
        kwargs[f.name] = tuple(v) if isinstance(v, list) else v
    return dc(**kwargs)


def _classifier(d: dict[str, Any]) -> Classifier:
    d = dict(d)
    d["attributes"] = tuple(_build(Attribute, a) for a in d.get("attributes", ()))
    d["literals"] = tuple(_build(EnumLiteral, x) for x in d.get("literals", ()))
    return _build(Classifier, d)


def _association(d: dict[str, Any]) -> Association:
    d = dict(d)
    d["ends"] = tuple(_build(AssociationEnd, e) for e in d["ends"])
    return _build(Association, d)
