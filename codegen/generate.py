"""Generate ``src/cim_python_sdk/model/**`` and ``src/cim_python_sdk/_registry.py`` from the resolved model.

The generator only lays out text. Every Python name comes from `codegen.normalize`; the
output shape is fixed by ``docs/RUNTIME.md`` and the mini model in ``tests/runtime/minimodel``.
Output is deterministic (sorted); ``tools/regen.py`` runs ``ruff format`` over it.
"""

from __future__ import annotations

import ast
import json
import re
import textwrap
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from codegen.ir import DEFAULT_NAMESPACE, Model
from codegen.normalize import MODULE_ROOT, RAssocEnd, RAttribute, RClass, REnum, ResolvedModel

TEMPLATE_DIR = Path(__file__).parent / "templates"
IDENTIFIED_OBJECT_MRID = "{C775F80A-A23D-4f38-AB9D-49D1FA882337}"
DOC_WIDTH = 88

# annotation spelling of the primitive Python types (RUNTIME.md rule 2)
PRIM_ANNOT = {
    "float": "float",
    "int": "int",
    "bool": "bool",
    "str": "str",
    "datetime": "_dt.datetime",
    "date": "_dt.date",
    "time": "_dt.time",
    "Decimal": "_decimal.Decimal",
}
STD_IMPORT = {
    "_dt": "import datetime as _dt",
    "_decimal": "import decimal as _decimal",
}
# names that annotations / generated bodies use at module level
RESERVED = frozenset(
    {
        "Any",
        "AttrMeta",
        "CimCompound",
        "CimDatatype",
        "CimEnum",
        "CimObject",
        "ClassMeta",
        "ClassVar",
        "Decimal",
        "EndMeta",
        "Iterable",
        "Many",
        "One",
        "Self",
        "new_mrid",
        "nonmember",
    }
)
BUILTIN_ANNOT = frozenset({"float", "int", "bool", "str", "_dt", "_decimal"})


class GenerateError(Exception):
    pass


# --------------------------------------------------------------------------
# text helpers
# --------------------------------------------------------------------------


def q(s: str) -> str:
    """A double-quoted Python string literal."""
    return json.dumps(s, ensure_ascii=not s.isprintable())


def natural_key(s: str) -> list[object]:
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def import_rank(name: str) -> tuple[int, str]:
    """isort `order-by-type`: CONSTANTS, then Classes, then variables; case-insensitive."""
    if name.isupper() and len(name) > 1:
        rank = 0
    elif name[0].isupper():
        rank = 1
    else:
        rank = 2
    return rank, name.lower()


def _clean_line(line: str) -> str:
    line = "".join(ch if ch.isprintable() else " " for ch in line)
    return " ".join(line.split())


def docstring(notes: str, fallback: str, indent: str = "    ") -> str:
    """A triple-quoted docstring from plain-text CIM notes; safe to embed.

    Paragraphs (one per note line) are wrapped and separated by blank lines.
    Continuation lines get `indent`; the first line follows the opening quotes.
    """
    paras = []
    for raw in notes.split("\n"):
        line = _clean_line(raw)
        if line:
            paras.append(
                textwrap.fill(line, width=DOC_WIDTH, break_long_words=False, break_on_hyphens=False)
            )
    text = "\n\n".join(paras) if paras else fallback
    text = text.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    if text.endswith('"'):
        text = text[:-1] + '\\"'
    lines = text.split("\n")
    out = [lines[0]] + [(indent + ln) if ln else "" for ln in lines[1:]]
    return '"""' + "\n".join(out) + '"""'


def module_path(module: str) -> Path:
    parts = module.split(".")
    if parts[:2] != ["cim_python_sdk", "model"]:
        raise GenerateError(f"module {module!r} is not under {MODULE_ROOT}")
    return Path(*parts[1:]).with_suffix(".py")


# --------------------------------------------------------------------------
# imports
# --------------------------------------------------------------------------


