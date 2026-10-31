"""CIM class AggregateNode (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.area_load_curve import (
        AreaLoadCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instructions import (
        Instructions,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.anode_type import AnodeType
    from cim_python_sdk.model.iec62325.market_operations.reference_data.cnode_distribution_factor import (
        CnodeDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class AggregateNode(IdentifiedObject):
    """An aggregated node can define a typed grouping further defined by the AnodeType
    enumeratuion. Types range from System Zone/Regions to Market Energy Regions to
    Aggregated Loads and Aggregated Generators."""

    __slots__ = (
        "_area_load_curve",
        "_cnode_distribution_factor",
        "_instruction",
        "_pnode",
        "_registered_resource",
        "_rto",
        "_sub_control_area",
        "anode_type",
        "qualif_as_order",
    )

    anode_type: AnodeType | None
    qualif_as_order: int | None

    cnode_distribution_factor: Many[CnodeDistributionFactor] = Many(
        EndMeta(
            name="cnode_distribution_factor",
            cim_role="CnodeDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.cnode_distribution_factor:CnodeDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="aggregate_node",
            aggregation="none",
        )
    )
    instruction: Many[Instructions] = Many(
        EndMeta(
            name="instruction",
            cim_role="Instruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instructions:Instructions",
            many=True,
            lower=0,
            upper=None,
            inverse="aggregate_node",
            aggregation="none",
        )
    )
    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=1,
            upper=1,
            inverse="aggregate_node",
            aggregation="none",
        )
    )
    sub_control_area: Many[SubControlArea] = Many(
        EndMeta(
            name="sub_control_area",
            cim_role="SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=True,
            lower=0,
            upper=None,
            inverse="aggregate_node",
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
            inverse="aggregate_node",
            aggregation="none",
        )
    )
    pnode: Many[Pnode] = Many(
        EndMeta(
            name="pnode",
            cim_role="Pnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=True,
            lower=0,
            upper=None,
            inverse="aggregate_node",
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
            inverse="aggregate_node",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AggregateNode",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{E0B7E648-99FC-46e1-8F74-5A9BD098FE23}",
        attributes=(
            AttrMeta("anode_type", "anodeType", "AnodeType", 0, 1, "enumeration"),
            AttrMeta("qualif_as_order", "qualifASOrder", "int", 0, 1, "primitive"),
        ),
        ends=(
            cnode_distribution_factor.meta,
            instruction.meta,
            rto.meta,
            sub_control_area.meta,
            area_load_curve.meta,
            pnode.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        anode_type: AnodeType | None = None,
        qualif_as_order: int | None = None,
        cnode_distribution_factor: Iterable[CnodeDistributionFactor] | None = None,
        instruction: Iterable[Instructions] | None = None,
        rto: RTO | None = None,
        sub_control_area: Iterable[SubControlArea] | None = None,
        area_load_curve: Iterable[AreaLoadCurve] | None = None,
        pnode: Iterable[Pnode] | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.anode_type = anode_type
        self.qualif_as_order = qualif_as_order
        if cnode_distribution_factor is not None:
            AggregateNode.cnode_distribution_factor.extend(self, cnode_distribution_factor)
        if instruction is not None:
            AggregateNode.instruction.extend(self, instruction)
        if rto is not None:
            self.rto = rto
        if sub_control_area is not None:
            AggregateNode.sub_control_area.extend(self, sub_control_area)
        if area_load_curve is not None:
            AggregateNode.area_load_curve.extend(self, area_load_curve)
        if pnode is not None:
            AggregateNode.pnode.extend(self, pnode)
        if registered_resource is not None:
            AggregateNode.registered_resource.extend(self, registered_resource)

    def add_cnode_distribution_factor(
        self, cnode_distribution_factor: CnodeDistributionFactor
    ) -> Self:
        return AggregateNode.cnode_distribution_factor.add(self, cnode_distribution_factor)

    def remove_cnode_distribution_factor(
        self, cnode_distribution_factor: CnodeDistributionFactor
    ) -> Self:
        return AggregateNode.cnode_distribution_factor.remove(self, cnode_distribution_factor)

    def clear_cnode_distribution_factor(self) -> Self:
        return AggregateNode.cnode_distribution_factor.clear(self)

    def num_cnode_distribution_factor(self) -> int:
        return AggregateNode.cnode_distribution_factor.count(self)

    def get_cnode_distribution_factor_by_mrid(self, mrid: str) -> CnodeDistributionFactor | None:
        return AggregateNode.cnode_distribution_factor.get_by_mrid(self, mrid)

    def add_instruction(self, instruction: Instructions) -> Self:
        return AggregateNode.instruction.add(self, instruction)

    def remove_instruction(self, instruction: Instructions) -> Self:
        return AggregateNode.instruction.remove(self, instruction)

    def clear_instruction(self) -> Self:
        return AggregateNode.instruction.clear(self)

    def num_instruction(self) -> int:
        return AggregateNode.instruction.count(self)

    def add_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return AggregateNode.sub_control_area.add(self, sub_control_area)

    def remove_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return AggregateNode.sub_control_area.remove(self, sub_control_area)

    def clear_sub_control_area(self) -> Self:
        return AggregateNode.sub_control_area.clear(self)

    def num_sub_control_area(self) -> int:
        return AggregateNode.sub_control_area.count(self)

    def get_sub_control_area_by_mrid(self, mrid: str) -> SubControlArea | None:
        return AggregateNode.sub_control_area.get_by_mrid(self, mrid)

    def add_area_load_curve(self, area_load_curve: AreaLoadCurve) -> Self:
        return AggregateNode.area_load_curve.add(self, area_load_curve)

    def remove_area_load_curve(self, area_load_curve: AreaLoadCurve) -> Self:
        return AggregateNode.area_load_curve.remove(self, area_load_curve)

    def clear_area_load_curve(self) -> Self:
        return AggregateNode.area_load_curve.clear(self)

    def num_area_load_curve(self) -> int:
        return AggregateNode.area_load_curve.count(self)

    def get_area_load_curve_by_mrid(self, mrid: str) -> AreaLoadCurve | None:
        return AggregateNode.area_load_curve.get_by_mrid(self, mrid)

    def add_pnode(self, pnode: Pnode) -> Self:
        return AggregateNode.pnode.add(self, pnode)

    def remove_pnode(self, pnode: Pnode) -> Self:
        return AggregateNode.pnode.remove(self, pnode)

    def clear_pnode(self) -> Self:
        return AggregateNode.pnode.clear(self)

    def num_pnode(self) -> int:
        return AggregateNode.pnode.count(self)

    def get_pnode_by_mrid(self, mrid: str) -> Pnode | None:
        return AggregateNode.pnode.get_by_mrid(self, mrid)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return AggregateNode.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return AggregateNode.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return AggregateNode.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return AggregateNode.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return AggregateNode.registered_resource.get_by_mrid(self, mrid)
