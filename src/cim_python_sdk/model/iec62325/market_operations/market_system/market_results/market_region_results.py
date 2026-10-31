"""CIM class MarketRegionResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_product import (
        MarketProduct,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ancillary_service_clearing import (
        AncillaryServiceClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.resource_limit_indicator import (
        ResourceLimitIndicator,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.reference_data.market_region import (
        MarketRegion,
    )


class MarketRegionResults(CimObject):
    """Provides all Region Ancillary Service results for the DA and RT markets. The specific
    data is commodity type (Regulation Up, Regulation Down, Spinning Reserve, Non-spinning
    Reserve, or Total Up reserves) based for the cleared MW, cleared price, and total
    capacity required for the region."""

    __slots__ = (
        "_ancillary_service_clearing",
        "_market_product",
        "_market_region",
        "cleared_mw",
        "cleared_price",
        "dispatch_ct_mw",
        "dispatch_hydro_mw",
        "dispatch_rate",
        "dispatch_steam_mw",
        "imbalance_energy_bias",
        "limit_flag",
        "lumpy_indicator",
        "max_sufficiency_index",
        "min_sufficiency_index",
        "req_max_mw",
        "req_min_mw",
        "self_schedule_mw",
    )

    cleared_mw: float | None
    cleared_price: float | None
    dispatch_ct_mw: float | None
    dispatch_hydro_mw: float | None
    dispatch_rate: float | None
    dispatch_steam_mw: float | None
    imbalance_energy_bias: float | None
    limit_flag: ResourceLimitIndicator | None
    lumpy_indicator: YesNo | None
    max_sufficiency_index: float | None
    min_sufficiency_index: float | None
    req_max_mw: float | None
    req_min_mw: float | None
    self_schedule_mw: float | None

    market_region: One[MarketRegion] = One(
        EndMeta(
            name="market_region",
            cim_role="MarketRegion",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.market_region:MarketRegion",
            many=False,
            lower=1,
            upper=1,
            inverse="market_region_results",
            aggregation="none",
        )
    )
    market_product: One[MarketProduct] = One(
        EndMeta(
            name="market_product",
            cim_role="MarketProduct",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_product:MarketProduct",
            many=False,
            lower=0,
            upper=1,
            inverse="market_region_results",
            aggregation="none",
        )
    )
    ancillary_service_clearing: One[AncillaryServiceClearing] = One(
        EndMeta(
            name="ancillary_service_clearing",
            cim_role="AncillaryServiceClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ancillary_service_clearing:AncillaryServiceClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="market_region_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketRegionResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{1F94ED51-CDDB-48f7-85CB-407110E194EB}",
        attributes=(
            AttrMeta("cleared_mw", "clearedMW", "float", 0, 1, "primitive"),
            AttrMeta("cleared_price", "clearedPrice", "float", 0, 1, "primitive"),
            AttrMeta("dispatch_ct_mw", "dispatchCtMW", "float", 0, 1, "primitive"),
            AttrMeta("dispatch_hydro_mw", "dispatchHydroMW", "float", 0, 1, "primitive"),
            AttrMeta("dispatch_rate", "dispatchRate", "float", 0, 1, "primitive"),
            AttrMeta("dispatch_steam_mw", "dispatchSteamMW", "float", 0, 1, "primitive"),
            AttrMeta("imbalance_energy_bias", "imbalanceEnergyBias", "float", 0, 1, "primitive"),
            AttrMeta("limit_flag", "limitFlag", "ResourceLimitIndicator", 0, 1, "enumeration"),
            AttrMeta("lumpy_indicator", "lumpyIndicator", "YesNo", 0, 1, "enumeration"),
            AttrMeta("max_sufficiency_index", "maxSufficiencyIndex", "float", 0, 1, "primitive"),
            AttrMeta("min_sufficiency_index", "minSufficiencyIndex", "float", 0, 1, "primitive"),
            AttrMeta("req_max_mw", "reqMaxMW", "float", 0, 1, "primitive"),
            AttrMeta("req_min_mw", "reqMinMW", "float", 0, 1, "primitive"),
            AttrMeta("self_schedule_mw", "selfScheduleMW", "float", 0, 1, "primitive"),
        ),
        ends=(
            market_region.meta,
            market_product.meta,
            ancillary_service_clearing.meta,
        ),
    )

    def __init__(
        self,
        *,
        cleared_mw: float | None = None,
        cleared_price: float | None = None,
        dispatch_ct_mw: float | None = None,
        dispatch_hydro_mw: float | None = None,
        dispatch_rate: float | None = None,
        dispatch_steam_mw: float | None = None,
        imbalance_energy_bias: float | None = None,
        limit_flag: ResourceLimitIndicator | None = None,
        lumpy_indicator: YesNo | None = None,
        max_sufficiency_index: float | None = None,
        min_sufficiency_index: float | None = None,
        req_max_mw: float | None = None,
        req_min_mw: float | None = None,
        self_schedule_mw: float | None = None,
        market_region: MarketRegion | None = None,
        market_product: MarketProduct | None = None,
        ancillary_service_clearing: AncillaryServiceClearing | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cleared_mw = cleared_mw
        self.cleared_price = cleared_price
        self.dispatch_ct_mw = dispatch_ct_mw
        self.dispatch_hydro_mw = dispatch_hydro_mw
        self.dispatch_rate = dispatch_rate
        self.dispatch_steam_mw = dispatch_steam_mw
        self.imbalance_energy_bias = imbalance_energy_bias
        self.limit_flag = limit_flag
        self.lumpy_indicator = lumpy_indicator
        self.max_sufficiency_index = max_sufficiency_index
        self.min_sufficiency_index = min_sufficiency_index
        self.req_max_mw = req_max_mw
        self.req_min_mw = req_min_mw
        self.self_schedule_mw = self_schedule_mw
        if market_region is not None:
            self.market_region = market_region
        if market_product is not None:
            self.market_product = market_product
        if ancillary_service_clearing is not None:
            self.ancillary_service_clearing = ancillary_service_clearing
