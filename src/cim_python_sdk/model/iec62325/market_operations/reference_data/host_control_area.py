"""CIM class HostControlArea (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.control_area_operator import (
        ControlAreaOperator,
    )
    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.sys_load_distribution_factor import (
        SysLoadDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transfer_interface import (
        TransferInterface,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.loss_clearing_results import (
        LossClearingResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.area_control_mode import (
        AreaControlMode,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_self_sched import (
        BidSelfSched,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.adjacent_ca_set import (
        AdjacentCASet,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.cnode_distribution_factor import (
        CnodeDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class HostControlArea(PowerSystemResource):
    """A HostControlArea has a set of tie points and a set of generator controls (i.e., AGC).
    It also has a total load, including transmission and distribution losses."""

    __slots__ = (
        "_adjacent_ca_set",
        "_bid_self_sched",
        "_cnode_distribution_factor",
        "_controls_controlled_by",
        "_flowgate",
        "_loss_clearing_results",
        "_registered_resource",
        "_rto",
        "_sub_control_areas",
        "_sys_load_distribu_factor",
        "_transfer_interface",
        "area_control_mode",
        "freq_set_point",
        "frequency_bias_factor",
    )

    area_control_mode: AreaControlMode | None
    freq_set_point: float | None  # Frequency
    frequency_bias_factor: float | None

    controls_controlled_by: One[ControlAreaOperator] = One(
        EndMeta(
            name="controls_controlled_by",
            cim_role="Controls",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.control_area_operator:ControlAreaOperator",
            many=False,
            lower=1,
            upper=1,
            inverse="controlled_by",
            aggregation="none",
        )
    )
    cnode_distribution_factor: Many[CnodeDistributionFactor] = Many(
        EndMeta(
            name="cnode_distribution_factor",
            cim_role="CnodeDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.cnode_distribution_factor:CnodeDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="host_control_area",
            aggregation="none",
        )
    )
    sys_load_distribu_factor: Many[SysLoadDistributionFactor] = Many(
        EndMeta(
            name="sys_load_distribu_factor",
            cim_role="SysLoadDistribuFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.sys_load_distribution_factor:SysLoadDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="host_control_area",
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
            inverse="host_control_area",
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
            inverse="host_control_area",
            aggregation="none",
        )
    )
    adjacent_ca_set: One[AdjacentCASet] = One(
        EndMeta(
            name="adjacent_ca_set",
            cim_role="AdjacentCASet",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.adjacent_ca_set:AdjacentCASet",
            many=False,
            lower=0,
            upper=1,
            inverse="host_control_area",
            aggregation="none",
        )
    )
    transfer_interface: Many[TransferInterface] = Many(
        EndMeta(
            name="transfer_interface",
            cim_role="TransferInterface",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transfer_interface:TransferInterface",
            many=True,
            lower=0,
            upper=None,
            inverse="host_control_area",
            aggregation="none",
        )
    )
    bid_self_sched: Many[BidSelfSched] = Many(
        EndMeta(
            name="bid_self_sched",
            cim_role="BidSelfSched",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_self_sched:BidSelfSched",
            many=True,
            lower=0,
            upper=None,
            inverse="host_control_area",
            aggregation="none",
        )
    )
    loss_clearing_results: Many[LossClearingResults] = Many(
        EndMeta(
            name="loss_clearing_results",
            cim_role="LossClearingResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.loss_clearing_results:LossClearingResults",
            many=True,
            lower=0,
            upper=None,
            inverse="host_control_area",
            aggregation="none",
        )
    )
    flowgate: Many[Flowgate] = Many(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=True,
            lower=0,
            upper=None,
            inverse="host_control_area",
            aggregation="none",
        )
    )
    sub_control_areas: Many[SubControlArea] = Many(
        EndMeta(
            name="sub_control_areas",
            cim_role="SubControlAreas",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=True,
            lower=0,
            upper=None,
            inverse="host_control_area",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HostControlArea",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{B16A7A82-06A9-49e2-A693-D9853F1DFCFE}",
        attributes=(
            AttrMeta(
                "area_control_mode", "areaControlMode", "AreaControlMode", 0, 1, "enumeration"
            ),
            AttrMeta("freq_set_point", "freqSetPoint", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("frequency_bias_factor", "frequencyBiasFactor", "float", 0, 1, "primitive"),
        ),
        ends=(
            controls_controlled_by.meta,
            cnode_distribution_factor.meta,
            sys_load_distribu_factor.meta,
            registered_resource.meta,
            rto.meta,
            adjacent_ca_set.meta,
            transfer_interface.meta,
            bid_self_sched.meta,
            loss_clearing_results.meta,
            flowgate.meta,
            sub_control_areas.meta,
        ),
    )

    def __init__(
        self,
        *,
        area_control_mode: AreaControlMode | None = None,
        freq_set_point: float | None = None,
        frequency_bias_factor: float | None = None,
        controls_controlled_by: ControlAreaOperator | None = None,
        cnode_distribution_factor: Iterable[CnodeDistributionFactor] | None = None,
        sys_load_distribu_factor: Iterable[SysLoadDistributionFactor] | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        rto: RTO | None = None,
        adjacent_ca_set: AdjacentCASet | None = None,
        transfer_interface: Iterable[TransferInterface] | None = None,
        bid_self_sched: Iterable[BidSelfSched] | None = None,
        loss_clearing_results: Iterable[LossClearingResults] | None = None,
        flowgate: Iterable[Flowgate] | None = None,
        sub_control_areas: Iterable[SubControlArea] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.area_control_mode = area_control_mode
        self.freq_set_point = freq_set_point
        self.frequency_bias_factor = frequency_bias_factor
        if controls_controlled_by is not None:
            self.controls_controlled_by = controls_controlled_by
        if cnode_distribution_factor is not None:
            HostControlArea.cnode_distribution_factor.extend(self, cnode_distribution_factor)
        if sys_load_distribu_factor is not None:
            HostControlArea.sys_load_distribu_factor.extend(self, sys_load_distribu_factor)
        if registered_resource is not None:
            HostControlArea.registered_resource.extend(self, registered_resource)
        if rto is not None:
            self.rto = rto
        if adjacent_ca_set is not None:
            self.adjacent_ca_set = adjacent_ca_set
        if transfer_interface is not None:
            HostControlArea.transfer_interface.extend(self, transfer_interface)
        if bid_self_sched is not None:
            HostControlArea.bid_self_sched.extend(self, bid_self_sched)
        if loss_clearing_results is not None:
            HostControlArea.loss_clearing_results.extend(self, loss_clearing_results)
        if flowgate is not None:
            HostControlArea.flowgate.extend(self, flowgate)
        if sub_control_areas is not None:
            HostControlArea.sub_control_areas.extend(self, sub_control_areas)

    def add_cnode_distribution_factor(
        self, cnode_distribution_factor: CnodeDistributionFactor
    ) -> Self:
        return HostControlArea.cnode_distribution_factor.add(self, cnode_distribution_factor)

    def remove_cnode_distribution_factor(
        self, cnode_distribution_factor: CnodeDistributionFactor
    ) -> Self:
        return HostControlArea.cnode_distribution_factor.remove(self, cnode_distribution_factor)

    def clear_cnode_distribution_factor(self) -> Self:
        return HostControlArea.cnode_distribution_factor.clear(self)

    def num_cnode_distribution_factor(self) -> int:
        return HostControlArea.cnode_distribution_factor.count(self)

    def get_cnode_distribution_factor_by_mrid(self, mrid: str) -> CnodeDistributionFactor | None:
        return HostControlArea.cnode_distribution_factor.get_by_mrid(self, mrid)

    def add_sys_load_distribu_factor(
        self, sys_load_distribu_factor: SysLoadDistributionFactor
    ) -> Self:
        return HostControlArea.sys_load_distribu_factor.add(self, sys_load_distribu_factor)

    def remove_sys_load_distribu_factor(
        self, sys_load_distribu_factor: SysLoadDistributionFactor
    ) -> Self:
        return HostControlArea.sys_load_distribu_factor.remove(self, sys_load_distribu_factor)

    def clear_sys_load_distribu_factor(self) -> Self:
        return HostControlArea.sys_load_distribu_factor.clear(self)

    def num_sys_load_distribu_factor(self) -> int:
        return HostControlArea.sys_load_distribu_factor.count(self)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return HostControlArea.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return HostControlArea.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return HostControlArea.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return HostControlArea.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return HostControlArea.registered_resource.get_by_mrid(self, mrid)

    def add_transfer_interface(self, transfer_interface: TransferInterface) -> Self:
        return HostControlArea.transfer_interface.add(self, transfer_interface)

    def remove_transfer_interface(self, transfer_interface: TransferInterface) -> Self:
        return HostControlArea.transfer_interface.remove(self, transfer_interface)

    def clear_transfer_interface(self) -> Self:
        return HostControlArea.transfer_interface.clear(self)

    def num_transfer_interface(self) -> int:
        return HostControlArea.transfer_interface.count(self)

    def get_transfer_interface_by_mrid(self, mrid: str) -> TransferInterface | None:
        return HostControlArea.transfer_interface.get_by_mrid(self, mrid)

    def add_bid_self_sched(self, bid_self_sched: BidSelfSched) -> Self:
        return HostControlArea.bid_self_sched.add(self, bid_self_sched)

    def remove_bid_self_sched(self, bid_self_sched: BidSelfSched) -> Self:
        return HostControlArea.bid_self_sched.remove(self, bid_self_sched)

    def clear_bid_self_sched(self) -> Self:
        return HostControlArea.bid_self_sched.clear(self)

    def num_bid_self_sched(self) -> int:
        return HostControlArea.bid_self_sched.count(self)

    def get_bid_self_sched_by_mrid(self, mrid: str) -> BidSelfSched | None:
        return HostControlArea.bid_self_sched.get_by_mrid(self, mrid)

    def add_loss_clearing_result(self, loss_clearing_result: LossClearingResults) -> Self:
        return HostControlArea.loss_clearing_results.add(self, loss_clearing_result)

    def remove_loss_clearing_result(self, loss_clearing_result: LossClearingResults) -> Self:
        return HostControlArea.loss_clearing_results.remove(self, loss_clearing_result)

    def clear_loss_clearing_results(self) -> Self:
        return HostControlArea.loss_clearing_results.clear(self)

    def num_loss_clearing_result(self) -> int:
        return HostControlArea.loss_clearing_results.count(self)

    def add_flowgate(self, flowgate: Flowgate) -> Self:
        return HostControlArea.flowgate.add(self, flowgate)

    def remove_flowgate(self, flowgate: Flowgate) -> Self:
        return HostControlArea.flowgate.remove(self, flowgate)

    def clear_flowgate(self) -> Self:
        return HostControlArea.flowgate.clear(self)

    def num_flowgate(self) -> int:
        return HostControlArea.flowgate.count(self)

    def get_flowgate_by_mrid(self, mrid: str) -> Flowgate | None:
        return HostControlArea.flowgate.get_by_mrid(self, mrid)

    def add_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return HostControlArea.sub_control_areas.add(self, sub_control_area)

    def remove_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return HostControlArea.sub_control_areas.remove(self, sub_control_area)

    def clear_sub_control_areas(self) -> Self:
        return HostControlArea.sub_control_areas.clear(self)

    def num_sub_control_area(self) -> int:
        return HostControlArea.sub_control_areas.count(self)

    def get_sub_control_area_by_mrid(self, mrid: str) -> SubControlArea | None:
        return HostControlArea.sub_control_areas.get_by_mrid(self, mrid)
