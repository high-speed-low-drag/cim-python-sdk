"""Generic CIMXML (IEC 61970-552 RDF/XML) writer and reader, driven by ``_cim_meta``.

The naming, id, value and association rules are in `cim_python_sdk.serialization._common`.
Stdlib only (``xml.etree.ElementTree``).

Output shape::

    <rdf:RDF xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:rdf="...">
      <cim:ACLineSegment rdf:ID="_<mrid>">
        <cim:IdentifiedObject.name>L1</cim:IdentifiedObject.name>
        <cim:Equipment.EquipmentContainer rdf:resource="#_<mrid>"/>
      </cim:ACLineSegment>
    </rdf:RDF>

Objects without an mrid get ``rdf:ID="_gen<N>"``. An mrid for which ``_<mrid>`` is not a valid
XML NCName (e.g. ``a#b``) is written ``rdf:about="#_<percent-encoded mrid>"`` and referenced the
same way; the reader decodes it. Strings with XML-invalid control characters raise ``ValueError``
at write time (``\\r`` is preserved as ``&#13;``). A compound attribute is written with
``rdf:parseType="Resource"``; an enum value as ``rdf:resource="<ns>Enum.literal"``.

CGMES European extensions use the ``eu`` prefix (``http://iec.ch/TC57/CIM100-European#``) for
their classes, members and enum values, e.g. ``<eu:BoundaryPoint>``,
``<eu:IdentifiedObject.shortName>`` inside a ``<cim:ACLineSegment>``, and
``rdf:resource="http://iec.ch/TC57/CIM100-European#LimitKind.patl"``. ``xmlns:eu`` is declared
only when the document has such an element. The reader matches local names and ignores the
namespace of class and property elements.
"""

from __future__ import annotations

import io
import os
import re
import xml.etree.ElementTree as ET

from cim_python_sdk._runtime import CimCompound, CimEnum, CimObject
from cim_python_sdk.serialization._common import (
    CIM_NS,
    NAMESPACES,
    AttrSpec,
    CimDocument,
    ClassPlan,
    EndSpec,
    ReaderBase,
    assign_ids,
    class_plan,
    collect,
    decode_enum,
    default_header_about,
    enum_resource,
    literal_text,
    normalize_id,
    resolve_class,
    warn_roleless,
    wire_fragment,
    xml_name_ok,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any, BinaryIO, TextIO

    PathOrFile = str | os.PathLike[str] | BinaryIO | TextIO

__all__ = ["CimDocument", "CimXmlError", "read_cimxml", "to_cimxml_string", "write_cimxml"]

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
MD_NS = "http://iec.ch/TC57/61970-552/ModelDescription/1#"

_RDF_ID = f"{{{RDF_NS}}}ID"
_RDF_ABOUT = f"{{{RDF_NS}}}about"
_RDF_NODE_ID = f"{{{RDF_NS}}}nodeID"
_RDF_RESOURCE = f"{{{RDF_NS}}}resource"
_RDF_ROOT = f"{{{RDF_NS}}}RDF"

# header properties that are resources (urn:uuid references) rather than literals
_HEADER_RESOURCES = frozenset({"DependentOn", "Supersedes"})


class CimXmlError(ValueError):
    """Raised for malformed documents, and for any problem when ``strict=True``."""


# --------------------------------------------------------------------------------------
# writer
# --------------------------------------------------------------------------------------


# characters XML 1.0 cannot carry: controls other than \t \n \r, surrogates, U+FFFE, U+FFFF
_XML_BAD = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f\ud800-\udfff\ufffe\uffff]")
_CR = "\x00"  # stands in for \r while building (U+0000 can never occur in valid text)


def _xml_text(value: Any, where: str, prop: str) -> str:
    text = literal_text(value)
    m = _XML_BAD.search(text)
    if m is not None:
        raise ValueError(
            f"{where}: {prop} contains the character U+{ord(m.group()):04X}, "
            f"which is not valid in XML (use the JSON-LD format or remove it)"
        )
    return text.replace("\r", _CR) if "\r" in text else text


