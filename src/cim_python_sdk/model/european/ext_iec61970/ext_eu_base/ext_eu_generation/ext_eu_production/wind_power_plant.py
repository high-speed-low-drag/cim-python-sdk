"""CGMES European extension class WindPowerPlant (EuropeanCIMExtensions/ExtIEC61970/ExtEuBase/ExtEuGeneration/ExtEuProduction). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.production.wind_generating_unit import (
        WindGeneratingUnit,
    )


class WindPowerPlant(PowerSystemResource):
    """Wind power plant."""

    __slots__ = ("_wind_generating_units",)

    wind_generating_units: Many[WindGeneratingUnit] = Many(
        EndMeta(
            name="wind_generating_units",
            cim_role="WindGeneratingUnits",
            target="cim_python_sdk.model.iec61970.base.generation.production.wind_generating_unit:WindGeneratingUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="wind_power_plant",
            aggregation="none",
            namespace="eu",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindPowerPlant",
        package="EuropeanCIMExtensions/ExtIEC61970/ExtEuBase/ExtEuGeneration/ExtEuProduction",
        guid="{52E21930-D9C8-4243-AF07-B57B20CE94B0}",
        namespace="eu",
        ends=(wind_generating_units.meta,),
    )

    def __init__(
        self,
        *,
        wind_generating_units: Iterable[WindGeneratingUnit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_generating_units is not None:
            WindPowerPlant.wind_generating_units.extend(self, wind_generating_units)

    def add_wind_generating_unit(self, wind_generating_unit: WindGeneratingUnit) -> Self:
        return WindPowerPlant.wind_generating_units.add(self, wind_generating_unit)

    def remove_wind_generating_unit(self, wind_generating_unit: WindGeneratingUnit) -> Self:
        return WindPowerPlant.wind_generating_units.remove(self, wind_generating_unit)

    def clear_wind_generating_units(self) -> Self:
        return WindPowerPlant.wind_generating_units.clear(self)

    def num_wind_generating_unit(self) -> int:
        return WindPowerPlant.wind_generating_units.count(self)

    def get_wind_generating_unit_by_mrid(self, mrid: str) -> WindGeneratingUnit | None:
        return WindPowerPlant.wind_generating_units.get_by_mrid(self, mrid)
