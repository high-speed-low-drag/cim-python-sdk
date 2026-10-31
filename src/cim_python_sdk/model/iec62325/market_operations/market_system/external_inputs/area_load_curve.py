"""CIM class AreaLoadCurve (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.load_forecast_type import (
        LoadForecastType,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node import (
        AggregateNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.tac_area import TACArea


class AreaLoadCurve(RegularIntervalSchedule):
    """Area load curve definition."""

    __slots__ = ("_aggregate_node", "_tac_area", "forecast_type")

    forecast_type: LoadForecastType | None

    tac_area: One[TACArea] = One(
        EndMeta(
            name="tac_area",
            cim_role="TACArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.tac_area:TACArea",
            many=False,
            lower=0,
            upper=1,
            inverse="area_load_curve",
            aggregation="none",
        )
    )
    aggregate_node: One[AggregateNode] = One(
        EndMeta(
            name="aggregate_node",
            cim_role="AggregateNode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node:AggregateNode",
            many=False,
            lower=0,
            upper=1,
            inverse="area_load_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AreaLoadCurve",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{B75407FF-3F23-4159-B25E-8F0C6E9BDB1A}",
        attributes=(
            AttrMeta("forecast_type", "forecastType", "LoadForecastType", 0, 1, "enumeration"),
        ),
        ends=(
            tac_area.meta,
            aggregate_node.meta,
        ),
    )

    def __init__(
        self,
        *,
        forecast_type: LoadForecastType | None = None,
        tac_area: TACArea | None = None,
        aggregate_node: AggregateNode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.forecast_type = forecast_type
        if tac_area is not None:
            self.tac_area = tac_area
        if aggregate_node is not None:
            self.aggregate_node = aggregate_node