def _write_value(el: ET.Element, value: Any, namespace: str, where: str, prop: str) -> None:
    if isinstance(value, CimEnum):
        el.set("rdf:resource", enum_resource(value, namespace))
    elif isinstance(value, CimCompound):
        el.set("rdf:parseType", "Resource")
        plan = class_plan(type(value))
        for s in plan.attrs:
            v = getattr(value, s.name, None)
            if v is not None:
                _write_value(ET.SubElement(el, s.qname), v, namespace, where, f"{prop}/{s.prop}")
    else:
        el.text = _xml_text(value, where, prop)


def _header_element(header: dict[str, Any]) -> ET.Element:
    items = dict(header)
    about = items.pop("about", None)
    if about is None:
        about = default_header_about(items)
    el = ET.Element("md:FullModel", {"rdf:about": str(about)})
    for key, val in items.items():
        name = key if key.startswith("Model.") else f"Model.{key}"
        short = name[len("Model.") :]
        for v in val if isinstance(val, list | tuple) else (val,):
            sub = ET.SubElement(el, "md:" + name)
            if short in _HEADER_RESOURCES:
                sub.set("rdf:resource", str(v))
            else:
                sub.text = _xml_text(v, "header", name)
    return el


def _build(
    objects: Any,
    namespace: str,
    include_reachable: bool,
    write_both_ends: bool,
    header: dict[str, Any] | None,
) -> ET.Element:
    objs = collect(objects, include_reachable)
    ids = assign_ids(objs)
    order = {o: i for i, o in enumerate(objs)}
    attrib = {"xmlns:cim": namespace, "xmlns:rdf": RDF_NS}
    if header is not None:
        attrib["xmlns:md"] = MD_NS
    root = ET.Element("rdf:RDF", attrib)
    if header is not None:
        root.append(_header_element(header))
    refs = {o: _wire_ids(i) for o, i in ids.items()}
    warned: set[str] = set()
    for obj in objs:
        plan = class_plan(type(obj))
        el = ET.SubElement(root, plan.qname, dict([refs[obj][0]]))
        where = f"{plan.cim_name} {ids[obj]!r}"
        for a in plan.attrs:
            if a.is_id:
                continue
            v = getattr(obj, a.name, None)
            if v is not None:
                _write_value(ET.SubElement(el, a.qname), v, namespace, where, a.prop)
        for e in plan.ends:
            if not (e.writes or write_both_ends):
                continue
            v = e.desc.__get__(obj)  # type: ignore[attr-defined]
            if e.many:
                targets = sorted((t for t in v if t in order), key=order.__getitem__)
            else:
                targets = [v] if v is not None and v in order else []
            tag = e.qname
            if targets:
                warn_roleless(e, warned)
            for t in targets:
                ET.SubElement(el, tag, {"rdf:resource": refs[t][1]})
    _declare_extra_namespaces(root)
    ET.indent(root, space="  ")
    return root


def _declare_extra_namespaces(root: ET.Element) -> None:
    """Add ``xmlns:<prefix>`` (after ``xmlns:cim``) for every other model prefix in use."""
    used = {el.tag.partition(":")[0] for el in root.iter() if ":" in el.tag}
    extra = sorted(p for p in used if p != "cim" and p in NAMESPACES)
    if extra:
        attrib = {"xmlns:cim": root.attrib.pop("xmlns:cim")}
        attrib.update({f"xmlns:{p}": NAMESPACES[p] for p in extra})
        attrib.update(root.attrib)
        root.attrib = attrib


def _wire_ids(ident: str) -> tuple[tuple[str, str], str]:
    """``((attribute, value), reference)`` of an id: ``rdf:ID="_x"`` / ``#_x`` when ``_x`` is an
    XML NCName, else ``rdf:about="#_<percent-encoded>"`` for both."""
    if xml_name_ok(ident):
        return ("rdf:ID", "_" + ident), "#_" + ident
    ref = "#" + wire_fragment(ident)
    return ("rdf:about", ref), ref


def _serialize(root: ET.Element) -> bytes:
    data = ET.tostring(root, encoding="utf-8", xml_declaration=True) + b"\n"
    return data.replace(b"\x00", b"&#13;") if b"\x00" in data else data


def to_cimxml_string(
    objects: Any,
    *,
    namespace: str = CIM_NS,
    include_reachable: bool = True,
    write_both_ends: bool = False,
    header: dict[str, Any] | None = None,
) -> str:
    """The CIMXML document as a string (same content as `write_cimxml`)."""
    root = _build(objects, namespace, include_reachable, write_both_ends, header)
    return _serialize(root).decode("utf-8")


