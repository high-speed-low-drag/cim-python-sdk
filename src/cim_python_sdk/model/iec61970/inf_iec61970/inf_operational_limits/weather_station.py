"""CIM class WeatherStation (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment


class WeatherStation(PowerSystemResource):
    """This represents a source of ambient temperature."""

    __slots__ = ("_equipment",)

    equipment: Many[Equipment] = Many(
        EndMeta(
            name="equipment",
            cim_role="Equipment",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=True,
            lower=0,
            upper=None,
            inverse="weather_station",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WeatherStation",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{122DAA6F-E5F6-43e0-9E7D-5ECC985513B7}",
        ends=(equipment.meta,),
    )

    def __init__(
        self,
        *,
        equipment: Iterable[Equipment] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if equipment is not None:
            WeatherStation.equipment.extend(self, equipment)

    def add_equipment(self, equipment: Equipment) -> Self:
        return WeatherStation.equipment.add(self, equipment)

    def remove_equipment(self, equipment: Equipment) -> Self:
        return WeatherStation.equipment.remove(self, equipment)

    def clear_equipment(self) -> Self:
        return WeatherStation.equipment.clear(self)

    def num_equipment(self) -> int:
        return WeatherStation.equipment.count(self)

    def get_equipment_by_mrid(self, mrid: str) -> Equipment | None:
        return WeatherStation.equipment.get_by_mrid(self, mrid)
