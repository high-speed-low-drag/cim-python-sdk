"""CIM class RampRateCurve (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.constraint_ramp_type import (
        ConstraintRampType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.ramp_rate_condition import (
        RampRateCondition,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.ramp_rate_type import (
        RampRateType,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid import (
        GeneratingBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.inter_tie_bid import (
        InterTieBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_bid import (
        LoadBid,
    )


class RampRateCurve(Curve):
    """Ramp rate as a function of resource MW output."""

    __slots__ = (
        "_generating_bid",
        "_inter_tie_bid",
        "_load_bid",
        "_registered_resource",
        "condition",
        "constraint_ramp_type",
        "ramp_rate_type",
    )

    condition: RampRateCondition | None
    constraint_ramp_type: ConstraintRampType | None
    ramp_rate_type: RampRateType | None

    inter_tie_bid: One[InterTieBid] = One(
        EndMeta(
            name="inter_tie_bid",
            cim_role="InterTieBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.inter_tie_bid:InterTieBid",
            many=False,
            lower=0,
            upper=1,
            inverse="ramp_rate_curve",
            aggregation="none",
        )
    )
    load_bid: One[LoadBid] = One(
        EndMeta(
            name="load_bid",
            cim_role="LoadBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_bid:LoadBid",
            many=False,
            lower=0,
            upper=1,
            inverse="ramp_rate_curve",
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
            inverse="ramp_rate_curve",
            aggregation="none",
        )
    )
    generating_bid: One[GeneratingBid] = One(
        EndMeta(
            name="generating_bid",
            cim_role="GeneratingBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid:GeneratingBid",
            many=False,
            lower=0,
            upper=1,
            inverse="ramp_rate_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RampRateCurve",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{24CCE498-D38B-4e4b-94FF-E84EFBA6E05D}",
        attributes=(
            AttrMeta("condition", "condition", "RampRateCondition", 0, 1, "enumeration"),
            AttrMeta(
                "constraint_ramp_type",
                "constraintRampType",
                "ConstraintRampType",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("ramp_rate_type", "rampRateType", "RampRateType", 0, 1, "enumeration"),
        ),
        ends=(
            inter_tie_bid.meta,
            load_bid.meta,
            registered_resource.meta,
            generating_bid.meta,
        ),
    )

    def __init__(
        self,
        *,
        condition: RampRateCondition | None = None,
        constraint_ramp_type: ConstraintRampType | None = None,
        ramp_rate_type: RampRateType | None = None,
        inter_tie_bid: InterTieBid | None = None,
        load_bid: LoadBid | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        generating_bid: GeneratingBid | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.condition = condition
        self.constraint_ramp_type = constraint_ramp_type
        self.ramp_rate_type = ramp_rate_type
        if inter_tie_bid is not None:
            self.inter_tie_bid = inter_tie_bid
        if load_bid is not None:
            self.load_bid = load_bid
        if registered_resource is not None:
            RampRateCurve.registered_resource.extend(self, registered_resource)
        if generating_bid is not None:
            self.generating_bid = generating_bid

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return RampRateCurve.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return RampRateCurve.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return RampRateCurve.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return RampRateCurve.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return RampRateCurve.registered_resource.get_by_mrid(self, mrid)
