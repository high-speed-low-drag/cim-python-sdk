"""Normalization: turn the IR into a `ResolvedModel` with every naming decision made.

The code generator (M5) consumes only `ResolvedModel`; it never decides names.
Everything is keyed by classifier GUID, never by name.

Naming rules (all deterministic):

* `snake()` converts CIM names to snake_case (see its docstring).
* Class module: ``cim_python_sdk.model.<package segments snake-cased>.<snake(py_name)>``; the root
  package ``TC57CIM`` is dropped and ``EuropeanCIMExtensions`` (the CGMES ``eu`` extensions)
  becomes ``european``.
* Duplicate class names: the canonical copy is the most referenced one (attribute
  types + association-end targets); ties prefer a package without an ``Inf*`` /
  ``Doc*`` segment, then the lowest GUID. Other copies in a package that already
  holds that name get ``_2``, ``_3`` ... on `py_name` and module; copies in other
  packages keep their name and are importable by module path only.
* Member names are checked over own + inherited members + generated method names.
  Resolution order: keyword (`_` suffix), attribute override of an inherited
  attribute (`overrides=<guid>`), association-end collision (rename the later end by
  appending ``_<inverse role>``, or ``_<target class>`` if that still collides).
  Anything else raises `NormalizeError` listing every occurrence.
* Namespaces: every resolved class, enum, attribute and end keeps the IR namespace prefix
  (``cim``/``eu``). A class name used in two namespaces raises `NormalizeError`.
"""

from __future__ import annotations

import datetime as _dt
import keyword
import math
import re
from dataclasses import dataclass, field
from pathlib import Path

from codegen.ir import DEFAULT_NAMESPACE, Association, Classifier, Model, merge

MODULE_ROOT = "cim_python_sdk.model"
ROOT_PACKAGE = "TC57CIM"
# IR root package -> leading module segments under cim_python_sdk.model
ROOT_MODULES = {ROOT_PACKAGE: (), "EuropeanCIMExtensions": ("european",)}
SNAPSHOT = Path(__file__).parent / "snapshot" / "cim100_ir.json"
EU_SNAPSHOT = Path(__file__).parent / "snapshot" / "eu_ir.json"

PRIMITIVE_PY = {
    "Float": "float",
    "Integer": "int",
    "Boolean": "bool",
    "String": "str",
    "Decimal": "Decimal",
    "DateTime": "datetime",
    "Date": "date",
    "Time": "time",
    "Duration": "str",
    "MonthDay": "str",
}
RESERVED_NAMES = frozenset({"validate", "_cim_meta"})


class NormalizeError(Exception):
    """Raised for naming collisions that no rule covers."""


# --------------------------------------------------------------------------
# snake / identifier helpers
# --------------------------------------------------------------------------

_RE_NONWORD = re.compile(r"[^A-Za-z0-9]+")
_RE_LOWER_UPPER = re.compile(r"([a-z0-9])([A-Z])")
_RE_ACRONYM = re.compile(r"([A-Z]+)([A-Z][a-z])")
_RE_ACRONYM_PLURAL = re.compile(r"([A-Z]{2,})s(?![a-z])")
_RE_MRID = re.compile(r"(?<![A-Za-z])mRID(?![a-z])|(?<=[a-z])MRID(?![a-z])")


