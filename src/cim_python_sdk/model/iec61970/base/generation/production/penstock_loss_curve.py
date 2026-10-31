"""CIM class PenstockLossCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.hydro_generating_unit import (
        HydroGeneratingUnit,
    )


class PenstockLossCurve(Curve):
    """Relationship between penstock head loss (in meters) and total discharge through the
    penstock (in cubic meters per second). One or more turbines may be connected to the same
    penstock."""

    __slots__ = ("_hydro_generating_unit",)

    hydro_generating_unit: One[HydroGeneratingUnit] = One(
        EndMeta(
            name="hydro_generating_unit",
            cim_role="HydroGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_generating_unit:HydroGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="penstock_loss_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PenstockLossCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{1B61FB4A-C9C4-4bfb-9240-5D174664320A}",
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
