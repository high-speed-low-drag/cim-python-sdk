"""CIM class MarketParticipant (TC57CIM/IEC62325/MarketCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation import Organisation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.market_role import MarketRole
    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_management.market_document import MarketDocument
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid
    from cim_python_sdk.model.iec62325.market_operations.reference_data.market_person import (
        MarketPerson,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator import (
        SchedulingCoordinator,
    )


class MarketParticipant(Organisation):
    """An identification of a party acting in a electricity market business process. This class
    is used to identify organizations that can participate in market management and/or
    market operations."""

    __slots__ = (
        "_bid",
        "_market_document",
        "_market_person",
        "_market_role",
        "_registered_resource",
        "_scheduling_coordinator",
        "_time_series",
    )

    market_document: Many[MarketDocument] = Many(
        EndMeta(
            name="market_document",
            cim_role="MarketDocument",
            target="cim_python_sdk.model.iec62325.market_management.market_document:MarketDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="market_participant",
            aggregation="none",
        )
    )
    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="market_participant",
            aggregation="none",
        )
    )
    market_role: Many[MarketRole] = Many(
        EndMeta(
            name="market_role",
            cim_role="MarketRole",
            target="cim_python_sdk.model.iec62325.market_common.market_role:MarketRole",
            many=True,
            lower=0,
            upper=None,
            inverse="market_participant",
            aggregation="none",
        )
    )
    bid: Many[Bid] = Many(
        EndMeta(
            name="bid",
            cim_role="Bid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid:Bid",
            many=True,
            lower=0,
            upper=None,
            inverse="market_participant",
            aggregation="none",
        )
    )
    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="market_participant",
            aggregation="none",
        )
    )
    scheduling_coordinator: Many[SchedulingCoordinator] = Many(
        EndMeta(
            name="scheduling_coordinator",
            cim_role="SchedulingCoordinator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator:SchedulingCoordinator",
            many=True,
            lower=0,
            upper=None,
            inverse="market_participant",
            aggregation="none",
        )
    )
    market_person: Many[MarketPerson] = Many(
        EndMeta(
            name="market_person",
            cim_role="MarketPerson",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.market_person:MarketPerson",
            many=True,
            lower=0,
            upper=None,
            inverse="market_participant",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketParticipant",
        package="TC57CIM/IEC62325/MarketCommon",
        guid="{75B473D1-2626-4e11-BB45-1B2434163D6D}",
        ends=(
            market_document.meta,
            time_series.meta,
            market_role.meta,
            bid.meta,
            registered_resource.meta,
            scheduling_coordinator.meta,
            market_person.meta,
        ),
    )

    def __init__(
        self,
        *,
        market_document: Iterable[MarketDocument] | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        market_role: Iterable[MarketRole] | None = None,
        bid: Iterable[Bid] | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        scheduling_coordinator: Iterable[SchedulingCoordinator] | None = None,
        market_person: Iterable[MarketPerson] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if market_document is not None:
            MarketParticipant.market_document.extend(self, market_document)
        if time_series is not None:
            MarketParticipant.time_series.extend(self, time_series)
        if market_role is not None:
            MarketParticipant.market_role.extend(self, market_role)
        if bid is not None:
            MarketParticipant.bid.extend(self, bid)
        if registered_resource is not None:
            MarketParticipant.registered_resource.extend(self, registered_resource)
        if scheduling_coordinator is not None:
            MarketParticipant.scheduling_coordinator.extend(self, scheduling_coordinator)
        if market_person is not None:
            MarketParticipant.market_person.extend(self, market_person)

    def add_market_document(self, market_document: MarketDocument) -> Self:
        return MarketParticipant.market_document.add(self, market_document)

    def remove_market_document(self, market_document: MarketDocument) -> Self:
        return MarketParticipant.market_document.remove(self, market_document)

    def clear_market_document(self) -> Self:
        return MarketParticipant.market_document.clear(self)

    def num_market_document(self) -> int:
        return MarketParticipant.market_document.count(self)

    def get_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return MarketParticipant.market_document.get_by_mrid(self, mrid)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return MarketParticipant.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return MarketParticipant.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return MarketParticipant.time_series.clear(self)

    def num_time_series(self) -> int:
        return MarketParticipant.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return MarketParticipant.time_series.get_by_mrid(self, mrid)

    def add_market_role(self, market_role: MarketRole) -> Self:
        return MarketParticipant.market_role.add(self, market_role)

    def remove_market_role(self, market_role: MarketRole) -> Self:
        return MarketParticipant.market_role.remove(self, market_role)

    def clear_market_role(self) -> Self:
        return MarketParticipant.market_role.clear(self)

    def num_market_role(self) -> int:
        return MarketParticipant.market_role.count(self)

    def get_market_role_by_mrid(self, mrid: str) -> MarketRole | None:
        return MarketParticipant.market_role.get_by_mrid(self, mrid)

    def add_bid(self, bid: Bid) -> Self:
        return MarketParticipant.bid.add(self, bid)

    def remove_bid(self, bid: Bid) -> Self:
        return MarketParticipant.bid.remove(self, bid)

    def clear_bid(self) -> Self:
        return MarketParticipant.bid.clear(self)

    def num_bid(self) -> int:
        return MarketParticipant.bid.count(self)

    def get_bid_by_mrid(self, mrid: str) -> Bid | None:
        return MarketParticipant.bid.get_by_mrid(self, mrid)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return MarketParticipant.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return MarketParticipant.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return MarketParticipant.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return MarketParticipant.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return MarketParticipant.registered_resource.get_by_mrid(self, mrid)

    def add_scheduling_coordinator(self, scheduling_coordinator: SchedulingCoordinator) -> Self:
        return MarketParticipant.scheduling_coordinator.add(self, scheduling_coordinator)

    def remove_scheduling_coordinator(self, scheduling_coordinator: SchedulingCoordinator) -> Self:
        return MarketParticipant.scheduling_coordinator.remove(self, scheduling_coordinator)

    def clear_scheduling_coordinator(self) -> Self:
        return MarketParticipant.scheduling_coordinator.clear(self)

    def num_scheduling_coordinator(self) -> int:
        return MarketParticipant.scheduling_coordinator.count(self)

    def get_scheduling_coordinator_by_mrid(self, mrid: str) -> SchedulingCoordinator | None:
        return MarketParticipant.scheduling_coordinator.get_by_mrid(self, mrid)

    def add_market_person(self, market_person: MarketPerson) -> Self:
        return MarketParticipant.market_person.add(self, market_person)

    def remove_market_person(self, market_person: MarketPerson) -> Self:
        return MarketParticipant.market_person.remove(self, market_person)

    def clear_market_person(self) -> Self:
        return MarketParticipant.market_person.clear(self)

    def num_market_person(self) -> int:
        return MarketParticipant.market_person.count(self)

    def get_market_person_by_mrid(self, mrid: str) -> MarketPerson | None:
        return MarketParticipant.market_person.get_by_mrid(self, mrid)
