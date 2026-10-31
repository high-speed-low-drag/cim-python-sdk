"""CGMES European extension class SolarPowerPlant (EuropeanCIMExtensions/ExtIEC61970/ExtEuBase/ExtEuGeneration/ExtEuProduction). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.production.solar_generating_unit import (
        SolarGeneratingUnit,
    )


class SolarPowerPlant(PowerSystemResource):
    """Solar power plant."""

    __slots__ = ("_solar_generating_units",)

    solar_generating_units: Many[SolarGeneratingUnit] = Many(
        EndMeta(
            name="solar_generating_units",
            cim_role="SolarGeneratingUnits",
            target="cim_python_sdk.model.iec61970.base.generation.production.solar_generating_unit:SolarGeneratingUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="solar_power_plant",
            aggregation="none",
            namespace="eu",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SolarPowerPlant",
        package="EuropeanCIMExtensions/ExtIEC61970/ExtEuBase/ExtEuGeneration/ExtEuProduction",
        guid="{FCAC387C-33C5-4446-AD70-4E6B02809D92}",
        namespace="eu",
        ends=(solar_generating_units.meta,),
    )

    def __init__(
        self,
        *,
        solar_generating_units: Iterable[SolarGeneratingUnit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if solar_generating_units is not None:
            SolarPowerPlant.solar_generating_units.extend(self, solar_generating_units)

    def add_solar_generating_unit(self, solar_generating_unit: SolarGeneratingUnit) -> Self:
        return SolarPowerPlant.solar_generating_units.add(self, solar_generating_unit)

    def remove_solar_generating_unit(self, solar_generating_unit: SolarGeneratingUnit) -> Self:
        return SolarPowerPlant.solar_generating_units.remove(self, solar_generating_unit)

    def clear_solar_generating_units(self) -> Self:
        return SolarPowerPlant.solar_generating_units.clear(self)

    def num_solar_generating_unit(self) -> int:
        return SolarPowerPlant.solar_generating_units.count(self)

    def get_solar_generating_unit_by_mrid(self, mrid: str) -> SolarGeneratingUnit | None:
        return SolarPowerPlant.solar_generating_units.get_by_mrid(self, mrid)
