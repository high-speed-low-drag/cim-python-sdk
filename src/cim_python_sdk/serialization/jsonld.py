"""CIM JSON-LD writer and reader, driven by ``_cim_meta``.

The naming, id, value and association rules are in `cim_python_sdk.serialization._common`. Stdlib only
(``json``). The format follows the DIGIN10 convention ("CIMJSON-LD",
3lbits/CIM4NoUtility ``Telemark-120/docs/CIMJSON-LD.adoc``; the UCAIug draft
cimug-org/CIM_JSON-LD_Syntax is not final).

Output shape::

    {
      "@context": {"cim": "http://iec.ch/TC57/CIM100#", "rdf": "...", "md": "...", "xsd": "..."},
      "@graph": [
        {
          "@id": "urn:uuid:<mrid>",
          "@type": "cim:ACLineSegment",
          "cim:Conductor.length": 12.5,
          "cim:Equipment.EquipmentContainer": {"@id": "#_sub-1"},
          "cim:Terminal.phases": {"@id": "cim:PhaseCode.ABC"}
        }
      ]
    }

Followed from the DIGIN convention
    * ``@context`` with prefixes, ``@graph`` holding the objects, and, when a header is given,
      the dataset description as extra top-level keys next to ``@graph`` (``@id`` = the
      ``rdf:about`` of the model, ``@type`` ``dcat:Dataset``).
    * ``@id`` is ``urn:uuid:<mrid>``; ``@type`` is ``cim:<ClassName>``; properties are
      ``cim:<DeclaringClass>.<attr>``; ``cim:IdentifiedObject.mRID`` is written as well.
    * References are ``{"@id": ...}``; an enum value is ``{"@id": "cim:<Enum>.<literal>"}`` (the
      compact form of the CIMXML URL, "just the prefix"); primitives are native JSON values
      (numbers, booleans, strings); a CIM ``Decimal`` is a string, since JSON has no decimal.
    * Header mapping CIMXML to JSON-LD: ``rdf:about`` to ``@id``, ``created`` to
      ``prov:generatedAtTime`` (xsd:dateTime) and ``dcterms:issued`` (xsd:date), ``scenarioTime``
      to ``dcterms:temporal`` (``dcterms:PeriodOfTime`` with ``dcat:startDate``), ``description``
      to a ``dcterms:description`` array of ``@language`` ``en`` values, ``modelingAuthoritySet``
      to ``dcat:isVersionOf``, ``profile`` to a ``dcterms:conformsTo`` array, ``version`` to
      ``dcat:version``, ``DependentOn`` to a ``dcterms:references`` array. The reader maps back
      (``prov:generatedAtTime`` wins over ``dcterms:issued``); other top-level terms (title,
      publisher, ...) are kept in the header under their compact name, and header keys that
      contain a ``:`` are written back verbatim.

Inferred (the convention is silent) and mirrored from CIMXML
    * Namespace: ``cim`` maps to ``namespace`` (default ``CIM_NS``, the CIM100 namespace, where
      DIGIN uses its own ``https://cim.ucaiug.io/ns#``); the reader treats any prefix that maps to
      a CIM namespace (or ``cim``/``eu``) as the CIM vocabulary.
    * CGMES European extensions use the prefix ``eu`` (``http://iec.ch/TC57/CIM100-European#``):
      ``"@type": "eu:BoundaryPoint"``, ``"eu:IdentifiedObject.shortName"``,
      ``{"@id": "eu:LimitKind.patl"}``. The context gets ``eu`` only when the document uses it.
    * Association direction, sorting, generated ids and property naming are those of
      `cim_python_sdk.serialization._common`. A single-valued end is one ``{"@id"}`` object; a
      many-valued end is always an array (also with one target).
    * An mrid that is not a UUID is written ``"@id": "#_<percent-encoded mrid>"`` (a relative IRI,
      same fragment form as CIMXML); an object without mrid gets the blank node ``_:gen<N>``.
    * Compounds are nested objects without ``@id`` and with ``@type`` ``cim:<Compound>``.
    * datetime/date/time are typed literals ``{"@value": ..., "@type": "xsd:dateTime"}`` (also
      ``xsd:date``, ``xsd:time``); the reader also takes plain strings. NaN and infinity cannot
      be JSON numbers and are written as ``{"@value": "NaN" | "INF" | "-INF", "@type":
      "xsd:double"}``. Values are decoded by the declared attribute type, so ``5`` is accepted
      for a float and ``"5"`` for an int.
    * Strings may contain any control character (JSON escapes them); output is UTF-8.
    * The reader is two-pass and tolerant like ``read_cimxml``: unknown classes, properties,
      bad literals and dangling references become warnings (``strict=True`` raises
      `CimJsonLdError`). Ids may be ``urn:uuid:x``, ``_x``, ``#_x``, ``_:x``, an IRI ending in
      ``#_x`` or a compact IRI (``ex:x`` with ``ex`` in the context). Properties and types may
      lack the ``cim:`` prefix when the context defines ``@vocab``; context terms that alias a CIM
      property (``"name": "cim:IdentifiedObject.name"``) work too. A top-level array, a single
      node, or an object with ``@graph`` are all accepted. Embedded nodes are read as references
      (their other properties are ignored with a warning).
"""

