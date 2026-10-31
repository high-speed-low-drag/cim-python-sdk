"""CIM class TradingHubValues (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.trading_hub_price import (
        TradingHubPrice,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode import (
        AggregatedPnode,
    )


class TradingHubValues(CimObject):
    """Models prices at Trading Hubs."""

    __slots__ = ("_aggregated_pnode", "_trading_hub_price", "price")

    price: float | None

    aggregated_pnode: One[AggregatedPnode] = One(
        EndMeta(
            name="aggregated_pnode",
            cim_role="AggregatedPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode:AggregatedPnode",
            many=False,
            lower=1,
            upper=1,
            inverse="trading_hub_values",
            aggregation="none",
        )
    )
    trading_hub_price: One[TradingHubPrice] = One(
        EndMeta(
            name="trading_hub_price",
            cim_role="TradingHubPrice",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.trading_hub_price:TradingHubPrice",
            many=False,
            lower=1,
            upper=1,
            inverse="trading_hub_values",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TradingHubValues",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{1DCB9371-4DAC-4c6a-ACCF-04219ABCA46E}",
        attributes=(AttrMeta("price", "price", "float", 0, 1, "primitive"),),
        ends=(
            aggregated_pnode.meta,
            trading_hub_price.meta,
        ),
    )

    def __init__(
        self,
        *,
        price: float | None = None,
        aggregated_pnode: AggregatedPnode | None = None,
        trading_hub_price: TradingHubPrice | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.price = price
        if aggregated_pnode is not None:
            self.aggregated_pnode = aggregated_pnode
        if trading_hub_price is not None:
            self.trading_hub_price = trading_hub_price
