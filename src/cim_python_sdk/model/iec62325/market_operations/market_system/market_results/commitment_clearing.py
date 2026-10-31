"""CIM class CommitmentClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commitments import (
        Commitments,
    )


class CommitmentClearing(MarketFactors):
    """Models results of market clearing which call for commitment of units."""

    __slots__ = ("_commitments",)

    commitments: Many[Commitments] = Many(
        EndMeta(
            name="commitments",
            cim_role="Commitments",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commitments:Commitments",
            many=True,
            lower=1,
            upper=None,
            inverse="commitment_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CommitmentClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{05332947-266B-420b-ADCC-A18F03233938}",
        ends=(commitments.meta,),
    )

    def __init__(
        self,
        *,
        commitments: Iterable[Commitments] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if commitments is not None:
            CommitmentClearing.commitments.extend(self, commitments)

    def add_commitment(self, commitment: Commitments) -> Self:
        return CommitmentClearing.commitments.add(self, commitment)

    def remove_commitment(self, commitment: Commitments) -> Self:
        return CommitmentClearing.commitments.remove(self, commitment)

    def clear_commitments(self) -> Self:
        return CommitmentClearing.commitments.clear(self)

    def num_commitment(self) -> int:
        return CommitmentClearing.commitments.count(self)
