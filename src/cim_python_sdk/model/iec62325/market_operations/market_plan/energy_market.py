"""CIM class EnergyMarket (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.market_plan.market import Market

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_results import (
        MarketResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.settlement import (
        Settlement,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class EnergyMarket(Market):
    """Energy and Ancillary Market (e.g. Energy, Spinning Reserve, Non-Spinning Reserve) with a
    description of the Market operation control parameters."""

    __slots__ = ("_bids", "_market_results", "_registered_resources", "_rto", "_settlements")

    market_results: One[MarketResults] = One(
        EndMeta(
            name="market_results",
            cim_role="MarketResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_results:MarketResults",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_market",
            aggregation="none",
        )
    )
    registered_resources: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resources",
            cim_role="RegisteredResources",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_markets",
            aggregation="none",
        )
    )
    settlements: Many[Settlement] = Many(
        EndMeta(
            name="settlements",
            cim_role="Settlements",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.settlement:Settlement",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_market",
            aggregation="none",
        )
    )
    bids: Many[Bid] = Many(
        EndMeta(
            name="bids",
            cim_role="Bids",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid:Bid",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_market",
            aggregation="none",
        )
    )
    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_markets",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyMarket",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{F337A947-95CB-4554-BC83-05EEA592CB8E}",
        ends=(
            market_results.meta,
            registered_resources.meta,
            settlements.meta,
            bids.meta,
            rto.meta,
        ),
    )

    def __init__(
        self,
        *,
        market_results: MarketResults | None = None,
        registered_resources: Iterable[RegisteredResource] | None = None,
        settlements: Iterable[Settlement] | None = None,
        bids: Iterable[Bid] | None = None,
        rto: RTO | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if market_results is not None:
            self.market_results = market_results
        if registered_resources is not None:
            EnergyMarket.registered_resources.extend(self, registered_resources)
        if settlements is not None:
            EnergyMarket.settlements.extend(self, settlements)
        if bids is not None:
            EnergyMarket.bids.extend(self, bids)
        if rto is not None:
            self.rto = rto

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return EnergyMarket.registered_resources.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return EnergyMarket.registered_resources.remove(self, registered_resource)

    def clear_registered_resources(self) -> Self:
        return EnergyMarket.registered_resources.clear(self)

    def num_registered_resource(self) -> int:
        return EnergyMarket.registered_resources.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return EnergyMarket.registered_resources.get_by_mrid(self, mrid)

    def add_settlement(self, settlement: Settlement) -> Self:
        return EnergyMarket.settlements.add(self, settlement)

    def remove_settlement(self, settlement: Settlement) -> Self:
        return EnergyMarket.settlements.remove(self, settlement)

    def clear_settlements(self) -> Self:
        return EnergyMarket.settlements.clear(self)

    def num_settlement(self) -> int:
        return EnergyMarket.settlements.count(self)

    def get_settlement_by_mrid(self, mrid: str) -> Settlement | None:
        return EnergyMarket.settlements.get_by_mrid(self, mrid)

    def add_bid(self, bid: Bid) -> Self:
        return EnergyMarket.bids.add(self, bid)

    def remove_bid(self, bid: Bid) -> Self:
        return EnergyMarket.bids.remove(self, bid)

    def clear_bids(self) -> Self:
        return EnergyMarket.bids.clear(self)

    def num_bid(self) -> int:
        return EnergyMarket.bids.count(self)

    def get_bid_by_mrid(self, mrid: str) -> Bid | None:
        return EnergyMarket.bids.get_by_mrid(self, mrid)
