"""CIM class MPMTestCategory (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_resource_status import (
        MPMResourceStatus,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_test_results import (
        MPMTestResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mpm_test_identifier_type import (
        MPMTestIdentifierType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mpm_test_method_type import (
        MPMTestMethodType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.purpose_flag_type import (
        PurposeFlagType,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mpm_test_threshold import (
        MPMTestThreshold,
    )


class MPMTestCategory(IdentifiedObject):
    """Provides a reference to the Market Power Mitigation test identifiers and methods for the
    results of the DA or RT markets. Specific data is the test identifier (Price, Conduct,
    or Impact) and the test method (System MPM, Local MPM, Alternate System MPM, or
    Alternate Local MPM)."""

    __slots__ = (
        "_mpm_resource_status",
        "_mpm_test_results",
        "_mpm_test_threshold",
        "purpose_flag",
        "test_identifier",
        "test_method",
    )

    test_identifier: MPMTestIdentifierType | None
    test_method: MPMTestMethodType | None
    purpose_flag: PurposeFlagType | None

    mpm_test_threshold: Many[MPMTestThreshold] = Many(
        EndMeta(
            name="mpm_test_threshold",
            cim_role="MPMTestThreshold",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mpm_test_threshold:MPMTestThreshold",
            many=True,
            lower=0,
            upper=None,
            inverse="mpm_test_category",
            aggregation="none",
        )
    )
    mpm_test_results: Many[MPMTestResults] = Many(
        EndMeta(
            name="mpm_test_results",
            cim_role="MPMTestResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_test_results:MPMTestResults",
            many=True,
            lower=0,
            upper=None,
            inverse="mpm_test_category",
            aggregation="none",
        )
    )
    mpm_resource_status: Many[MPMResourceStatus] = Many(
        EndMeta(
            name="mpm_resource_status",
            cim_role="MPMResourceStatus",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_resource_status:MPMResourceStatus",
            many=True,
            lower=0,
            upper=None,
            inverse="mpm_test_category",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MPMTestCategory",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{1C74B6FD-241F-4d4f-9281-DD92367C23D9}",
        attributes=(
            AttrMeta(
                "test_identifier", "testIdentifier", "MPMTestIdentifierType", 0, 1, "enumeration"
            ),
            AttrMeta("test_method", "testMethod", "MPMTestMethodType", 0, 1, "enumeration"),
            AttrMeta("purpose_flag", "purposeFlag", "PurposeFlagType", 0, 1, "enumeration"),
        ),
        ends=(
            mpm_test_threshold.meta,
            mpm_test_results.meta,
            mpm_resource_status.meta,
        ),
    )

    def __init__(
        self,
        *,
        test_identifier: MPMTestIdentifierType | None = None,
        test_method: MPMTestMethodType | None = None,
        purpose_flag: PurposeFlagType | None = None,
        mpm_test_threshold: Iterable[MPMTestThreshold] | None = None,
        mpm_test_results: Iterable[MPMTestResults] | None = None,
        mpm_resource_status: Iterable[MPMResourceStatus] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.test_identifier = test_identifier
        self.test_method = test_method
        self.purpose_flag = purpose_flag
        if mpm_test_threshold is not None:
            MPMTestCategory.mpm_test_threshold.extend(self, mpm_test_threshold)
        if mpm_test_results is not None:
            MPMTestCategory.mpm_test_results.extend(self, mpm_test_results)
        if mpm_resource_status is not None:
            MPMTestCategory.mpm_resource_status.extend(self, mpm_resource_status)

    def add_mpm_test_threshold(self, mpm_test_threshold: MPMTestThreshold) -> Self:
        return MPMTestCategory.mpm_test_threshold.add(self, mpm_test_threshold)

    def remove_mpm_test_threshold(self, mpm_test_threshold: MPMTestThreshold) -> Self:
        return MPMTestCategory.mpm_test_threshold.remove(self, mpm_test_threshold)

    def clear_mpm_test_threshold(self) -> Self:
        return MPMTestCategory.mpm_test_threshold.clear(self)

    def num_mpm_test_threshold(self) -> int:
        return MPMTestCategory.mpm_test_threshold.count(self)

    def add_mpm_test_result(self, mpm_test_result: MPMTestResults) -> Self:
        return MPMTestCategory.mpm_test_results.add(self, mpm_test_result)

    def remove_mpm_test_result(self, mpm_test_result: MPMTestResults) -> Self:
        return MPMTestCategory.mpm_test_results.remove(self, mpm_test_result)

    def clear_mpm_test_results(self) -> Self:
        return MPMTestCategory.mpm_test_results.clear(self)

    def num_mpm_test_result(self) -> int:
        return MPMTestCategory.mpm_test_results.count(self)

    def add_mpm_resource_status(self, mpm_resource_status: MPMResourceStatus) -> Self:
        return MPMTestCategory.mpm_resource_status.add(self, mpm_resource_status)

    def remove_mpm_resource_status(self, mpm_resource_status: MPMResourceStatus) -> Self:
        return MPMTestCategory.mpm_resource_status.remove(self, mpm_resource_status)

    def clear_mpm_resource_status(self) -> Self:
        return MPMTestCategory.mpm_resource_status.clear(self)

    def num_mpm_resource_status(self) -> int:
        return MPMTestCategory.mpm_resource_status.count(self)