class Imports:
    """Collects the model classes a module refers to and assigns import aliases."""

    def __init__(self, own: RClass | REnum) -> None:
        self.own = own
        self.runtime: set[str] = set()  # guids needing a real import
        self.typing: set[str] = set()  # guids needing a TYPE_CHECKING import
        self.std: set[str] = set()  # "_dt", "_decimal"
        self.typing_names: set[str] = set()  # Any, ClassVar, Self
        self.iterable = False
        self.rt_names: set[str] = set()  # names from cim_python_sdk._runtime
        self.rt_std: set[str] = set()  # raw stdlib import lines at runtime
        self.alias: dict[str, str] = {}
        self.objs: dict[str, RClass | REnum] = {}
        self.final = False

    def need(self, obj: RClass | REnum, runtime: bool) -> None:
        if obj.guid == self.own.guid:
            return
        self.objs[obj.guid] = obj
        (self.runtime if runtime else self.typing).add(obj.guid)

    def finalize(self) -> None:
        used = set(RESERVED) | {self.own.py_name}
        self.alias = {}
        for obj in sorted(self.objs.values(), key=lambda o: (o.module, o.guid)):
            name = obj.py_name
            k = 1
            while name in used:
                name = f"{obj.py_name}_dup{k}"
                k += 1
            used.add(name)
            self.alias[obj.guid] = name
        self.final = True

    def name(self, obj: RClass | REnum) -> str:
        if obj.guid == self.own.guid:
            return obj.py_name
        return self.alias.get(obj.guid, obj.py_name) if self.final else obj.py_name

    def _line(self, obj: RClass | REnum) -> tuple[str, str]:
        name = self.name(obj)
        suffix = "" if name == obj.py_name else f" as {name}"
        return obj.module, f"from {obj.module} import {obj.py_name}{suffix}"

    def used_names(self) -> set[str]:
        names = {self.name(o) for o in self.objs.values()}
        names |= self.std | self.typing_names | self.rt_names
        if self.iterable:
            names.add("Iterable")
        return names

    def render(self) -> str:
        """The import block (everything between the docstring and the class)."""
        blocks: list[list[str]] = [["from __future__ import annotations"]]
        if self.rt_std:
            blocks.append(sorted(self.rt_std, key=lambda s: (s.startswith("from"), s)))
        first_party = [("cim_python_sdk._runtime", f"from cim_python_sdk._runtime import {self._rt()}")]
        first_party += [self._line(self.objs[g]) for g in self.runtime]
        blocks.append([line for _, line in sorted(first_party, key=lambda t: t[0].lower())])

        tc: list[list[str]] = []
        std_lines = sorted(STD_IMPORT[s] for s in self.std if STD_IMPORT[s] not in self.rt_std)
        if self.iterable:
            std_lines.append("from collections.abc import Iterable")
        if self.typing_names:
            names = ", ".join(sorted(self.typing_names, key=import_rank))
            std_lines.append(f"from typing import {names}")
        std_lines.sort(key=lambda s: (s.startswith("from"), s.split()[1]))
        if std_lines:
            tc.append(std_lines)
        mod_lines = sorted(
            (self._line(self.objs[g]) for g in self.typing - self.runtime),
            key=lambda t: t[0].lower(),
        )
        if mod_lines:
            tc.append([line for _, line in mod_lines])
        out = "\n\n".join("\n".join(b) for b in blocks)
        if tc:
            body = "\n\n".join("\n".join("    " + ln for ln in b) for b in tc)
            out += "\n\nTYPE_CHECKING = False\nif TYPE_CHECKING:\n" + body
        return out

    def _rt(self) -> str:
        return ", ".join(sorted(self.rt_names, key=import_rank))


# --------------------------------------------------------------------------
# class / enum builders
# --------------------------------------------------------------------------


