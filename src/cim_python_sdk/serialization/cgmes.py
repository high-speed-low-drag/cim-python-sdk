"""CGMES 3.0 writer: one CIMXML file per profile (EQ, SSH, TP, SV, ...), driven by the profile
snapshot of `cim_python_sdk.profiles` (``cgmes3``).

    from cim_python_sdk.serialization.cgmes import CgmesHeader, write_cgmes

    report = write_cgmes(network, "out/", name="grid",
                         header=CgmesHeader(scenario_time=t, modeling_authority_set="http://x.eu/"))
    # out/grid_EQ.xml, out/grid_SSH.xml, out/grid_TP.xml, out/grid_SV.xml

`write_cgmes` writes to a directory, or into a zip when `out` ends with ``.zip``; `to_cgmes_strings`
returns ``{keyword: document}``. Value encoding (floats, booleans, dates, enum resources,
compounds) and wire ids follow `cim_python_sdk.serialization._common`; this module only decides which
object, which property and which header goes into which file.

Conventions (verified against the ENTSO-E CGMES 3.0 conformity test configuration
"MicroGrid BaseCase" v3.0.2, BE and NL EQ/SSH/TP/SV files, as shipped in powsybl-core
``cgmes/cgmes-conformity/src/main/resources/conformity/cas-3-data-3.0.2/MicroGrid/BaseCase/``
at commit f6749ad368fba8dd3776099c040fed07023a1ba3, https://github.com/powsybl/powsybl-core; and
against powsybl-core's CGMES export, ``CgmesExportUtil.java`` / ``CgmesExport.java``, same commit)
------------------------------------------------------------------------------------------------
Root and namespaces
    ``rdf:RDF`` always declares ``cim`` (``http://iec.ch/TC57/CIM100#``), ``md``
    (``http://iec.ch/TC57/61970-552/ModelDescription/1#``), ``rdf`` and ``eu``
    (``http://iec.ch/TC57/CIM100-European#``), in this order, as the samples do (``eu`` even
    when unused). No ``dcat``/``dcterms``: CGMES 3.0 files use the IEC 61970-552:2016
    ``md:FullModel`` header, not the dcat header of later profiles.
Header (``md:FullModel``, IEC 61970-552:2016), first element, in the samples' order:
    ``rdf:about="urn:uuid:<model id>"``; ``md:Model.created``; ``md:Model.scenarioTime`` (both
    ``YYYY-MM-DDTHH:MM:SSZ``, UTC); ``md:Model.description``; ``md:Model.modelingAuthoritySet``;
    ``md:Model.profile`` (the profile URI, e.g. ``http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0``;
    repeatable: the sample EQ files also carry the ShortCircuit URI); ``md:Model.version``;
    ``md:Model.DependentOn`` and ``md:Model.Supersedes`` (``rdf:resource="urn:uuid:..."``).
    See `CgmesHeader`.
Dependencies (``md:Model.DependentOn``)
    The CGMES 3.0 samples chain the files: SSH -> EQ, TP -> SSH, SV -> TP (and EQ -> EQBD).
    powsybl's export uses the CGMES 2.4.15 pattern instead (TP -> EQ, SSH -> EQ, SV -> TP + SSH).
    This writer follows the samples. A profile whose preferred dependency is not written falls
    back to the next one (TP -> EQ without SSH; SV -> SSH, else EQ, without TP); DL, GL, OP and SC
    depend on EQ. Dependencies outside the written set (a boundary set) come from
    ``CgmesHeader.dependent_on``.
Ids
    An object is written with ``rdf:ID="_<mrid>"`` in a profile that defines it (its class is
    concrete there and not a ``description``: `ProfileSet.defining_profiles`) and with
    ``rdf:about="#_<mrid>"`` in every other profile. A class that is concrete in both EQ and EQBD
    (BaseVoltage, ConnectivityNode, Line, Substation, Terminal, ...) is defined in exactly one of
    them: EQ, or EQBD for the objects passed as ``boundary=`` (the writer cannot tell boundary
    objects from the others); the other file only describes it, and is left without the
    element when that adds nothing. References are ``rdf:resource="#_<mrid>"``.
    ``cim:IdentifiedObject.mRID`` is written as an element (the plain mrid, no ``_``) in the
    defining file only, when the profile lists it for the class (the samples never repeat it in
    ``rdf:about`` elements; classes outside IdentifiedObject, e.g. ``SvPowerFlow``, have none).
    Objects without an mrid get ``_gen<N>`` as in the generic writer.
Objects and properties per file
    A file holds the profile's properties only (`Profile.properties`, Python name -> profile
    ``qname``, ``eu:`` for extensions). Every property value is written once over the whole
    file set: a description (``rdf:about``) element leaves out the properties that a profile
    defining the class lists (so TP terminals carry ``Terminal.TopologicalNode`` but not the EQ
    name), and among the written profiles the defining ones claim a property first, then the
    others in order. An object appears in a file when that file defines it, or when it has a
    value for one of the file's remaining properties. When the object's own class is not in the
    profile, it is described under its nearest profile ancestor that adds properties: the sample
    SSH files write ``<cim:Equipment rdf:about="#_<line>">`` with ``Equipment.inService`` for
    lines, transformers and busbars. Objects whose class is in no profile of the set are not
    written (reported).
Associations
    Written from the side the profile lists (`PropertyInfo.owner`), which differs from the
    generic writer's rule for e.g. SV ``TopologicalIsland.TopologicalNodes``. A reference may
    point at an object outside the written set (e.g. a boundary ConnectivityNode) when that
    object has an mrid.
Units
    The SDK holds SI values (V, W, VAr, VA, m). CGMES fixes a multiplier per datatype (kV, MW,
    MVAr, MVA, km; `ProfileSet.unit_exponent`), so with ``units="si"`` (the default) the writer
    divides and the reader multiplies by it. The shift is done on the decimal text
    (`_scaled_text`, `_CgmesReader._value`), so it is exact both ways: ``220.1`` kV reads as
    ``220100.0`` V and writes back as ``220.1``, and a value with float noise such as
    ``33.605000000000004`` m is written as ``0.033605000000000004`` km and reads back as the
    same float. ``units="cgmes"`` writes
    and reads the numbers as they are, for objects that already hold CGMES units. Compound
    attributes are not scaled (no CGMES compound has a scaled datatype).
Enumerations
    ``rdf:resource="<namespace><Enum>.<literal>"``; ``eu`` enums (``LimitKind``) use the ``eu``
    URI. File names default to ``<name>_<KEYWORD>.xml``; the ENTSO-E convention
    ``<scenarioTime>_<process>_<TSO>_<KEYWORD>_<version>.xml`` is available through
    ``file_name`` (fields ``name keyword version scenario``).

Several profiles in one file
    ``CgmesHeader.combine`` (``{"EQ": ["SC"]}``) writes the ShortCircuit properties into the EQ
    file, as the ENTSO-E samples do, and lists both profile URIs in its header. Without it every
    selected profile gets its own file, so an EQ file read with two profile URIs is split on
    rewrite; ``CgmesDocument.header_for_rewrite()`` sets ``combine`` to keep such files whole.

Reading (`read_cgmes`)
    A CGMES file set (directory, ``.zip``, paths, or ``(name, bytes)`` pairs) is merged into one
    object graph (`CgmesDocument`). An ``rdf:ID`` element defines an object; ``rdf:about`` elements
    in any other file describe the same object (merged by normalized id, whatever the file order).
    An element whose class is an ancestor of the object's (SSH ``<cim:Equipment rdf:about=...>``)
    only adds properties; it neither creates an object nor changes the defined class. An id that is
    only described gets the most specific class seen (warning). ``mRID`` is the
    ``IdentifiedObject.mRID`` element, else the id without its ``_``. Each file's ``md:FullModel``
    is kept (`CgmesFileHeader`); the profiles named by its ``md:Model.profile`` URIs (unknown URIs
    warn) classify the file's properties: not in the profile, or a known SDK gap
    (``python_name`` None), is a warning. A value that differs from one
    set by an earlier file (or element) is a warning too; the later one wins, so the file order
    only matters for such conflicts. Objects defined in an EQBD file are listed in
    ``CgmesDocument.boundary_objects``. Non-strict readers collect
    warnings and dangling references (checked after all files are merged); ``strict=True`` raises.

Reporting
    Before writing, `validate_profile` runs against the selected profiles (``validate=True``).
    Every property value, link or object that no written file carries is listed in
    `CgmesReport.dropped`. Without ``strict`` a single ``warnings.warn`` summarises validation
    errors and dropped data; ``strict=True`` raises `CgmesWriteError` instead, before anything
    is written.
"""

