"""CIM class SubLoadArea (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.load_model.energy_area import EnergyArea

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.load_model.load_area import LoadArea
    from cim_python_sdk.model.iec61970.base.load_model.load_group import LoadGroup


class SubLoadArea(EnergyArea):
    """The class is the second level in a hierarchical structure for grouping of loads for the
    purpose of load flow load scaling."""

    __slots__ = ("_load_area", "_load_groups")

    load_groups: Many[LoadGroup] = Many(
        EndMeta(
            name="load_groups",
            cim_role="LoadGroups",
            target="cim_python_sdk.model.iec61970.base.load_model.load_group:LoadGroup",
            many=True,
            lower=1,
            upper=None,
            inverse="sub_load_area",
            aggregation="shared",
        )
    )
    load_area: One[LoadArea] = One(
        EndMeta(
            name="load_area",
            cim_role="LoadArea",
            target="cim_python_sdk.model.iec61970.base.load_model.load_area:LoadArea",
            many=False,
            lower=1,
            upper=1,
            inverse="sub_load_areas",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SubLoadArea",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{A9E17C64-1729-4286-B30E-A26DED501DAC}",
        ends=(
            load_groups.meta,
            load_area.meta,
        ),
    )

    def __init__(
        self,
        *,
        load_groups: Iterable[LoadGroup] | None = None,
        load_area: LoadArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if load_groups is not None:
            SubLoadArea.load_groups.extend(self, load_groups)
        if load_area is not None:
            self.load_area = load_area

    def add_load_group(self, load_group: LoadGroup) -> Self:
        return SubLoadArea.load_groups.add(self, load_group)

    def remove_load_group(self, load_group: LoadGroup) -> Self:
        return SubLoadArea.load_groups.remove(self, load_group)

    def clear_load_groups(self) -> Self:
        return SubLoadArea.load_groups.clear(self)

    def num_load_group(self) -> int:
        return SubLoadArea.load_groups.count(self)

    def get_load_group_by_mrid(self, mrid: str) -> LoadGroup | None:
        return SubLoadArea.load_groups.get_by_mrid(self, mrid)