def write_cimxml(
    objects: Any,
    path_or_file: PathOrFile,
    *,
    namespace: str = CIM_NS,
    include_reachable: bool = True,
    write_both_ends: bool = False,
    header: dict[str, Any] | None = None,
) -> None:
    """Write `objects` (and, by default, everything reachable from them) as CIMXML, UTF-8.

    `header`, when given, adds an ``md:FullModel`` element. Keys are ``Model.<name>``
    properties without the prefix (``created``, ``description``, ``version``, ``profile`` ...);
    a list value repeats the element; ``DependentOn`` and ``Supersedes`` are written as
    resources; ``about`` sets ``rdf:about`` (default: a deterministic ``urn:uuid:``).
    A file object may be binary or text.
    """
    data = _serialize(_build(objects, namespace, include_reachable, write_both_ends, header))
    if isinstance(path_or_file, str | os.PathLike):
        with open(path_or_file, "wb") as f:
            f.write(data)
    elif isinstance(path_or_file, io.TextIOBase):
        path_or_file.write(data.decode("utf-8"))
    else:
        path_or_file.write(data)  # type: ignore[arg-type]


# --------------------------------------------------------------------------------------
# reader
# --------------------------------------------------------------------------------------


def _split(tag: str) -> tuple[str, str]:
    if tag.startswith("{"):
        ns, _, local = tag[1:].partition("}")
        return ns, local
    return "", tag


