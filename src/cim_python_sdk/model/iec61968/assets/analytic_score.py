"""CIM class AnalyticScore (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.aggregate_score import AggregateScore
    from cim_python_sdk.model.iec61968.assets.analytic import Analytic
    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.asset_group import AssetGroup


class AnalyticScore(IdentifiedObject):
    """An indicative scoring by an analytic that can be used to characterize the health of or
    the risk associated with one or more assets. The analytic score reflects the results of
    an execution of an analytic against an asset or group of assets."""

    __slots__ = (
        "_analytic",
        "_asset",
        "_asset_aggregate_score",
        "_asset_group",
        "calculation_date_time",
        "effective_date_time",
        "value",
    )

    value: float | None
    calculation_date_time: _dt.datetime | None
    effective_date_time: _dt.datetime | None

    asset_aggregate_score: One[AggregateScore] = One(
        EndMeta(
            name="asset_aggregate_score",
            cim_role="AssetAggregateScore",
            target="cim_python_sdk.model.iec61968.assets.aggregate_score:AggregateScore",
            many=False,
            lower=0,
            upper=1,
            inverse="analytic_score",
            aggregation="none",
        )
    )
    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="analytic_score",
            aggregation="none",
        )
    )
    analytic: One[Analytic] = One(
        EndMeta(
            name="analytic",
            cim_role="Analytic",
            target="cim_python_sdk.model.iec61968.assets.analytic:Analytic",
            many=False,
            lower=0,
            upper=1,
            inverse="analytic_score",
            aggregation="none",
        )
    )
    asset_group: One[AssetGroup] = One(
        EndMeta(
            name="asset_group",
            cim_role="AssetGroup",
            target="cim_python_sdk.model.iec61968.assets.asset_group:AssetGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="analytic_score",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AnalyticScore",
        package="TC57CIM/IEC61968/Assets",
        guid="{F9FCF4BF-9DF2-47db-9FD7-608D02E3F3C8}",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("calculation_date_time", "calculationDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("effective_date_time", "effectiveDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            asset_aggregate_score.meta,
            asset.meta,
            analytic.meta,
            asset_group.meta,
        ),
    )

    def __init__(
        self,
        *,
        value: float | None = None,
        calculation_date_time: _dt.datetime | None = None,
        effective_date_time: _dt.datetime | None = None,
        asset_aggregate_score: AggregateScore | None = None,
        asset: Asset | None = None,
        analytic: Analytic | None = None,
        asset_group: AssetGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
        self.calculation_date_time = calculation_date_time
        self.effective_date_time = effective_date_time
        if asset_aggregate_score is not None:
            self.asset_aggregate_score = asset_aggregate_score
        if asset is not None:
            self.asset = asset
        if analytic is not None:
            self.analytic = analytic
        if asset_group is not None:
            self.asset_group = asset_group
