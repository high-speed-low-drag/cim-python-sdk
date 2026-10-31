"""CIM class TACArea (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.area_load_curve import (
        AreaLoadCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode import (
        AggregatedPnode,
    )


class TACArea(IdentifiedObject):
    """Transmission Access Charge Area. Charges assessed, on behalf of the Participating
    Transmission Owner, to parties who require access to the controlled grid."""

    __slots__ = ("_aggregated_pnode", "_area_load_curve")

    aggregated_pnode: Many[AggregatedPnode] = Many(
        EndMeta(
            name="aggregated_pnode",
            cim_role="AggregatedPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode:AggregatedPnode",
            many=True,
            lower=0,
            upper=None,
            inverse="tac_area",
            aggregation="none",
        )
    )
    area_load_curve: Many[AreaLoadCurve] = Many(
        EndMeta(
            name="area_load_curve",
            cim_role="AreaLoadCurve",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.area_load_curve:AreaLoadCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="tac_area",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TACArea",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{6DE57238-5C2B-49f5-96B5-4FB480581646}",
        ends=(
            aggregated_pnode.meta,
            area_load_curve.meta,
        ),
    )

    def __init__(
        self,
        *,
        aggregated_pnode: Iterable[AggregatedPnode] | None = None,
        area_load_curve: Iterable[AreaLoadCurve] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if aggregated_pnode is not None:
            TACArea.aggregated_pnode.extend(self, aggregated_pnode)
        if area_load_curve is not None:
            TACArea.area_load_curve.extend(self, area_load_curve)

    def add_aggregated_pnode(self, aggregated_pnode: AggregatedPnode) -> Self:
        return TACArea.aggregated_pnode.add(self, aggregated_pnode)

    def remove_aggregated_pnode(self, aggregated_pnode: AggregatedPnode) -> Self:
        return TACArea.aggregated_pnode.remove(self, aggregated_pnode)

    def clear_aggregated_pnode(self) -> Self:
        return TACArea.aggregated_pnode.clear(self)

    def num_aggregated_pnode(self) -> int:
        return TACArea.aggregated_pnode.count(self)

    def get_aggregated_pnode_by_mrid(self, mrid: str) -> AggregatedPnode | None:
        return TACArea.aggregated_pnode.get_by_mrid(self, mrid)

    def add_area_load_curve(self, area_load_curve: AreaLoadCurve) -> Self:
        return TACArea.area_load_curve.add(self, area_load_curve)

    def remove_area_load_curve(self, area_load_curve: AreaLoadCurve) -> Self:
        return TACArea.area_load_curve.remove(self, area_load_curve)

    def clear_area_load_curve(self) -> Self:
        return TACArea.area_load_curve.clear(self)

    def num_area_load_curve(self) -> int:
        return TACArea.area_load_curve.count(self)

    def get_area_load_curve_by_mrid(self, mrid: str) -> AreaLoadCurve | None:
        return TACArea.area_load_curve.get_by_mrid(self, mrid)
