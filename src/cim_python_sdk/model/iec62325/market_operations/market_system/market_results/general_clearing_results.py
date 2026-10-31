"""CIM class GeneralClearingResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.general_clearing import (
        GeneralClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class GeneralClearingResults(CimObject):
    """Provides the adjusted load forecast value on a load forecast zone basis."""

    __slots__ = (
        "_general_clearing",
        "_sub_control_area",
        "load_forecast",
        "total_load",
        "total_net_interchange",
    )

    load_forecast: float | None  # ActivePower
    total_load: float | None
    total_net_interchange: float | None

    sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="sub_control_area",
            cim_role="SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="general_clearing_results",
            aggregation="none",
        )
    )
    general_clearing: One[GeneralClearing] = One(
        EndMeta(
            name="general_clearing",
            cim_role="GeneralClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.general_clearing:GeneralClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="general_clearing_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GeneralClearingResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{221DD6A3-C3E6-4218-BBD9-4F0A30A232FF}",
        attributes=(
            AttrMeta("load_forecast", "loadForecast", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("total_load", "totalLoad", "float", 0, 1, "primitive"),
            AttrMeta("total_net_interchange", "totalNetInterchange", "float", 0, 1, "primitive"),
        ),
        ends=(
            sub_control_area.meta,
            general_clearing.meta,
        ),
    )

    def __init__(
        self,
        *,
        load_forecast: float | None = None,
        total_load: float | None = None,
        total_net_interchange: float | None = None,
        sub_control_area: SubControlArea | None = None,
        general_clearing: GeneralClearing | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.load_forecast = load_forecast
        self.total_load = total_load
        self.total_net_interchange = total_net_interchange
        if sub_control_area is not None:
            self.sub_control_area = sub_control_area
        if general_clearing is not None:
            self.general_clearing = general_clearing
