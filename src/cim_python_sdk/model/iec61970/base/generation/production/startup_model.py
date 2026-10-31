"""CIM class StartupModel (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.start_ign_fuel_curve import (
        StartIgnFuelCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.start_main_fuel_curve import (
        StartMainFuelCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.start_ramp_curve import (
        StartRampCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class StartupModel(IdentifiedObject):
    """Unit start up characteristics depending on how long the unit has been off line."""

    __slots__ = (
        "_start_ign_fuel_curve",
        "_start_main_fuel_curve",
        "_start_ramp_curve",
        "_thermal_generating_unit",
        "fixed_maint_cost",
        "hot_standby_heat",
        "incremental_maint_cost",
        "minimum_down_time",
        "minimum_run_time",
        "risk_factor_cost",
        "startup_cost",
        "startup_date",
        "startup_priority",
        "stby_aux_p",
    )

    fixed_maint_cost: float | None  # CostRate
    hot_standby_heat: float | None  # HeatRate
    incremental_maint_cost: float | None  # CostPerEnergyUnit
    minimum_down_time: float | None  # Hours
    minimum_run_time: float | None  # Hours
    risk_factor_cost: _decimal.Decimal | None  # Money
    startup_cost: _decimal.Decimal | None  # Money
    startup_date: _dt.datetime | None
    startup_priority: int | None
    stby_aux_p: float | None  # ActivePower

    start_main_fuel_curve: One[StartMainFuelCurve] = One(
        EndMeta(
            name="start_main_fuel_curve",
            cim_role="StartMainFuelCurve",
            target="cim_python_sdk.model.iec61970.base.generation.production.start_main_fuel_curve:StartMainFuelCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="startup_model",
            aggregation="shared",
        )
    )
    start_ramp_curve: One[StartRampCurve] = One(
        EndMeta(
            name="start_ramp_curve",
            cim_role="StartRampCurve",
            target="cim_python_sdk.model.iec61970.base.generation.production.start_ramp_curve:StartRampCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="startup_model",
            aggregation="shared",
        )
    )
    thermal_generating_unit: One[ThermalGeneratingUnit] = One(
        EndMeta(
            name="thermal_generating_unit",
            cim_role="ThermalGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="startup_model",
            aggregation="none",
        )
    )
    start_ign_fuel_curve: One[StartIgnFuelCurve] = One(
        EndMeta(
            name="start_ign_fuel_curve",
            cim_role="StartIgnFuelCurve",
            target="cim_python_sdk.model.iec61970.base.generation.production.start_ign_fuel_curve:StartIgnFuelCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="startup_model",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StartupModel",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{FBC83D02-01EA-487c-8FAD-3BE0BA87C6ED}",
        attributes=(
            AttrMeta("fixed_maint_cost", "fixedMaintCost", "CostRate", 0, 1, "cimdatatype"),
            AttrMeta("hot_standby_heat", "hotStandbyHeat", "HeatRate", 0, 1, "cimdatatype"),
            AttrMeta(
                "incremental_maint_cost",
                "incrementalMaintCost",
                "CostPerEnergyUnit",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("minimum_down_time", "minimumDownTime", "Hours", 0, 1, "cimdatatype"),
            AttrMeta("minimum_run_time", "minimumRunTime", "Hours", 0, 1, "cimdatatype"),
            AttrMeta("risk_factor_cost", "riskFactorCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("startup_cost", "startupCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("startup_date", "startupDate", "datetime", 0, 1, "primitive"),
            AttrMeta("startup_priority", "startupPriority", "int", 0, 1, "primitive"),
            AttrMeta("stby_aux_p", "stbyAuxP", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            start_main_fuel_curve.meta,
            start_ramp_curve.meta,
            thermal_generating_unit.meta,
            start_ign_fuel_curve.meta,
        ),
    )

    def __init__(
        self,
        *,
        fixed_maint_cost: float | None = None,
        hot_standby_heat: float | None = None,
        incremental_maint_cost: float | None = None,
        minimum_down_time: float | None = None,
        minimum_run_time: float | None = None,
        risk_factor_cost: _decimal.Decimal | None = None,
        startup_cost: _decimal.Decimal | None = None,
        startup_date: _dt.datetime | None = None,
        startup_priority: int | None = None,
        stby_aux_p: float | None = None,
        start_main_fuel_curve: StartMainFuelCurve | None = None,
        start_ramp_curve: StartRampCurve | None = None,
        thermal_generating_unit: ThermalGeneratingUnit | None = None,
        start_ign_fuel_curve: StartIgnFuelCurve | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.fixed_maint_cost = fixed_maint_cost
        self.hot_standby_heat = hot_standby_heat
        self.incremental_maint_cost = incremental_maint_cost
        self.minimum_down_time = minimum_down_time
        self.minimum_run_time = minimum_run_time
        self.risk_factor_cost = risk_factor_cost
        self.startup_cost = startup_cost
        self.startup_date = startup_date
        self.startup_priority = startup_priority
        self.stby_aux_p = stby_aux_p
        if start_main_fuel_curve is not None:
            self.start_main_fuel_curve = start_main_fuel_curve
        if start_ramp_curve is not None:
            self.start_ramp_curve = start_ramp_curve
        if thermal_generating_unit is not None:
            self.thermal_generating_unit = thermal_generating_unit
        if start_ign_fuel_curve is not None:
            self.start_ign_fuel_curve = start_ign_fuel_curve
