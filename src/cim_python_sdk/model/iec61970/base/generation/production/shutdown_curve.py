"""CIM class ShutdownCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class ShutdownCurve(Curve):
    """Relationship between the rate in gross active power/minute (Y-axis) at which a unit
    should be shutdown and its present gross MW output (X-axis)."""

    __slots__ = ("_thermal_generating_unit", "shutdown_cost", "shutdown_date")

    shutdown_cost: _decimal.Decimal | None  # Money
    shutdown_date: _dt.datetime | None

    thermal_generating_unit: One[ThermalGeneratingUnit] = One(
        EndMeta(
            name="thermal_generating_unit",
            cim_role="ThermalGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="shutdown_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ShutdownCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{AAF85FC5-3F25-44db-BDDF-E595F3D1442A}",
        attributes=(
            AttrMeta("shutdown_cost", "shutdownCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("shutdown_date", "shutdownDate", "datetime", 0, 1, "primitive"),
        ),
        ends=(thermal_generating_unit.meta,),
    )

    def __init__(
        self,
        *,
        shutdown_cost: _decimal.Decimal | None = None,
        shutdown_date: _dt.datetime | None = None,
        thermal_generating_unit: ThermalGeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.shutdown_cost = shutdown_cost
        self.shutdown_date = shutdown_date
        if thermal_generating_unit is not None:
            self.thermal_generating_unit = thermal_generating_unit
