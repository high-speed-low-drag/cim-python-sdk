"""CIM class GrossToNetActivePowerCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.generating_unit import (
        GeneratingUnit,
    )


class GrossToNetActivePowerCurve(Curve):
    """Relationship between the generating unit's gross active power output on the X-axis
    (measured at the terminals of the machine(s)) and the generating unit's net active power
    output on the Y-axis (based on utility-defined measurements at the power station).
    Station service loads, when modelled, should be treated as non-conforming bus loads.
    There may be more than one curve, depending on the auxiliary equipment that is in
    service."""

    __slots__ = ("_generating_unit",)

    generating_unit: One[GeneratingUnit] = One(
        EndMeta(
            name="generating_unit",
            cim_role="GeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.generating_unit:GeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="gross_to_net_active_power_curves",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GrossToNetActivePowerCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{830A0115-F812-4eb9-8973-ACC87D49F8CB}",
        ends=(generating_unit.meta,),
    )

    def __init__(
        self,
        *,
        generating_unit: GeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if generating_unit is not None:
            self.generating_unit = generating_unit
