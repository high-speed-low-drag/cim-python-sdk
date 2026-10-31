"""CIM class ExPostMarketRegionResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_market_region import (
        ExPostMarketRegion,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.market_region import (
        MarketRegion,
    )


class ExPostMarketRegionResults(CimObject):
    """Model of expost calculation of cleared MW on a region basis. Includes cleared price."""

    __slots__ = ("_ex_post_market_region", "_market_region", "ex_post_cleared_price")

    ex_post_cleared_price: float | None

    ex_post_market_region: One[ExPostMarketRegion] = One(
        EndMeta(
            name="ex_post_market_region",
            cim_role="ExPostMarketRegion",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_market_region:ExPostMarketRegion",
            many=False,
            lower=1,
            upper=1,
            inverse="ex_post_market_region_results",
            aggregation="none",
        )
    )
    market_region: One[MarketRegion] = One(
        EndMeta(
            name="market_region",
            cim_role="MarketRegion",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.market_region:MarketRegion",
            many=False,
            lower=1,
            upper=1,
            inverse="ex_post_market_region_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExPostMarketRegionResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{BF56AD5D-4BC9-41fc-9BB3-98A5E21A2ABE}",
        attributes=(
            AttrMeta("ex_post_cleared_price", "exPostClearedPrice", "float", 0, 1, "primitive"),
        ),
        ends=(
            ex_post_market_region.meta,
            market_region.meta,
        ),
    )

    def __init__(
        self,
        *,
        ex_post_cleared_price: float | None = None,
        ex_post_market_region: ExPostMarketRegion | None = None,
        market_region: MarketRegion | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ex_post_cleared_price = ex_post_cleared_price
        if ex_post_market_region is not None:
            self.ex_post_market_region = ex_post_market_region
        if market_region is not None:
            self.market_region = market_region
