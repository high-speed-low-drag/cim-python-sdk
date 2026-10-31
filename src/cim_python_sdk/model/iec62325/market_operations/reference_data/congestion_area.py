"""CIM class CongestionArea (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode import (
    AggregatedPnode,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.individual_pnode import (
        IndividualPnode,
    )


class CongestionArea(AggregatedPnode):
    """Designated Congestion Area Definition (DCA)."""

    __slots__ = ("_individual_pnode",)

    individual_pnode: Many[IndividualPnode] = Many(
        EndMeta(
            name="individual_pnode",
            cim_role="IndividualPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.individual_pnode:IndividualPnode",
            many=True,
            lower=0,
            upper=None,
            inverse="congestion_area",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CongestionArea",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{CBD147E6-2BFE-451e-A558-27BD22B7CDE1}",
        ends=(individual_pnode.meta,),
    )

    def __init__(
        self,
        *,
        individual_pnode: Iterable[IndividualPnode] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if individual_pnode is not None:
            CongestionArea.individual_pnode.extend(self, individual_pnode)

    def add_individual_pnode(self, individual_pnode: IndividualPnode) -> Self:
        return CongestionArea.individual_pnode.add(self, individual_pnode)

    def remove_individual_pnode(self, individual_pnode: IndividualPnode) -> Self:
        return CongestionArea.individual_pnode.remove(self, individual_pnode)

    def clear_individual_pnode(self) -> Self:
        return CongestionArea.individual_pnode.clear(self)

    def num_individual_pnode(self) -> int:
        return CongestionArea.individual_pnode.count(self)

    def get_individual_pnode_by_mrid(self, mrid: str) -> IndividualPnode | None:
        return CongestionArea.individual_pnode.get_by_mrid(self, mrid)