from __future__ import annotations

import datetime as _dt
import io
import json
import math
import os
from decimal import Decimal

from cim_python_sdk._runtime import CimCompound, CimEnum, CimObject
from cim_python_sdk.serialization._common import (
    CIM_NS,
    NAMESPACES,
    AttrSpec,
    CimDocument,
    EndSpec,
    ReaderBase,
    assign_ids,
    class_plan,
    collect,
    decode_enum,
    default_header_about,
    enum_resource,
    is_uuid,
    literal_text,
    normalize_id,
    resolve_class,
    warn_roleless,
    wire_fragment,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any, BinaryIO, TextIO

    PathOrFile = str | os.PathLike[str] | BinaryIO | TextIO

__all__ = [
    "CimJsonLdError",
    "read_jsonld",
    "to_jsonld_dict",
    "to_jsonld_string",
    "write_jsonld",
]

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
MD_NS = "http://iec.ch/TC57/61970-552/ModelDescription/1#"
XSD_NS = "http://www.w3.org/2001/XMLSchema#"
_HEADER_CONTEXT = {
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
}
_CIM_NAMESPACES = ("http://iec.ch/TC57/CIM", "https://cim.ucaiug.io/ns#")

# header keys that are resources rather than literals
_HEADER_RESOURCES = frozenset({"DependentOn", "Supersedes"})


class CimJsonLdError(ValueError):
    """Raised for malformed documents, and for any problem when ``strict=True``."""


# --------------------------------------------------------------------------------------
# writer
# --------------------------------------------------------------------------------------


def _typed(text: str, xsd_type: str) -> dict[str, str]:
    return {"@value": text, "@type": xsd_type}


def _jvalue(value: Any, used: set[str]) -> Any:
    """JSON form of an attribute value (see the module docstring); namespace prefixes of the
    written names are added to `used`."""
    if isinstance(value, CimEnum):
        used.add(value._cim_meta.namespace)
        return {"@id": enum_resource(value, compact=True)}
    if isinstance(value, CimCompound):
        out: dict[str, Any] = {}
        plan = class_plan(type(value))
        out["@type"] = plan.qname
        used.add(plan.ns)
        for s in plan.attrs:
            v = getattr(value, s.name, None)
            if v is not None:
                out[s.qname] = _jvalue(v, used)
                used.add(s.ns)
        return out
    if isinstance(value, bool | int | str):
        return value
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return _typed(literal_text(value), "xsd:double")
        return value
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, _dt.datetime):
        return _typed(value.isoformat(), "xsd:dateTime")
    if isinstance(value, _dt.date):
        return _typed(value.isoformat(), "xsd:date")
    if isinstance(value, _dt.time):
        return _typed(value.isoformat(), "xsd:time")
    return literal_text(value)