class _Reader(ReaderBase):
    def __init__(self, strict: bool) -> None:
        super().__init__(strict, CimXmlError)
        self._class_cache: dict[str, type | None] = {}

    # -- pass 1 ---------------------------------------------------------------------

    def read(self, root: ET.Element) -> CimDocument:
        if root.tag != _RDF_ROOT:
            raise CimXmlError(f"root element is {root.tag!r}, expected rdf:RDF")
        doc = self.doc
        work: list[tuple[CimObject, ET.Element]] = []
        for el in root:
            ns, local = _split(el.tag)
            if ns == MD_NS and local == "FullModel":
                doc.header = self._read_header(el)
                continue
            cls = self._class_cache.get(local, False)  # type: ignore[arg-type]
            if cls is False:
                cls = self._class_cache[local] = resolve_class(local)
            if cls is None:
                self.warn(f"unknown class {local!r}: elements skipped")
                continue
            ref = el.get(_RDF_ID) or el.get(_RDF_ABOUT) or el.get(_RDF_NODE_ID)
            if not ref:
                self.warn(f"{local} element without rdf:ID/rdf:about skipped")
                continue
            key = normalize_id(ref)
            obj = doc.by_id.get(key)
            if obj is None:
                plan = class_plan(cls)  # type: ignore[arg-type]
                obj = cls(mrid=key) if plan.mrid_name else cls()  # type: ignore[operator]
                doc.by_id[key] = obj
                doc.objects.append(obj)
            elif type(obj) is not cls:
                self.warn(
                    f"id {key!r} used by {type(obj).__name__} and {local}; merged into the first"
                )
            work.append((obj, el))
        # -- pass 2 -----------------------------------------------------------------
        for obj, el in work:
            self._apply(obj, el)
        self.finish()
        return doc

    def _read_header(self, el: ET.Element) -> dict[str, Any]:
        header: dict[str, Any] = {}
        about = el.get(_RDF_ABOUT)
        if about is not None:
            header["about"] = about
        for sub in el:
            _, local = _split(sub.tag)
            name = local.removeprefix("Model.")
            value = sub.get(_RDF_RESOURCE)
            if value is None:
                value = sub.text or ""
            if name in header:
                prev = header[name]
                header[name] = [*prev, value] if isinstance(prev, list) else [prev, value]
            else:
                header[name] = value
        return header

    # -- pass 2 ---------------------------------------------------------------------

    def _spec_for(self, plan: ClassPlan, prop: str) -> AttrSpec | EndSpec | None:
        """The attribute or end named by a property tag, or None (after a warning)."""
        spec = plan.by_prop.get(prop)
        if spec is None and prop not in plan.static_props:
            self.warn(f"unknown property {prop!r} on {plan.cim_name}")
        return spec

    def _apply(self, obj: CimObject, el: ET.Element, *, reset: bool = True) -> None:
        plan = class_plan(type(obj))
        if reset:
            for name in plan.defaulted:  # absent means unset, not "constructor default"
                setattr(obj, name, None)
        src = el.get(_RDF_ID) or el.get(_RDF_ABOUT) or el.get(_RDF_NODE_ID) or ""
        for child in el:
            _, prop = _split(child.tag)
            spec = self._spec_for(plan, prop)
            if spec is None:
                continue
            if isinstance(spec, EndSpec):
                self._link(obj, spec, child, normalize_id(src))
                continue
            value = self._value(child, spec, f"{plan.cim_name}: {prop}")
            if value is not None:
                self._set_attr(obj, spec, value)

    def _set_attr(self, obj: CimObject, spec: AttrSpec, value: Any) -> None:
        setattr(obj, spec.name, value)

    def _set_link(self, obj: CimObject, spec: EndSpec, target: CimObject) -> None:
        if spec.many:
            spec.desc.add(obj, target)  # type: ignore[attr-defined]
        else:
            setattr(obj, spec.name, target)

    def _link(self, obj: CimObject, spec: EndSpec, child: ET.Element, src: str) -> None:
        ref = child.get(_RDF_RESOURCE) or child.get(_RDF_NODE_ID)
        if ref is None:
            self.warn(f"{spec.prop} has no rdf:resource (nested objects are not supported)")
            return
        target = self.doc.by_id.get(normalize_id(ref))
        if target is None:
            self.doc.dangling.append((src, spec.prop, ref))
            self.warn(f"dangling reference in {spec.prop}")
            return
        try:
            self._set_link(obj, spec, target)
        except TypeError as e:
            self.warn(f"cannot link {spec.prop}: {e}")

    def _value(self, el: ET.Element, spec: AttrSpec, where: str) -> Any:
        kind = spec.kind
        if kind == "enumeration":
            ref = el.get(_RDF_RESOURCE) or el.text or ""
            member = decode_enum(ref, spec.type_classes())
            if member is None:
                self.warn(f"{where}: unknown enum value {ref!r}")
            return member
        if kind == "compound":
            classes = spec.type_classes()
            if not classes:
                self.warn(f"{where}: unknown compound type {spec.type_name!r}")
                return None
            return self._compound(el, classes[0], where)
        text = el.text or ""
        decode = spec.decode
        if decode is None:
            return text
        try:
            return decode(text)
        except (ValueError, ArithmeticError):
            self.warn(f"{where}: cannot parse {text!r} as {spec.type_name}")
            return None

    def _compound(self, el: ET.Element, cls: type, where: str) -> Any:
        plan = class_plan(cls)
        comp = cls()
        for name in plan.defaulted:
            setattr(comp, name, None)
        subs = list(el)
        if len(subs) == 1 and _split(subs[0].tag)[1] == plan.cim_name:  # wrapper element form
            subs = list(subs[0])
        for sub in subs:
            _, prop = _split(sub.tag)
            spec = plan.by_prop.get(prop)
            if not isinstance(spec, AttrSpec):
                self.warn(f"unknown property {prop!r} on {plan.cim_name}")
                continue
            value = self._value(sub, spec, f"{where}/{prop}")
            if value is not None:
                setattr(comp, spec.name, value)
        return comp


def read_cimxml(path_or_file: PathOrFile, *, strict: bool = False) -> CimDocument:
    """Read a CIMXML document into SDK objects.

    Pass 1 creates every object (ids ``_x``, ``#_x``, ``urn:uuid:x`` give mrid ``x``; classes
    without an mrid get none). Pass 2 sets attributes and links through the public descriptors,
    so inverses are maintained; associations may be written on either end or both. Unknown
    classes/properties, unparsable literals and references to objects not in the document are
    collected in ``warnings`` (references also in ``dangling``); ``strict=True`` raises
    `CimXmlError` instead.
    """
    try:
        tree = ET.parse(path_or_file)  # type: ignore[arg-type]
    except ET.ParseError as e:
        raise CimXmlError(f"not well-formed XML: {e}") from e
    return _Reader(strict).read(tree.getroot())
