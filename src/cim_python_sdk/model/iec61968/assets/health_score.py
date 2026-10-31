"""CIM class HealthScore (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.assets.aggregate_score import AggregateScore

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.risk_score import RiskScore


class HealthScore(AggregateScore):
    """Score that is indicative of the health of one or more assets."""

    __slots__ = ("_asset_risk_score",)

    asset_risk_score: One[RiskScore] = One(
        EndMeta(
            name="asset_risk_score",
            cim_role="AssetRiskScore",
            target="cim_python_sdk.model.iec61968.assets.risk_score:RiskScore",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_health_score",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HealthScore",
        package="TC57CIM/IEC61968/Assets",
        guid="{E0135417-A3CC-4e66-AE7D-C1643FCC1E8C}",
        ends=(asset_risk_score.meta,),
    )

    def __init__(
        self,
        *,
        asset_risk_score: RiskScore | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if asset_risk_score is not None:
            self.asset_risk_score = asset_risk_score
