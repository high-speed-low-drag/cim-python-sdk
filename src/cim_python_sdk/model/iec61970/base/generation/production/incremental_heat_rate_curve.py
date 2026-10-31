"""CIM class IncrementalHeatRateCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class IncrementalHeatRateCurve(Curve):
    """Relationship between unit incremental heat rate in (delta energy/time) per (delta active
    power) and unit output in active power. The IHR curve represents the slope of the
    HeatInputCurve. Note that the "incremental heat rate" and the "heat rate" have the same
    engineering units."""

    __slots__ = ("_thermal_generating_unit", "is_net_gross_p")

    is_net_gross_p: bool | None

    thermal_generating_unit: One[ThermalGeneratingUnit] = One(
        EndMeta(
            name="thermal_generating_unit",
            cim_role="ThermalGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="incremental_heat_rate_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IncrementalHeatRateCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{C785D117-CA7F-43b9-9781-A2C4F23C539C}",
        attributes=(AttrMeta("is_net_gross_p", "isNetGrossP", "bool", 0, 1, "primitive"),),
        ends=(thermal_generating_unit.meta,),
    )

    def __init__(
        self,
        *,
        is_net_gross_p: bool | None = None,
        thermal_generating_unit: ThermalGeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_net_gross_p = is_net_gross_p
        if thermal_generating_unit is not None:
            self.thermal_generating_unit = thermal_generating_unit
