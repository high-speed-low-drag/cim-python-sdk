"""CIM class ReserveReqCurve (TC57CIM/IEC62325/InfIEC62325/InfExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.reserve_req import (
        ReserveReq,
    )


class ReserveReqCurve(Curve):
    """A curve relating reserve requirement versus time, showing the values of a specific
    reserve requirement for each unit of the period covered. The curve can be based on
    "absolute" time or on "normalized' time.

    X is time, typically expressed in absolute time

    Y1 is reserve requirement, typically expressed in MW"""

    __slots__ = ("_reserve_req",)

    reserve_req: One[ReserveReq] = One(
        EndMeta(
            name="reserve_req",
            cim_role="ReserveReq",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.reserve_req:ReserveReq",
            many=False,
            lower=1,
            upper=1,
            inverse="reserve_req_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReserveReqCurve",
        package="TC57CIM/IEC62325/InfIEC62325/InfExternalInputs",
        guid="{71B015A0-EACE-438f-8303-7BCD769465A6}",
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
