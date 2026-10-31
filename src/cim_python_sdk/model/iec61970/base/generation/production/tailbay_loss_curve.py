"""CIM class TailbayLossCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.hydro_generating_unit import (
        HydroGeneratingUnit,
    )


class TailbayLossCurve(Curve):
    """Relationship between tailbay head loss height (Y-axis) and the total discharge into the
    power station's tailbay volume per time unit (X-axis) . There could be more than one
    curve depending on the level of the tailbay reservoir or river level."""

    __slots__ = ("_hydro_generating_unit",)

    hydro_generating_unit: One[HydroGeneratingUnit] = One(
        EndMeta(
            name="hydro_generating_unit",
            cim_role="HydroGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_generating_unit:HydroGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="tailbay_loss_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TailbayLossCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{C4341551-417C-46df-AD8D-4AAB455DF8CB}",
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