def snake(name: str) -> str:
    """CIM name to snake_case.

    Non-alphanumeric runs become one `_`; a lower/digit-to-Upper boundary splits
    (``bPerSection`` -> ``b_per_section``); an acronym followed by a capitalised
    word splits before that word (``ACLineSegment`` -> ``ac_line_segment``);
    digits stay attached to the preceding letters (``r0``, ``iec61970_cim_version``).
    an all-caps acronym plus a word-final lowercase ``s`` stays together
    (``DesignLocationCUs`` -> ``design_location_cus``); ``mRID`` is special-cased to ``mrid``. All-caps names collapse (``HVDC`` -> ``hvdc``).
    """
    s = _RE_MRID.sub("Mrid", name)
    s = _RE_NONWORD.sub("_", s)
    s = _RE_ACRONYM_PLURAL.sub(r"\1S", s)  # CUs -> CUS: stays one word
    s = _RE_ACRONYM.sub(r"\1_\2", s)
    s = _RE_LOWER_UPPER.sub(r"\1_\2", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s.lower()


def sanitize_ident(name: str) -> str:
    """Make `name` a valid identifier: invalid chars -> `_`, leading `_` stripped,
    leading digit (or empty) prefixed `v`, keyword -> trailing `_`. Case is preserved.
    Never returns a name starting with `_`."""
    if name.isidentifier() and not keyword.iskeyword(name) and not name.startswith("_"):
        return name
    s = re.sub(r"[^0-9A-Za-z_]", "_", name).lstrip("_")
    if not s or s[0].isdigit():
        s = "v" + s
    if keyword.iskeyword(s):
        s += "_"
    return s


def escape_keyword(name: str) -> str:
    return name + "_" if keyword.iskeyword(name) else name


_NO_SINGULAR = frozenset({"series", "species", "data", "dynamics", "status", "news", "analysis"})
_NO_SINGULAR_SUFFIX = ("us", "ss", "is", "ics")


def singularize(name: str) -> str:
    last = name.rsplit("_", 1)[-1]
    if last != "cus" and (last in _NO_SINGULAR or last.endswith(_NO_SINGULAR_SUFFIX)):  # cus: CUs
        return name
    if name.endswith("ies") and len(name) > 3:
        return name[:-3] + "y"
    if name.endswith("sses"):
        return name[:-2]
    if name.endswith("s") and not name.endswith("ss"):
        return name[:-1]
    return name


def pluralize(name: str) -> str:
    """Plural for generated role names (``network_boundary`` -> ``network_boundaries``)."""
    if len(name) > 1 and name.endswith("y") and name[-2] not in "aeiou_0123456789":
        return name[:-1] + "ies"
    if name.endswith(("s", "x", "z", "ch", "sh")):
        return name + "es"
    return name + "s"


_LITERAL_SYMBOLS = {"%": "percent", "$": "dollar", "+": "plus", "#": "hash", "&": "and", "\u00b0": "deg"}
_RE_PLAIN_LITERAL = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)*")


