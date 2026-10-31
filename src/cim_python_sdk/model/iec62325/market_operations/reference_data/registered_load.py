"""CIM class RegisteredLoad (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_object import (
        AuxiliaryObject,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_bid import (
        LoadBid,
    )


class RegisteredLoad(RegisteredResource):
    """Model of a load that is registered to participate in the market.

    RegisteredLoad is used to model any load that is served by the wholesale market
    directly. RegisteredLoads may be dispatchable or non-dispatchable and may or may not
    have bid curves. Examples of RegisteredLoads would include: distribution company load,
    energy retailer load, large bulk power system connected facility load.

    Loads that are served indirectly, for example - through an energy retailer or a vertical
    utility, should be modeled as RegisteredDistributedResources. Examples of
    RegisteredDistributedResources would include: distribution level storage, distribution
    level generation and distribution level demand response."""

    __slots__ = (
        "_auxillary_object",
        "_load_bids",
        "block_load_transfer",
        "dynamically_scheduled_load_resource",
        "dynamically_scheduled_qualification",
    )

    block_load_transfer: bool | None
    dynamically_scheduled_load_resource: bool | None
    dynamically_scheduled_qualification: bool | None

    load_bids: Many[LoadBid] = Many(
        EndMeta(
            name="load_bids",
            cim_role="LoadBids",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_bid:LoadBid",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_load",
            aggregation="none",
        )
    )
    auxillary_object: Many[AuxiliaryObject] = Many(
        EndMeta(
            name="auxillary_object",
            cim_role="AuxillaryObject",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_object:AuxiliaryObject",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_load",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegisteredLoad",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{02F67FF4-9BCC-401f-ADDC-C56F8D9A19B6}",
        attributes=(
            AttrMeta("block_load_transfer", "blockLoadTransfer", "bool", 0, 1, "primitive"),
            AttrMeta(
                "dynamically_scheduled_load_resource",
                "dynamicallyScheduledLoadResource",
                "bool",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "dynamically_scheduled_qualification",
                "dynamicallyScheduledQualification",
                "bool",
                0,
                1,
                "primitive",
            ),
        ),
        ends=(
            load_bids.meta,
            auxillary_object.meta,
        ),
    )

    def __init__(
        self,
        *,
        block_load_transfer: bool | None = None,
        dynamically_scheduled_load_resource: bool | None = None,
        dynamically_scheduled_qualification: bool | None = None,
        load_bids: Iterable[LoadBid] | None = None,
        auxillary_object: Iterable[AuxiliaryObject] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.block_load_transfer = block_load_transfer
        self.dynamically_scheduled_load_resource = dynamically_scheduled_load_resource
        self.dynamically_scheduled_qualification = dynamically_scheduled_qualification
        if load_bids is not None:
            RegisteredLoad.load_bids.extend(self, load_bids)
        if auxillary_object is not None:
            RegisteredLoad.auxillary_object.extend(self, auxillary_object)

    def add_load_bid(self, load_bid: LoadBid) -> Self:
        return RegisteredLoad.load_bids.add(self, load_bid)

    def remove_load_bid(self, load_bid: LoadBid) -> Self:
        return RegisteredLoad.load_bids.remove(self, load_bid)

    def clear_load_bids(self) -> Self:
        return RegisteredLoad.load_bids.clear(self)

    def num_load_bid(self) -> int:
        return RegisteredLoad.load_bids.count(self)

    def get_load_bid_by_mrid(self, mrid: str) -> LoadBid | None:
        return RegisteredLoad.load_bids.get_by_mrid(self, mrid)

    def add_auxillary_object(self, auxillary_object: AuxiliaryObject) -> Self:
        return RegisteredLoad.auxillary_object.add(self, auxillary_object)

    def remove_auxillary_object(self, auxillary_object: AuxiliaryObject) -> Self:
        return RegisteredLoad.auxillary_object.remove(self, auxillary_object)

    def clear_auxillary_object(self) -> Self:
        return RegisteredLoad.auxillary_object.clear(self)

    def num_auxillary_object(self) -> int:
        return RegisteredLoad.auxillary_object.count(self)
