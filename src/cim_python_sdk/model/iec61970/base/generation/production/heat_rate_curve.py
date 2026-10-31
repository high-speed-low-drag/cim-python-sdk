"""CIM class HeatRateCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class HeatRateCurve(Curve):
    """Relationship between unit heat rate per active power (Y-axis) and unit output (X-axis).
    The heat input is from all fuels."""

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
            inverse="heat_rate_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HeatRateCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{8C0D7783-0EF9-4d60-B329-C9E7ED71AECA}",
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