def literal_ident(value: str) -> str:
    """py_name for an enumeration literal (before collision de-duplication)."""
    if _RE_PLAIN_LITERAL.fullmatch(value) and not keyword.iskeyword(value):
        return value
    s = "".join(f"_{_LITERAL_SYMBOLS[ch]}_" if ch in _LITERAL_SYMBOLS else ch for ch in value)
    s = re.sub(r"[^0-9A-Za-z_]", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if not s or s[0].isdigit():
        s = "v" + s
    if keyword.iskeyword(s):
        s += "_"
    return s


# --------------------------------------------------------------------------
# resolved data model
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class RAttribute:
    guid: str
    cim_name: str
    py_name: str
    type_kind: str  # primitive / cimdatatype / enumeration / compound
    type_guid: str
    py_type: str
    value_py_type: str | None  # primitive Python type; None for enumeration / compound
    lower: int
    upper: int | None
    default: str | None  # Python source expression, e.g. "'ohm'", "UnitSymbol.W", "1.5"
    is_static: bool
    deprecated: bool
    notes: str
    overrides: str | None = None  # guid of the ancestor class whose attribute is re-declared
    rename_reason: str | None = None  # set when py_name differs from snake(cim_name)
    # False when an override re-declares the ancestor attribute with a different, non-narrowing
    # type; the generator treats it as a redeclared annotation.
    override_compatible: bool = True
    namespace: str = DEFAULT_NAMESPACE


@dataclass(frozen=True)
class RAssocEnd:
    owner_guid: str
    association_guid: str
    end_index: int  # 0/1 position inside the IR association
    cim_role: str | None
    py_name: str
    item_name: str
    target_guid: str
    lower: int
    upper: int | None
    many: bool
    inverse: tuple[str, str]  # (owner guid, py_name) of the other end
    aggregation: str
    notes: str
    methods: tuple[str, ...] = ()  # generated method names (many ends only)
    generated_role: bool = False  # role name was missing in the model
    renamed_from: str | None = None  # py_name before collision renaming
    rename_reason: str | None = None
    namespace: str = DEFAULT_NAMESPACE  # of the association


@dataclass(frozen=True)
class RLiteral:
    guid: str
    cim_value: str
    py_name: str
    ea_value: str | None  # EA "Default" column (e.g. ISO 4217 number), usually None
    notes: str


@dataclass(frozen=True)
class RClass:
    guid: str
    cim_name: str
    py_name: str
    module: str  # dotted, under cim_python_sdk.model
    package: str  # IR package path
    kind: str  # class / cimdatatype / compound / primitive
    superclass_guid: str | None
    ancestors: tuple[str, ...]  # nearest first
    is_canonical: bool
    deprecated: bool
    notes: str
    attributes: tuple[RAttribute, ...] = ()
    ends: tuple[RAssocEnd, ...] = ()
    namespace: str = DEFAULT_NAMESPACE


@dataclass(frozen=True)
class REnum:
    guid: str
    cim_name: str
    py_name: str
    module: str
    package: str
    is_canonical: bool
    deprecated: bool
    notes: str
    literals: tuple[RLiteral, ...] = ()
    kind: str = "enumeration"
    namespace: str = DEFAULT_NAMESPACE


@dataclass(frozen=True)
class Report:
    """Data behind naming_report.md."""

    duplicate_classes: tuple[tuple, ...] = ()  # (cim_name, guid, package, py_name, module, canonical)
    class_sanitized: tuple[tuple, ...] = ()  # (guid, cim_name, py_name)
    member_renames: tuple[tuple, ...] = ()  # (class cim_name, class guid, kind, cim, py, reason)
    generated_roles: tuple[tuple, ...] = ()  # (owner name, owner guid, assoc guid, py_name)
    sanitized_literals: tuple[tuple, ...] = ()  # (enum name, enum guid, ((cim, py), ...))
    primitive_fallbacks: tuple[tuple, ...] = ()  # (primitive name, guid)
    default_unparsed: tuple[tuple, ...] = ()  # (class name, attr name, default)
    incompatible_overrides: tuple[tuple, ...] = ()  # (class name, attr name, py_type, ancestor name)
    counts: tuple[tuple[str, int], ...] = ()


@dataclass(frozen=True)
class ResolvedModel:
    classes: tuple[RClass, ...]  # every non-enumeration classifier, sorted by (module, guid)
    enums: tuple[REnum, ...]
    report: Report = field(default_factory=Report)

    def by_guid(self) -> dict[str, RClass | REnum]:
        d: dict[str, RClass | REnum] = {c.guid: c for c in self.classes}
        d.update({e.guid: e for e in self.enums})
        return d


# --------------------------------------------------------------------------
# step 1: classes, modules, duplicates
# --------------------------------------------------------------------------


def _package_segments(package: str) -> list[str]:
    """Module segments (not yet snake-cased) for an IR package path."""
    parts = package.split("/")
    if parts[0] not in ROOT_MODULES:
        raise NormalizeError(f"package {package!r} is not under {' or '.join(ROOT_MODULES)}")
    return [*ROOT_MODULES[parts[0]], *parts[1:]]


def _module_segment(seg: str) -> str:
    s = snake(seg) or "_"
    return escape_keyword(s)


def _is_inf_or_doc(package: str) -> bool:
    return any(p.startswith(("Inf", "Doc")) for p in package.split("/"))


def _reference_counts(model: Model) -> dict[str, int]:
    refs: dict[str, int] = {}
    for c in model.classifiers:
        if c.kind == "enumeration":
            continue
        for a in c.attributes:
            if a.type_guid:
                refs[a.type_guid] = refs.get(a.type_guid, 0) + 1
    for assoc in model.associations:
        for e in assoc.ends:
            refs[e.target] = refs.get(e.target, 0) + 1
    return refs


def _resolve_classes(model: Model):
    """Return (py_name, module, is_canonical, py_sanitized) maps keyed by guid and the
    duplicate-handling report rows."""
    refs = _reference_counts(model)
    by_name: dict[str, list[Classifier]] = {}
    for c in model.classifiers:
        by_name.setdefault(c.name, []).append(c)

    py_name: dict[str, str] = {}
    canonical: dict[str, bool] = {}
    dup_rows: list[tuple] = []
    for name in sorted(by_name):
        group = by_name[name]
        if len({c.namespace for c in group}) > 1:
            raise NormalizeError(
                f"class name {name!r} is used in namespaces {sorted({c.namespace for c in group})}"
            )
        base = sanitize_ident(name)
        if len(group) == 1:
            py_name[group[0].guid] = base
            canonical[group[0].guid] = True
            continue
        ordered = sorted(
            group,
            key=lambda c: (-refs.get(c.guid, 0), _is_inf_or_doc(c.package), c.guid),
        )
        canon = ordered[0]
        py_name[canon.guid] = base
        canonical[canon.guid] = True
        taken_pkgs = {canon.package}
        next_suffix: dict[str, int] = {}
        for c in ordered[1:]:
            canonical[c.guid] = False
            if c.package in taken_pkgs:
                n = next_suffix.get(c.package, 2)
                next_suffix[c.package] = n + 1
                py_name[c.guid] = f"{base}_{n}"
            else:
                py_name[c.guid] = base
                taken_pkgs.add(c.package)

    module: dict[str, str] = {}
    for c in model.classifiers:
        segs = [_module_segment(s) for s in _package_segments(c.package)]
        segs.append(escape_keyword(snake(py_name[c.guid])))
        module[c.guid] = ".".join([MODULE_ROOT, *segs])

    for name in sorted(by_name):
        if len(by_name[name]) > 1:
            for c in sorted(by_name[name], key=lambda c: (not canonical[c.guid], c.guid)):
                dup_rows.append(
                    (name, c.guid, c.package, py_name[c.guid], module[c.guid], canonical[c.guid])
                )
    return py_name, module, canonical, dup_rows


# --------------------------------------------------------------------------
# step 2: enumerations
# --------------------------------------------------------------------------


def _resolve_literals(c: Classifier) -> tuple[RLiteral, ...]:
    taken: set[str] = set()
    out: list[RLiteral] = []
    for lit in c.literals:  # model order; the first claimant keeps the plain name
        cand = literal_ident(lit.name)
        final, n = cand, 2
        while final in taken:
            final = f"{cand}_{n}"
            n += 1
        taken.add(final)
        out.append(RLiteral(lit.guid, lit.name, final, lit.value, lit.notes))
    return tuple(out)


# --------------------------------------------------------------------------
# step 3: attribute types and defaults
# --------------------------------------------------------------------------


def _parse_default(raw: str | None, tkind: str, prim: str | None, enum: REnum | None):
    """Return a Python source expression for the default, or None if not safely parseable."""
    if raw is None:
        return None
    raw = raw.strip()
    if raw == "":
        return None
    if tkind == "enumeration" and enum is not None:
        for lit in enum.literals:
            if lit.cim_value == raw:
                return f"{enum.py_name}.{lit.py_name}"
        return None
    if tkind == "primitive":
        try:
            if prim == "float":
                v = float(raw)
                return repr(v) if math.isfinite(v) else None
            if prim == "int":
                return repr(int(raw))
            if prim == "bool":
                if raw.lower() in ("true", "false"):
                    return "True" if raw.lower() == "true" else "False"
                return None
            if prim == "str":
                return repr(raw)
            if prim == "date":
                d = _dt.date.fromisoformat(raw)
                return f"_dt.date({d.year}, {d.month}, {d.day})"
        except ValueError:
            return None
    return None


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


@dataclass
class _End:
    """Mutable working record for an association end during name resolution."""

    owner: str
    assoc: str
    idx: int
    cim_role: str | None
    base: str  # base py name (snake, keyword-escaped, plural if generated)
    target: str
    lower: int
    upper: int | None
    aggregation: str
    notes: str
    generated: bool
    many: bool
    py_name: str = ""
    item_name: str = ""
    methods: tuple[str, ...] = ()
    renamed_from: str | None = None
    rename_reason: str | None = None


def _methods(py_name: str, item: str, by_mrid: bool = True) -> tuple[str, ...]:
    m = (f"add_{item}", f"remove_{item}", f"clear_{py_name}", f"num_{item}")
    return m + (f"get_{item}_by_mrid",) if by_mrid else m


def normalize(model: Model) -> ResolvedModel:
    errors: list[str] = []
    cls = model.classifier_by_guid()
    py_name, module, canonical, dup_rows = _resolve_classes(model)

    # modules must be unique
    seen_mod: dict[str, str] = {}
    for c in sorted(model.classifiers, key=lambda c: c.guid):
        m = module[c.guid]
        if m in seen_mod:
            errors.append(f"module path {m} used by {seen_mod[m]} and {c.guid} ({c.name})")
        seen_mod[m] = c.guid
    # canonical py_names must be unique
    seen_py: dict[str, str] = {}
    for c in sorted(model.classifiers, key=lambda c: c.guid):
        if canonical[c.guid]:
            if py_name[c.guid] in seen_py:
                errors.append(
                    f"canonical class name {py_name[c.guid]} used by {seen_py[py_name[c.guid]]}"
                    f" and {c.guid}"
                )
            seen_py[py_name[c.guid]] = c.guid

    # enumerations
    enums: dict[str, REnum] = {}
    for c in model.classifiers:
        if c.kind == "enumeration":
            enums[c.guid] = REnum(
                guid=c.guid,
                cim_name=c.name,
                py_name=py_name[c.guid],
                module=module[c.guid],
                package=c.package,
                is_canonical=canonical[c.guid],
                deprecated=c.deprecated,
                notes=c.notes,
                literals=_resolve_literals(c),
                namespace=c.namespace,
            )

    # primitive python types
    prim_py: dict[str, str] = {}
    fallbacks: list[tuple] = []
    for c in model.classifiers:
        if c.kind == "primitive":
            if c.name in PRIMITIVE_PY:
                prim_py[c.guid] = PRIMITIVE_PY[c.name]
            else:
                prim_py[c.guid] = "str"
                fallbacks.append((c.name, c.guid))

    def datatype_value_type(c: Classifier) -> str | None:
        for a in c.attributes:
            if a.name == "value" and a.type_guid in prim_py:
                return prim_py[a.type_guid]
        return None

    dt_value = {c.guid: datatype_value_type(c) for c in model.classifiers if c.kind == "cimdatatype"}
    for g, v in dt_value.items():
        if v is None:
            errors.append(f"CIMDatatype {cls[g].name} ({g}) has no primitive 'value' attribute")

    # ancestry, processed superclass-first
    for c in model.classifiers:
        if c.superclass is not None and c.superclass not in cls:
            errors.append(f"{c.name} ({c.guid}) has unknown superclass {c.superclass}")
    if errors:
        raise NormalizeError("\n".join(errors))

    def ancestors_of(c: Classifier) -> tuple[str, ...]:
        out: list[str] = []
        cur = c
        while cur.superclass is not None:
            if cur.superclass in out or cur.superclass == c.guid:
                raise NormalizeError(f"inheritance cycle at {c.name} ({c.guid})")
            out.append(cur.superclass)
            cur = cls[cur.superclass]
        return tuple(out)

    ancestors = {c.guid: ancestors_of(c) for c in model.classifiers}
    has_mrid = {
        c.guid: any(
            snake(a.name) == "mrid" for k in (c.guid, *ancestors[c.guid]) for a in cls[k].attributes
        )
        for c in model.classifiers
    }

    # ----- association ends, grouped by owner, deterministic order -----
    ends_by_owner: dict[str, list[_End]] = {}
    assoc_by_guid: dict[str, Association] = {a.guid: a for a in model.associations}
    generated_roles: list[tuple] = []
    for assoc in sorted(model.associations, key=lambda a: a.guid):
        for idx, e in enumerate(assoc.ends):
            for g in (e.owner, e.target):
                if g not in cls:
                    errors.append(f"association {assoc.guid} references unknown class {g}")
            if e.owner not in cls or e.target not in cls:
                continue
            many = e.upper is None or e.upper > 1
            if e.role is None:
                base = snake(py_name[e.target])
                if many:
                    base = pluralize(base)
                generated = True
            else:
                base = snake(e.role)
                generated = False
            base = escape_keyword(base or "_")
            if base.startswith("_"):
                errors.append(
                    f"end {assoc.guid}[{idx}] on {cls[e.owner].name}: name {base!r} starts with _"
                )
            ends_by_owner.setdefault(e.owner, []).append(
                _End(e.owner, assoc.guid, idx, e.role, base, e.target, e.lower, e.upper,
                     e.owner_aggregation, e.notes, generated, many)
            )
            if generated:
                generated_roles.append((cls[e.owner].name, e.owner, assoc.guid, base))

    # ----- member resolution, superclass first -----
    order = sorted(model.classifiers, key=lambda c: (len(ancestors[c.guid]), c.guid))
    # ns[guid]: member name -> (kind, declaring class guid); kinds: attr / end / method
    ns: dict[str, dict[str, tuple[str, str]]] = {}
    res_attrs: dict[str, list[RAttribute]] = {}
    res_ends: dict[str, list[_End]] = {}
    member_renames: list[tuple] = []
    default_unparsed: list[tuple] = []

    for c in order:
        if c.kind == "enumeration":
            continue
        space: dict[str, tuple[str, str]] = dict(ns[c.superclass]) if c.superclass else {}
        attrs: list[RAttribute] = []
        own_names: dict[str, str] = {}  # own member name -> description
        for a in c.attributes:
            t = cls.get(a.type_guid) if a.type_guid else None
            if t is None:
                errors.append(f"{c.name}.{a.name} ({c.guid}): unresolved type {a.type_name!r}")
                continue
            if t.kind not in ("primitive", "cimdatatype", "enumeration", "compound"):
                errors.append(f"{c.name}.{a.name}: type {t.name} has unexpected kind {t.kind}")
                continue
            base = snake(a.name)
            name = escape_keyword(base)
            reason = "python keyword" if name != base else None
            if not name or name.startswith("_") or name in RESERVED_NAMES:
                errors.append(f"{c.name}.{a.name} ({c.guid}): reserved/invalid member name {name!r}")
                continue
            overrides = None
            if name in own_names:
                errors.append(
                    f"{c.name} ({c.guid}): attribute {a.name!r} -> {name!r} duplicates "
                    f"own member {own_names[name]}"
                )
                continue
            if name in space:
                kind, decl = space[name]
                if kind == "attr":
                    overrides = decl
                    reason = f"overrides inherited attribute of {cls[decl].name}"
                else:
                    errors.append(
                        f"{c.name} ({c.guid}): attribute {a.name!r} collides with inherited "
                        f"{kind} {name!r} from {cls[decl].name}"
                    )
                    continue
            own_names[name] = f"attribute {a.name}"
            space[name] = ("attr", c.guid)
            if reason:
                member_renames.append((c.name, c.guid, "attribute", a.name, name, reason))
            tk = t.kind
            if tk == "primitive":
                vtype, ptype = prim_py[t.guid], prim_py[t.guid]
            elif tk == "cimdatatype":
                vtype, ptype = dt_value[t.guid], py_name[t.guid]
            elif tk == "enumeration":
                vtype, ptype = None, py_name[t.guid]
            else:
                vtype, ptype = None, py_name[t.guid]
            default = _parse_default(a.default, tk, vtype, enums.get(t.guid))
            if a.default not in (None, "") and default is None:
                default_unparsed.append((c.name, a.name, a.default))
            is_static = a.is_static or (
                c.kind == "cimdatatype" and a.name in ("unit", "multiplier") and default is not None
            )
            compatible = True
            if overrides is not None:
                anc = next((x for x in res_attrs[overrides] if x.py_name == name), None)
                if anc is not None and anc.py_type != ptype:
                    compatible = tk in ("enumeration", "compound") and anc.type_kind == tk
            attrs.append(
                RAttribute(
                    guid=a.guid, cim_name=a.name, py_name=name, type_kind=tk, type_guid=t.guid,
                    py_type=ptype, value_py_type=vtype, lower=a.lower, upper=a.upper,
                    default=default, is_static=is_static, deprecated=a.deprecated, notes=a.notes,
                    overrides=overrides, rename_reason=reason,
                    override_compatible=compatible, namespace=a.namespace,
                )
            )

        ends = ends_by_owner.get(c.guid, [])
        for e in ends:
            other_owner = assoc_by_guid[e.assoc].ends[1 - e.idx]
            other = next(
                x for x in ends_by_owner.get(other_owner.owner, ())
                if x.assoc == e.assoc and x.idx == 1 - e.idx
            )

            def candidates(e=e, other=other):
                yield e.base, None
                yield f"{e.base}_{other.base.rstrip('_')}", f"collision; appended inverse role {other.base!r}"
                tgt = snake(py_name[e.target])
                yield f"{e.base}_{tgt}", f"collision; appended target class {tgt!r}"

            chosen = None
            problems: list[str] = []
            for name, why in candidates():
                item = singularize(name) if e.many else name
                used_items = {x.item_name for x in ends if x.item_name and x is not e}
                if not item or item in space or item in used_items or item in own_names:
                    item = name
                names = [name] + (list(_methods(name, item, has_mrid[e.target])) if e.many else [])
                bad = [
                    n for n in names
                    if n in space or n in RESERVED_NAMES or n.startswith("_") or n in own_names
                    or names.count(n) > 1
                ]
                if not bad:
                    chosen = (name, item, why)
                    break
                problems.append(f"{name!r} (clashes: {', '.join(sorted(set(bad)))})")
            if chosen is None:
                errors.append(
                    f"{c.name} ({c.guid}): association end {e.cim_role!r} (assoc {e.assoc}) "
                    f"cannot be named; tried {'; '.join(problems)}"
                )
                continue
            name, item, why = chosen
            e.py_name, e.item_name = name, item
            e.methods = _methods(name, item, has_mrid[e.target]) if e.many else ()
            if why:
                e.renamed_from, e.rename_reason = e.base, why
                member_renames.append((c.name, c.guid, "end", e.cim_role or "(generated)", name, why))
            space[name] = ("end", c.guid)
            own_names[name] = f"end {e.cim_role}"
            for m in e.methods:
                space[m] = ("method", c.guid)
                own_names[m] = f"method of end {e.cim_role}"
        ns[c.guid] = space
        res_attrs[c.guid] = attrs
        res_ends[c.guid] = [e for e in ends if e.py_name]

    if errors:
        raise NormalizeError(
            f"{len(errors)} unresolved naming problem(s):\n" + "\n".join(errors)
        )

    # ----- build immutable results; resolve inverses -----
    end_index: dict[tuple[str, int], _End] = {}
    for lst in res_ends.values():
        for e in lst:
            end_index[(e.assoc, e.idx)] = e

    classes: list[RClass] = []
    for c in model.classifiers:
        if c.kind == "enumeration":
            continue
        rends = []
        for e in res_ends[c.guid]:
            inv = end_index[(e.assoc, 1 - e.idx)]
            rends.append(
                RAssocEnd(
                    owner_guid=e.owner, association_guid=e.assoc, end_index=e.idx,
                    cim_role=e.cim_role, py_name=e.py_name, item_name=e.item_name,
                    target_guid=e.target, lower=e.lower, upper=e.upper, many=e.many,
                    inverse=(inv.owner, inv.py_name), aggregation=e.aggregation, notes=e.notes,
                    methods=e.methods, generated_role=e.generated,
                    renamed_from=e.renamed_from, rename_reason=e.rename_reason,
                    namespace=assoc_by_guid[e.assoc].namespace,
                )
            )
        classes.append(
            RClass(
                guid=c.guid, cim_name=c.name, py_name=py_name[c.guid], module=module[c.guid],
                package=c.package, kind=c.kind, superclass_guid=c.superclass,
                ancestors=ancestors[c.guid], is_canonical=canonical[c.guid],
                deprecated=c.deprecated, notes=c.notes,
                attributes=tuple(res_attrs[c.guid]), ends=tuple(rends), namespace=c.namespace,
            )
        )
    classes.sort(key=lambda r: (r.module, r.guid))
    enum_list = sorted(enums.values(), key=lambda r: (r.module, r.guid))

    # ----- report -----
    class_sanitized = tuple(
        sorted((c.guid, c.name, py_name[c.guid]) for c in model.classifiers
               if py_name[c.guid] != c.name and canonical[c.guid] and sanitize_ident(c.name) != c.name)
    )
    sanitized_lits = []
    for en in enum_list:
        rows = tuple((l.cim_value, l.py_name) for l in en.literals if l.cim_value != l.py_name)
        if rows:
            sanitized_lits.append((en.cim_name, en.guid, rows))
    incompatible = tuple(sorted(
        (c.cim_name, a.cim_name, a.py_type, cls[a.overrides].name)
        for c in classes for a in c.attributes if a.overrides and not a.override_compatible
    ))
    n_assoc_ends = sum(len(c.ends) for c in classes)
    counts = (
        ("classifiers", len(model.classifiers)),
        ("classes_non_enum", len(classes)),
        ("enumerations", len(enum_list)),
        ("literals", sum(len(e.literals) for e in enum_list)),
        ("literals_sanitized", sum(len(r[2]) for r in sanitized_lits)),
        ("enums_with_sanitized_literals", len(sanitized_lits)),
        ("attributes", sum(len(c.attributes) for c in classes)),
        ("attribute_overrides", sum(1 for c in classes for a in c.attributes if a.overrides)),
        ("attributes_keyword_escaped", sum(
            1 for c in classes for a in c.attributes if a.rename_reason == "python keyword")),
        ("association_ends", n_assoc_ends),
        ("self_associations", sum(1 for a in model.associations if a.ends[0].owner == a.ends[1].target
                                  and a.ends[0].owner == a.ends[1].owner)),
        ("generated_role_names", len(generated_roles)),
        ("end_collision_renames", sum(1 for c in classes for e in c.ends if e.renamed_from)),
        ("many_ends", sum(1 for c in classes for e in c.ends if e.many)),
        ("duplicate_class_names", len({r[0] for r in dup_rows})),
        ("non_canonical_classes", sum(1 for r in dup_rows if not r[5])),
        ("class_names_sanitized", len(class_sanitized)),
        ("primitive_fallbacks", len(fallbacks)),
        ("defaults_unparsed", len(default_unparsed)),
        ("incompatible_overrides", len(incompatible)),
    )
    report = Report(
        duplicate_classes=tuple(dup_rows),
        class_sanitized=class_sanitized,
        member_renames=tuple(sorted(member_renames, key=lambda r: (r[0], r[1], r[2], r[3], r[4]))),
        generated_roles=tuple(sorted(generated_roles)),
        sanitized_literals=tuple(sanitized_lits),
        primitive_fallbacks=tuple(sorted(fallbacks)),
        default_unparsed=tuple(sorted(default_unparsed)),
        incompatible_overrides=incompatible,
        counts=counts,
    )
    return ResolvedModel(classes=tuple(classes), enums=tuple(enum_list), report=report)


def load_snapshot(path: str | Path | None = None) -> Model:
    """The CIM100 IR snapshot (codegen/snapshot/cim100_ir.json) only."""
    p = Path(path) if path else SNAPSHOT
    return Model.from_json(p.read_text(encoding="utf-8"))


def load_eu_snapshot(path: str | Path | None = None) -> Model:
    """The CGMES European extension IR (codegen/snapshot/eu_ir.json, see tools/dump_eu_ir.py)."""
    p = Path(path) if path else EU_SNAPSHOT
    return Model.from_json(p.read_text(encoding="utf-8"))


def load_model() -> Model:
    """What the code is generated from: the CIM100 snapshot merged with the eu extensions."""
    return merge(load_snapshot(), load_eu_snapshot())
