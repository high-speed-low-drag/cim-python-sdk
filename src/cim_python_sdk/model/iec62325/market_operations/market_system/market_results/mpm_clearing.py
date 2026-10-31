"""CIM class MPMClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_test_results import (
        MPMTestResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class MPMClearing(MarketFactors):
    """Model of results of Market Power tests, and possible mitigation. Interval based."""

    __slots__ = (
        "_mpm_test_results",
        "lmpm_final_flag",
        "mitigation_occured_flag",
        "smpm_final_flag",
    )

    lmpm_final_flag: YesNo | None
    smpm_final_flag: YesNo | None
    mitigation_occured_flag: YesNo | None

    mpm_test_results: Many[MPMTestResults] = Many(
        EndMeta(
            name="mpm_test_results",
            cim_role="MPMTestResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_test_results:MPMTestResults",
            many=True,
            lower=0,
            upper=None,
            inverse="mpm_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MPMClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{D3251165-323E-4741-8CDB-9D20FB10A74F}",
        attributes=(
            AttrMeta("lmpm_final_flag", "LMPMFinalFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("smpm_final_flag", "SMPMFinalFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "mitigation_occured_flag", "mitigationOccuredFlag", "YesNo", 0, 1, "enumeration"
            ),
        ),
        ends=(mpm_test_results.meta,),
    )

    def __init__(
        self,
        *,
        lmpm_final_flag: YesNo | None = None,
        smpm_final_flag: YesNo | None = None,
        mitigation_occured_flag: YesNo | None = None,
        mpm_test_results: Iterable[MPMTestResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.lmpm_final_flag = lmpm_final_flag
        self.smpm_final_flag = smpm_final_flag
        self.mitigation_occured_flag = mitigation_occured_flag
        if mpm_test_results is not None:
            MPMClearing.mpm_test_results.extend(self, mpm_test_results)

    def add_mpm_test_result(self, mpm_test_result: MPMTestResults) -> Self:
        return MPMClearing.mpm_test_results.add(self, mpm_test_result)

    def remove_mpm_test_result(self, mpm_test_result: MPMTestResults) -> Self:
        return MPMClearing.mpm_test_results.remove(self, mpm_test_result)

    def clear_mpm_test_results(self) -> Self:
        return MPMClearing.mpm_test_results.clear(self)

    def num_mpm_test_result(self) -> int:
        return MPMClearing.mpm_test_results.count(self)
