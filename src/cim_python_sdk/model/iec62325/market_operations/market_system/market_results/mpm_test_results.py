"""CIM class MPMTestResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_clearing import (
        MPMClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mpm_test_outcome import (
        MPMTestOutcome,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode import (
        AggregatedPnode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mpm_test_category import (
        MPMTestCategory,
    )


class MPMTestResults(CimObject):
    """Provides the outcome and margin percent (as appropriate) result data for the MPM tests.
    There are relationships to Zone for Designated Congestion Area Tests, CurveSchedData for
    bid segment tests, to the SubControlArea for the system wide level tests, and Pnodes for
    the LMPM impact tests."""

    __slots__ = (
        "_aggregated_pnode",
        "_mpm_clearing",
        "_mpm_test_category",
        "margin_percent",
        "outcome",
    )

    outcome: MPMTestOutcome | None
    margin_percent: float | None  # PerCent

    mpm_clearing: One[MPMClearing] = One(
        EndMeta(
            name="mpm_clearing",
            cim_role="MPMClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_clearing:MPMClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="mpm_test_results",
            aggregation="none",
        )
    )
    mpm_test_category: One[MPMTestCategory] = One(
        EndMeta(
            name="mpm_test_category",
            cim_role="MPMTestCategory",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mpm_test_category:MPMTestCategory",
            many=False,
            lower=1,
            upper=1,
            inverse="mpm_test_results",
            aggregation="none",
        )
    )
    aggregated_pnode: One[AggregatedPnode] = One(
        EndMeta(
            name="aggregated_pnode",
            cim_role="AggregatedPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode:AggregatedPnode",
            many=False,
            lower=1,
            upper=1,
            inverse="mpm_test_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MPMTestResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{CF50DDD1-6FF8-4e5f-8C6E-0990AFCE6C9B}",
        attributes=(
            AttrMeta("outcome", "outcome", "MPMTestOutcome", 0, 1, "enumeration"),
            AttrMeta("margin_percent", "marginPercent", "PerCent", 0, 1, "cimdatatype"),
        ),
        ends=(
            mpm_clearing.meta,
            mpm_test_category.meta,
            aggregated_pnode.meta,
        ),
    )

    def __init__(
        self,
        *,
        outcome: MPMTestOutcome | None = None,
        margin_percent: float | None = None,
        mpm_clearing: MPMClearing | None = None,
        mpm_test_category: MPMTestCategory | None = None,
        aggregated_pnode: AggregatedPnode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.outcome = outcome
        self.margin_percent = margin_percent
        if mpm_clearing is not None:
            self.mpm_clearing = mpm_clearing
        if mpm_test_category is not None:
            self.mpm_test_category = mpm_test_category
        if aggregated_pnode is not None:
            self.aggregated_pnode = aggregated_pnode
