"""CIM class HeatInputCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class HeatInputCurve(Curve):
    """Relationship between unit heat input in energy per time for main fuel (Y1-axis) and
    supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of
    main fuel used to sustain generation at this output level is prorated for throttling
    between definition points. The quantity of supplemental fuel used at this output level
    is fixed and not prorated."""

    __slots__ = (
        "_thermal_generating_unit",
        "aux_power_mult",
        "aux_power_offset",
        "heat_input_eff",
        "heat_input_offset",
        "is_net_gross_p",
    )

    aux_power_mult: float | None  # PU
    aux_power_offset: float | None  # ActivePower
    heat_input_eff: float | None  # PU
    heat_input_offset: float | None  # HeatRate
    is_net_gross_p: bool | None

    thermal_generating_unit: One[ThermalGeneratingUnit] = One(
        EndMeta(
            name="thermal_generating_unit",
            cim_role="ThermalGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="heat_input_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HeatInputCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{5FC9AE23-A924-4e2e-81AB-F793F5712C34}",
        attributes=(
            AttrMeta("aux_power_mult", "auxPowerMult", "PU", 0, 1, "cimdatatype"),
            AttrMeta("aux_power_offset", "auxPowerOffset", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("heat_input_eff", "heatInputEff", "PU", 0, 1, "cimdatatype"),
            AttrMeta("heat_input_offset", "heatInputOffset", "HeatRate", 0, 1, "cimdatatype"),
            AttrMeta("is_net_gross_p", "isNetGrossP", "bool", 0, 1, "primitive"),
        ),
        ends=(thermal_generating_unit.meta,),
    )

    def __init__(
        self,
        *,
        aux_power_mult: float | None = None,
        aux_power_offset: float | None = None,
        heat_input_eff: float | None = None,
        heat_input_offset: float | None = None,
        is_net_gross_p: bool | None = None,
        thermal_generating_unit: ThermalGeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.aux_power_mult = aux_power_mult
        self.aux_power_offset = aux_power_offset
        self.heat_input_eff = heat_input_eff
        self.heat_input_offset = heat_input_offset
        self.is_net_gross_p = is_net_gross_p
        if thermal_generating_unit is not None:
            self.thermal_generating_unit = thermal_generating_unit
