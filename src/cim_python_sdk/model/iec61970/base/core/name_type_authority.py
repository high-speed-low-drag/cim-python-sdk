"""CIM class NameTypeAuthority (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.name_type import NameType


class NameTypeAuthority(CimObject):
    """Authority responsible for creation and management of names of a given type; typically an
    organization or an enterprise system."""

    __slots__ = ("_name_types", "description", "name")

    name: str | None
    description: str | None

    name_types: Many[NameType] = Many(
        EndMeta(
            name="name_types",
            cim_role="NameTypes",
            target="cim_python_sdk.model.iec61970.base.core.name_type:NameType",
            many=True,
            lower=0,
            upper=None,
            inverse="name_type_authority",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NameTypeAuthority",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{F4E2C3FE-B480-46c9-8840-DF8D3F3BD6CC}",
        attributes=(
            AttrMeta("name", "name", "str", 0, 1, "primitive"),
            AttrMeta("description", "description", "str", 0, 1, "primitive"),
        ),
        ends=(name_types.meta,),
    )

    def __init__(
        self,
        *,
        name: str | None = None,
        description: str | None = None,
        name_types: Iterable[NameType] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        if name_types is not None:
            NameTypeAuthority.name_types.extend(self, name_types)

    def add_name_type(self, name_type: NameType) -> Self:
        return NameTypeAuthority.name_types.add(self, name_type)

    def remove_name_type(self, name_type: NameType) -> Self:
        return NameTypeAuthority.name_types.remove(self, name_type)

    def clear_name_types(self) -> Self:
        return NameTypeAuthority.name_types.clear(self)

    def num_name_type(self) -> int:
        return NameTypeAuthority.name_types.count(self)
