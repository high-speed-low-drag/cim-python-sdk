"""CIM class MktActivityRecord (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import (
        MarketFactors,
    )


class MktActivityRecord(ActivityRecord):
    """Subclass of IEC61968: Common:ActivityRecord."""

    __slots__ = ("_market_factors",)

    market_factors: Many[MarketFactors] = Many(
        EndMeta(
            name="market_factors",
            cim_role="MarketFactors",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors:MarketFactors",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_activity_record",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktActivityRecord",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{F3BA1ABB-530F-4267-843F-D65CBB609987}",
        ends=(market_factors.meta,),
    )

    def __init__(
        self,
        *,
        market_factors: Iterable[MarketFactors] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if market_factors is not None:
            MktActivityRecord.market_factors.extend(self, market_factors)

    def add_market_factor(self, market_factor: MarketFactors) -> Self:
        return MktActivityRecord.market_factors.add(self, market_factor)

    def remove_market_factor(self, market_factor: MarketFactors) -> Self:
        return MktActivityRecord.market_factors.remove(self, market_factor)

    def clear_market_factors(self) -> Self:
        return MktActivityRecord.market_factors.clear(self)

    def num_market_factor(self) -> int:
        return MktActivityRecord.market_factors.count(self)

    def get_market_factor_by_mrid(self, mrid: str) -> MarketFactors | None:
        return MktActivityRecord.market_factors.get_by_mrid(self, mrid)
