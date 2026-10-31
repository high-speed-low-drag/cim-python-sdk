"""CIM class CombinedCyclePlant (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class CombinedCyclePlant(PowerSystemResource):
    """A set of combustion turbines and steam turbines where the exhaust heat from the
    combustion turbines is recovered to make steam for the steam turbines, resulting in
    greater overall plant efficiency."""

    __slots__ = ("_thermal_generating_units", "comb_cycle_plant_rating")

    comb_cycle_plant_rating: float | None  # ActivePower

    thermal_generating_units: Many[ThermalGeneratingUnit] = Many(
        EndMeta(
            name="thermal_generating_units",
            cim_role="ThermalGeneratingUnits",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="combined_cycle_plant",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CombinedCyclePlant",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{C2AD1355-F8F9-4a21-9EF9-E276C34F277C}",
        attributes=(
            AttrMeta(
                "comb_cycle_plant_rating",
                "combCyclePlantRating",
                "ActivePower",
                0,
                1,
                "cimdatatype",
            ),
        ),
        ends=(thermal_generating_units.meta,),
    )

    def __init__(
        self,
        *,
        comb_cycle_plant_rating: float | None = None,
        thermal_generating_units: Iterable[ThermalGeneratingUnit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.comb_cycle_plant_rating = comb_cycle_plant_rating
        if thermal_generating_units is not None:
            CombinedCyclePlant.thermal_generating_units.extend(self, thermal_generating_units)

    def add_thermal_generating_unit(self, thermal_generating_unit: ThermalGeneratingUnit) -> Self:
        return CombinedCyclePlant.thermal_generating_units.add(self, thermal_generating_unit)

    def remove_thermal_generating_unit(
        self, thermal_generating_unit: ThermalGeneratingUnit
    ) -> Self:
        return CombinedCyclePlant.thermal_generating_units.remove(self, thermal_generating_unit)

    def clear_thermal_generating_units(self) -> Self:
        return CombinedCyclePlant.thermal_generating_units.clear(self)

    def num_thermal_generating_unit(self) -> int:
        return CombinedCyclePlant.thermal_generating_units.count(self)

    def get_thermal_generating_unit_by_mrid(self, mrid: str) -> ThermalGeneratingUnit | None:
        return CombinedCyclePlant.thermal_generating_units.get_by_mrid(self, mrid)
