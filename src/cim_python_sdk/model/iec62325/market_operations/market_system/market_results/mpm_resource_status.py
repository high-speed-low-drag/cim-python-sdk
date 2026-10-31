"""CIM class MPMResourceStatus (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mitigated_bid_clearing import (
        MitigatedBidClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mpm_test_category import (
        MPMTestCategory,
    )


class MPMResourceStatus(CimObject):
    """Model of results of Market Power tests, gives status of resource for the associated
    interval."""

    __slots__ = (
        "_mitigated_bid_clearing",
        "_mpm_test_category",
        "_registered_resource",
        "resource_status",
    )

    resource_status: str | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="mpm_resource_status",
            aggregation="none",
        )
    )
    mitigated_bid_clearing: Many[MitigatedBidClearing] = Many(
        EndMeta(
            name="mitigated_bid_clearing",
            cim_role="MitigatedBidClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mitigated_bid_clearing:MitigatedBidClearing",
            many=True,
            lower=1,
            upper=None,
            inverse="mpm_resource_status",
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
            inverse="mpm_resource_status",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MPMResourceStatus",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{7B63A03C-B965-4f27-B50E-CE3E077C0774}",
        attributes=(AttrMeta("resource_status", "resourceStatus", "str", 0, 1, "primitive"),),
        ends=(
            registered_resource.meta,
            mitigated_bid_clearing.meta,
            mpm_test_category.meta,
        ),
    )

    def __init__(
        self,
        *,
        resource_status: str | None = None,
        registered_resource: RegisteredResource | None = None,
        mitigated_bid_clearing: Iterable[MitigatedBidClearing] | None = None,
        mpm_test_category: MPMTestCategory | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.resource_status = resource_status
        if registered_resource is not None:
            self.registered_resource = registered_resource
        if mitigated_bid_clearing is not None:
            MPMResourceStatus.mitigated_bid_clearing.extend(self, mitigated_bid_clearing)
        if mpm_test_category is not None:
            self.mpm_test_category = mpm_test_category

    def add_mitigated_bid_clearing(self, mitigated_bid_clearing: MitigatedBidClearing) -> Self:
        return MPMResourceStatus.mitigated_bid_clearing.add(self, mitigated_bid_clearing)

    def remove_mitigated_bid_clearing(self, mitigated_bid_clearing: MitigatedBidClearing) -> Self:
        return MPMResourceStatus.mitigated_bid_clearing.remove(self, mitigated_bid_clearing)

    def clear_mitigated_bid_clearing(self) -> Self:
        return MPMResourceStatus.mitigated_bid_clearing.clear(self)

    def num_mitigated_bid_clearing(self) -> int:
        return MPMResourceStatus.mitigated_bid_clearing.count(self)

    def get_mitigated_bid_clearing_by_mrid(self, mrid: str) -> MitigatedBidClearing | None:
        return MPMResourceStatus.mitigated_bid_clearing.get_by_mrid(self, mrid)