class Generator:
    def __init__(self, resolved: ResolvedModel, model: Model) -> None:
        self.rm = resolved
        self.model = model
        self.by_guid = resolved.by_guid()
        self.env = Environment(
            loader=FileSystemLoader(TEMPLATE_DIR),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
            undefined=StrictUndefined,
            autoescape=False,
        )

    # -- annotations -------------------------------------------------------
    def _core(self, a: RAttribute, imp: Imports) -> str:
        """The annotation type of an attribute without `| None`."""
        if a.type_kind in ("enumeration", "compound"):
            obj = self.by_guid[a.type_guid]
            imp.need(obj, runtime=False)
            return imp.name(obj)
        if a.value_py_type not in PRIM_ANNOT:
            raise GenerateError(f"unsupported value type {a.value_py_type!r} for {a.py_name}")
        t = PRIM_ANNOT[a.value_py_type]
        if "." in t:
            imp.std.add(t.split(".")[0])
        return t

    def _core_key(self, a: RAttribute) -> tuple[str, str]:
        if a.type_kind in ("enumeration", "compound"):
            return (a.type_kind, a.type_guid)
        return ("prim", str(a.value_py_type))

    def _default(self, a: RAttribute, imp: Imports) -> str:
        d = a.default
        if d is None:
            return "None"
        if a.type_kind == "enumeration":
            obj = self.by_guid[a.type_guid]
            if not d.startswith(obj.py_name + "."):
                raise GenerateError(f"enum default {d!r} does not start with {obj.py_name}")
            imp.need(obj, runtime=True)
            return imp.name(obj) + d[len(obj.py_name) :]
        if d.startswith("_dt.date("):
            imp.rt_std.add("import datetime as _dt")  # the default is evaluated at import time
            return d
        ast.literal_eval(d)  # must be a plain literal
        return d

    def _meta_attr(self, a: RAttribute, imp: Imports) -> str:
        parts = [
            q(a.py_name),
            q(a.cim_name),
            q(a.py_type if a.type_kind == "primitive" else self.by_guid[a.type_guid].cim_name),
            str(a.lower),
            "None" if a.upper is None else str(a.upper),
            q(a.type_kind),
        ]
        if a.default is not None:
            parts.append(self._default(a, imp))
        if a.is_static:
            parts.append("static=True")
        if a.deprecated:
            parts.append("deprecated=True")
        if a.namespace != DEFAULT_NAMESPACE:
            parts.append(f"namespace={q(a.namespace)}")
        imp.rt_names.add("AttrMeta")
        return f"AttrMeta({', '.join(parts)})"

    def _inherited_attr(self, c: RClass, a: RAttribute) -> tuple[RClass, RAttribute] | None:
        start = self.by_guid.get(a.overrides) if a.overrides else None
        chain = [start] if start else []
        chain += [self.by_guid[g] for g in c.ancestors if g != (start.guid if start else None)]
        for anc in chain:
            for b in anc.attributes:
                if b.py_name == a.py_name:
                    return anc, b
        return None

    # -- one class ----------------------------------------------------------
    def build_class(self, c: RClass) -> str:
        imp = Imports(c)
        for _ in range(2):  # pass 1 collects references, pass 2 renders with final aliases
            ctx = self._class_ctx(c, imp)
            imp.finalize()
        self._check_names(c, ctx, imp)
        ctx["imports"] = imp.render()
        return self.env.get_template("class.py.j2").render(**ctx)

    def _class_ctx(self, c: RClass, imp: Imports) -> dict:
        kind = c.kind
        if kind not in ("class", "cimdatatype", "compound"):
            raise GenerateError(f"cannot generate kind {kind!r} ({c.cim_name})")
        imp.rt_names.add("ClassMeta")
        if kind != "class" and c.ends:
            raise GenerateError(f"{c.cim_name}: {kind} with association ends")

        # base class
        if kind == "cimdatatype":
            base = "CimDatatype"
            imp.rt_names.add(base)
        elif kind == "compound":
            base = "CimCompound"
            imp.rt_names.add(base)
        elif c.superclass_guid:
            sup = self.by_guid[c.superclass_guid]
            imp.need(sup, runtime=True)
            base = imp.name(sup)
        else:
            base = "CimObject"
            imp.rt_names.add(base)

        own_slots: list[str] = []
        statics: list[dict] = []
        attrs: list[dict] = []
        params: list[dict] = []
        body: list[str] = []
        meta_attrs: list[str] = []
        datatype_attrs: list[str] = []

        for a in c.attributes:
            meta_attrs.append(self._meta_attr(a, imp))
            if kind == "cimdatatype":
                if a.is_static and a.default is not None:
                    datatype_attrs.append(f"{a.py_name} = {self._default(a, imp)}")
                if a.py_name == "value":
                    vt = a.value_py_type
                    if vt == "Decimal":
                        imp.rt_std.add("from decimal import Decimal")
                    elif vt not in ("float", "int", "str", "bool"):
                        raise GenerateError(f"{c.cim_name}: value type {vt}")
                    datatype_attrs.insert(0, f"value_type = {vt}")
                continue
            core = self._core(a, imp)
            if a.is_static:
                imp.typing_names.add("ClassVar")
                statics.append(
                    {
                        "name": a.py_name,
                        "type": core if a.default is not None else f"{core} | None",
                        "default": self._default(a, imp),
                    }
                )
                continue
            if not a.overrides:
                own_slots.append(a.py_name)
            ann = {"name": a.py_name, "type": f"{core} | None", "comment": "", "note": ""}
            comments = []
            if a.overrides:
                inh = self._inherited_attr(c, a)
                if inh is None or self._core_key(inh[1]) != self._core_key(a):
                    comments.append("type: ignore[assignment]")
                if not a.override_compatible:
                    if inh is None:
                        raise GenerateError(
                            f"{c.cim_name}.{a.py_name}: ancestor attribute not found"
                        )
                    ann["note"] = (
                        f"overrides {inh[0].py_name}.{inh[1].py_name} ({inh[1].py_type})"
                        " with an incompatible type"
                    )
            if a.type_kind == "cimdatatype":
                comments.append(a.py_type)
            if comments:
                ann["comment"] = "  # " + "  # ".join(comments)
            attrs.append(ann)
            if kind == "class":
                dflt = self._default(a, imp)
                if a.guid == IDENTIFIED_OBJECT_MRID:
                    imp.rt_names.add("new_mrid")
                    params.append({"name": a.py_name, "type": ann["type"], "default": "None"})
                    body.append(
                        f"self.{a.py_name} = new_mrid() if {a.py_name} is None else {a.py_name}"
                    )
                else:
                    params.append({"name": a.py_name, "type": ann["type"], "default": dflt})
                    body.append(f"self.{a.py_name} = {a.py_name}")

        ends: list[dict] = []
        methods: list[dict] = []
        end_names: list[str] = []
        for e in c.ends:
            tgt = self.by_guid[e.target_guid]
            if not isinstance(tgt, RClass):
                raise GenerateError(f"{c.cim_name}.{e.py_name}: target is not a class")
            imp.need(tgt, runtime=False)
            tname = imp.name(tgt)
            own_slots.append(f"_{e.py_name}")
            end_names.append(e.py_name)
            inverse = e.inverse[1]
            imp.rt_names.update({"EndMeta", "Many" if e.many else "One"})
            ends.append(
                {
                    "name": e.py_name,
                    "cls": "Many" if e.many else "One",
                    "target": tname,
                    "q_name": q(e.py_name),
                    "cim_role": "None" if e.cim_role is None else q(e.cim_role),
                    "target_ref": q(f"{tgt.module}:{tgt.py_name}"),
                    "many": str(e.many),
                    "lower": e.lower,
                    "upper": "None" if e.upper is None else e.upper,
                    "inverse": q(inverse),
                    "aggregation": q(e.aggregation),
                    "namespace": "" if e.namespace == DEFAULT_NAMESPACE else q(e.namespace),
                }
            )
            if e.many:
                imp.iterable = True
                imp.typing_names.add("Self")
                params.append(
                    {"name": e.py_name, "type": f"Iterable[{tname}] | None", "default": "None"}
                )
                body.append(f"if {e.py_name} is not None:")
                body.append(f"    {c.py_name}.{e.py_name}.extend(self, {e.py_name})")
                methods += self._many_methods(c, e, tname)
            else:
                params.append({"name": e.py_name, "type": f"{tname} | None", "default": "None"})
                body.append(f"if {e.py_name} is not None:")
                body.append(f"    self.{e.py_name} = {e.py_name}")

        if params:
            imp.typing_names.add("Any")

        header = (
            f"{_ORIGIN[c.namespace]} {_KIND_WORD[kind]} {c.cim_name} ({c.package}). "
            "Generated code: do not edit."
        )
        return {
            "header": _escape(header),
            "name": c.py_name,
            "base": base,
            "doc": docstring(c.notes, f"{_ORIGIN[c.namespace]} {_KIND_WORD[kind]} {c.cim_name}."),
            "slots": _tuple_literal(sorted(own_slots, key=natural_key)),
            "statics": statics,
            "attrs": attrs,
            "datatype_attrs": datatype_attrs,
            "ends": ends,
            "cim_name": q(c.cim_name),
            "package": q(c.package),
            "guid": q(c.guid),
            "kind_arg": q(kind) if kind != "class" else "",
            "deprecated": c.deprecated,
            "namespace": "" if c.namespace == DEFAULT_NAMESPACE else q(c.namespace),
            "meta_attrs": meta_attrs,
            "end_names": end_names,
            "params": params,
            "init_body": body,
            "methods": methods,
        }

    def _many_methods(self, c: RClass, e: RAssocEnd, tname: str) -> list[dict]:
        names = e.methods
        if len(names) not in (4, 5):
            raise GenerateError(f"{c.cim_name}.{e.py_name}: unexpected methods {names}")
        item = e.item_name
        ref = f"{c.py_name}.{e.py_name}"
        out = [
            {
                "name": names[0],
                "args": f", {item}: {tname}",
                "ret": "Self",
                "body": f"{ref}.add(self, {item})",
            },
            {
                "name": names[1],
                "args": f", {item}: {tname}",
                "ret": "Self",
                "body": f"{ref}.remove(self, {item})",
            },
            {"name": names[2], "args": "", "ret": "Self", "body": f"{ref}.clear(self)"},
            {"name": names[3], "args": "", "ret": "int", "body": f"{ref}.count(self)"},
        ]
        if len(names) == 5:
            out.append(
                {
                    "name": names[4],
                    "args": ", mrid: str",
                    "ret": f"{tname} | None",
                    "body": f"{ref}.get_by_mrid(self, mrid)",
                }
            )
        return out

    def _check_names(self, c: RClass, ctx: dict, imp: Imports) -> None:
        """No member of the class may shadow a name its annotations or bodies use."""
        members = {a.py_name for a in c.attributes} | {e.py_name for e in c.ends}
        members |= {m["name"] for m in ctx["methods"]}
        members |= {"self", "kwargs", c.py_name}
        for e in c.ends:
            members.add(e.item_name)
        used = imp.used_names() | BUILTIN_ANNOT
        used.discard(c.py_name)
        clash = (members - {"self", "kwargs", c.py_name}) & used
        # class names referenced in annotations are CamelCase, members snake_case
        params = {p["name"] for p in ctx["params"]}
        if clash or params & {"self", "kwargs"}:
            raise GenerateError(f"{c.cim_name}: member names shadow referenced names: {clash}")
        if c.py_name in {a.py_name for a in c.attributes} | {e.py_name for e in c.ends}:
            raise GenerateError(f"{c.cim_name}: member named like its class")

    # -- one enum -----------------------------------------------------------
    def build_enum(self, e: REnum) -> str:
        return self.env.get_template("enum.py.j2").render(
            header=_escape(
                f"{_ORIGIN[e.namespace]} enumeration {e.cim_name} ({e.package}). "
                "Generated code: do not edit."
            ),
            name=e.py_name,
            doc=docstring(e.notes, f"{_ORIGIN[e.namespace]} enumeration {e.cim_name}."),
            literals=[{"name": lit.py_name, "value": q(lit.cim_value)} for lit in e.literals],
            cim_name=q(e.cim_name),
            package=q(e.package),
            guid=q(e.guid),
            deprecated=e.deprecated,
            namespace="" if e.namespace == DEFAULT_NAMESPACE else q(e.namespace),
        )

    # -- registry -----------------------------------------------------------
    def build_registry(self, objs: list[RClass | REnum]) -> str:
        by_guid = sorted((o.guid, o) for o in objs)
        by_name = sorted((o.py_name, o) for o in objs if o.is_canonical)
        versions = sorted(self.model.versions.items())
        return self.env.get_template("registry.py.j2").render(
            by_guid=[(q(g), q(f"{o.module}:{o.py_name}")) for g, o in by_guid],
            by_name=[(q(n), q(f"{o.module}:{o.py_name}")) for n, o in by_name],
            versions=[(q(k), q(v)) for k, v in versions],
        )

    # -- everything ---------------------------------------------------------
    def generate(self, outdir: Path) -> list[Path]:
        """Write ``model/**`` and ``_registry.py`` under `outdir` (which plays ``src/cim_python_sdk``)."""
        files: dict[Path, str] = {}
        objs: list[RClass | REnum] = []
        for c in self.rm.classes:
            if c.kind == "primitive":
                continue
            objs.append(c)
            files[module_path(c.module)] = self.build_class(c)
        for e in self.rm.enums:
            objs.append(e)
            files[module_path(e.module)] = self.build_enum(e)

        # directory / module name clashes, and the __init__ of every package directory
        pkgs: set[Path] = {Path("model")}
        for p in files:
            pkgs.update(p.parents)
        pkgs.discard(Path("."))
        mods = {p.with_suffix("") for p in files}
        if mods & pkgs:
            raise GenerateError(f"module and package share a path: {sorted(mods & pkgs)}")
        init_tpl = self.env.get_template("package_init.py.j2")
        for d in pkgs:
            dotted = "cim_python_sdk." + ".".join(d.parts)
            files[d / "__init__.py"] = init_tpl.render(name=dotted)
        files[Path("_registry.py")] = self.build_registry(objs)

        written = []
        for rel in sorted(files):
            path = outdir / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(files[rel], encoding="utf-8", newline="\n")
            written.append(path)
        return written


_KIND_WORD = {"class": "class", "cimdatatype": "datatype", "compound": "compound"}
_ORIGIN = {DEFAULT_NAMESPACE: "CIM", "eu": "CGMES European extension"}


def _escape(s: str) -> str:
    s = s.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    return s[:-1] + '\\"' if s.endswith('"') else s


def _tuple_literal(items: list[str]) -> str:
    if not items:
        return "()"
    inner = ", ".join(q(i) for i in items)
    return f"({inner},)" if len(items) == 1 else f"({inner})"


def generate(resolved: ResolvedModel, model: Model, outdir: Path) -> list[Path]:
    return Generator(resolved, model).generate(outdir)