from __future__ import annotations

import datetime as _dt
import io
import os
import uuid
import warnings
import xml.etree.ElementTree as ET
import zipfile
from collections.abc import Mapping
from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path

from cim_python_sdk._runtime import CimCompound, CimObject
from cim_python_sdk.profiles._model import Profile, ProfileSet
from cim_python_sdk.profiles._validate import ProfileIssue, validate_profile
from cim_python_sdk.serialization._common import (
    CIM_NS,
    EU_NS,
    AttrSpec,
    CimDocument,
    ClassPlan,
    EndSpec,
    assign_ids,
    class_plan,
    collect,
    encode_value,
    normalize_id,
    resolve_class,
)
from cim_python_sdk.serialization.cimxml import (
    _RDF_ABOUT,
    _RDF_ID,
    _RDF_NODE_ID,
    _RDF_ROOT,
    MD_NS,
    RDF_NS,
    CimXmlError,
    _Reader,
    _serialize,
    _split,
    _wire_ids,
    _write_value,
    _xml_text,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator, Sequence
    from typing import Any

    from cim_python_sdk.profiles._model import PropertyInfo

__all__ = [
    "DEFAULT_PROFILES",
    "CgmesDocument",
    "CgmesFileHeader",
    "CgmesHeader",
    "CgmesReadError",
    "CgmesReport",
    "CgmesWriteError",
    "read_cgmes",
    "to_cgmes_strings",
    "write_cgmes",
]

DEFAULT_PROFILES = ("EQ", "SSH", "TP", "SV")
_BOUNDARY = "EQBD"  # keyword of the equipment boundary profile
DEFAULT_MAS = "http://cim-python-sdk.invalid/modelingAuthoritySet"

# preferred DependentOn, first written alternative wins (see the module docstring)
_DEPENDS: dict[str, tuple[tuple[str, ...], ...]] = {
    "EQ": (("EQBD",),),
    "SSH": (("EQ",),),
    "TP": (("SSH", "EQ"),),
    "SV": (("TP", "SSH", "EQ"),),
    "DL": (("EQ",),),
    "GL": (("EQ",),),
    "OP": (("EQ",),),
    "SC": (("EQ",),),
    "DY": (("SSH", "EQ"),),
}

_ROOT_NS = (("cim", CIM_NS), ("md", MD_NS), ("rdf", RDF_NS), ("eu", EU_NS))
_UNITS = ("si", "cgmes")


def _check_units(units: str) -> bool:
    """True when values are to be scaled (``units="si"``)."""
    if units not in _UNITS:
        raise ValueError(f"units must be one of {_UNITS}, not {units!r}")
    return units == "si"


def _exponent(spec: AttrSpec | None, pset: ProfileSet) -> int:
    """Power of ten between the SDK value of `spec` and its CGMES value (0: as held)."""
    if spec is None or spec.kind != "cimdatatype":
        return 0
    return pset.unit_exponent(spec.type_name)


def _scaled_text(value: Any, exponent: int) -> str | None:
    """Text of `value` times ``10**exponent``, shifted in decimal, or None for a value that is
    not a finite number. The shortest float text when it is exact (``110.0``), else every digit
    of the shift (``0.033605000000000004``), so the reader's shift gives back the same float."""
    if isinstance(value, bool) or not isinstance(value, int | float | Decimal):
        return None
    d = (value if isinstance(value, Decimal) else Decimal(repr(value))).scaleb(exponent)
    if not d.is_finite():
        return None
    if isinstance(value, Decimal):
        return str(d)
    f = float(d)
    return repr(f) if Decimal(repr(f)) == d else str(d)


class CgmesWriteError(ValueError):
    """Raised by ``strict=True`` for validation errors or data no written file carries."""


@dataclass(frozen=True)
class CgmesHeader:
    """Header (``md:FullModel``) values for a CGMES file set.

    Scalars apply to every file; ``overrides`` replaces them per profile keyword
    (``{"SSH": {"version": "2"}}``). ``model_ids`` fixes the model id of a file (``urn:uuid:``
    added to a bare UUID; default: a random UUID per file and call). ``dependent_on`` and
    ``supersedes`` add model ids per keyword (e.g. the boundary EQ for ``"EQ"``); dependencies
    between the files written together are added automatically unless ``auto_dependencies`` is
    false. ``profile_uris`` adds ``md:Model.profile`` URIs per keyword (a file holding EQ and SC
    data lists both). ``created`` defaults to now (UTC, one value for the call),
    ``scenario_time`` to ``created``; naive datetimes are taken as UTC.

    ``combine`` writes several selected profiles into one file: ``{"EQ": ["SC"]}`` puts the
    ShortCircuit properties into the EQ file (as the ENTSO-E samples do), joined to the EQ
    element of each object, and lists both profile URIs in its header. The guest profile gets no
    file of its own, model id or dependencies. Profiles that are not selected are ignored.
    """

    scenario_time: _dt.datetime | None = None
    created: _dt.datetime | None = None
    modeling_authority_set: str = DEFAULT_MAS
    description: str | None = None
    version: str | int = "1"
    model_ids: Mapping[str, str] = field(default_factory=dict)
    dependent_on: Mapping[str, Sequence[str]] = field(default_factory=dict)
    supersedes: Mapping[str, Sequence[str]] = field(default_factory=dict)
    profile_uris: Mapping[str, Sequence[str]] = field(default_factory=dict)
    overrides: Mapping[str, Mapping[str, Any]] = field(default_factory=dict)
    auto_dependencies: bool = True
    combine: Mapping[str, Sequence[str]] = field(default_factory=dict)


@dataclass
class CgmesReport:
    """What `write_cgmes` wrote and what it could not place."""

    files: dict[str, str] = field(default_factory=dict)  # keyword -> file name / zip member
    model_ids: dict[str, str] = field(default_factory=dict)  # keyword -> urn:uuid:...
    headers: dict[str, dict[str, Any]] = field(default_factory=dict)  # keyword -> header items
    issues: list[ProfileIssue] = field(default_factory=list)  # validate_profile findings
    dropped: list[ProfileIssue] = field(default_factory=list)  # values no written file carries

    @property
    def errors(self) -> list[ProfileIssue]:
        return [i for i in self.issues if i.severity == "error"]


# --------------------------------------------------------------------------------------
# header
# --------------------------------------------------------------------------------------


def _utc(t: _dt.datetime) -> str:
    if t.tzinfo is not None:
        t = t.astimezone(_dt.UTC)
    return t.replace(tzinfo=None, microsecond=0).isoformat() + "Z"


def _urn(model_id: str) -> str:
    return model_id if ":" in model_id else f"urn:uuid:{model_id}"


def _header_items(
    header: CgmesHeader, profiles: Sequence[Profile], now: _dt.datetime
) -> dict[str, dict[str, Any]]:
    kws = [p.keyword for p in profiles]
    ids = {}
    for kw in kws:
        given = header.model_ids.get(kw)
        ids[kw] = _urn(given) if given else f"urn:uuid:{uuid.uuid4()}"
    out: dict[str, dict[str, Any]] = {}
    for p in profiles:
        kw = p.keyword
        o = dict(header.overrides.get(kw, {}))
        created = o.pop("created", header.created) or now
        scenario = o.pop("scenario_time", header.scenario_time) or created
        deps: list[str] = []
        if header.auto_dependencies:
            for alternatives in _DEPENDS.get(kw, ()):
                dep = next((d for d in alternatives if d in ids), None)
                if dep is not None:
                    deps.append(ids[dep])
        deps += [_urn(d) for d in header.dependent_on.get(kw, ())]
        items: dict[str, Any] = {
            "about": ids[kw],
            "created": _utc(created),
            "scenarioTime": _utc(scenario),
            "description": o.pop("description", header.description),
            "modelingAuthoritySet": o.pop("modeling_authority_set", header.modeling_authority_set),
            "profile": [p.uri, *header.profile_uris.get(kw, ())],
            "version": str(o.pop("version", header.version)),
            "DependentOn": list(dict.fromkeys(deps)),
            "Supersedes": [_urn(d) for d in header.supersedes.get(kw, ())],
        }
        if o:
            raise TypeError(f"unknown header override(s) for {kw}: {', '.join(sorted(o))}")
        out[kw] = items
    return out


def _header_element(items: dict[str, Any]) -> ET.Element:
    el = ET.Element("md:FullModel", {"rdf:about": items["about"]})
    for key, val in items.items():
        if key == "about" or val is None:
            continue
        for v in val if isinstance(val, list) else (val,):
            sub = ET.SubElement(el, f"md:Model.{key}")
            if key in ("DependentOn", "Supersedes"):
                sub.set("rdf:resource", v)
            else:
                sub.text = _xml_text(v, "header", f"Model.{key}")
    return el


# --------------------------------------------------------------------------------------
# per-class plans
# --------------------------------------------------------------------------------------


@dataclass
class _ClassPlan:
    tag: str  # element qname
    defining: bool
    mrid: bool  # write IdentifiedObject.mRID (defining and listed)
    props: tuple[PropertyInfo, ...]  # attributes and ends to write (mRID excluded)


def _owner(chosen: Sequence[Profile], boundary: bool) -> Profile | None:
    """The one profile that defines an object (``rdf:ID``, mRID) among the written profiles that
    could: EQ before EQBD, or EQBD for a boundary object. Classes concrete in both are the only
    case (BaseVoltage, ConnectivityNode, Line, Substation, ...)."""
    if not chosen:
        return None
    if boundary:
        for p in chosen:
            if p.keyword == _BOUNDARY:
                return p
    for p in chosen:  # `chosen` is in profile set order
        if p.keyword != _BOUNDARY:
            return p
    return chosen[0]


def _plans_for(
    cls: type, profiles: Sequence[Profile], pset: ProfileSet, boundary: bool = False
) -> dict[str, _ClassPlan | None]:
    """Per written profile keyword, how instances of `cls` are written there (None: never)."""
    if not pset.has_class(cls):
        return {p.keyword: None for p in profiles}
    defining_all = pset.defining_profiles(cls)
    chosen = [p for p in defining_all if p in profiles]
    owner = _owner(chosen, boundary)
    defined_props = {i.name for d in defining_all for i in d.properties(cls)}
    owner_props = defined_props if owner is None else {i.name for i in owner.properties(cls)}
    # the owner claims first, then the other defining profiles, then the descriptions
    order = sorted(profiles, key=lambda p: (p is not owner, p not in chosen))
    claimed: set[str] = set()
    out: dict[str, _ClassPlan | None] = {}
    for p in order:
        el_cls = p.element_class(cls)
        if el_cls is None:
            out[p.keyword] = None
            continue
        defining = p is owner
        skip = owner_props if p in chosen else defined_props  # properties another file carries
        mrid = False
        props = []
        for info in p.properties(el_cls):
            if info.python_name is None:
                continue
            if info.name == "IdentifiedObject.mRID":
                mrid = defining
                continue
            if not defining and info.name in skip:
                continue
            if info.python_name in claimed:
                continue
            claimed.add(info.python_name)
            props.append(info)
        out[p.keyword] = _ClassPlan(class_plan(el_cls).qname, defining, mrid, tuple(props))
    return out


# --------------------------------------------------------------------------------------
# building
# --------------------------------------------------------------------------------------


def _select(
    profiles: Iterable[Profile | str] | Profile | str, pset: ProfileSet
) -> tuple[Profile, ...]:
    if isinstance(profiles, Profile | str):
        profiles = (profiles,)
    out = []
    for p in profiles:
        prof = pset.by_keyword(p) if isinstance(p, str) else p
        if not isinstance(prof, Profile):
            raise TypeError(f"not a Profile or keyword: {p!r}")
        if prof not in out:
            out.append(prof)
    if not out:
        raise ValueError("no profiles selected")
    return tuple(out)


def _default_set() -> ProfileSet:
    from cim_python_sdk.profiles import cgmes3

    return cgmes3.profile_set  # type: ignore[no-any-return]


def _build(
    objects: Any,
    profiles: Iterable[Profile | str] | Profile | str,
    header: CgmesHeader | None,
    include_reachable: bool,
    validate: bool,
    strict: bool,
    profile_set: ProfileSet | None,
    boundary: Iterable[CimObject] = (),
    units: str = "si",
) -> tuple[dict[str, bytes], CgmesReport]:
    scale = _check_units(units)
    pset = profile_set if profile_set is not None else _default_set()
    selected = _select(profiles, pset)
    hdr = header or CgmesHeader()
    combine = _combine_plan(hdr.combine, selected)
    boundary_ids = {id(o) for o in boundary}
    if isinstance(objects, CimObject):
        objects = [objects]
    objs = collect(objects, include_reachable)
    ids = assign_ids(objs)
    order = {o: i for i, o in enumerate(objs)}
    refs = {o: _wire_ids(i) for o, i in ids.items()}
    report = CgmesReport()
    if validate:
        report.issues = validate_profile(objs, selected, include_reachable=False)

    def ref_of(t: CimObject) -> str | None:
        r = refs.get(t)
        if r is not None:
            return r[1]
        m = getattr(t, "mrid", None)
        return _wire_ids(m)[1] if isinstance(m, str) else None

    plans: dict[tuple[type, bool], dict[str, _ClassPlan | None]] = {}
    written_attrs: set[tuple[int, str]] = set()
    written_links: set[tuple[int, str, int]] = set()
    placed: set[int] = set()
    bodies: dict[str, list[ET.Element]] = {p.keyword: [] for p in selected}
    for obj in objs:
        cls = type(obj)
        pkey = (cls, id(obj) in boundary_ids)
        per = plans.get(pkey)
        if per is None:
            per = plans[pkey] = _plans_for(cls, selected, pset, pkey[1])
        where = f"{class_plan(cls).cim_name} {ids[obj]!r}"
        for p in selected:
            plan = per[p.keyword]
            if plan is None:
                continue
            children: list[ET.Element] = []
            if plan.mrid and isinstance(getattr(obj, "mrid", None), str):
                mrid_el = ET.Element("cim:IdentifiedObject.mRID")
                mrid_el.text = _xml_text(obj.mrid, where, "IdentifiedObject.mRID")  # type: ignore[attr-defined]
                children.append(mrid_el)
            for info in plan.props:
                name = info.python_name
                assert name is not None
                if info.is_association:
                    desc = getattr(cls, name)
                    v = desc.__get__(obj)
                    targets = list(v) if info.many else ([] if v is None else [v])
                    targets.sort(key=lambda t: (order.get(t, len(order)), ref_of(t) or ""))
                    for t in targets:
                        r = ref_of(t)
                        if r is None:
                            continue
                        children.append(ET.Element(info.qname, {"rdf:resource": r}))
                        written_links.add((id(obj), name, id(t)))
                else:
                    v = getattr(obj, name, None)
                    if v is None:
                        continue
                    el = ET.Element(info.qname)
                    exp = _exponent(info._spec, pset) if scale else 0
                    text = _scaled_text(v, -exp) if exp else None
                    if text is None:
                        _write_value(el, v, CIM_NS, where, info.name)
                    else:
                        el.text = text
                    children.append(el)
                    written_attrs.add((id(obj), name))
            if not plan.defining and not children:
                continue
            ident, ref = refs[obj]
            attrib = dict([ident]) if plan.defining else {"rdf:about": ref}
            el = ET.Element(plan.tag, attrib)
            el.extend(children)
            bodies[p.keyword].append(el)
            placed.add(id(obj))
    report.dropped = _dropped(objs, placed, written_attrs, written_links, ids)

    errors = report.errors
    if strict and (errors or report.dropped):
        lines = [str(i) for i in (errors + report.dropped)[:20]]
        more = len(errors) + len(report.dropped) - len(lines)
        tail = f"\n... and {more} more" if more > 0 else ""
        raise CgmesWriteError("CGMES export problems:\n" + "\n".join(lines) + tail)
    if errors or report.dropped:
        warnings.warn(
            f"CGMES export: {len(errors)} validation error(s), {len(report.dropped)} value(s) "
            f"not written in the selected profiles ({', '.join(p.keyword for p in selected)}); "
            f"see CgmesReport.issues / .dropped",
            stacklevel=3,
        )

    now = _dt.datetime.now(_dt.UTC)
    headers = _header_items(hdr, selected, now)
    for host, guests in combine.items():  # the guests' elements and URIs move into the host file
        bodies[host.keyword] = _merge_bodies(
            bodies[host.keyword], [e for g in guests for e in bodies[g.keyword]]
        )
        headers[host.keyword]["profile"] += [g.uri for g in guests]
        for g in guests:
            del headers[g.keyword], bodies[g.keyword]
    report.headers = headers
    report.model_ids = {kw: h["about"] for kw, h in headers.items()}
    docs: dict[str, bytes] = {}
    for p in selected:
        if p.keyword not in headers:
            continue
        root = ET.Element("rdf:RDF", {f"xmlns:{k}": v for k, v in _ROOT_NS})
        root.append(_header_element(headers[p.keyword]))
        root.extend(bodies[p.keyword])
        ET.indent(root, space="  ")
        docs[p.keyword] = _serialize(root)
    return docs, report


def _combine_plan(
    combine: Mapping[str, Sequence[str]], selected: Sequence[Profile]
) -> dict[Profile, list[Profile]]:
    """``{host: [guests]}`` as Profile objects: the guests are written into the host's file."""
    by_kw = {p.keyword: p for p in selected}
    out: dict[Profile, list[Profile]] = {}
    used: set[str] = set()
    for host_kw, guest_kws in combine.items():
        if isinstance(guest_kws, str):
            guest_kws = (guest_kws,)
        host = by_kw.get(host_kw)
        guests = [by_kw[k] for k in dict.fromkeys(guest_kws) if k in by_kw and k != host_kw]
        if host is None:
            if guests:
                raise ValueError(f"combine: {host_kw!r} is not among the selected profiles")
            continue
        for g in guests:
            if g.keyword in combine or g.keyword in used:
                raise ValueError(
                    f"combine: {g.keyword!r} is both a host and a guest, or twice a guest"
                )
            used.add(g.keyword)
        if guests:
            out[host] = guests
    return out


def _ref_key(el: ET.Element) -> str:
    return (el.get("rdf:ID") or el.get("rdf:about") or "").lstrip("#")


def _merge_bodies(host: list[ET.Element], guest: list[ET.Element]) -> list[ET.Element]:
    """`guest` elements joined to the `host` element of the same object (and element class);
    elements without a counterpart are appended."""
    index = {(el.tag, _ref_key(el)): el for el in host}
    out = list(host)
    for g in guest:
        h = index.get((g.tag, _ref_key(g)))
        if h is not None:
            h.extend(list(g))
        else:
            out.append(g)
            index[(g.tag, _ref_key(g))] = g
    return out


def _dropped(
    objs: list[CimObject],
    placed: set[int],
    written_attrs: set[tuple[int, str]],
    written_links: set[tuple[int, str, int]],
    ids: dict[CimObject, str],
) -> list[ProfileIssue]:
    out: list[ProfileIssue] = []
    for obj in objs:
        plan = class_plan(type(obj))
        if id(obj) not in placed:
            out.append(
                ProfileIssue("warning", obj, None, None,
                             f"{plan.cim_name} {ids[obj]!r} is in none of the written files")
            )  # fmt: skip
            continue
        for a in plan.attrs:
            if a.is_id:
                continue
            v = getattr(obj, a.name, None)
            if v is None or (a.meta.default is not None and v == a.meta.default):
                continue
            if (id(obj), a.name) not in written_attrs:
                out.append(ProfileIssue("warning", obj, None, a.prop, f"{a.prop} is not written"))
        for e in plan.ends:
            v = e.desc.__get__(obj)  # type: ignore[attr-defined]
            targets = v if e.many else (() if v is None else (v,))
            inv = e.desc.inverse.name  # type: ignore[attr-defined]
            missing = [
                t
                for t in targets
                if (id(obj), e.name, id(t)) not in written_links
                and (id(t), inv, id(obj)) not in written_links
            ]
            if missing:
                out.append(
                    ProfileIssue("warning", obj, None, e.prop,
                                 f"{e.prop} is not written ({len(missing)} link(s))")
                )  # fmt: skip
    return out


# --------------------------------------------------------------------------------------
# public API
# --------------------------------------------------------------------------------------


def to_cgmes_strings(
    objects: Any,
    *,
    profiles: Iterable[Profile | str] | Profile | str = DEFAULT_PROFILES,
    header: CgmesHeader | None = None,
    include_reachable: bool = True,
    validate: bool = True,
    strict: bool = False,
    profile_set: ProfileSet | None = None,
    boundary: Iterable[CimObject] = (),
    units: str = "si",
) -> dict[str, str]:
    """The CGMES documents as ``{keyword: CIMXML string}`` (same content as `write_cgmes`;
    problems are reported by ``warnings.warn``, or raised with ``strict=True``)."""
    docs, _ = _build(
        objects,
        profiles,
        header,
        include_reachable,
        validate,
        strict,
        profile_set,
        boundary,
        units,
    )
    return {kw: d.decode("utf-8") for kw, d in docs.items()}


def write_cgmes(
    objects: Any,
    out: str | os.PathLike[str],
    *,
    profiles: Iterable[Profile | str] | Profile | str = DEFAULT_PROFILES,
    header: CgmesHeader | None = None,
    name: str = "model",
    file_name: str = "{name}_{keyword}.xml",
    include_reachable: bool = True,
    validate: bool = True,
    strict: bool = False,
    profile_set: ProfileSet | None = None,
    boundary: Iterable[CimObject] = (),
    units: str = "si",
) -> CgmesReport:
    """Write `objects` (and, by default, everything reachable) as a CGMES file set.

    `profiles` are keywords or `Profile` objects of `profile_set` (default: CGMES 3.0 EQ, SSH,
    TP, SV). `out` is a directory (created when missing) or a ``.zip`` file. Each file is named
    by `file_name`, formatted with ``name``, ``keyword``, ``version`` and ``scenario``
    (``YYYYMMDDTHHMMZ``). Returns a `CgmesReport` (file names, model ids, headers, validation
    issues, dropped values). `boundary` lists the objects that belong to the equipment boundary
    set (``CgmesDocument.boundary_objects`` of a read): with EQBD selected they are defined there
    instead of in EQ. Values are SI in the objects and scaled to the CGMES multipliers (kV, MW,
    km, ...) in the files; ``units="cgmes"`` writes them unscaled. See the module docstring for
    the conventions.
    """
    docs, report = _build(
        objects,
        profiles,
        header,
        include_reachable,
        validate,
        strict,
        profile_set,
        boundary,
        units,
    )
    for kw, items in report.headers.items():
        scen = items["scenarioTime"].replace("-", "").replace(":", "")[:13] + "Z"
        report.files[kw] = file_name.format(
            name=name, keyword=kw, version=items["version"], scenario=scen
        )
    if len(set(report.files.values())) != len(report.files):
        raise ValueError(f"file_name {file_name!r} gives the same name to several profiles")
    target = Path(out)
    if target.suffix.lower() == ".zip":
        target.parent.mkdir(parents=True, exist_ok=True)
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            for kw, data in docs.items():
                info = zipfile.ZipInfo(report.files[kw], date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                zf.writestr(info, data)
        target.write_bytes(buf.getvalue())
    else:
        target.mkdir(parents=True, exist_ok=True)
        for kw, data in docs.items():
            (target / report.files[kw]).write_bytes(data)
    return report


# --------------------------------------------------------------------------------------
# reader
# --------------------------------------------------------------------------------------


class CgmesReadError(CimXmlError):
    """Raised for unreadable sources and malformed files, and for any problem when
    ``strict=True``."""


def _parse_time(text: str | None) -> _dt.datetime | None:
    if not text:
        return None
    try:
        return _dt.datetime.fromisoformat(text.strip())
    except ValueError:
        return None


@dataclass
class CgmesFileHeader:
    """The ``md:FullModel`` header of one file of a CGMES set (strings as written)."""

    file: str
    about: str | None = None  # model id, ``urn:uuid:...``
    created: _dt.datetime | None = None
    scenario_time: _dt.datetime | None = None
    description: str | None = None
    modeling_authority_set: str | None = None
    version: str | None = None
    profile_uris: tuple[str, ...] = ()  # every ``md:Model.profile``
    profiles: tuple[str, ...] = ()  # keywords of the known URIs, in set order
    dependent_on: tuple[str, ...] = ()
    supersedes: tuple[str, ...] = ()
    raw: dict[str, Any] = field(default_factory=dict)  # header as `read_cimxml` returns it

    @property
    def model_id(self) -> str | None:
        return self.about


@dataclass
class CgmesDocument(CimDocument):
    """Result of `read_cgmes`: one merged graph (`objects`, `by_id`, `warnings`, `dangling` as in
    `CimDocument`) plus the header of every file."""

    headers: dict[str, CgmesFileHeader] = field(default_factory=dict)  # file name -> header
    profile_set: ProfileSet | None = None
    boundary_objects: list[CimObject] = field(default_factory=list)  # defined in an EQBD file

    @property
    def profiles(self) -> tuple[str, ...]:
        """Keywords of the profiles present in the set (known ``md:Model.profile`` URIs)."""
        present = {kw for h in self.headers.values() for kw in h.profiles}
        order = self.profile_set.keywords if self.profile_set is not None else ()
        return tuple(sorted(present, key=lambda k: (order.index(k) if k in order else 99, k)))

    @property
    def headers_by_profile(self) -> dict[str, list[CgmesFileHeader]]:
        """Keyword -> headers of the files carrying that profile (several when e.g. two TSOs'
        EQ files were read together; a file with two profiles appears under both)."""
        out: dict[str, list[CgmesFileHeader]] = {}
        for kw in self.profiles:
            out[kw] = [h for h in self.headers.values() if kw in h.profiles]
        return out

    def header_for_rewrite(self) -> CgmesHeader:
        """A `CgmesHeader` that makes `write_cgmes` reproduce this set's headers: model ids,
        DependentOn / Supersedes, times, description, version and the profile URIs. Uses the
        first file of each profile, and the file's first profile as its keyword (a file with EQ
        and SC URIs gives ``combine["EQ"]=["SC"]``, so selecting EQ and SC writes both into one
        file again). Pass ``profiles=`` explicitly when writing; automatic dependencies are
        switched off."""
        by_kw: dict[str, CgmesFileHeader] = {}
        for h in self.headers.values():
            if h.profiles and h.profiles[0] not in by_kw:
                by_kw[h.profiles[0]] = h
        pset = self.profile_set
        base = next(iter(by_kw.values()), None)
        scalars = {
            "created": base.created if base else None,
            "scenario_time": base.scenario_time if base else None,
            "description": base.description if base else None,
            "modeling_authority_set": (base.modeling_authority_set if base else None)
            or DEFAULT_MAS,
            "version": (base.version if base else None) or "1",
        }
        model_ids: dict[str, str] = {}
        combine: dict[str, list[str]] = {}
        dep: dict[str, list[str]] = {}
        sup: dict[str, list[str]] = {}
        uris: dict[str, list[str]] = {}
        overrides: dict[str, dict[str, Any]] = {}
        for kw, h in by_kw.items():
            if h.about:
                model_ids[kw] = h.about
            dep[kw] = list(h.dependent_on)
            sup[kw] = list(h.supersedes)
            own = pset.by_keyword(kw).uri if pset is not None else None
            if len(h.profiles) > 1:
                combine[kw] = list(h.profiles[1:])
            known = {pset.by_keyword(k).uri for k in h.profiles} if pset is not None else {own}
            uris[kw] = [u for u in h.profile_uris if u not in known]
            diff = {
                k: v
                for k, v in {
                    "created": h.created,
                    "scenario_time": h.scenario_time,
                    "description": h.description,
                    "modeling_authority_set": h.modeling_authority_set,
                    "version": h.version,
                }.items()
                if v is not None and v != scalars[k]
            }
            if diff:
                overrides[kw] = diff
        return CgmesHeader(
            scenario_time=scalars["scenario_time"],
            created=scalars["created"],
            modeling_authority_set=scalars["modeling_authority_set"],
            description=scalars["description"],
            version=scalars["version"],
            model_ids=model_ids,
            dependent_on=dep,
            supersedes=sup,
            profile_uris=uris,
            overrides=overrides,
            auto_dependencies=False,
            combine=combine,
        )


# -- sources ------------------------------------------------------------------------


_MAX_ZIP_DEPTH = 3


def _is_xml_name(name: str) -> bool:
    base = name.rpartition("/")[2]
    return name.lower().endswith(".xml") and not base.startswith(".")


def _zip_members(data: Any, label: str, depth: int) -> Iterator[tuple[str, bytes | str]]:
    try:
        zf = zipfile.ZipFile(data)
    except zipfile.BadZipFile as e:
        raise CgmesReadError(f"{label}: not a zip file: {e}") from e
    with zf:
        for info in zf.infolist():
            name = info.filename
            if info.is_dir() or name.startswith("__MACOSX/"):
                continue
            if _is_xml_name(name):
                yield name, zf.read(info)
            elif name.lower().endswith(".zip") and depth < _MAX_ZIP_DEPTH:
                yield from _zip_members(io.BytesIO(zf.read(info)), f"{label}/{name}", depth + 1)


def _from_path(path: Path) -> Iterator[tuple[str, bytes | str]]:
    if path.is_dir():
        for child in sorted(path.iterdir()):
            low = child.name.lower()
            if child.is_file() and not child.name.startswith("."):
                if low.endswith(".xml"):
                    yield child.name, child.read_bytes()
                elif low.endswith(".zip"):
                    yield from _zip_members(child, str(child), 1)
    elif path.suffix.lower() == ".zip":
        yield from _zip_members(path, str(path), 1)
    else:
        yield path.name, path.read_bytes()


def _from_item(name: Any, data: Any) -> tuple[str, bytes | str]:
    if hasattr(data, "read"):
        data = data.read()
    if not isinstance(data, bytes | str):
        raise TypeError(f"CGMES source {name!r}: expected bytes or str, got {type(data).__name__}")
    return str(name), data


def _gather(sources: Any) -> list[tuple[str, bytes | str]]:
    if isinstance(sources, str | os.PathLike):
        items = list(_from_path(Path(sources)))
    elif isinstance(sources, Mapping):
        items = [_from_item(k, v) for k, v in sources.items()]
    else:
        items = []
        for it in sources:
            if isinstance(it, str | os.PathLike):
                items.extend(_from_path(Path(it)))
            else:
                try:
                    name, data = it
                except (TypeError, ValueError):
                    raise TypeError(f"not a path or a (name, data) pair: {it!r}") from None
                items.append(_from_item(name, data))
    out: list[tuple[str, bytes | str]] = []
    seen: dict[str, int] = {}
    for name, data in items:  # file names key the headers: make them unique
        n = seen.get(name, 0)
        seen[name] = n + 1
        out.append((name if n == 0 else f"{name} ({n + 1})", data))
    return out


# -- the reader ---------------------------------------------------------------------


@dataclass
class _Entry:
    file: str
    el: ET.Element
    cls: type
    defines: bool
    profiles: tuple[Profile, ...]


def _kws(profiles: Sequence[Profile]) -> str:
    return "+".join(p.keyword for p in profiles)


class _CgmesReader(_Reader):
    def __init__(self, strict: bool, pset: ProfileSet, scale: bool = True) -> None:
        super().__init__(strict)
        self.error_cls = CgmesReadError
        self.pset = pset
        self._scale = scale
        self.cdoc = CgmesDocument(profile_set=pset)
        self.doc = self.cdoc
        self._gaps: set[str] = set()
        self._profiles: tuple[Profile, ...] = ()
        self._el_cls: type | None = None
        self._file = ""

    # -- headers --------------------------------------------------------------------

    def _file_header(
        self, name: str, el: ET.Element | None
    ) -> tuple[CgmesFileHeader, tuple[Profile, ...]]:
        if el is None:
            self.warn(
                f"{name}: no md:FullModel header, properties are not checked against a profile"
            )
            return CgmesFileHeader(name), ()
        raw = self._read_header(el)

        def many(key: str) -> tuple[str, ...]:
            v = raw.get(key)
            vals = [] if v is None else (v if isinstance(v, list) else [v])
            return tuple(str(x).strip() for x in vals)

        uris = many("profile")
        profiles: list[Profile] = []
        for uri in uris:
            try:
                p = self.pset.by_uri(uri)
            except KeyError:
                self.warn(f"{name}: unknown profile URI {uri!r}")
                continue
            if p not in profiles:
                profiles.append(p)
        profiles.sort(key=lambda p: self.pset.profiles.index(p))
        empty = [p for p in profiles if not p.class_names]
        if empty:
            self.warn(
                f"{name}: profile(s) {_kws(empty)} have no classes in the profile set, "
                f"so the file is not checked against them"
            )

        def one(key: str) -> str | None:
            v = raw.get(key)
            return str(v[0] if isinstance(v, list) else v) if v is not None else None

        header = CgmesFileHeader(
            file=name,
            about=raw.get("about"),
            created=_parse_time(one("created")),
            scenario_time=_parse_time(one("scenarioTime")),
            description=one("description"),
            modeling_authority_set=one("modelingAuthoritySet"),
            version=one("version"),
            profile_uris=uris,
            profiles=tuple(p.keyword for p in profiles),
            dependent_on=many("DependentOn"),
            supersedes=many("Supersedes"),
            raw=raw,
        )
        return header, tuple(p for p in profiles if p.class_names)

    # -- read -----------------------------------------------------------------------

    def read_files(self, files: list[tuple[str, ET.Element]]) -> CgmesDocument:
        doc = self.cdoc
        if not files:
            self.warn("no XML files found in the source")
        by_key: dict[str, list[_Entry]] = {}
        for name, root in files:
            if root.tag != _RDF_ROOT:
                raise CgmesReadError(f"{name}: root element is {root.tag!r}, expected rdf:RDF")
            header, profiles = self._file_header(name, root.find(f"{{{MD_NS}}}FullModel"))
            doc.headers[name] = header
            for el in root:
                ns, local = _split(el.tag)
                if ns == MD_NS and local == "FullModel":
                    continue
                cls = resolve_class(local)
                if cls is None:
                    self.warn(f"unknown class {local!r}: elements skipped")
                    continue
                ref = el.get(_RDF_ID) or el.get(_RDF_ABOUT) or el.get(_RDF_NODE_ID)
                if not ref:
                    self.warn(f"{local} element without rdf:ID/rdf:about skipped")
                    continue
                if profiles and not any(p.has_class(cls) for p in profiles):
                    self.warn(f"class {local!r} is not in profile(s) {_kws(profiles)}")
                defines = bool(el.get(_RDF_ID)) or not profiles
                if not defines:  # rdf:about of a class the file's profile defines (non-NCName ids)
                    defines = any(
                        p.is_concrete(cls) and not p.is_description(cls) for p in profiles
                    )
                by_key.setdefault(normalize_id(ref), []).append(
                    _Entry(name, el, cls, defines, profiles)
                )
        # -- objects: one per id, class from the defining element -------------------
        for key, entries in by_key.items():
            cls = self._object_class(key, entries)
            plan = class_plan(cls)
            obj = cls(mrid=key) if plan.mrid_name else cls()  # type: ignore[operator]
            for attr in plan.defaulted:  # absent means unset, not "constructor default"
                setattr(obj, attr, None)
            doc.by_id[key] = obj
            doc.objects.append(obj)
            if any(e.defines and any(p.keyword == _BOUNDARY for p in e.profiles) for e in entries):
                doc.boundary_objects.append(obj)
        # -- properties --------------------------------------------------------------
        for key, entries in by_key.items():
            obj = doc.by_id[key]
            for e in entries:
                self._profiles = e.profiles
                self._el_cls = e.cls
                self._file = e.file
                self._apply(obj, e.el, reset=False)
        self._check_mrids()
        self.finish()
        return doc

    def _check_mrids(self) -> None:
        """An ``IdentifiedObject.mRID`` element wins over the id; one that differs from the id
        is reported, and one that another object already has is dropped (the id stays)."""
        by_id = self.cdoc.by_id
        used: dict[str, str] = {}
        odd: list[tuple[str, CimObject]] = []
        for key, obj in by_id.items():
            mrid = getattr(obj, "mrid", None)
            if mrid == key:
                used[key] = key
            elif isinstance(mrid, str):
                odd.append((key, obj))
        for key, obj in odd:
            mrid = obj.mrid  # type: ignore[attr-defined]
            name = type(obj).__name__
            if mrid in used:
                self.warn(
                    f"{name} {key!r}: mRID {mrid!r} is also the mRID of {used[mrid]!r}; "
                    f"kept the id as mRID"
                )
                obj.mrid = key  # type: ignore[attr-defined]
                used.setdefault(key, key)
            else:
                self.warn(f"{name} {key!r}: mRID element {mrid!r} differs from the id")
                used[mrid] = key

    def _object_class(self, key: str, entries: list[_Entry]) -> type:
        defs = [e for e in entries if e.defines]
        if defs:
            cls = defs[0].cls
            for d in defs[1:]:
                if d.cls is not cls:
                    self.warn(
                        f"id {key!r} defined as {cls.__name__} and {d.cls.__name__}; "
                        f"merged into the first"
                    )
                else:
                    self.warn(f"{cls.__name__} defined more than once; merged")
        else:
            cls = max(
                (e.cls for e in entries), key=lambda c: len(c.__mro__)
            )  # the most specific class described
            self.warn(f"object only described (no definition): created as {cls.__name__}")
        for e in entries:
            if not issubclass(cls, e.cls):
                self.warn(
                    f"id {key!r} is a {cls.__name__} but {e.file} describes it as {e.cls.__name__}"
                )
        return cls

    # -- conflicting values ------------------------------------------------------------

    def _value(self, el: ET.Element, spec: AttrSpec, where: str) -> Any:
        value = super()._value(el, spec, where)
        exp = _exponent(spec, self.pset) if self._scale else 0
        if exp == 0 or isinstance(value, bool) or not isinstance(value, int | float | Decimal):
            return value
        d = Decimal((el.text or "").strip()).scaleb(exp)  # from the text: exact
        if not d.is_finite():
            return value
        return d if isinstance(value, Decimal) else float(d)

    def _set_attr(self, obj: CimObject, spec: AttrSpec, value: Any) -> None:
        old = None if spec.is_id else getattr(obj, spec.name, None)  # mRID: see _check_mrids
        if old is not None and _encoded(old) != _encoded(value):
            self.warn(
                f"{self._file}: {type(obj).__name__} {_ident(obj)!r}: {spec.prop} is {value!r} "
                f"here, {old!r} in an earlier element; the later one is kept"
            )
        super()._set_attr(obj, spec, value)

    def _set_link(self, obj: CimObject, spec: EndSpec, target: CimObject) -> None:
        if spec.many:
            inv = spec.desc.inverse  # type: ignore[attr-defined]
            old = None if inv.meta.many else inv.__get__(target)
            if old is not None and old is not obj:
                self.warn(
                    f"{self._file}: {type(target).__name__} {_ident(target)!r}: {inv.meta.name} "
                    f"is {_ident(obj)!r} here, {_ident(old)!r} in an earlier element; "
                    f"the later one is kept"
                )
        else:
            old = getattr(obj, spec.name, None)
            if old is not None and old is not target:
                self.warn(
                    f"{self._file}: {type(obj).__name__} {_ident(obj)!r}: {spec.prop} is "
                    f"{_ident(target)!r} here, {_ident(old)!r} in an earlier element; "
                    f"the later one is kept"
                )
        super()._set_link(obj, spec, target)

    # -- property classification ------------------------------------------------------

    def _spec_for(self, plan: ClassPlan, prop: str) -> AttrSpec | EndSpec | None:
        spec = plan.by_prop.get(prop)
        if spec is None and prop in plan.static_props:
            return None
        profiles = self._profiles
        if profiles and self._el_cls is not None:
            info = next(
                (i for i in (p.property(self._el_cls, prop) for p in profiles) if i is not None),
                None,
            )
            if info is not None and info.python_name is None:
                key = f"known SDK gap: {info.qname} has no SDK member"
                if key not in self._gaps:
                    self._gaps.add(key)
                    self.warn(key)
                return None
            if (
                info is None
                and spec is not None
                and any(p.has_class(self._el_cls) for p in profiles)
            ):
                self.warn(
                    f"property {prop!r} of {self._el_cls.__name__} is not in profile(s) "
                    f"{_kws(profiles)}"
                )
        if spec is None:
            self.warn(f"unknown property {prop!r} on {plan.cim_name}")
        return spec


def _encoded(value: Any) -> Any:
    return encode_value(value) if isinstance(value, CimCompound) else value


def _ident(obj: CimObject) -> str:
    return str(getattr(obj, "mrid", None) or type(obj).__name__)


def _profile_set(profile_set: Any) -> ProfileSet:
    if profile_set is None:
        return _default_set()
    inner = getattr(profile_set, "profile_set", None)  # the ``cgmes3`` facade module
    return inner if isinstance(inner, ProfileSet) else profile_set  # type: ignore[no-any-return]


def read_cgmes(
    sources: Any,
    *,
    strict: bool = False,
    profile_set: ProfileSet | Any | None = None,
    units: str = "si",
) -> CgmesDocument:
    """Read a CGMES file set into one merged object graph.

    `sources` is a directory (its ``.xml`` and ``.zip`` files), a ``.zip`` file, an ``.xml``
    path, an iterable of paths, a mapping ``{name: bytes | str}`` or an iterable of
    ``(name, bytes | str)`` pairs. All files are merged by id (see the module docstring), so the
    order of the files does not matter. `profile_set` defaults to CGMES 3.0 (`cgmes3`). Problems
    (unknown classes, properties outside the file's profiles, SDK gaps, unknown profile URIs, bad
    literals, dangling references) are collected in ``warnings``; ``strict=True`` raises
    `CgmesReadError` at the first. Malformed XML always raises. Values are scaled from the CGMES
    multipliers (kV, MW, km, ...) to SI; ``units="cgmes"`` keeps them as written.
    """
    scale = _check_units(units)
    pset = _profile_set(profile_set)
    files: list[tuple[str, ET.Element]] = []
    for name, data in _gather(sources):
        try:
            files.append((name, ET.XML(data)))
        except ET.ParseError as e:
            raise CgmesReadError(f"{name}: not well-formed XML: {e}") from e
    return _CgmesReader(strict, pset, scale).read_files(files)