def _wire_id(ident: str, has_mrid: bool) -> str:
    if not has_mrid:
        return "_:" + ident
    if is_uuid(ident):
        return "urn:uuid:" + ident
    return "#" + wire_fragment(ident)


def _dateish(text: str) -> str:
    return text[:10] if len(text) >= 10 and text[4] == "-" and text[7] == "-" else text


def _header_dict(header: dict[str, Any]) -> dict[str, Any]:
    """The dataset description (extra top-level JSON-LD keys) for a CIMXML-style header."""
    items = dict(header)
    about = items.pop("about", None)
    if about is None:
        about = default_header_about(items)
    out: dict[str, Any] = {"@id": str(about), "@type": "dcat:Dataset"}

    def values(val: Any) -> list[Any]:
        return list(val) if isinstance(val, list | tuple) else [val]

    for key, val in items.items():
        name = key.removeprefix("Model.")
        if ":" in key:  # a JSON-LD term kept from a read header: verbatim
            out[key] = val
        elif name == "created":
            text = literal_text(val)
            out["prov:generatedAtTime"] = _typed(text, "xsd:dateTime")
            out["dcterms:issued"] = _typed(_dateish(text), "xsd:date")
        elif name == "scenarioTime":
            out["dcterms:temporal"] = {
                "@type": "dcterms:PeriodOfTime",
                "dcat:startDate": _typed(literal_text(val), "xsd:dateTime"),
            }
        elif name == "description":
            out["dcterms:description"] = [
                {"@value": literal_text(v), "@language": "en"} for v in values(val)
            ]
        elif name == "modelingAuthoritySet":
            out["dcat:isVersionOf"] = {"@id": str(val)}
        elif name == "profile":
            out["dcterms:conformsTo"] = [{"@id": str(v)} for v in values(val)]
        elif name == "version":
            out["dcat:version"] = literal_text(val)
        elif name == "DependentOn":
            out["dcterms:references"] = [{"@id": str(v)} for v in values(val)]
        elif name in _HEADER_RESOURCES:
            out["md:Model." + name] = [{"@id": str(v)} for v in values(val)]
        else:
            vs = [literal_text(v) for v in values(val)]
            out["md:Model." + name] = vs[0] if len(vs) == 1 else vs
    return out


