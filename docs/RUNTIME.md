# Runtime contract for generated code (M4 -> M5)

`cim_python_sdk._runtime` is hand-written, stdlib-only and imports nothing from `cim_python_sdk.model`
(import cost ~10 ms; it avoids importing `typing`). Generated modules are thin: slots,
annotations, metadata, descriptors, a keyword-only `__init__` and one-line methods.

The mini model in `tests/runtime/minimodel/` is written exactly as M5 must emit it, and
`tests/runtime/test_contract_doc.py` checks that every code block below matches it
byte for byte. Module paths there are `tests.runtime.minimodel.<snake>`; generated code
uses `RClass.module` (`cim_python_sdk.model.<std>.<pkg...>.<snake>`).

## Runtime API

| Name | Use |
|---|---|
| `CimObject` | base of every plain class; `__slots__ = ()`; `validate()`; `__repr__`; identity eq/hash |
| `One(EndMeta)` | descriptor for an end with upper bound 1, storage slot `_<name>` |
| `Many(EndMeta)` | descriptor for upper bound > 1, storage slot `_<name>`; reading gives a `tuple` snapshot |
| `Many.add / remove / clear / count / get_by_mrid / extend` | called by the generated methods and `__init__` |
| `ClassMeta`, `AttrMeta`, `EndMeta` | frozen metadata; `_cim_meta` holds only what the class itself declares |
| `all_metas(cls)`, `cim_attributes(cls)`, `cim_ends(cls)` | metas merged over the MRO (overrides replace in place) |
| `CimEnum`, `CimCompound`, `CimDatatype` | value-type bases |
| `resolve(ref)` | class or `"module:ClassName"` -> class, imported lazily and cached |
| `new_mrid()` | random UUID4 string (~1 us; `str(uuid4())` costs ~6 us and `import uuid` ~7 ms) |

Linking: assigning a `One` or calling `add_*` links both ends; replacing a target removes the
object from the old target's end; assigning `None`, `remove_*` and `clear_*` unlink both
ends. Re-assigning or re-adding the same object does nothing. Targets are type-checked with
`isinstance` against the lazily resolved target class (`TypeError`); `remove_*` of an absent
item raises `ValueError`. Inverses are maintained by one-sided primitives, so nothing
recurses. Lower/upper bounds are only reported by `validate()`. The runtime is not
thread-safe (like plain Python containers under concurrent mutation).

Construction is atomic per end: `Many.extend` type-checks every item before linking any, so
`ConductingEquipment(terminals=[t, 5])` raises `TypeError` and `t` stays unlinked. (Across
different ends of one `__init__`, earlier ends are already linked when a later one fails.)
A target that cannot be imported raises `RuntimeError("<Owner>.<end>: cannot resolve target
'<ref>'")` chained (`__cause__`) to the original error.

Copying: `copy.deepcopy` and `pickle` are supported, including cyclic graphs and
self-associations; the copy is a separate, consistent graph (Many dicts are rebuilt with the
new `id()` keys in `__setstate__`). Only the slot values are copied, so any class that follows
rule 3 works. `copy.copy` (shallow) raises `TypeError` telling the user to use `deepcopy`,
because a shallow copy would share half-links with the original graph.

Memory: links are strong in both directions, so a graph is freed only by the cyclic GC (not
by refcounting alone). `CimObject` has a `__weakref__` slot (a pointer, measured +16 B per object), so
instances can be weakly referenced. Class-level caches (`_checks`, metas, resolved targets)
hold classes, never instances.

## Rules for a generated class module

1. Header: module docstring, `from __future__ import annotations`, then **runtime imports**:
   names from `cim_python_sdk._runtime`, the superclass, and enums used as default values. Then
   `TYPE_CHECKING = False` / `if TYPE_CHECKING:` (not `typing.TYPE_CHECKING`: importing
   `typing` costs ~15 ms; mypy and pyright treat any `TYPE_CHECKING` name as true) with everything used
   only in annotations: `datetime as _dt`, `decimal as _decimal`, `collections.abc.Iterable`,
   `typing.Any/Self/ClassVar`, association targets, enum/compound attribute types.
   If two imported classes share a py_name (duplicate CIM names), alias one deterministically.
2. Annotation types (always `X | None`): `float int bool str` bare; `datetime`, `date`, `time`
   as `_dt.datetime`, `_dt.date`, `_dt.time`; `Decimal` as `_decimal.Decimal`. Never a bare
   `date`/`time`: attributes named `date`, `time`, `open`, `max`, `sum`, `type`, `input` exist and
   their slot descriptors shadow such names in the class namespace. A CIMDatatype attribute is
   annotated with its `value_py_type` plus a trailing `# <Datatype>` comment; it holds the plain value.
