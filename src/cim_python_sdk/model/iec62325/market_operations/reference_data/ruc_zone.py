"""CIM class RUCZone (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node import (
    AggregateNode,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.loss_clearing_results import (
        LossClearingResults,
    )


class RUCZone(AggregateNode):
    """A specialized class of type AggregatedNode type. Defines RUC Zones. A forecast region
    represents a collection of Nodes for which the Market operator has developed sufficient
    historical demand and relevant weather data to perform a demand forecast for such area.
    The Market Operator may further adjust this forecast to ensure that the Reliability Unit
    Commitment produces adequate local capacity procurement."""

    __slots__ = ("_loss_clearing_results",)

    loss_clearing_results: Many[LossClearingResults] = Many(
        EndMeta(
            name="loss_clearing_results",
            cim_role="LossClearingResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.loss_clearing_results:LossClearingResults",
            many=True,
            lower=0,
            upper=None,
            inverse="ruc_zone",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RUCZone",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{CEF61B01-E182-415c-836A-9423A9A98BAD}",
        ends=(loss_clearing_results.meta,),
    )

    def __init__(
        self,
        *,
        loss_clearing_results: Iterable[LossClearingResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if loss_clearing_results is not None:
            RUCZone.loss_clearing_results.extend(self, loss_clearing_results)

    def add_loss_clearing_result(self, loss_clearing_result: LossClearingResults) -> Self:
        return RUCZone.loss_clearing_results.add(self, loss_clearing_result)

    def remove_loss_clearing_result(self, loss_clearing_result: LossClearingResults) -> Self:
        return RUCZone.loss_clearing_results.remove(self, loss_clearing_result)

    def clear_loss_clearing_results(self) -> Self:
        return RUCZone.loss_clearing_results.clear(self)

    def num_loss_clearing_result(self) -> int:
        return RUCZone.loss_clearing_results.count(self)
