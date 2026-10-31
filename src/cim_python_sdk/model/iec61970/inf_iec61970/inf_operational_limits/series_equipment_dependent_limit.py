"""CIM class SeriesEquipmentDependentLimit (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.limit_dependency import (
    LimitDependency,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.equipment_limit_series_component import (
        EquipmentLimitSeriesComponent,
    )


class SeriesEquipmentDependentLimit(LimitDependency):
    """Limit based on most restrictive series equipment limit.

    A specification of of equipment that determines the calculated operational limit values
    based upon other equipment and their ratings. The most restrictive limit connected in
    series within the group is used. The physical connection based on switch status for
    example may also impact which elements in the group are considered. Any equipment in the
    group that are presently connected in series with the equipment of the directly
    associated operational limit are used. This provides a means to indicate which
    potentially series equipment limits are considered for a computed operational limit. The
    operational limit of the same operational limit type is assumed to be used from the
    grouped equipment. It is also possible to make assumptions or calculations regarding how
    flow might split if the equipment is not simply in series."""

    __slots__ = ("_equipment_limit_series_component",)

    equipment_limit_series_component: Many[EquipmentLimitSeriesComponent] = Many(
        EndMeta(
            name="equipment_limit_series_component",
            cim_role="EquipmentLimitSeriesComponent",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.equipment_limit_series_component:EquipmentLimitSeriesComponent",
            many=True,
            lower=0,
            upper=None,
            inverse="series_equipment_dependent_limit",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SeriesEquipmentDependentLimit",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{5F8AFC2E-E319-4c12-B886-CBFDB4CFC78B}",
        ends=(equipment_limit_series_component.meta,),
    )

    def __init__(
        self,
        *,
        equipment_limit_series_component: Iterable[EquipmentLimitSeriesComponent] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if equipment_limit_series_component is not None:
            SeriesEquipmentDependentLimit.equipment_limit_series_component.extend(
                self, equipment_limit_series_component
            )

    def add_equipment_limit_series_component(
        self, equipment_limit_series_component: EquipmentLimitSeriesComponent
    ) -> Self:
        return SeriesEquipmentDependentLimit.equipment_limit_series_component.add(
            self, equipment_limit_series_component
        )

    def remove_equipment_limit_series_component(
        self, equipment_limit_series_component: EquipmentLimitSeriesComponent
    ) -> Self:
        return SeriesEquipmentDependentLimit.equipment_limit_series_component.remove(
            self, equipment_limit_series_component
        )

    def clear_equipment_limit_series_component(self) -> Self:
        return SeriesEquipmentDependentLimit.equipment_limit_series_component.clear(self)

    def num_equipment_limit_series_component(self) -> int:
        return SeriesEquipmentDependentLimit.equipment_limit_series_component.count(self)

    def get_equipment_limit_series_component_by_mrid(
        self, mrid: str
    ) -> EquipmentLimitSeriesComponent | None:
        return SeriesEquipmentDependentLimit.equipment_limit_series_component.get_by_mrid(
            self, mrid
        )
