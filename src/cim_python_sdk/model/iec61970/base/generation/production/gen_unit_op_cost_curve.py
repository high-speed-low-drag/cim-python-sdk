"""CIM class GenUnitOpCostCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.generating_unit import (
        GeneratingUnit,
    )


class GenUnitOpCostCurve(Curve):
    """Relationship between unit operating cost (Y-axis) and unit output active power (X-axis).
    The operating cost curve for thermal units is derived from heat input and fuel costs.
    The operating cost curve for hydro units is derived from water flow rates and equivalent
    water costs."""

    __slots__ = ("_generating_unit", "is_net_gross_p")

    is_net_gross_p: bool | None

    generating_unit: One[GeneratingUnit] = One(
        EndMeta(
            name="generating_unit",
            cim_role="GeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.generating_unit:GeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="gen_unit_op_cost_curves",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GenUnitOpCostCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{62F9E804-3243-40f6-8C02-F860EAF75514}",
        attributes=(AttrMeta("is_net_gross_p", "isNetGrossP", "bool", 0, 1, "primitive"),),
        ends=(generating_unit.meta,),
    )

    def __init__(
        self,
        *,
        is_net_gross_p: bool | None = None,
        generating_unit: GeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_net_gross_p = is_net_gross_p
        if generating_unit is not None:
            self.generating_unit = generating_unit
