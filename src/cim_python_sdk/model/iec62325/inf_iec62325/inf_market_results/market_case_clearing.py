"""CIM class MarketCaseClearing (TC57CIM/IEC62325/InfIEC62325/InfMarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ancillary_service_clearing import (
        AncillaryServiceClearing,
    )


class MarketCaseClearing(MarketFactors):
    """Market case clearing results are posted for a given settlement period."""

    __slots__ = ("_market_product_clearing", "case_type", "modified_date", "posted_date")

    case_type: str | None
    posted_date: _dt.datetime | None
    modified_date: _dt.datetime | None

    market_product_clearing: Many[AncillaryServiceClearing] = Many(
        EndMeta(
            name="market_product_clearing",
            cim_role="MarketProductClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ancillary_service_clearing:AncillaryServiceClearing",
            many=True,
            lower=0,
            upper=None,
            inverse="market_case_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketCaseClearing",
        package="TC57CIM/IEC62325/InfIEC62325/InfMarketResults",
        guid="{310853AB-4168-40e4-ABE4-7631C0024991}",
        attributes=(
            AttrMeta("case_type", "caseType", "str", 0, 1, "primitive"),
            AttrMeta("posted_date", "postedDate", "datetime", 0, 1, "primitive"),
            AttrMeta("modified_date", "modifiedDate", "datetime", 0, 1, "primitive"),
        ),
        ends=(market_product_clearing.meta,),
    )

    def __init__(
        self,
        *,
        case_type: str | None = None,
        posted_date: _dt.datetime | None = None,
        modified_date: _dt.datetime | None = None,
        market_product_clearing: Iterable[AncillaryServiceClearing] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.case_type = case_type
        self.posted_date = posted_date
        self.modified_date = modified_date
        if market_product_clearing is not None:
            MarketCaseClearing.market_product_clearing.extend(self, market_product_clearing)

    def add_market_product_clearing(
        self, market_product_clearing: AncillaryServiceClearing
    ) -> Self:
        return MarketCaseClearing.market_product_clearing.add(self, market_product_clearing)

    def remove_market_product_clearing(
        self, market_product_clearing: AncillaryServiceClearing
    ) -> Self:
        return MarketCaseClearing.market_product_clearing.remove(self, market_product_clearing)

    def clear_market_product_clearing(self) -> Self:
        return MarketCaseClearing.market_product_clearing.clear(self)

    def num_market_product_clearing(self) -> int:
        return MarketCaseClearing.market_product_clearing.count(self)

    def get_market_product_clearing_by_mrid(self, mrid: str) -> AncillaryServiceClearing | None:
        return MarketCaseClearing.market_product_clearing.get_by_mrid(self, mrid)
