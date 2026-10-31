"""CIM class AssetGroup (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.analytic import Analytic
    from cim_python_sdk.model.iec61968.assets.analytic_score import AnalyticScore
    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.asset_group_kind import AssetGroupKind


class AssetGroup(Document):
    """A grouping of assets created for a purpose such as fleet analytics, inventory or
    compliance management."""

    __slots__ = ("_analytic", "_analytic_score", "_asset", "kind")

    kind: AssetGroupKind | None

    analytic_score: Many[AnalyticScore] = Many(
        EndMeta(
            name="analytic_score",
            cim_role="AnalyticScore",
            target="cim_python_sdk.model.iec61968.assets.analytic_score:AnalyticScore",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_group",
            aggregation="none",
        )
    )
    asset: Many[Asset] = Many(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_group",
            aggregation="none",
        )
    )
    analytic: Many[Analytic] = Many(
        EndMeta(
            name="analytic",
            cim_role="Analytic",
            target="cim_python_sdk.model.iec61968.assets.analytic:Analytic",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetGroup",
        package="TC57CIM/IEC61968/Assets",
        guid="{D12CA3E8-532D-46df-A804-131A56F3E56E}",
        attributes=(AttrMeta("kind", "kind", "AssetGroupKind", 1, 1, "enumeration"),),
        ends=(
            analytic_score.meta,
            asset.meta,
            analytic.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: AssetGroupKind | None = None,
        analytic_score: Iterable[AnalyticScore] | None = None,
        asset: Iterable[Asset] | None = None,
        analytic: Iterable[Analytic] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if analytic_score is not None:
            AssetGroup.analytic_score.extend(self, analytic_score)
        if asset is not None:
            AssetGroup.asset.extend(self, asset)
        if analytic is not None:
            AssetGroup.analytic.extend(self, analytic)

    def add_analytic_score(self, analytic_score: AnalyticScore) -> Self:
        return AssetGroup.analytic_score.add(self, analytic_score)

    def remove_analytic_score(self, analytic_score: AnalyticScore) -> Self:
        return AssetGroup.analytic_score.remove(self, analytic_score)

    def clear_analytic_score(self) -> Self:
        return AssetGroup.analytic_score.clear(self)

    def num_analytic_score(self) -> int:
        return AssetGroup.analytic_score.count(self)

    def get_analytic_score_by_mrid(self, mrid: str) -> AnalyticScore | None:
        return AssetGroup.analytic_score.get_by_mrid(self, mrid)

    def add_asset(self, asset: Asset) -> Self:
        return AssetGroup.asset.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return AssetGroup.asset.remove(self, asset)

    def clear_asset(self) -> Self:
        return AssetGroup.asset.clear(self)

    def num_asset(self) -> int:
        return AssetGroup.asset.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return AssetGroup.asset.get_by_mrid(self, mrid)

    def add_analytic(self, analytic: Analytic) -> Self:
        return AssetGroup.analytic.add(self, analytic)

    def remove_analytic(self, analytic: Analytic) -> Self:
        return AssetGroup.analytic.remove(self, analytic)

    def clear_analytic(self) -> Self:
        return AssetGroup.analytic.clear(self)

    def num_analytic(self) -> int:
        return AssetGroup.analytic.count(self)

    def get_analytic_by_mrid(self, mrid: str) -> Analytic | None:
        return AssetGroup.analytic.get_by_mrid(self, mrid)
