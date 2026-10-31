"""CIM class LoadArea (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.load_model.energy_area import EnergyArea

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.load_model.sub_load_area import SubLoadArea


class LoadArea(EnergyArea):
    """The class is the root or first level in a hierarchical structure for grouping of loads
    for the purpose of load flow load scaling."""

    __slots__ = ("_sub_load_areas",)

    sub_load_areas: Many[SubLoadArea] = Many(
        EndMeta(
            name="sub_load_areas",
            cim_role="SubLoadAreas",
            target="cim_python_sdk.model.iec61970.base.load_model.sub_load_area:SubLoadArea",
            many=True,
            lower=1,
            upper=None,
            inverse="load_area",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadArea",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{88627287-3FFF-4f0b-954D-3CDA82016DEB}",
        ends=(sub_load_areas.meta,),
    )

    def __init__(
        self,
        *,
        sub_load_areas: Iterable[SubLoadArea] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if sub_load_areas is not None:
            LoadArea.sub_load_areas.extend(self, sub_load_areas)

    def add_sub_load_area(self, sub_load_area: SubLoadArea) -> Self:
        return LoadArea.sub_load_areas.add(self, sub_load_area)

    def remove_sub_load_area(self, sub_load_area: SubLoadArea) -> Self:
        return LoadArea.sub_load_areas.remove(self, sub_load_area)

    def clear_sub_load_areas(self) -> Self:
        return LoadArea.sub_load_areas.clear(self)

    def num_sub_load_area(self) -> int:
        return LoadArea.sub_load_areas.count(self)

    def get_sub_load_area_by_mrid(self, mrid: str) -> SubLoadArea | None:
        return LoadArea.sub_load_areas.get_by_mrid(self, mrid)
