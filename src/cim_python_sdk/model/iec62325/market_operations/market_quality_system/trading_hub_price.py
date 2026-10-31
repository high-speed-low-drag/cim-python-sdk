"""CIM class TradingHubPrice (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.trading_hub_values import (
        TradingHubValues,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType


class TradingHubPrice(CimObject):
    """Models prices at Trading Hubs, interval based."""

    __slots__ = (
        "_trading_hub_values",
        "interval_start_time",
        "market_type",
        "update_time_stamp",
        "update_user",
    )

    interval_start_time: _dt.datetime | None
    market_type: MarketType | None
    update_user: str | None
    update_time_stamp: _dt.datetime | None

    trading_hub_values: Many[TradingHubValues] = Many(
        EndMeta(
            name="trading_hub_values",
            cim_role="TradingHubValues",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.trading_hub_values:TradingHubValues",
            many=True,
            lower=1,
            upper=None,
            inverse="trading_hub_price",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TradingHubPrice",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{6AE25FE5-559A-4df8-8DBB-CE11CA6B35CC}",
        attributes=(
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
        ),
        ends=(trading_hub_values.meta,),
    )

    def __init__(
        self,
        *,
        interval_start_time: _dt.datetime | None = None,
        market_type: MarketType | None = None,
        update_user: str | None = None,
        update_time_stamp: _dt.datetime | None = None,
        trading_hub_values: Iterable[TradingHubValues] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_start_time = interval_start_time
        self.market_type = market_type
        self.update_user = update_user
        self.update_time_stamp = update_time_stamp
        if trading_hub_values is not None:
            TradingHubPrice.trading_hub_values.extend(self, trading_hub_values)

    def add_trading_hub_value(self, trading_hub_value: TradingHubValues) -> Self:
        return TradingHubPrice.trading_hub_values.add(self, trading_hub_value)

    def remove_trading_hub_value(self, trading_hub_value: TradingHubValues) -> Self:
        return TradingHubPrice.trading_hub_values.remove(self, trading_hub_value)

    def clear_trading_hub_values(self) -> Self:
        return TradingHubPrice.trading_hub_values.clear(self)

    def num_trading_hub_value(self) -> int:
        return TradingHubPrice.trading_hub_values.count(self)
