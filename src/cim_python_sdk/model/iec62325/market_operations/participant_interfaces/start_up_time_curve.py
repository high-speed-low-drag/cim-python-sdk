"""CIM class StartUpTimeCurve (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid import (
        GeneratingBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )


class StartUpTimeCurve(Curve):
    """Startup time curve as a function of down time, where time is specified in minutes.
    Relationship between unit startup time (Y1-axis) vs. unit elapsed down time (X-axis)."""

    __slots__ = ("_generating_bid", "_registered_generator")

    generating_bid: Many[GeneratingBid] = Many(
        EndMeta(
            name="generating_bid",
            cim_role="GeneratingBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid:GeneratingBid",
            many=True,
            lower=0,
            upper=None,
            inverse="start_up_time_curve",
            aggregation="none",
        )
    )
    registered_generator: One[RegisteredGenerator] = One(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=False,
            lower=0,
            upper=1,
            inverse="start_up_time_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StartUpTimeCurve",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{016B40BA-1E07-4f91-9113-EA0006C71B19}",
        ends=(
            generating_bid.meta,
            registered_generator.meta,
        ),
    )

    def __init__(
        self,
        *,
        generating_bid: Iterable[GeneratingBid] | None = None,
        registered_generator: RegisteredGenerator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if generating_bid is not None:
            StartUpTimeCurve.generating_bid.extend(self, generating_bid)
        if registered_generator is not None:
            self.registered_generator = registered_generator

    def add_generating_bid(self, generating_bid: GeneratingBid) -> Self:
        return StartUpTimeCurve.generating_bid.add(self, generating_bid)

    def remove_generating_bid(self, generating_bid: GeneratingBid) -> Self:
        return StartUpTimeCurve.generating_bid.remove(self, generating_bid)

    def clear_generating_bid(self) -> Self:
        return StartUpTimeCurve.generating_bid.clear(self)

    def num_generating_bid(self) -> int:
        return StartUpTimeCurve.generating_bid.count(self)

    def get_generating_bid_by_mrid(self, mrid: str) -> GeneratingBid | None:
        return StartUpTimeCurve.generating_bid.get_by_mrid(self, mrid)
