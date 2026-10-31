"""CIM class SubControlArea (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.area_reserve_spec import (
        AreaReserveSpec,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.dynamic_schedule import (
        DynamicSchedule,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.inadvertent_account import (
        InadvertentAccount,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.tie_line import TieLine
    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction import (
        EnergyTransaction,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_loss_results import (
        ExPostLossResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.general_clearing_results import (
        GeneralClearingResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.loss_clearing_results import (
        LossClearingResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_self_sched import (
        BidSelfSched,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.adjacent_ca_set import (
        AdjacentCASet,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node import (
        AggregateNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.cnode_distribution_factor import (
        CnodeDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.control_area_designation import (
        ControlAreaDesignation,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class SubControlArea(PowerSystemResource):
    """An area defined for the purpose of tracking interchange with surrounding areas via tie
    points; may or may not serve as a control area."""

    __slots__ = (
        "_adjacent_ca_set",
        "_aggregate_node",
        "_area_reserve_specification",
        "_bid_self_sched",
        "_cnode_distribution_factor",
        "_control_area_designation",
        "_ex_post_loss_results",
        "_export_energy_transactions",
        "_from_flowgate",
        "_general_clearing_results",
        "_host_control_area",
        "_import_energy_transactions",
        "_inadvertent_account",
        "_loss_clearing_results",
        "_pnode",
        "_receive_dynamic_schedules",
        "_registered_resource",
        "_rto",
        "_send_dynamic_schedules",
        "_side_a_tie_lines",
        "_side_b_tie_lines",
        "_to_flowgate",
        "area_short_name",
        "constant_coefficient",
        "embedded_control_area",
        "internal_ca",
        "linear_coefficient",
        "local_ca",
        "max_self_sched_mw",
        "min_self_sched_mw",
        "quadratic_coefficient",
    )

    area_short_name: str | None
    constant_coefficient: float | None
    embedded_control_area: YesNo | None
    internal_ca: YesNo | None
    linear_coefficient: float | None
    local_ca: YesNo | None
    max_self_sched_mw: float | None
    min_self_sched_mw: float | None
    quadratic_coefficient: float | None

    from_flowgate: Many[Flowgate] = Many(
        EndMeta(
            name="from_flowgate",
            cim_role="From_Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=True,
            lower=0,
            upper=None,
            inverse="from_sub_control_area",
            aggregation="none",
        )
    )
    import_energy_transactions: Many[EnergyTransaction] = Many(
        EndMeta(
            name="import_energy_transactions",
            cim_role="Import_EnergyTransactions",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction:EnergyTransaction",
            many=True,
            lower=0,
            upper=None,
            inverse="import_sub_control_area",
            aggregation="none",
        )
    )
    inadvertent_account: Many[InadvertentAccount] = Many(
        EndMeta(
            name="inadvertent_account",
            cim_role="InadvertentAccount",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.inadvertent_account:InadvertentAccount",
            many=True,
            lower=0,
            upper=None,
            inverse="sub_control_area",
            aggregation="shared",
        )
    )
    side_b_tie_lines: Many[TieLine] = Many(
        EndMeta(
            name="side_b_tie_lines",
            cim_role="SideB_TieLines",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.tie_line:TieLine",
            many=True,
            lower=0,
            upper=None,
            inverse="side_b_sub_control_area",
            aggregation="none",
        )
    )
    general_clearing_results: Many[GeneralClearingResults] = Many(
        EndMeta(
            name="general_clearing_results",
            cim_role="GeneralClearingResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.general_clearing_results:GeneralClearingResults",
            many=True,
            lower=0,
            upper=None,
            inverse="sub_control_area",
            aggregation="none",
        )
    )
    loss_clearing_results: Many[LossClearingResults] = Many(
        EndMeta(
            name="loss_clearing_results",
            cim_role="LossClearingResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.loss_clearing_results:LossClearingResults",
            many=True,
            lower=1,
            upper=None,
            inverse="sub_control_area",
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
            inverse="sub_control_area",
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
            inverse="sub_control_area",
            aggregation="none",
        )
    )
    ex_post_loss_results: Many[ExPostLossResults] = Many(
        EndMeta(
            name="ex_post_loss_results",
            cim_role="ExPostLossResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_loss_results:ExPostLossResults",
            many=True,
            lower=0,
            upper=None,
            inverse="sub_control_area",
            aggregation="none",
        )
    )
    receive_dynamic_schedules: Many[DynamicSchedule] = Many(
        EndMeta(
            name="receive_dynamic_schedules",
            cim_role="Receive_DynamicSchedules",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.dynamic_schedule:DynamicSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="receive_sub_control_area",
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
            inverse="sub_control_area",
            aggregation="none",
        )
    )
    to_flowgate: Many[Flowgate] = Many(
        EndMeta(
            name="to_flowgate",
            cim_role="To_Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=True,
            lower=0,
            upper=None,
            inverse="to_sub_control_area",
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
            inverse="sub_control_area",
            aggregation="none",
        )
    )
    aggregate_node: Many[AggregateNode] = Many(
        EndMeta(
            name="aggregate_node",
            cim_role="AggregateNode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node:AggregateNode",
            many=True,
            lower=0,
            upper=None,
            inverse="sub_control_area",
            aggregation="none",
        )
    )
    side_a_tie_lines: Many[TieLine] = Many(
        EndMeta(
            name="side_a_tie_lines",
            cim_role="SideA_TieLines",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.tie_line:TieLine",
            many=True,
            lower=0,
            upper=None,
            inverse="side_a_sub_control_area",
            aggregation="none",
        )
    )
    control_area_designation: Many[ControlAreaDesignation] = Many(
        EndMeta(
            name="control_area_designation",
            cim_role="ControlAreaDesignation",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.control_area_designation:ControlAreaDesignation",
            many=True,
            lower=0,
            upper=None,
            inverse="sub_control_area",
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
            inverse="sub_control_area",
            aggregation="none",
        )
    )
    send_dynamic_schedules: Many[DynamicSchedule] = Many(
        EndMeta(
            name="send_dynamic_schedules",
            cim_role="Send_DynamicSchedules",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.dynamic_schedule:DynamicSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="send_sub_control_area",
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
            inverse="sub_control_area",
            aggregation="none",
        )
    )
    area_reserve_specification: One[AreaReserveSpec] = One(
        EndMeta(
            name="area_reserve_specification",
            cim_role="AreaReserveSpecification",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.area_reserve_spec:AreaReserveSpec",
            many=False,
            lower=1,
            upper=1,
            inverse="sub_control_area",
            aggregation="none",
        )
    )
    host_control_area: One[HostControlArea] = One(
        EndMeta(
            name="host_control_area",
            cim_role="HostControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area:HostControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="sub_control_areas",
            aggregation="none",
        )
    )
    export_energy_transactions: Many[EnergyTransaction] = Many(
        EndMeta(
            name="export_energy_transactions",
            cim_role="Export_EnergyTransactions",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction:EnergyTransaction",
            many=True,
            lower=0,
            upper=None,
            inverse="export_sub_control_area",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SubControlArea",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{1A77F399-87B3-4dce-A329-739AEAB09175}",
        attributes=(
            AttrMeta("area_short_name", "areaShortName", "str", 0, 1, "primitive"),
            AttrMeta("constant_coefficient", "constantCoefficient", "float", 0, 1, "primitive"),
            AttrMeta("embedded_control_area", "embeddedControlArea", "YesNo", 0, 1, "enumeration"),
            AttrMeta("internal_ca", "internalCA", "YesNo", 0, 1, "enumeration"),
            AttrMeta("linear_coefficient", "linearCoefficient", "float", 0, 1, "primitive"),
            AttrMeta("local_ca", "localCA", "YesNo", 0, 1, "enumeration"),
            AttrMeta("max_self_sched_mw", "maxSelfSchedMW", "float", 0, 1, "primitive"),
            AttrMeta("min_self_sched_mw", "minSelfSchedMW", "float", 0, 1, "primitive"),
            AttrMeta("quadratic_coefficient", "quadraticCoefficient", "float", 0, 1, "primitive"),
        ),
        ends=(
            from_flowgate.meta,
            import_energy_transactions.meta,
            inadvertent_account.meta,
            side_b_tie_lines.meta,
            general_clearing_results.meta,
            loss_clearing_results.meta,
            cnode_distribution_factor.meta,
            adjacent_ca_set.meta,
            ex_post_loss_results.meta,
            receive_dynamic_schedules.meta,
            registered_resource.meta,
            to_flowgate.meta,
            bid_self_sched.meta,
            aggregate_node.meta,
            side_a_tie_lines.meta,
            control_area_designation.meta,
            rto.meta,
            send_dynamic_schedules.meta,
            pnode.meta,
            area_reserve_specification.meta,
            host_control_area.meta,
            export_energy_transactions.meta,
        ),
    )

    def __init__(
        self,
        *,
        area_short_name: str | None = None,
        constant_coefficient: float | None = None,
        embedded_control_area: YesNo | None = None,
        internal_ca: YesNo | None = None,
        linear_coefficient: float | None = None,
        local_ca: YesNo | None = None,
        max_self_sched_mw: float | None = None,
        min_self_sched_mw: float | None = None,
        quadratic_coefficient: float | None = None,
        from_flowgate: Iterable[Flowgate] | None = None,
        import_energy_transactions: Iterable[EnergyTransaction] | None = None,
        inadvertent_account: Iterable[InadvertentAccount] | None = None,
        side_b_tie_lines: Iterable[TieLine] | None = None,
        general_clearing_results: Iterable[GeneralClearingResults] | None = None,
        loss_clearing_results: Iterable[LossClearingResults] | None = None,
        cnode_distribution_factor: Iterable[CnodeDistributionFactor] | None = None,
        adjacent_ca_set: AdjacentCASet | None = None,
        ex_post_loss_results: Iterable[ExPostLossResults] | None = None,
        receive_dynamic_schedules: Iterable[DynamicSchedule] | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        to_flowgate: Iterable[Flowgate] | None = None,
        bid_self_sched: Iterable[BidSelfSched] | None = None,
        aggregate_node: Iterable[AggregateNode] | None = None,
        side_a_tie_lines: Iterable[TieLine] | None = None,
        control_area_designation: Iterable[ControlAreaDesignation] | None = None,
        rto: RTO | None = None,
        send_dynamic_schedules: Iterable[DynamicSchedule] | None = None,
        pnode: Iterable[Pnode] | None = None,
        area_reserve_specification: AreaReserveSpec | None = None,
        host_control_area: HostControlArea | None = None,
        export_energy_transactions: Iterable[EnergyTransaction] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.area_short_name = area_short_name
        self.constant_coefficient = constant_coefficient
        self.embedded_control_area = embedded_control_area
        self.internal_ca = internal_ca
        self.linear_coefficient = linear_coefficient
        self.local_ca = local_ca
        self.max_self_sched_mw = max_self_sched_mw
        self.min_self_sched_mw = min_self_sched_mw
        self.quadratic_coefficient = quadratic_coefficient
        if from_flowgate is not None:
            SubControlArea.from_flowgate.extend(self, from_flowgate)
        if import_energy_transactions is not None:
            SubControlArea.import_energy_transactions.extend(self, import_energy_transactions)
        if inadvertent_account is not None:
            SubControlArea.inadvertent_account.extend(self, inadvertent_account)
        if side_b_tie_lines is not None:
            SubControlArea.side_b_tie_lines.extend(self, side_b_tie_lines)
        if general_clearing_results is not None:
            SubControlArea.general_clearing_results.extend(self, general_clearing_results)
        if loss_clearing_results is not None:
            SubControlArea.loss_clearing_results.extend(self, loss_clearing_results)
        if cnode_distribution_factor is not None:
            SubControlArea.cnode_distribution_factor.extend(self, cnode_distribution_factor)
        if adjacent_ca_set is not None:
            self.adjacent_ca_set = adjacent_ca_set
        if ex_post_loss_results is not None:
            SubControlArea.ex_post_loss_results.extend(self, ex_post_loss_results)
        if receive_dynamic_schedules is not None:
            SubControlArea.receive_dynamic_schedules.extend(self, receive_dynamic_schedules)
        if registered_resource is not None:
            SubControlArea.registered_resource.extend(self, registered_resource)
        if to_flowgate is not None:
            SubControlArea.to_flowgate.extend(self, to_flowgate)
        if bid_self_sched is not None:
            SubControlArea.bid_self_sched.extend(self, bid_self_sched)
        if aggregate_node is not None:
            SubControlArea.aggregate_node.extend(self, aggregate_node)
        if side_a_tie_lines is not None:
            SubControlArea.side_a_tie_lines.extend(self, side_a_tie_lines)
        if control_area_designation is not None:
            SubControlArea.control_area_designation.extend(self, control_area_designation)
        if rto is not None:
            self.rto = rto
        if send_dynamic_schedules is not None:
            SubControlArea.send_dynamic_schedules.extend(self, send_dynamic_schedules)
        if pnode is not None:
            SubControlArea.pnode.extend(self, pnode)
        if area_reserve_specification is not None:
            self.area_reserve_specification = area_reserve_specification
        if host_control_area is not None:
            self.host_control_area = host_control_area
        if export_energy_transactions is not None:
            SubControlArea.export_energy_transactions.extend(self, export_energy_transactions)

    def add_from_flowgate(self, from_flowgate: Flowgate) -> Self:
        return SubControlArea.from_flowgate.add(self, from_flowgate)

    def remove_from_flowgate(self, from_flowgate: Flowgate) -> Self:
        return SubControlArea.from_flowgate.remove(self, from_flowgate)

    def clear_from_flowgate(self) -> Self:
        return SubControlArea.from_flowgate.clear(self)

    def num_from_flowgate(self) -> int:
        return SubControlArea.from_flowgate.count(self)

    def get_from_flowgate_by_mrid(self, mrid: str) -> Flowgate | None:
        return SubControlArea.from_flowgate.get_by_mrid(self, mrid)

    def add_import_energy_transaction(self, import_energy_transaction: EnergyTransaction) -> Self:
        return SubControlArea.import_energy_transactions.add(self, import_energy_transaction)

    def remove_import_energy_transaction(
        self, import_energy_transaction: EnergyTransaction
    ) -> Self:
        return SubControlArea.import_energy_transactions.remove(self, import_energy_transaction)

    def clear_import_energy_transactions(self) -> Self:
        return SubControlArea.import_energy_transactions.clear(self)

    def num_import_energy_transaction(self) -> int:
        return SubControlArea.import_energy_transactions.count(self)

    def get_import_energy_transaction_by_mrid(self, mrid: str) -> EnergyTransaction | None:
        return SubControlArea.import_energy_transactions.get_by_mrid(self, mrid)

    def add_inadvertent_account(self, inadvertent_account: InadvertentAccount) -> Self:
        return SubControlArea.inadvertent_account.add(self, inadvertent_account)

    def remove_inadvertent_account(self, inadvertent_account: InadvertentAccount) -> Self:
        return SubControlArea.inadvertent_account.remove(self, inadvertent_account)

    def clear_inadvertent_account(self) -> Self:
        return SubControlArea.inadvertent_account.clear(self)

    def num_inadvertent_account(self) -> int:
        return SubControlArea.inadvertent_account.count(self)

    def add_side_b_tie_line(self, side_b_tie_line: TieLine) -> Self:
        return SubControlArea.side_b_tie_lines.add(self, side_b_tie_line)

    def remove_side_b_tie_line(self, side_b_tie_line: TieLine) -> Self:
        return SubControlArea.side_b_tie_lines.remove(self, side_b_tie_line)

    def clear_side_b_tie_lines(self) -> Self:
        return SubControlArea.side_b_tie_lines.clear(self)

    def num_side_b_tie_line(self) -> int:
        return SubControlArea.side_b_tie_lines.count(self)

    def get_side_b_tie_line_by_mrid(self, mrid: str) -> TieLine | None:
        return SubControlArea.side_b_tie_lines.get_by_mrid(self, mrid)

    def add_general_clearing_result(self, general_clearing_result: GeneralClearingResults) -> Self:
        return SubControlArea.general_clearing_results.add(self, general_clearing_result)

    def remove_general_clearing_result(
        self, general_clearing_result: GeneralClearingResults
    ) -> Self:
        return SubControlArea.general_clearing_results.remove(self, general_clearing_result)

    def clear_general_clearing_results(self) -> Self:
        return SubControlArea.general_clearing_results.clear(self)

    def num_general_clearing_result(self) -> int:
        return SubControlArea.general_clearing_results.count(self)

    def add_loss_clearing_result(self, loss_clearing_result: LossClearingResults) -> Self:
        return SubControlArea.loss_clearing_results.add(self, loss_clearing_result)

    def remove_loss_clearing_result(self, loss_clearing_result: LossClearingResults) -> Self:
        return SubControlArea.loss_clearing_results.remove(self, loss_clearing_result)

    def clear_loss_clearing_results(self) -> Self:
        return SubControlArea.loss_clearing_results.clear(self)

    def num_loss_clearing_result(self) -> int:
        return SubControlArea.loss_clearing_results.count(self)

    def add_cnode_distribution_factor(
        self, cnode_distribution_factor: CnodeDistributionFactor
    ) -> Self:
        return SubControlArea.cnode_distribution_factor.add(self, cnode_distribution_factor)

    def remove_cnode_distribution_factor(
        self, cnode_distribution_factor: CnodeDistributionFactor
    ) -> Self:
        return SubControlArea.cnode_distribution_factor.remove(self, cnode_distribution_factor)

    def clear_cnode_distribution_factor(self) -> Self:
        return SubControlArea.cnode_distribution_factor.clear(self)

    def num_cnode_distribution_factor(self) -> int:
        return SubControlArea.cnode_distribution_factor.count(self)

    def get_cnode_distribution_factor_by_mrid(self, mrid: str) -> CnodeDistributionFactor | None:
        return SubControlArea.cnode_distribution_factor.get_by_mrid(self, mrid)

    def add_ex_post_loss_result(self, ex_post_loss_result: ExPostLossResults) -> Self:
        return SubControlArea.ex_post_loss_results.add(self, ex_post_loss_result)

    def remove_ex_post_loss_result(self, ex_post_loss_result: ExPostLossResults) -> Self:
        return SubControlArea.ex_post_loss_results.remove(self, ex_post_loss_result)

    def clear_ex_post_loss_results(self) -> Self:
        return SubControlArea.ex_post_loss_results.clear(self)

    def num_ex_post_loss_result(self) -> int:
        return SubControlArea.ex_post_loss_results.count(self)

    def add_receive_dynamic_schedule(self, receive_dynamic_schedule: DynamicSchedule) -> Self:
        return SubControlArea.receive_dynamic_schedules.add(self, receive_dynamic_schedule)

    def remove_receive_dynamic_schedule(self, receive_dynamic_schedule: DynamicSchedule) -> Self:
        return SubControlArea.receive_dynamic_schedules.remove(self, receive_dynamic_schedule)

    def clear_receive_dynamic_schedules(self) -> Self:
        return SubControlArea.receive_dynamic_schedules.clear(self)

    def num_receive_dynamic_schedule(self) -> int:
        return SubControlArea.receive_dynamic_schedules.count(self)

    def get_receive_dynamic_schedule_by_mrid(self, mrid: str) -> DynamicSchedule | None:
        return SubControlArea.receive_dynamic_schedules.get_by_mrid(self, mrid)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return SubControlArea.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return SubControlArea.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return SubControlArea.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return SubControlArea.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return SubControlArea.registered_resource.get_by_mrid(self, mrid)

    def add_to_flowgate(self, to_flowgate: Flowgate) -> Self:
        return SubControlArea.to_flowgate.add(self, to_flowgate)

    def remove_to_flowgate(self, to_flowgate: Flowgate) -> Self:
        return SubControlArea.to_flowgate.remove(self, to_flowgate)

    def clear_to_flowgate(self) -> Self:
        return SubControlArea.to_flowgate.clear(self)

    def num_to_flowgate(self) -> int:
        return SubControlArea.to_flowgate.count(self)

    def get_to_flowgate_by_mrid(self, mrid: str) -> Flowgate | None:
        return SubControlArea.to_flowgate.get_by_mrid(self, mrid)

    def add_bid_self_sched(self, bid_self_sched: BidSelfSched) -> Self:
        return SubControlArea.bid_self_sched.add(self, bid_self_sched)

    def remove_bid_self_sched(self, bid_self_sched: BidSelfSched) -> Self:
        return SubControlArea.bid_self_sched.remove(self, bid_self_sched)

    def clear_bid_self_sched(self) -> Self:
        return SubControlArea.bid_self_sched.clear(self)

    def num_bid_self_sched(self) -> int:
        return SubControlArea.bid_self_sched.count(self)

    def get_bid_self_sched_by_mrid(self, mrid: str) -> BidSelfSched | None:
        return SubControlArea.bid_self_sched.get_by_mrid(self, mrid)

    def add_aggregate_node(self, aggregate_node: AggregateNode) -> Self:
        return SubControlArea.aggregate_node.add(self, aggregate_node)

    def remove_aggregate_node(self, aggregate_node: AggregateNode) -> Self:
        return SubControlArea.aggregate_node.remove(self, aggregate_node)

    def clear_aggregate_node(self) -> Self:
        return SubControlArea.aggregate_node.clear(self)

    def num_aggregate_node(self) -> int:
        return SubControlArea.aggregate_node.count(self)

    def get_aggregate_node_by_mrid(self, mrid: str) -> AggregateNode | None:
        return SubControlArea.aggregate_node.get_by_mrid(self, mrid)

    def add_side_a_tie_line(self, side_a_tie_line: TieLine) -> Self:
        return SubControlArea.side_a_tie_lines.add(self, side_a_tie_line)

    def remove_side_a_tie_line(self, side_a_tie_line: TieLine) -> Self:
        return SubControlArea.side_a_tie_lines.remove(self, side_a_tie_line)

    def clear_side_a_tie_lines(self) -> Self:
        return SubControlArea.side_a_tie_lines.clear(self)

    def num_side_a_tie_line(self) -> int:
        return SubControlArea.side_a_tie_lines.count(self)

    def get_side_a_tie_line_by_mrid(self, mrid: str) -> TieLine | None:
        return SubControlArea.side_a_tie_lines.get_by_mrid(self, mrid)

    def add_control_area_designation(
        self, control_area_designation: ControlAreaDesignation
    ) -> Self:
        return SubControlArea.control_area_designation.add(self, control_area_designation)

    def remove_control_area_designation(
        self, control_area_designation: ControlAreaDesignation
    ) -> Self:
        return SubControlArea.control_area_designation.remove(self, control_area_designation)

    def clear_control_area_designation(self) -> Self:
        return SubControlArea.control_area_designation.clear(self)

    def num_control_area_designation(self) -> int:
        return SubControlArea.control_area_designation.count(self)

    def add_send_dynamic_schedule(self, send_dynamic_schedule: DynamicSchedule) -> Self:
        return SubControlArea.send_dynamic_schedules.add(self, send_dynamic_schedule)

    def remove_send_dynamic_schedule(self, send_dynamic_schedule: DynamicSchedule) -> Self:
        return SubControlArea.send_dynamic_schedules.remove(self, send_dynamic_schedule)

    def clear_send_dynamic_schedules(self) -> Self:
        return SubControlArea.send_dynamic_schedules.clear(self)

    def num_send_dynamic_schedule(self) -> int:
        return SubControlArea.send_dynamic_schedules.count(self)

    def get_send_dynamic_schedule_by_mrid(self, mrid: str) -> DynamicSchedule | None:
        return SubControlArea.send_dynamic_schedules.get_by_mrid(self, mrid)

    def add_pnode(self, pnode: Pnode) -> Self:
        return SubControlArea.pnode.add(self, pnode)

    def remove_pnode(self, pnode: Pnode) -> Self:
        return SubControlArea.pnode.remove(self, pnode)

    def clear_pnode(self) -> Self:
        return SubControlArea.pnode.clear(self)

    def num_pnode(self) -> int:
        return SubControlArea.pnode.count(self)

    def get_pnode_by_mrid(self, mrid: str) -> Pnode | None:
        return SubControlArea.pnode.get_by_mrid(self, mrid)

    def add_export_energy_transaction(self, export_energy_transaction: EnergyTransaction) -> Self:
        return SubControlArea.export_energy_transactions.add(self, export_energy_transaction)

    def remove_export_energy_transaction(
        self, export_energy_transaction: EnergyTransaction
    ) -> Self:
        return SubControlArea.export_energy_transactions.remove(self, export_energy_transaction)

    def clear_export_energy_transactions(self) -> Self:
        return SubControlArea.export_energy_transactions.clear(self)

    def num_export_energy_transaction(self) -> int:
        return SubControlArea.export_energy_transactions.count(self)

    def get_export_energy_transaction_by_mrid(self, mrid: str) -> EnergyTransaction | None:
        return SubControlArea.export_energy_transactions.get_by_mrid(self, mrid)
