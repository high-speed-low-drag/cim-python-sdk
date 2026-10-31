"""CIM class SensitivityPriceCurve (TC57CIM/IEC62325/InfIEC62325/InfExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.reserve_req import (
        ReserveReq,
    )


class SensitivityPriceCurve(Curve):
    """Optionally, this curve expresses elasticity of the associated requirement. For example,
    used to reduce requirements when clearing price exceeds reasonable values when the
    supply quantity becomes scarce. For example, a single point value of $1000/MW for a
    spinning reserve will cause a reduction in the required spinning reserve.

    X axis is constrained quantity (e.g., MW)

    Y1 axis is money per constrained quantity"""

    __slots__ = ("_reserve_req",)

    reserve_req: One[ReserveReq] = One(
        EndMeta(
            name="reserve_req",
            cim_role="ReserveReq",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.reserve_req:ReserveReq",
            many=False,
            lower=0,
            upper=1,
            inverse="sensitivity_price_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SensitivityPriceCurve",
        package="TC57CIM/IEC62325/InfIEC62325/InfExternalInputs",
        guid="{236E1822-6F83-4df3-9F29-8796386E876B}",
        ends=(reserve_req.meta,),
    )

    def __init__(
        self,
        *,
        reserve_req: ReserveReq | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if reserve_req is not None:
            self.reserve_req = reserve_req
