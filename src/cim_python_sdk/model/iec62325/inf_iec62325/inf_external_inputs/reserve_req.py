"""CIM class ReserveReq (TC57CIM/IEC62325/InfIEC62325/InfExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.resource_group_req import (
    ResourceGroupReq,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.reserve_req_curve import (
        ReserveReqCurve,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.sensitivity_price_curve import (
        SensitivityPriceCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_product import (
        MarketProduct,
    )


class ReserveReq(ResourceGroupReq):
    """Requirements for minimum amount of reserve and/or regulation to be supplied by a set of
    qualified resources."""

    __slots__ = ("_market_product", "_reserve_req_curve", "_sensitivity_price_curve")

    sensitivity_price_curve: One[SensitivityPriceCurve] = One(
        EndMeta(
            name="sensitivity_price_curve",
            cim_role="SensitivityPriceCurve",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.sensitivity_price_curve:SensitivityPriceCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="reserve_req",
            aggregation="none",
        )
    )
    reserve_req_curve: One[ReserveReqCurve] = One(
        EndMeta(
            name="reserve_req_curve",
            cim_role="ReserveReqCurve",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.reserve_req_curve:ReserveReqCurve",
            many=False,
            lower=1,
            upper=1,
            inverse="reserve_req",
            aggregation="none",
        )
    )
    market_product: One[MarketProduct] = One(
        EndMeta(
            name="market_product",
            cim_role="MarketProduct",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_product:MarketProduct",
            many=False,
            lower=1,
            upper=1,
            inverse="reserve_reqs",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReserveReq",
        package="TC57CIM/IEC62325/InfIEC62325/InfExternalInputs",
        guid="{8E435FB0-35C8-4ece-AEEA-1A9F5C65798D}",
        ends=(
            sensitivity_price_curve.meta,
            reserve_req_curve.meta,
            market_product.meta,
        ),
    )

    def __init__(
        self,
        *,
        sensitivity_price_curve: SensitivityPriceCurve | None = None,
        reserve_req_curve: ReserveReqCurve | None = None,
        market_product: MarketProduct | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if sensitivity_price_curve is not None:
            self.sensitivity_price_curve = sensitivity_price_curve
        if reserve_req_curve is not None:
            self.reserve_req_curve = reserve_req_curve
        if market_product is not None:
            self.market_product = market_product
