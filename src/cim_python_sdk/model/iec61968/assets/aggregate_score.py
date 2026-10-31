"""CIM class AggregateScore (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.analytic_score import AnalyticScore

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self


class AggregateScore(AnalyticScore):
    """An aggregated indicative scoring by an analytic, which is based on other analytic
    scores, that can be used to characterize the health of or the risk associated with one
    or more assets."""

    __slots__ = ("_analytic_score",)

    analytic_score: Many[AnalyticScore] = Many(
        EndMeta(
            name="analytic_score",
            cim_role="AnalyticScore",
            target="cim_python_sdk.model.iec61968.assets.analytic_score:AnalyticScore",
            many=True,
            lower=1,
            upper=None,
            inverse="asset_aggregate_score",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AggregateScore",
        package="TC57CIM/IEC61968/Assets",
        guid="{BFA64B46-A4E4-424e-BCB9-67BA79DC21DE}",
        ends=(analytic_score.meta,),
    )

    def __init__(
        self,
        *,
        analytic_score: Iterable[AnalyticScore] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if analytic_score is not None:
            AggregateScore.analytic_score.extend(self, analytic_score)

    def add_analytic_score(self, analytic_score: AnalyticScore) -> Self:
        return AggregateScore.analytic_score.add(self, analytic_score)

    def remove_analytic_score(self, analytic_score: AnalyticScore) -> Self:
        return AggregateScore.analytic_score.remove(self, analytic_score)

    def clear_analytic_score(self) -> Self:
        return AggregateScore.analytic_score.clear(self)

    def num_analytic_score(self) -> int:
        return AggregateScore.analytic_score.count(self)

    def get_analytic_score_by_mrid(self, mrid: str) -> AnalyticScore | None:
        return AggregateScore.analytic_score.get_by_mrid(self, mrid)
