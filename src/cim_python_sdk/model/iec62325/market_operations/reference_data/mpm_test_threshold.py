"""CIM class MPMTestThreshold (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode import (
        AggregatedPnode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mpm_test_category import (
        MPMTestCategory,
    )


class MPMTestThreshold(CimObject):
    """Market Power Mitigation (MPM) test thresholds for resource as well as designated
    congestion areas (DCAs)."""

    __slots__ = (
        "_aggregated_pnode",
        "_mpm_test_category",
        "_registered_resource",
        "market_type",
        "percent",
        "price",
    )

    price: float | None  # CostPerEnergyUnit
    percent: float | None  # PerCent
    market_type: MarketType | None

    aggregated_pnode: Many[AggregatedPnode] = Many(
        EndMeta(
            name="aggregated_pnode",
            cim_role="AggregatedPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode:AggregatedPnode",
            many=True,
            lower=0,
            upper=None,
            inverse="mpm_test_threshold",
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
            inverse="mpm_test_threshold",
            aggregation="none",
        )
    )
    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="mpm_test_threshold",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MPMTestThreshold",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{B33BA46E-DC3B-4b67-BE55-EEDDE0B2DFAC}",
        attributes=(
            AttrMeta("price", "price", "CostPerEnergyUnit", 0, 1, "cimdatatype"),
            AttrMeta("percent", "percent", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
        ),
        ends=(
            aggregated_pnode.meta,
            mpm_test_category.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        price: float | None = None,
        percent: float | None = None,
        market_type: MarketType | None = None,
        aggregated_pnode: Iterable[AggregatedPnode] | None = None,
        mpm_test_category: MPMTestCategory | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.price = price
        self.percent = percent
        self.market_type = market_type
        if aggregated_pnode is not None:
            MPMTestThreshold.aggregated_pnode.extend(self, aggregated_pnode)
        if mpm_test_category is not None:
            self.mpm_test_category = mpm_test_category
        if registered_resource is not None:
            MPMTestThreshold.registered_resource.extend(self, registered_resource)

    def add_aggregated_pnode(self, aggregated_pnode: AggregatedPnode) -> Self:
        return MPMTestThreshold.aggregated_pnode.add(self, aggregated_pnode)

    def remove_aggregated_pnode(self, aggregated_pnode: AggregatedPnode) -> Self:
        return MPMTestThreshold.aggregated_pnode.remove(self, aggregated_pnode)

    def clear_aggregated_pnode(self) -> Self:
        return MPMTestThreshold.aggregated_pnode.clear(self)

    def num_aggregated_pnode(self) -> int:
        return MPMTestThreshold.aggregated_pnode.count(self)

    def get_aggregated_pnode_by_mrid(self, mrid: str) -> AggregatedPnode | None:
        return MPMTestThreshold.aggregated_pnode.get_by_mrid(self, mrid)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return MPMTestThreshold.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return MPMTestThreshold.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return MPMTestThreshold.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return MPMTestThreshold.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return MPMTestThreshold.registered_resource.get_by_mrid(self, mrid)
