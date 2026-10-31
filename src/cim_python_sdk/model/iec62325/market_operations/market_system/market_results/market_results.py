"""CIM class MarketResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_plan.energy_market import (
        EnergyMarket,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class MarketResults(CimObject):
    """This class holds elements that are single values for the entire market time horizon.
    That is, for the Day Ahead market, there is 1 value for each element, not hourly based.
    Is a summary of the market run."""

    __slots__ = (
        "_energy_market",
        "ancillary_svc_cost",
        "contingent_operating_res_avail",
        "energy_cost",
        "minimum_load_cost",
        "start_up_cost",
        "total_cost",
        "total_ruc_cost",
    )

    start_up_cost: float | None
    minimum_load_cost: float | None
    contingent_operating_res_avail: YesNo | None
    energy_cost: float | None
    total_cost: float | None
    ancillary_svc_cost: float | None
    total_ruc_cost: float | None

    energy_market: One[EnergyMarket] = One(
        EndMeta(
            name="energy_market",
            cim_role="EnergyMarket",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.energy_market:EnergyMarket",
            many=False,
            lower=1,
            upper=1,
            inverse="market_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{DBD013BA-5C9D-4450-8A6F-1551BE77FC75}",
        attributes=(
            AttrMeta("start_up_cost", "startUpCost", "float", 0, 1, "primitive"),
            AttrMeta("minimum_load_cost", "minimumLoadCost", "float", 0, 1, "primitive"),
            AttrMeta(
                "contingent_operating_res_avail",
                "contingentOperatingResAvail",
                "YesNo",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("energy_cost", "energyCost", "float", 0, 1, "primitive"),
            AttrMeta("total_cost", "totalCost", "float", 0, 1, "primitive"),
            AttrMeta("ancillary_svc_cost", "ancillarySvcCost", "float", 0, 1, "primitive"),
            AttrMeta("total_ruc_cost", "totalRucCost", "float", 0, 1, "primitive"),
        ),
        ends=(energy_market.meta,),
    )

    def __init__(
        self,
        *,
        start_up_cost: float | None = None,
        minimum_load_cost: float | None = None,
        contingent_operating_res_avail: YesNo | None = None,
        energy_cost: float | None = None,
        total_cost: float | None = None,
        ancillary_svc_cost: float | None = None,
        total_ruc_cost: float | None = None,
        energy_market: EnergyMarket | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.start_up_cost = start_up_cost
        self.minimum_load_cost = minimum_load_cost
        self.contingent_operating_res_avail = contingent_operating_res_avail
        self.energy_cost = energy_cost
        self.total_cost = total_cost
        self.ancillary_svc_cost = ancillary_svc_cost
        self.total_ruc_cost = total_ruc_cost
        if energy_market is not None:
            self.energy_market = energy_market
