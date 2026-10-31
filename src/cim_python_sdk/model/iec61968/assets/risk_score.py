"""CIM class RiskScore (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.aggregate_score import AggregateScore

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.health_score import HealthScore
    from cim_python_sdk.model.iec61968.assets.risk_score_kind import RiskScoreKind


class RiskScore(AggregateScore):
    """Score that is indicative of the risk associated with one or more assets."""

    __slots__ = ("_asset_health_score", "kind")

    kind: RiskScoreKind | None

    asset_health_score: Many[HealthScore] = Many(
        EndMeta(
            name="asset_health_score",
            cim_role="AssetHealthScore",
            target="cim_python_sdk.model.iec61968.assets.health_score:HealthScore",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_risk_score",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RiskScore",
        package="TC57CIM/IEC61968/Assets",
        guid="{72633FD4-C345-4b4b-B26D-88085BCB1973}",
        attributes=(AttrMeta("kind", "kind", "RiskScoreKind", 0, 1, "enumeration"),),
        ends=(asset_health_score.meta,),
    )

    def __init__(
        self,
        *,
        kind: RiskScoreKind | None = None,
        asset_health_score: Iterable[HealthScore] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if asset_health_score is not None:
            RiskScore.asset_health_score.extend(self, asset_health_score)

    def add_asset_health_score(self, asset_health_score: HealthScore) -> Self:
        return RiskScore.asset_health_score.add(self, asset_health_score)

    def remove_asset_health_score(self, asset_health_score: HealthScore) -> Self:
        return RiskScore.asset_health_score.remove(self, asset_health_score)

    def clear_asset_health_score(self) -> Self:
        return RiskScore.asset_health_score.clear(self)

    def num_asset_health_score(self) -> int:
        return RiskScore.asset_health_score.count(self)

    def get_asset_health_score_by_mrid(self, mrid: str) -> HealthScore | None:
        return RiskScore.asset_health_score.get_by_mrid(self, mrid)
