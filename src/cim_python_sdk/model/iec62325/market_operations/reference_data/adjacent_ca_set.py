"""CIM class AdjacentCASet (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_self_sched import (
        BidSelfSched,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class AdjacentCASet(IdentifiedObject):
    """Groups Adjacent Control Areas."""

    __slots__ = (
        "_bid_self_sched",
        "_host_control_area",
        "_registered_resource",
        "_rto",
        "_sub_control_area",
        "loss_percentage",
    )

    loss_percentage: float | None

    sub_control_area: Many[SubControlArea] = Many(
        EndMeta(
            name="sub_control_area",
            cim_role="SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=True,
            lower=0,
            upper=None,
            inverse="adjacent_ca_set",
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
            inverse="adjacent_ca_set",
            aggregation="none",
        )
    )
    host_control_area: One[HostControlArea] = One(
        EndMeta(
            name="host_control_area",
            cim_role="HostControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area:HostControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="adjacent_ca_set",
            aggregation="none",
        )
    )
    bid_self_sched: Many[BidSelfSched] = Many(
        EndMeta(
            name="bid_self_sched",
            cim_role="BidSelfSched",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_self_sched:BidSelfSched",
            many=True,
            lower=0,
            upper=None,
            inverse="adjacent_ca_set",
            aggregation="none",
        )
    )
    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=1,
            upper=1,
            inverse="adjacent_ca_set",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AdjacentCASet",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{BE7798B5-C117-4bb3-A680-7F58DACC00A2}",
        attributes=(AttrMeta("loss_percentage", "lossPercentage", "float", 0, 1, "primitive"),),
        ends=(
            sub_control_area.meta,
            registered_resource.meta,
            host_control_area.meta,
            bid_self_sched.meta,
            rto.meta,
        ),
    )

    def __init__(
        self,
        *,
        loss_percentage: float | None = None,
        sub_control_area: Iterable[SubControlArea] | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        host_control_area: HostControlArea | None = None,
        bid_self_sched: Iterable[BidSelfSched] | None = None,
        rto: RTO | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.loss_percentage = loss_percentage
        if sub_control_area is not None:
            AdjacentCASet.sub_control_area.extend(self, sub_control_area)
        if registered_resource is not None:
            AdjacentCASet.registered_resource.extend(self, registered_resource)
        if host_control_area is not None:
            self.host_control_area = host_control_area
        if bid_self_sched is not None:
            AdjacentCASet.bid_self_sched.extend(self, bid_self_sched)
        if rto is not None:
            self.rto = rto

    def add_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return AdjacentCASet.sub_control_area.add(self, sub_control_area)

    def remove_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return AdjacentCASet.sub_control_area.remove(self, sub_control_area)

    def clear_sub_control_area(self) -> Self:
        return AdjacentCASet.sub_control_area.clear(self)

    def num_sub_control_area(self) -> int:
        return AdjacentCASet.sub_control_area.count(self)

    def get_sub_control_area_by_mrid(self, mrid: str) -> SubControlArea | None:
        return AdjacentCASet.sub_control_area.get_by_mrid(self, mrid)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return AdjacentCASet.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return AdjacentCASet.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return AdjacentCASet.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return AdjacentCASet.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return AdjacentCASet.registered_resource.get_by_mrid(self, mrid)

    def add_bid_self_sched(self, bid_self_sched: BidSelfSched) -> Self:
        return AdjacentCASet.bid_self_sched.add(self, bid_self_sched)

    def remove_bid_self_sched(self, bid_self_sched: BidSelfSched) -> Self:
        return AdjacentCASet.bid_self_sched.remove(self, bid_self_sched)

    def clear_bid_self_sched(self) -> Self:
        return AdjacentCASet.bid_self_sched.clear(self)

    def num_bid_self_sched(self) -> int:
        return AdjacentCASet.bid_self_sched.count(self)

    def get_bid_self_sched_by_mrid(self, mrid: str) -> BidSelfSched | None:
        return AdjacentCASet.bid_self_sched.get_by_mrid(self, mrid)