3. `__slots__`: a tuple, naturally sorted (ruff RUF023), with the class's **own** non-static
   attribute names plus `_<end name>` for each own association end. Nothing else: never an
   override (it reuses the parent's slot) and never an inherited member.
4. Class body order: `__slots__`, attribute annotations, end descriptors
   (`name: One[T] = One(EndMeta(...))` / `Many[T] = Many(...)`, all `EndMeta` fields as
   keywords, `target` = the target's `"module:ClassName"`), `_cim_meta`, `__init__`, methods.
   `_cim_meta = ClassMeta(cim_name, package, guid, [kind], [deprecated=True], attributes=(AttrMeta(...), ...), ends=(<end>.meta, ...))`.
   `AttrMeta` is positional: `name, cim_name, py_type, lower, upper, kind`, then `default` and
   `static=True` only when set. `py_type` is `RAttribute.py_type`, `kind` is `type_kind`.
   A deprecated attribute or end adds `deprecated=True` (keyword, only when true) to its
   `AttrMeta` / `EndMeta`, as for `ClassMeta`; the flag is metadata only, the runtime ignores it.
   Likewise a class, enum, attribute or end outside the CIM100 namespace adds
   `namespace="<prefix>"` (keyword, last; omitted for the default `"cim"`), e.g. `namespace="eu"`
   for the CGMES European extensions; `cim_python_sdk._runtime.NAMESPACES` maps prefixes to URIs.
5. `__init__(self, *, <own attributes>, <own ends>, **kwargs: Any) -> None`, in the order of
   `RClass.attributes` then `RClass.ends`, every parameter defaulting to the model default or
   `None`. Body: `super().__init__(**kwargs)`, then `self.<attr> = <attr>` for each attribute,
   then for each end `if <end> is not None:` followed by `self.<end> = <end>` (One) or
   `<Class>.<end>.extend(self, <end>)` (Many, accepts any iterable). `None` and missing
   kwargs therefore never touch links. `CimObject.__init__` raises `TypeError` naming unknown kwargs.
6. Methods for a Many end, named by `RAssocEnd.methods` `(add_<item>, remove_<item>,
   clear_<name>, num_<item>[, get_<item>_by_mrid])`, parameter named `item_name`:
   `return <Class>.<end>.add(self, x)` / `.remove(self, x)` / `.clear(self)` / `.count(self)` /
   `.get_by_mrid(self, mrid)`. `add/remove/clear` return `Self`.
7. Static attributes (`is_static`, e.g. `IEC61970CIMVersion.version`): `name: ClassVar[T] = <default or None>`;
   no slot, no `__init__` parameter; `AttrMeta(..., static=True)`.
8. Empty class: no own attributes, no own ends and no overrides. Emit `__slots__ = ()` and
   `_cim_meta` (no `attributes=` / `ends=`) and **omit `__init__`** (the superclass one is
   inherited); see `Conductor` below. A class with only an override is not empty (see Facility).
9. A superclass in another package is imported by its absolute module path, e.g.
   `from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject`.
10. Names: every Python name (members, methods, item names) comes precomputed from
    `codegen/normalize.py` (`RAttribute.py_name`, `RAssocEnd.py_name` / `item_name` / `methods`).
    The generator must never derive names itself; M3 has already resolved collisions.
11. Formatting: output is `ruff format`-stable (M5 may simply run `ruff format` on it). The mini
   model is mypy-clean: `MYPYPATH=. uv run --with mypy mypy src/cim_python_sdk/_runtime tests/runtime/minimodel`.

## Example: ConductingEquipment (attributes, a Many end, all methods)

<!-- file: tests/runtime/minimodel/conducting_equipment.py -->
```python
"""CIM class ConductingEquipment (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from tests.runtime.minimodel.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from tests.runtime.minimodel.terminal import Terminal


class ConductingEquipment(PowerSystemResource):
    """The parts of the AC power system that are designed to carry current or that are
    conductively connected through terminals."""

    __slots__ = ("_terminals", "nominal_voltage")

    nominal_voltage: float | None  # Voltage

    terminals: Many[Terminal] = Many(
        EndMeta(
            name="terminals",
            cim_role="Terminals",
            target="tests.runtime.minimodel.terminal:Terminal",
            many=True,
            lower=0,
            upper=None,
            inverse="conducting_equipment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConductingEquipment",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{00000000-0000-0000-0000-00000000C003}",
        attributes=(AttrMeta("nominal_voltage", "nominalVoltage", "Voltage", 0, 1, "cimdatatype"),),
        ends=(terminals.meta,),
    )

    def __init__(
        self,
        *,
        nominal_voltage: float | None = None,
        terminals: Iterable[Terminal] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.nominal_voltage = nominal_voltage
        if terminals is not None:
            ConductingEquipment.terminals.extend(self, terminals)

    def add_terminal(self, terminal: Terminal) -> Self:
        return ConductingEquipment.terminals.add(self, terminal)

    def remove_terminal(self, terminal: Terminal) -> Self:
        return ConductingEquipment.terminals.remove(self, terminal)

    def clear_terminals(self) -> Self:
        return ConductingEquipment.terminals.clear(self)

    def num_terminal(self) -> int:
        return ConductingEquipment.terminals.count(self)

    def get_terminal_by_mrid(self, mrid: str) -> Terminal | None:
        return ConductingEquipment.terminals.get_by_mrid(self, mrid)
```

## Empty class (Conductor)

<!-- file: tests/runtime/minimodel/conductor.py -->
```python
"""CIM class Conductor (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from tests.runtime.minimodel.conducting_equipment import ConductingEquipment


class Conductor(ConductingEquipment):
    """Combination of conducting material with consistent electrical characteristics."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="Conductor",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{00000000-0000-0000-0000-00000000C008}",
    )
```

## Single-valued end (Terminal)

<!-- file: tests/runtime/minimodel/terminal.py -->
```python
"""CIM class Terminal (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from tests.runtime.minimodel.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from tests.runtime.minimodel.conducting_equipment import ConductingEquipment


class Terminal(IdentifiedObject):
    """An AC electrical connection point to a piece of conducting equipment."""

    __slots__ = ("_conducting_equipment", "sequence_number")

    sequence_number: int | None

    conducting_equipment: One[ConductingEquipment] = One(
        EndMeta(
            name="conducting_equipment",
            cim_role="ConductingEquipment",
            target="tests.runtime.minimodel.conducting_equipment:ConductingEquipment",
            many=False,
            lower=1,
            upper=1,
            inverse="terminals",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Terminal",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{00000000-0000-0000-0000-00000000C004}",
        attributes=(AttrMeta("sequence_number", "sequenceNumber", "int", 1, 1, "primitive"),),
        ends=(conducting_equipment.meta,),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        conducting_equipment: ConductingEquipment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        if conducting_equipment is not None:
            self.conducting_equipment = conducting_equipment
```

## mRID default (IdentifiedObject)

`IdentifiedObject.mRID` (match by GUID) is the one special case: its parameter defaults to
`None` and the body assigns `new_mrid() if mrid is None else mrid`.

<!-- file: tests/runtime/minimodel/identified_object.py -->
```python
"""CIM class IdentifiedObject (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, new_mrid

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class IdentifiedObject(CimObject):
    """This is a root class to provide common identification for all classes needing
    identification and naming attributes."""

    __slots__ = ("description", "mrid", "name")

    description: str | None
    mrid: str | None
    name: str | None

    _cim_meta = ClassMeta(
        cim_name="IdentifiedObject",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{00000000-0000-0000-0000-00000000C001}",
        attributes=(
            AttrMeta("description", "description", "str", 0, 1, "primitive"),
            AttrMeta("mrid", "mRID", "str", 0, 1, "primitive"),
            AttrMeta("name", "name", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        description: str | None = None,
        mrid: str | None = None,
        name: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.description = description
        self.mrid = new_mrid() if mrid is None else mrid
        self.name = name
```

## Enum defaults and qualified date annotations (Asset excerpt)

An attribute default that is an enum literal (`RAttribute.default` such as
`"AssetKind.other"`) is used verbatim both as the `__init__` default and as `AttrMeta.default`,
so that enum is imported at runtime (enums import nothing from the model, so no cycles).
Primitive defaults (`1.5`, `'abc'`, `True`) are literals.

<!-- excerpt: tests/runtime/minimodel/asset.py -->
```python
TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from tests.runtime.minimodel.location import Location
    from tests.runtime.minimodel.power_system_resource import PowerSystemResource


class Asset(IdentifiedObject):
    """Tangible resource of the utility, including power system equipment."""

    __slots__ = ("_location", "_power_system_resources", "date", "kind")

    date: _dt.date | None
    kind: AssetKind | None

    location: One[Location] = One(
        EndMeta(
            name="location",
            cim_role="Location",
            target="tests.runtime.minimodel.location:Location",
            many=False,
            lower=0,
            upper=1,
            inverse="asset",
            aggregation="none",
        )
    )
    power_system_resources: Many[PowerSystemResource] = Many(
        EndMeta(
            name="power_system_resources",
            cim_role="PowerSystemResources",
            target="tests.runtime.minimodel.power_system_resource:PowerSystemResource",
            many=True,
            lower=1,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Asset",
        package="TC57CIM/IEC61968/Assets",
        guid="{00000000-0000-0000-0000-00000000C005}",
        attributes=(
            AttrMeta("date", "date", "date", 0, 1, "primitive"),
            AttrMeta("kind", "kind", "AssetKind", 0, 1, "enumeration", AssetKind.other),
        ),
        ends=(location.meta, power_system_resources.meta),
    )

    def __init__(
        self,
        *,
        date: _dt.date | None = None,
        kind: AssetKind | None = AssetKind.other,
        location: Location | None = None,
        power_system_resources: Iterable[PowerSystemResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.date = date
        self.kind = kind
        if location is not None:
            self.location = location
        if power_system_resources is not None:
            Asset.power_system_resources.extend(self, power_system_resources)
```

## Overrides (Facility)

A re-declared attribute (`RAttribute.overrides` set, e.g. `kind`) keeps the parent's slot:
it is **not** in the subclass `__slots__`. The subclass re-annotates it (narrowed type),
adds its own `AttrMeta` (which replaces the parent's in `cim_attributes`) and its own
`__init__` parameter: `super().__init__` first assigns the parent default, then the subclass
assigns its own. When the annotation differs from the inherited one, append
`# type: ignore[assignment]` (CIM's narrower enums are unrelated classes to a type checker);
when `override_compatible` is False (only `Facility.kind`), also add a comment line naming
the ancestor type.

<!-- file: tests/runtime/minimodel/facility.py -->
```python
"""CIM class Facility (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from tests.runtime.minimodel.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Facility(Asset):
    """A facility may contain buildings, storage facilities, switching facilities, etc."""

    __slots__ = ()

    # overrides Asset.kind (AssetKind) with an incompatible type
    kind: str | None  # type: ignore[assignment]

    _cim_meta = ClassMeta(
        cim_name="Facility",
        package="TC57CIM/IEC61968/Assets",
        guid="{00000000-0000-0000-0000-00000000C006}",
        attributes=(AttrMeta("kind", "kind", "str", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        kind: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
```

## Enumerations, compounds, datatypes

Enum members are `<RLiteral.py_name> = "<cim_value>"`; `_cim_meta` must be wrapped in
`enum.nonmember`. `str(member)` is the CIM spelling.

<!-- file: tests/runtime/minimodel/asset_kind.py -->
```python
"""CIM enumeration AssetKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetKind(CimEnum):
    """Kind of asset."""

    breaker = "breaker"
    other = "other"
    v3phase_transformer = "3phaseTransformer"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{00000000-0000-0000-0000-00000000A001}",
            kind="enumeration",
        )
    )
```

A compound declares slots, annotations and `_cim_meta` only: `CimCompound` supplies the
keyword `__init__` (defaults from the metas, `TypeError` on unknown names), value `__eq__`
and `__repr__`.

<!-- file: tests/runtime/minimodel/street_address.py -->
```python
"""CIM compound StreetAddress (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class StreetAddress(CimCompound):
    """General purpose street and postal address information."""

    __slots__ = ("postal_code", "street", "town")

    postal_code: str | None
    street: str | None
    town: str | None

    _cim_meta = ClassMeta(
        cim_name="StreetAddress",
        package="TC57CIM/IEC61968/Common",
        guid="{00000000-0000-0000-0000-00000000B002}",
        kind="compound",
        attributes=(
            AttrMeta("postal_code", "postalCode", "str", 0, 1, "primitive"),
            AttrMeta("street", "street", "str", 0, 1, "primitive"),
            AttrMeta("town", "town", "str", 0, 1, "primitive"),
        ),
    )
```

A datatype carries `value_type` (the `value` attribute's Python type) and, when the model
fixes them (a static default), `unit` / `multiplier` as class attributes; otherwise they stay
`None` from the base. Instances wrap one value (`Voltage(11.0)`), but model attributes typed
`Voltage` hold the plain float.

<!-- file: tests/runtime/minimodel/voltage.py -->
```python
"""CIM datatype Voltage (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from tests.runtime.minimodel.unit_symbol import UnitSymbol


class Voltage(CimDatatype):
    """Electrical voltage, can be both AC and DC."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.V

    _cim_meta = ClassMeta(
        cim_name="Voltage",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{00000000-0000-0000-0000-00000000B001}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.V, static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
```

## Registry

`cim_python_sdk/_registry.py` maps every class and enum GUID to `"module:ClassName"`
(see `tests/runtime/minimodel/_registry.py`); `resolve()` accepts these strings.
