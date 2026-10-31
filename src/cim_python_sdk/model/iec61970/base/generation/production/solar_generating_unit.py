"""CIM class SolarGeneratingUnit (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.generation.production.generating_unit import GeneratingUnit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_generation.ext_eu_production.solar_power_plant import (
        SolarPowerPlant,
    )


class SolarGeneratingUnit(GeneratingUnit):
    """A solar thermal generating unit, connected to the grid by means of a rotating machine.
    This class does not represent photovoltaic (PV) generation."""

    __slots__ = ("_solar_power_plant",)

    solar_power_plant: One[SolarPowerPlant] = One(
        EndMeta(
            name="solar_power_plant",
            cim_role="SolarPowerPlant",
            target="cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_generation.ext_eu_production.solar_power_plant:SolarPowerPlant",
            many=False,
            lower=0,
            upper=1,
            inverse="solar_generating_units",
            aggregation="none",
            namespace="eu",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SolarGeneratingUnit",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{C5A085AB-DDD3-41b0-91DE-9071B466AE9A}",
        ends=(solar_power_plant.meta,),
    )

    def __init__(
        self,
        *,
        solar_power_plant: SolarPowerPlant | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if solar_power_plant is not None:
            self.solar_power_plant = solar_power_plant
