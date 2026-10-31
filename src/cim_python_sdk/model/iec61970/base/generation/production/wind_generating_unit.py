"""CIM class WindGeneratingUnit (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.generation.production.generating_unit import GeneratingUnit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_generation.ext_eu_production.wind_power_plant import (
        WindPowerPlant,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.wind_gen_unit_kind import (
        WindGenUnitKind,
    )


class WindGeneratingUnit(GeneratingUnit):
    """A wind driven generating unit, connected to the grid by means of a rotating machine. May
    be used to represent a single turbine or an aggregation."""

    __slots__ = ("_wind_power_plant", "wind_gen_unit_type")

    wind_gen_unit_type: WindGenUnitKind | None

    wind_power_plant: One[WindPowerPlant] = One(
        EndMeta(
            name="wind_power_plant",
            cim_role="WindPowerPlant",
            target="cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_generation.ext_eu_production.wind_power_plant:WindPowerPlant",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_generating_units",
            aggregation="none",
            namespace="eu",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindGeneratingUnit",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{7B2E09D8-C9AD-4228-B014-0AA2DE3D4BDE}",
        attributes=(
            AttrMeta(
                "wind_gen_unit_type", "windGenUnitType", "WindGenUnitKind", 0, 1, "enumeration"
            ),
        ),
        ends=(wind_power_plant.meta,),
    )

    def __init__(
        self,
        *,
        wind_gen_unit_type: WindGenUnitKind | None = None,
        wind_power_plant: WindPowerPlant | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.wind_gen_unit_type = wind_gen_unit_type
        if wind_power_plant is not None:
            self.wind_power_plant = wind_power_plant
