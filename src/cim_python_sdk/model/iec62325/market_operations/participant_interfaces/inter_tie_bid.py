"""CIM class InterTieBid (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.resource_bid import (
    ResourceBid,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.ramp_rate_curve import (
        RampRateCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_inter_tie import (
        RegisteredInterTie,
    )


class InterTieBid(ResourceBid):
    """This class represents the inter tie bid."""

    __slots__ = ("_ramp_rate_curve", "_registered_inter_tie", "min_hourly_block")

    min_hourly_block: int | None

    ramp_rate_curve: Many[RampRateCurve] = Many(
        EndMeta(
            name="ramp_rate_curve",
            cim_role="RampRateCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.ramp_rate_curve:RampRateCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="inter_tie_bid",
            aggregation="none",
        )
    )
    registered_inter_tie: One[RegisteredInterTie] = One(
        EndMeta(
            name="registered_inter_tie",
            cim_role="RegisteredInterTie",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_inter_tie:RegisteredInterTie",
            many=False,
            lower=0,
            upper=1,
            inverse="inter_tie_bid",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InterTieBid",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{334A7315-32D5-4ec6-9948-7617450C554E}",
        attributes=(AttrMeta("min_hourly_block", "minHourlyBlock", "int", 0, 1, "primitive"),),
        ends=(
            ramp_rate_curve.meta,
            registered_inter_tie.meta,
        ),
    )

    def __init__(
        self,
        *,
        min_hourly_block: int | None = None,
        ramp_rate_curve: Iterable[RampRateCurve] | None = None,
        registered_inter_tie: RegisteredInterTie | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.min_hourly_block = min_hourly_block
        if ramp_rate_curve is not None:
            InterTieBid.ramp_rate_curve.extend(self, ramp_rate_curve)
        if registered_inter_tie is not None:
            self.registered_inter_tie = registered_inter_tie

    def add_ramp_rate_curve(self, ramp_rate_curve: RampRateCurve) -> Self:
        return InterTieBid.ramp_rate_curve.add(self, ramp_rate_curve)

    def remove_ramp_rate_curve(self, ramp_rate_curve: RampRateCurve) -> Self:
        return InterTieBid.ramp_rate_curve.remove(self, ramp_rate_curve)

    def clear_ramp_rate_curve(self) -> Self:
        return InterTieBid.ramp_rate_curve.clear(self)

    def num_ramp_rate_curve(self) -> int:
        return InterTieBid.ramp_rate_curve.count(self)

    def get_ramp_rate_curve_by_mrid(self, mrid: str) -> RampRateCurve | None:
        return InterTieBid.ramp_rate_curve.get_by_mrid(self, mrid)
