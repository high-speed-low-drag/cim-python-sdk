"""CIM class StartUpCostCurve (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
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


class StartUpCostCurve(Curve):
    """Startup costs and time as a function of down time. Relationship between unit startup
    cost (Y1-axis) vs. unit elapsed down time (X-axis)."""

    __slots__ = ("_generating_bid", "_registered_generators")

    generating_bid: Many[GeneratingBid] = Many(
        EndMeta(
            name="generating_bid",
            cim_role="GeneratingBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid:GeneratingBid",
            many=True,
            lower=0,
            upper=None,
            inverse="start_up_cost_curve",
            aggregation="none",
        )
    )
    registered_generators: Many[RegisteredGenerator] = Many(
        EndMeta(
            name="registered_generators",
            cim_role="RegisteredGenerators",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=True,
            lower=0,
            upper=None,
            inverse="start_up_cost_curves",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StartUpCostCurve",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{99245E92-6D85-42ac-91F7-7B044006140A}",
        ends=(
            generating_bid.meta,
            registered_generators.meta,
        ),
    )

    def __init__(
        self,
        *,
        generating_bid: Iterable[GeneratingBid] | None = None,
        registered_generators: Iterable[RegisteredGenerator] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if generating_bid is not None:
            StartUpCostCurve.generating_bid.extend(self, generating_bid)
        if registered_generators is not None:
            StartUpCostCurve.registered_generators.extend(self, registered_generators)

    def add_generating_bid(self, generating_bid: GeneratingBid) -> Self:
        return StartUpCostCurve.generating_bid.add(self, generating_bid)

    def remove_generating_bid(self, generating_bid: GeneratingBid) -> Self:
        return StartUpCostCurve.generating_bid.remove(self, generating_bid)

    def clear_generating_bid(self) -> Self:
        return StartUpCostCurve.generating_bid.clear(self)

    def num_generating_bid(self) -> int:
        return StartUpCostCurve.generating_bid.count(self)

    def get_generating_bid_by_mrid(self, mrid: str) -> GeneratingBid | None:
        return StartUpCostCurve.generating_bid.get_by_mrid(self, mrid)

    def add_registered_generator(self, registered_generator: RegisteredGenerator) -> Self:
        return StartUpCostCurve.registered_generators.add(self, registered_generator)

    def remove_registered_generator(self, registered_generator: RegisteredGenerator) -> Self:
        return StartUpCostCurve.registered_generators.remove(self, registered_generator)

    def clear_registered_generators(self) -> Self:
        return StartUpCostCurve.registered_generators.clear(self)

    def num_registered_generator(self) -> int:
        return StartUpCostCurve.registered_generators.count(self)

    def get_registered_generator_by_mrid(self, mrid: str) -> RegisteredGenerator | None:
        return StartUpCostCurve.registered_generators.get_by_mrid(self, mrid)
