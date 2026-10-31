"""CIM class EquipmentLimitSeriesComponent (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.series_equipment_dependent_limit import (
        SeriesEquipmentDependentLimit,
    )


class EquipmentLimitSeriesComponent(IdentifiedObject):
    """This represents one instance of an equipment that contributes to the calculation of an
    operational limit."""

    __slots__ = ("_equipment", "_series_equipment_dependent_limit")

    equipment: One[Equipment] = One(
        EndMeta(
            name="equipment",
            cim_role="Equipment",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=False,
            lower=1,
            upper=1,
            inverse="eqiupment_limit_series_component",
            aggregation="none",
        )
    )
    series_equipment_dependent_limit: One[SeriesEquipmentDependentLimit] = One(
        EndMeta(
            name="series_equipment_dependent_limit",
            cim_role="SeriesEquipmentDependentLimit",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.series_equipment_dependent_limit:SeriesEquipmentDependentLimit",
            many=False,
            lower=1,
            upper=1,
            inverse="equipment_limit_series_component",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EquipmentLimitSeriesComponent",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{56EBD7E2-15BD-4733-8247-B0D65C6C7F9C}",
        ends=(
            equipment.meta,
            series_equipment_dependent_limit.meta,
        ),
    )

    def __init__(
        self,
        *,
        equipment: Equipment | None = None,
        series_equipment_dependent_limit: SeriesEquipmentDependentLimit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if equipment is not None:
            self.equipment = equipment
        if series_equipment_dependent_limit is not None:
            self.series_equipment_dependent_limit = series_equipment_dependent_limit
