"""CIM class HydroGeneratingEfficiencyCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.hydro_generating_unit import (
        HydroGeneratingUnit,
    )


class HydroGeneratingEfficiencyCurve(Curve):
    """Relationship between unit efficiency as percentage and unit output active power for a
    given net head in meters. The relationship between efficiency, discharge, head, and
    power output is expressed as follows: E =KP/HQ

    where: E is the efficiency, as a percentage; P is the active power; H is the height; Q
    is the discharge, volume/time unit; K is a constant.

    For example, a curve instance for a given net head could show efficiency (Y-axis) versus
    active power output (X-axis) or versus discharge on the X-axis."""

    __slots__ = ("_hydro_generating_unit",)

    hydro_generating_unit: One[HydroGeneratingUnit] = One(
        EndMeta(
            name="hydro_generating_unit",
            cim_role="HydroGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_generating_unit:HydroGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="hydro_generating_efficiency_curves",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HydroGeneratingEfficiencyCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{DDE543F6-E0E1-4d0d-B58D-E725A4736E7D}",
        ends=(hydro_generating_unit.meta,),
    )

    def __init__(
        self,
        *,
        hydro_generating_unit: HydroGeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if hydro_generating_unit is not None:
            self.hydro_generating_unit = hydro_generating_unit
