"""CIM class Analytic (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.analytic_kind import AnalyticKind
    from cim_python_sdk.model.iec61968.assets.analytic_score import AnalyticScore
    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.asset_group import AssetGroup
    from cim_python_sdk.model.iec61968.assets.asset_health_event import AssetHealthEvent
    from cim_python_sdk.model.iec61968.assets.scale_kind import ScaleKind


class Analytic(Document):
    """An algorithm or calculation for making an assessment about an asset or asset grouping
    for lifecycle decision making."""

    __slots__ = (
        "_analytic_score",
        "_asset",
        "_asset_group",
        "_asset_health_event",
        "best_value",
        "kind",
        "scale_kind",
        "worst_value",
    )

    kind: AnalyticKind | None
    best_value: float | None
    worst_value: float | None
    scale_kind: ScaleKind | None

    asset: Many[Asset] = Many(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="analytic",
            aggregation="none",
        )
    )
    analytic_score: Many[AnalyticScore] = Many(
        EndMeta(
            name="analytic_score",
            cim_role="AnalyticScore",
            target="cim_python_sdk.model.iec61968.assets.analytic_score:AnalyticScore",
            many=True,
            lower=0,
            upper=None,
            inverse="analytic",
            aggregation="none",
        )
    )
    asset_health_event: Many[AssetHealthEvent] = Many(
        EndMeta(
            name="asset_health_event",
            cim_role="AssetHealthEvent",
            target="cim_python_sdk.model.iec61968.assets.asset_health_event:AssetHealthEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="analytic",
            aggregation="none",
        )
    )
    asset_group: Many[AssetGroup] = Many(
        EndMeta(
            name="asset_group",
            cim_role="AssetGroup",
            target="cim_python_sdk.model.iec61968.assets.asset_group:AssetGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="analytic",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Analytic",
        package="TC57CIM/IEC61968/Assets",
        guid="{827A4D52-94DC-449b-BD6A-4F9BCAEAB145}",
        attributes=(
            AttrMeta("kind", "kind", "AnalyticKind", 1, 1, "enumeration"),
            AttrMeta("best_value", "bestValue", "float", 0, 1, "primitive"),
            AttrMeta("worst_value", "worstValue", "float", 0, 1, "primitive"),
            AttrMeta("scale_kind", "scaleKind", "ScaleKind", 0, 1, "enumeration"),
        ),
        ends=(
            asset.meta,
            analytic_score.meta,
            asset_health_event.meta,
            asset_group.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: AnalyticKind | None = None,
        best_value: float | None = None,
        worst_value: float | None = None,
        scale_kind: ScaleKind | None = None,
        asset: Iterable[Asset] | None = None,
        analytic_score: Iterable[AnalyticScore] | None = None,
        asset_health_event: Iterable[AssetHealthEvent] | None = None,
        asset_group: Iterable[AssetGroup] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.best_value = best_value
        self.worst_value = worst_value
        self.scale_kind = scale_kind
        if asset is not None:
            Analytic.asset.extend(self, asset)
        if analytic_score is not None:
            Analytic.analytic_score.extend(self, analytic_score)
        if asset_health_event is not None:
            Analytic.asset_health_event.extend(self, asset_health_event)
        if asset_group is not None:
            Analytic.asset_group.extend(self, asset_group)

    def add_asset(self, asset: Asset) -> Self:
        return Analytic.asset.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return Analytic.asset.remove(self, asset)

    def clear_asset(self) -> Self:
        return Analytic.asset.clear(self)

    def num_asset(self) -> int:
        return Analytic.asset.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return Analytic.asset.get_by_mrid(self, mrid)

    def add_analytic_score(self, analytic_score: AnalyticScore) -> Self:
        return Analytic.analytic_score.add(self, analytic_score)

    def remove_analytic_score(self, analytic_score: AnalyticScore) -> Self:
        return Analytic.analytic_score.remove(self, analytic_score)

    def clear_analytic_score(self) -> Self:
        return Analytic.analytic_score.clear(self)

    def num_analytic_score(self) -> int:
        return Analytic.analytic_score.count(self)

    def get_analytic_score_by_mrid(self, mrid: str) -> AnalyticScore | None:
        return Analytic.analytic_score.get_by_mrid(self, mrid)

    def add_asset_health_event(self, asset_health_event: AssetHealthEvent) -> Self:
        return Analytic.asset_health_event.add(self, asset_health_event)

    def remove_asset_health_event(self, asset_health_event: AssetHealthEvent) -> Self:
        return Analytic.asset_health_event.remove(self, asset_health_event)

    def clear_asset_health_event(self) -> Self:
        return Analytic.asset_health_event.clear(self)

    def num_asset_health_event(self) -> int:
        return Analytic.asset_health_event.count(self)

    def get_asset_health_event_by_mrid(self, mrid: str) -> AssetHealthEvent | None:
        return Analytic.asset_health_event.get_by_mrid(self, mrid)

    def add_asset_group(self, asset_group: AssetGroup) -> Self:
        return Analytic.asset_group.add(self, asset_group)

    def remove_asset_group(self, asset_group: AssetGroup) -> Self:
        return Analytic.asset_group.remove(self, asset_group)

    def clear_asset_group(self) -> Self:
        return Analytic.asset_group.clear(self)

    def num_asset_group(self) -> int:
        return Analytic.asset_group.count(self)

    def get_asset_group_by_mrid(self, mrid: str) -> AssetGroup | None:
        return Analytic.asset_group.get_by_mrid(self, mrid)
