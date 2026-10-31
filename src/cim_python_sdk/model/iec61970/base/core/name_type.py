"""CIM class NameType (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.name import Name
    from cim_python_sdk.model.iec61970.base.core.name_type_authority import NameTypeAuthority


class NameType(CimObject):
    """Type of name. Possible values for attribute 'name' are implementation dependent but
    standard profiles may specify types. An enterprise may have multiple IT systems each
    having its own local name for the same object, e.g. a planning system may have different
    names from an EMS. An object may also have different names within the same IT system,
    e.g. localName as defined in CIM version 14. The definition from CIM14 is:

    The localName is a human readable name of the object. It is a free text name local to a
    node in a naming hierarchy similar to a file directory structure. A power system related
    naming hierarchy may be: Substation, VoltageLevel, Equipment etc. Children of the same
    parent in such a hierarchy have names that typically are unique among them."""

    __slots__ = ("_name_type_authority", "_names", "description", "name")

    name: str | None
    description: str | None

    name_type_authority: One[NameTypeAuthority] = One(
        EndMeta(
            name="name_type_authority",
            cim_role="NameTypeAuthority",
            target="cim_python_sdk.model.iec61970.base.core.name_type_authority:NameTypeAuthority",
            many=False,
            lower=0,
            upper=1,
            inverse="name_types",
            aggregation="none",
        )
    )
    names: Many[Name] = Many(
        EndMeta(
            name="names",
            cim_role="Names",
            target="cim_python_sdk.model.iec61970.base.core.name:Name",
            many=True,
            lower=0,
            upper=None,
            inverse="name_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NameType",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{666F94BF-13E3-4947-830F-3A2D4E7CC9FC}",
        attributes=(
            AttrMeta("name", "name", "str", 0, 1, "primitive"),
            AttrMeta("description", "description", "str", 0, 1, "primitive"),
        ),
        ends=(
            name_type_authority.meta,
            names.meta,
        ),
    )

    def __init__(
        self,
        *,
        name: str | None = None,
        description: str | None = None,
        name_type_authority: NameTypeAuthority | None = None,
        names: Iterable[Name] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        if name_type_authority is not None:
            self.name_type_authority = name_type_authority
        if names is not None:
            NameType.names.extend(self, names)

    def add_names(self, names: Name) -> Self:
        return NameType.names.add(self, names)

    def remove_names(self, names: Name) -> Self:
        return NameType.names.remove(self, names)

    def clear_names(self) -> Self:
        return NameType.names.clear(self)

    def num_names(self) -> int:
        return NameType.names.count(self)
