"""CIM class DefaultBidCurveData (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.curve_data import CurveData

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.bid_calculation_basis import (
        BidCalculationBasis,
    )


class DefaultBidCurveData(CurveData):
    """Curve data for default bid curve and startup cost curve."""

    __slots__ = ("bid_segment_calc_type",)

    bid_segment_calc_type: BidCalculationBasis | None

    _cim_meta = ClassMeta(
        cim_name="DefaultBidCurveData",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{138A7702-A943-43ce-BBBF-BC7A43E4CECE}",
        attributes=(
            AttrMeta(
                "bid_segment_calc_type",
                "bidSegmentCalcType",
                "BidCalculationBasis",
                0,
                1,
                "enumeration",
            ),
        ),
    )

    def __init__(
        self,
        *,
        bid_segment_calc_type: BidCalculationBasis | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bid_segment_calc_type = bid_segment_calc_type
