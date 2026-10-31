"""CIM class DefaultBidCurve (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.default_bid import (
        DefaultBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class DefaultBidCurve(Curve):
    """Default bid curve for default energy bid curve and default startup curves (cost and
    time)."""

    __slots__ = ("_default_bid", "curve_type", "deb_adder_flag")

    curve_type: str | None
    deb_adder_flag: YesNo | None

    default_bid: One[DefaultBid] = One(
        EndMeta(
            name="default_bid",
            cim_role="DefaultBid",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.default_bid:DefaultBid",
            many=False,
            lower=0,
            upper=1,
            inverse="default_bid_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DefaultBidCurve",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{4F72FADE-DFE4-40d9-8F6D-CA4B8F3AB58B}",
        attributes=(
            AttrMeta("curve_type", "curveType", "str", 0, 1, "primitive"),
            AttrMeta("deb_adder_flag", "debAdderFlag", "YesNo", 0, 1, "enumeration"),
        ),
        ends=(default_bid.meta,),
    )

    def __init__(
        self,
        *,
        curve_type: str | None = None,
        deb_adder_flag: YesNo | None = None,
        default_bid: DefaultBid | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.curve_type = curve_type
        self.deb_adder_flag = deb_adder_flag
        if default_bid is not None:
            self.default_bid = default_bid
