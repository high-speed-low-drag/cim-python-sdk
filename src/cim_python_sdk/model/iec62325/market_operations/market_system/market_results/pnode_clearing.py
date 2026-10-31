"""CIM class PnodeClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commodity_price import (
        CommodityPrice,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pnode_results import (
        PnodeResults,
    )


class PnodeClearing(MarketFactors):
    """Pricing node clearing results posted for a given settlement period."""

    __slots__ = ("_commodity_price", "_pnode_results")

    commodity_price: Many[CommodityPrice] = Many(
        EndMeta(
            name="commodity_price",
            cim_role="CommodityPrice",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commodity_price:CommodityPrice",
            many=True,
            lower=0,
            upper=None,
            inverse="pnode_clearing",
            aggregation="none",
        )
    )
    pnode_results: Many[PnodeResults] = Many(
        EndMeta(
            name="pnode_results",
            cim_role="PnodeResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pnode_results:PnodeResults",
            many=True,
            lower=1,
            upper=None,
            inverse="pnode_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PnodeClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{7D3FCF72-E47C-4d53-A9D9-AB7E6204C810}",
        ends=(
            commodity_price.meta,
            pnode_results.meta,
        ),
    )

    def __init__(
        self,
        *,
        commodity_price: Iterable[CommodityPrice] | None = None,
        pnode_results: Iterable[PnodeResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if commodity_price is not None:
            PnodeClearing.commodity_price.extend(self, commodity_price)
        if pnode_results is not None:
            PnodeClearing.pnode_results.extend(self, pnode_results)

    def add_commodity_price(self, commodity_price: CommodityPrice) -> Self:
        return PnodeClearing.commodity_price.add(self, commodity_price)

    def remove_commodity_price(self, commodity_price: CommodityPrice) -> Self:
        return PnodeClearing.commodity_price.remove(self, commodity_price)

    def clear_commodity_price(self) -> Self:
        return PnodeClearing.commodity_price.clear(self)

    def num_commodity_price(self) -> int:
        return PnodeClearing.commodity_price.count(self)

    def add_pnode_result(self, pnode_result: PnodeResults) -> Self:
        return PnodeClearing.pnode_results.add(self, pnode_result)

    def remove_pnode_result(self, pnode_result: PnodeResults) -> Self:
        return PnodeClearing.pnode_results.remove(self, pnode_result)

    def clear_pnode_results(self) -> Self:
        return PnodeClearing.pnode_results.clear(self)

    def num_pnode_result(self) -> int:
        return PnodeClearing.pnode_results.count(self)