def to_jsonld_dict(
    objects: Any,
    *,
    namespace: str = CIM_NS,
    include_reachable: bool = True,
    write_both_ends: bool = False,
    header: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """The JSON-LD document as a dict (same content as `write_jsonld`, in stable key order)."""
    objs = collect(objects, include_reachable)
    ids = assign_ids(objs)
    order = {o: i for i, o in enumerate(objs)}
    context: dict[str, str] = {"cim": namespace, "rdf": RDF_NS, "md": MD_NS, "xsd": XSD_NS}
    doc: dict[str, Any] = {"@context": context}
    if header is not None:
        context.update(_HEADER_CONTEXT)
        doc.update(_header_dict(header))
    wire = {o: _wire_id(ids[o], isinstance(getattr(o, "mrid", None), str)) for o in objs}
    warned: set[str] = set()
    used: set[str] = set()
    graph: list[dict[str, Any]] = []
    for obj in objs:
        plan = class_plan(type(obj))
        node: dict[str, Any] = {"@id": wire[obj], "@type": plan.qname}
        used.add(plan.ns)
        for a in plan.attrs:
            v = getattr(obj, a.name, None)
            if v is not None:
                node[a.qname] = _jvalue(v, used)
                used.add(a.ns)
        for e in plan.ends:
            if not (e.writes or write_both_ends):
                continue
            v = e.desc.__get__(obj)  # type: ignore[attr-defined]
            if e.many:
                targets = sorted((t for t in v if t in order), key=order.__getitem__)
                if not targets:
                    continue
                warn_roleless(e, warned)
                node[e.qname] = [{"@id": wire[t]} for t in targets]
                used.add(e.ns)
            elif v is not None and v in order:
                warn_roleless(e, warned)
                node[e.qname] = {"@id": wire[v]}
                used.add(e.ns)
        graph.append(node)
    extra = sorted(p for p in used if p != "cim" and p in NAMESPACES)
    if extra:  # declare after "cim"
        rest = {k: v for k, v in context.items() if k != "cim"}
        context.clear()
        context.update({"cim": namespace, **{p: NAMESPACES[p] for p in extra}, **rest})
    doc["@graph"] = graph
    return doc


def _dumps(doc: dict[str, Any], indent: int | None) -> str:
    return json.dumps(doc, indent=indent, ensure_ascii=False, allow_nan=False) + "\n"


def to_jsonld_string(
    objects: Any,
    *,
    namespace: str = CIM_NS,
    include_reachable: bool = True,
    write_both_ends: bool = False,
    header: dict[str, Any] | None = None,
    indent: int | None = 2,
) -> str:
    """The JSON-LD document as a string (same content as `write_jsonld`)."""
    doc = to_jsonld_dict(
        objects,
        namespace=namespace,
        include_reachable=include_reachable,
        write_both_ends=write_both_ends,
        header=header,
    )
    return _dumps(doc, indent)


def write_jsonld(
    objects: Any,
    path_or_file: PathOrFile,
    *,
    namespace: str = CIM_NS,
    include_reachable: bool = True,
    write_both_ends: bool = False,
    header: dict[str, Any] | None = None,
    indent: int | None = 2,
) -> None:
    """Write `objects` (and, by default, everything reachable from them) as CIM JSON-LD, UTF-8.

    `header` has the same keys as for ``write_cimxml`` and becomes the dataset description (see
    the module docstring). ``indent=None`` gives compact output. A file object may be binary
    or text.
    """
    text = to_jsonld_string(
        objects,
        namespace=namespace,
        include_reachable=include_reachable,
        write_both_ends=write_both_ends,
        header=header,
        indent=indent,
    )
    if isinstance(path_or_file, str | os.PathLike):
        with open(path_or_file, "wb") as f:
            f.write(text.encode("utf-8"))
    elif isinstance(path_or_file, io.TextIOBase):
        path_or_file.write(text)
    else:
        path_or_file.write(text.encode("utf-8"))  # type: ignore[arg-type]


# --------------------------------------------------------------------------------------
# reader
# --------------------------------------------------------------------------------------

_SCHEMES = ("urn:", "_:", "http:", "https:", "file:")


def _value_text(raw: Any) -> str:
    return raw if isinstance(raw, str) else literal_text(raw)


class _Reader(ReaderBase):
    def __init__(self, strict: bool) -> None:
        super().__init__(strict, CimJsonLdError)
        self.prefixes: dict[str, str] = {}
        self.aliases: dict[str, str] = {}
        self.vocab: str | None = None
        self._class_cache: dict[str, type | None] = {}
        self._prop_cache: dict[str, str | None] = {}

    # -- context --------------------------------------------------------------------

    def _context(self, ctx: Any) -> None:
        if isinstance(ctx, list):
            for c in ctx:
                self._context(c)
            return
        if not isinstance(ctx, dict):
            return  # a remote context (string) is not fetched
        for term, val in ctx.items():
            if term == "@vocab":
                if isinstance(val, str):
                    self.vocab = val
            elif term.startswith("@"):
                continue
            elif isinstance(val, str):
                if val.endswith(("#", "/")) or val.startswith(("http://", "https://")):
                    self.prefixes[term] = val
                else:
                    self.aliases[term] = val
            elif isinstance(val, dict) and isinstance(val.get("@id"), str):
                self.aliases[term] = val["@id"]
        self._prop_cache.clear()

    def _is_cim_prefix(self, prefix: str) -> bool:
        if prefix in ("cim", "eu"):
            return True
        ns = self.prefixes.get(prefix)
        if ns is None:
            return False
        return ns == self.vocab or ns.startswith(_CIM_NAMESPACES) or ns == self.prefixes.get("cim")

    def local(self, term: str, bare_ok: bool, depth: int = 0) -> str | None:
        """The CIM local name (``Class`` or ``Class.attr``) a term refers to, or None."""
        if term in self.aliases and depth < 4:
            return self.local(self.aliases[term], True, depth + 1)
        if "://" in term:
            if "#" in term:
                return term.rpartition("#")[2]
            return term.rpartition("/")[2]
        if ":" in term:
            prefix, _, rest = term.partition(":")
            return rest if self._is_cim_prefix(prefix) else None
        if bare_ok or self.vocab is not None:
            return term
        return None

    def prop(self, key: str) -> str | None:
        try:
            return self._prop_cache[key]
        except KeyError:
            r = self._prop_cache[key] = self.local(key, False)
            return r

    def ident(self, ref: str) -> str:
        """The mrid an id or reference names (compact IRIs of the context are expanded)."""
        if ":" in ref and not ref.startswith(_SCHEMES) and "#" not in ref and "/" not in ref:
            prefix, _, rest = ref.partition(":")
            if prefix in self.prefixes:
                ref = rest
        return normalize_id(ref)

    def cls(self, type_term: str) -> type | None:
        c = self._class_cache.get(type_term, False)  # type: ignore[arg-type]
        if c is False:
            name = self.local(type_term, True)
            c = self._class_cache[type_term] = resolve_class(name) if name else None
        return c  # type: ignore[return-value]

    # -- pass 1 ---------------------------------------------------------------------

    def read(self, top: Any) -> CimDocument:
        doc = self.doc
        if isinstance(top, dict):
            if "@context" in top:
                self._context(top["@context"])
            if "@graph" in top:
                graph = top["@graph"]
                header = self._header(top)
                if header:
                    doc.header = header
            else:
                graph = [top] if ("@type" in top or "@id" in top) else []
        elif isinstance(top, list):
            graph = top
        else:
            raise CimJsonLdError(f"top level is {type(top).__name__}, expected object or array")
        if isinstance(graph, dict):
            graph = [graph]
        if not isinstance(graph, list):
            raise CimJsonLdError("@graph must be an array")
        work: list[tuple[CimObject, dict[str, Any]]] = []
        for item in graph:
            if not isinstance(item, dict):
                self.warn("graph entry is not an object: skipped")
                continue
            if "@context" in item and len(item) == 1:
                self._context(item["@context"])
                continue
            types = item.get("@type")
            tlist = types if isinstance(types, list) else [types]
            cls = next((c for c in map(self._cls_of, tlist) if c is not None), None)
            if cls is None:
                shown = types if types else "(none)"
                self.warn(f"unknown class {shown!r}: nodes skipped")
                continue
            ref = item.get("@id")
            if not isinstance(ref, str) or not ref:
                ref = self._mrid_property(item)
            if not ref:
                self.warn(f"{cls._cim_meta.cim_name} node without @id skipped")  # type: ignore[attr-defined]
                continue
            key = self.ident(ref)
            obj = doc.by_id.get(key)
            if obj is None:
                plan = class_plan(cls)
                obj = cls(mrid=key) if plan.mrid_name else cls()
                doc.by_id[key] = obj
                doc.objects.append(obj)
            elif type(obj) is not cls:
                self.warn(
                    f"id {key!r} used by {type(obj).__name__} and {cls.__name__}; "
                    f"merged into the first"
                )
            work.append((obj, item))
        for obj, item in work:
            self._apply(obj, item)
        self.finish()
        return doc

    def _cls_of(self, t: Any) -> type | None:
        return self.cls(t) if isinstance(t, str) else None

    def _mrid_property(self, item: dict[str, Any]) -> str | None:
        for k, v in item.items():
            if (
                not k.startswith("@")
                and isinstance(v, str)
                and self.prop(k) == "IdentifiedObject.mRID"
            ):
                return v
        return None

    # -- header ---------------------------------------------------------------------

    def _header(self, top: dict[str, Any]) -> dict[str, Any]:
        h: dict[str, Any] = {}
        generated = issued = None
        for k, v in top.items():
            if k in ("@context", "@graph", "@type"):
                continue
            if k == "@id":
                if isinstance(v, str):
                    h["about"] = v
            elif k == "prov:generatedAtTime":
                generated = _plain(v)
            elif k == "dcterms:issued":
                issued = _plain(v)
            elif k == "dcterms:temporal":
                start = v.get("dcat:startDate") if isinstance(v, dict) else None
                if start is not None:
                    h["scenarioTime"] = _plain(start)
            elif k == "dcterms:description":
                texts = [
                    _plain(e)
                    for e in (v if isinstance(v, list) else [v])
                    if not (isinstance(e, dict) and e.get("@language", "en") != "en")
                ]
                if texts:
                    h["description"] = texts[0] if len(texts) == 1 else texts
            elif k == "dcat:isVersionOf":
                h["modelingAuthoritySet"] = _plain(v)
            elif k == "dcterms:conformsTo":
                vals = [_plain(e) for e in (v if isinstance(v, list) else [v])]
                h["profile"] = vals[0] if len(vals) == 1 else vals
            elif k == "dcat:version":
                h["version"] = _plain(v)
            elif k == "dcterms:references":
                vals = [_plain(e) for e in (v if isinstance(v, list) else [v])]
                h["DependentOn"] = vals[0] if len(vals) == 1 else vals
            elif k.startswith("md:Model."):
                name = k[len("md:Model.") :]
                vals = [_plain(e) for e in (v if isinstance(v, list) else [v])]
                h[name] = vals[0] if len(vals) == 1 else vals
            elif ":" in k:
                h[k] = v
        created = generated if generated is not None else issued
        if created is not None:
            h = {"created": created, **h}
        return h

    # -- pass 2 ---------------------------------------------------------------------

    def _apply(self, obj: CimObject, item: dict[str, Any]) -> None:
        plan = class_plan(type(obj))
        for name in plan.defaulted:  # absent means unset, not "constructor default"
            setattr(obj, name, None)
        src = ""
        for key, val in item.items():
            if key.startswith("@"):
                continue
            prop = self.prop(key)
            spec = plan.by_prop.get(prop) if prop is not None else None
            if spec is None:
                if prop not in plan.static_props:
                    self.warn(f"unknown property {prop or key!r} on {plan.cim_name}")
                continue
            if isinstance(spec, EndSpec):
                if not src:
                    ref = item.get("@id")
                    src = self.ident(ref) if isinstance(ref, str) else ""
                self._link(obj, spec, val, src)
                continue
            if spec.is_id:
                continue
            value = self._value(val, spec, f"{plan.cim_name}: {prop}")
            if value is not None:
                setattr(obj, spec.name, value)

    def _link(self, obj: CimObject, spec: EndSpec, val: Any, src: str) -> None:
        for item in val if isinstance(val, list) else [val]:
            if item is None:
                continue
            if isinstance(item, dict):
                ref = item.get("@id")
                if len(item.keys() - {"@id", "@type"}) > 0:
                    self.warn(f"{spec.prop}: properties of an embedded node are ignored")
            else:
                ref = item
            if not isinstance(ref, str):
                self.warn(f"{spec.prop}: value is not a reference")
                continue
            target = self.doc.by_id.get(self.ident(ref))
            if target is None:
                self.doc.dangling.append((src, spec.prop, ref))
                self.warn(f"dangling reference in {spec.prop}")
                continue
            try:
                if spec.many:
                    spec.desc.add(obj, target)  # type: ignore[attr-defined]
                else:
                    setattr(obj, spec.name, target)
            except TypeError as e:
                self.warn(f"cannot link {spec.prop}: {e}")

    def _value(self, val: Any, spec: AttrSpec, where: str) -> Any:
        if isinstance(val, list):
            if len(val) != 1:
                if val:
                    self.warn(f"{where}: several values for a single-valued property")
                return None
            val = val[0]
        if val is None:
            return None
        kind = spec.kind
        if kind == "enumeration":
            ref = val.get("@id", val.get("@value")) if isinstance(val, dict) else val
            member = None
            if isinstance(ref, str):
                name = self.local(ref.strip(), True) or ref
                member = decode_enum(name, spec.type_classes())
            if member is None:
                self.warn(f"{where}: unknown enum value {ref!r}")
            return member
        if kind == "compound":
            classes = spec.type_classes()
            if not classes:
                self.warn(f"{where}: unknown compound type {spec.type_name!r}")
                return None
            if not isinstance(val, dict):
                self.warn(f"{where}: compound value is not an object")
                return None
            return self._compound(val, classes[0], where)
        raw = val.get("@value") if isinstance(val, dict) else val
        if isinstance(raw, dict | list) or raw is None:
            self.warn(f"{where}: cannot read {val!r} as {spec.type_name}")
            return None
        decode = spec.decode
        text = _value_text(raw)
        if decode is None:
            return text if isinstance(raw, str) else raw
        try:
            return decode(text)
        except (ValueError, ArithmeticError):
            if isinstance(raw, float) and raw.is_integer():  # 5.0 for an int attribute
                try:
                    return decode(str(int(raw)))
                except (ValueError, ArithmeticError):
                    pass
            self.warn(f"{where}: cannot parse {text!r} as {spec.type_name}")
            return None

    def _compound(self, node: dict[str, Any], cls: type, where: str) -> Any:
        plan = class_plan(cls)
        comp = cls()
        for name in plan.defaulted:
            setattr(comp, name, None)
        for key, val in node.items():
            if key.startswith("@"):
                continue
            prop = self.prop(key)
            spec = plan.by_prop.get(prop) if prop is not None else None
            if not isinstance(spec, AttrSpec):
                self.warn(f"unknown property {prop or key!r} on {plan.cim_name}")
                continue
            value = self._value(val, spec, f"{where}/{prop}")
            if value is not None:
                setattr(comp, spec.name, value)
        return comp


def _plain(v: Any) -> Any:
    """The text of a header term value: ``{"@value"}``/``{"@id"}`` objects unwrapped."""
    if isinstance(v, dict):
        for k in ("@value", "@id"):
            if k in v:
                return v[k]
    return v


def read_jsonld(path_or_file: PathOrFile, *, strict: bool = False) -> CimDocument:
    """Read a CIM JSON-LD document into SDK objects.

    Same behaviour as ``read_cimxml``: pass 1 creates every object (the mrid comes from
    ``@id``, falling back to ``cim:IdentifiedObject.mRID``; classes without an mrid get none),
    pass 2 sets attributes and links through the public descriptors, so inverses are maintained
    and associations may be given on either end or both. Unknown classes/properties, unparsable
    literals and references to objects not in the document are collected in ``warnings``
    (references also in ``dangling``); ``strict=True`` raises `CimJsonLdError` instead.
    The dataset description (top-level keys next to ``@graph``) is returned as ``header``.
    """
    try:
        data: bytes | str
        if isinstance(path_or_file, str | os.PathLike):
            with open(path_or_file, "rb") as f:
                data = f.read()
        else:
            data = path_or_file.read()
        top = json.loads(data)
    except json.JSONDecodeError as e:
        raise CimJsonLdError(f"not valid JSON: {e}") from e
    except UnicodeDecodeError as e:
        raise CimJsonLdError(f"not valid UTF-8 JSON: {e}") from e
    return _Reader(strict).read(top)
