"""CIM class AuxiliaryValues (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_object import (
    AuxiliaryObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_cost import (
        AuxiliaryCost,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.five_min_auxiliary_data import (
        FiveMinAuxiliaryData,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.ten_min_auxiliary_data import (
        TenMinAuxiliaryData,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class AuxiliaryValues(AuxiliaryObject):
    """Models Auxiliary Values."""

    __slots__ = (
        "_auxillary_cost",
        "_five_min_auxillary_data",
        "_ten_min_auxillary_data",
        "avail_undispatched_q",
        "incremental_or_avail",
        "max_expost_capacity",
        "min_expost_capacity",
        "no_load_cost",
        "no_load_cost_eligibility_flag",
        "start_up_cost",
        "start_up_cost_eligibility_flag",
    )

    min_expost_capacity: float | None
    max_expost_capacity: float | None
    avail_undispatched_q: float | None
    incremental_or_avail: float | None
    start_up_cost: float | None
    start_up_cost_eligibility_flag: YesNo | None
    no_load_cost: float | None
    no_load_cost_eligibility_flag: YesNo | None

    five_min_auxillary_data: One[FiveMinAuxiliaryData] = One(
        EndMeta(
            name="five_min_auxillary_data",
            cim_role="FiveMinAuxillaryData",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.five_min_auxiliary_data:FiveMinAuxiliaryData",
            many=False,
            lower=1,
            upper=1,
            inverse="auxillary_values",
            aggregation="none",
        )
    )
    auxillary_cost: One[AuxiliaryCost] = One(
        EndMeta(
            name="auxillary_cost",
            cim_role="AuxillaryCost",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_cost:AuxiliaryCost",
            many=False,
            lower=1,
            upper=1,
            inverse="auxillary_values",
            aggregation="none",
        )
    )
    ten_min_auxillary_data: One[TenMinAuxiliaryData] = One(
        EndMeta(
            name="ten_min_auxillary_data",
            cim_role="TenMinAuxillaryData",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.ten_min_auxiliary_data:TenMinAuxiliaryData",
            many=False,
            lower=1,
            upper=1,
            inverse="auxillary_data",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AuxiliaryValues",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{73B1200C-1488-4b81-8B29-743FC0FD6A59}",
        attributes=(
            AttrMeta("min_expost_capacity", "minExpostCapacity", "float", 0, 1, "primitive"),
            AttrMeta("max_expost_capacity", "maxExpostCapacity", "float", 0, 1, "primitive"),
            AttrMeta("avail_undispatched_q", "availUndispatchedQ", "float", 0, 1, "primitive"),
            AttrMeta("incremental_or_avail", "incrementalORAvail", "float", 0, 1, "primitive"),
            AttrMeta("start_up_cost", "startUpCost", "float", 0, 1, "primitive"),
            AttrMeta(
                "start_up_cost_eligibility_flag",
                "startUpCostEligibilityFlag",
                "YesNo",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("no_load_cost", "noLoadCost", "float", 0, 1, "primitive"),
            AttrMeta(
                "no_load_cost_eligibility_flag",
                "noLoadCostEligibilityFlag",
                "YesNo",
                0,
                1,
                "enumeration",
            ),
        ),
        ends=(
            five_min_auxillary_data.meta,
            auxillary_cost.meta,
            ten_min_auxillary_data.meta,
        ),
    )

    def __init__(
        self,
        *,
        min_expost_capacity: float | None = None,
        max_expost_capacity: float | None = None,
        avail_undispatched_q: float | None = None,
        incremental_or_avail: float | None = None,
        start_up_cost: float | None = None,
        start_up_cost_eligibility_flag: YesNo | None = None,
        no_load_cost: float | None = None,
        no_load_cost_eligibility_flag: YesNo | None = None,
        five_min_auxillary_data: FiveMinAuxiliaryData | None = None,
        auxillary_cost: AuxiliaryCost | None = None,
        ten_min_auxillary_data: TenMinAuxiliaryData | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.min_expost_capacity = min_expost_capacity
        self.max_expost_capacity = max_expost_capacity
        self.avail_undispatched_q = avail_undispatched_q
        self.incremental_or_avail = incremental_or_avail
        self.start_up_cost = start_up_cost
        self.start_up_cost_eligibility_flag = start_up_cost_eligibility_flag
        self.no_load_cost = no_load_cost
        self.no_load_cost_eligibility_flag = no_load_cost_eligibility_flag
        if five_min_auxillary_data is not None:
            self.five_min_auxillary_data = five_min_auxillary_data
        if auxillary_cost is not None:
            self.auxillary_cost = auxillary_cost
        if ten_min_auxillary_data is not None:
            self.ten_min_auxillary_data = ten_min_auxillary_data
