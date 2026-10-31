"""CIM class Flowgate (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_congestion_revenue_rights.ftr import FTR
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_congestion_revenue_rights.violation_limit import (
        ViolationLimit,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_market_results.inter_tie_results import (
        InterTieResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.congestion_revenue_right import (
        CongestionRevenueRight,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_line import MktLine
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_power_transformer import (
        MktPowerTransformer,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_terminal import (
        MktTerminal,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.generating_unit_dynamic_values import (
        GeneratingUnitDynamicValues,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.generic_constraints import (
        GenericConstraints,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraints import (
        SecurityConstraints,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_capacity import (
        TransmissionCapacity,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_interface_right_entitlement import (
        TransmissionInterfaceRightEntitlement,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.constraint_results import (
        ConstraintResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.inter_tie_direction import (
        InterTieDirection,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_distribution_factor import (
        ContractDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate_relief import (
        FlowgateRelief,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate_value import (
        FlowgateValue,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_inter_tie import (
        RegisteredInterTie,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_point import (
        SchedulingPoint,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class Flowgate(PowerSystemResource):
    """A flowgate, is single or group of transmission elements intended to model MW flow impact
    relating to transmission limitations and transmission service usage."""

    __slots__ = (
        "_congestion_revenue_right",
        "_constraint_results",
        "_contract_distribution_factor",
        "_flowgate_relief",
        "_flowgate_value",
        "_from_sub_control_area",
        "_ftrs",
        "_generating_unit_dynamic_values",
        "_generic_constraints",
        "_host_control_area",
        "_inter_tie",
        "_inter_tie_results",
        "_mkt_line",
        "_mkt_power_transformer",
        "_mkt_terminal",
        "_registered_inter_tie",
        "_security_constraints",
        "_to_sub_control_area",
        "_tranmission_right_entitlement",
        "_transmission_capacity",
        "_violation_limits",
        "direction",
        "export_mw_rating",
        "import_mw_rating",
    )

    direction: InterTieDirection | None
    export_mw_rating: float | None  # ActivePower
    import_mw_rating: float | None  # ActivePower

    inter_tie: Many[SchedulingPoint] = Many(
        EndMeta(
            name="inter_tie",
            cim_role="InterTie",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_point:SchedulingPoint",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    from_sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="from_sub_control_area",
            cim_role="From_SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="from_flowgate",
            aggregation="none",
        )
    )
    constraint_results: Many[ConstraintResults] = Many(
        EndMeta(
            name="constraint_results",
            cim_role="ConstraintResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.constraint_results:ConstraintResults",
            many=True,
            lower=1,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    flowgate_value: Many[FlowgateValue] = Many(
        EndMeta(
            name="flowgate_value",
            cim_role="FlowgateValue",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate_value:FlowgateValue",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    contract_distribution_factor: Many[ContractDistributionFactor] = Many(
        EndMeta(
            name="contract_distribution_factor",
            cim_role="ContractDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_distribution_factor:ContractDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    tranmission_right_entitlement: Many[TransmissionInterfaceRightEntitlement] = Many(
        EndMeta(
            name="tranmission_right_entitlement",
            cim_role="TranmissionRightEntitlement",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_interface_right_entitlement:TransmissionInterfaceRightEntitlement",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    violation_limits: Many[ViolationLimit] = Many(
        EndMeta(
            name="violation_limits",
            cim_role="ViolationLimits",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_congestion_revenue_rights.violation_limit:ViolationLimit",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    to_sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="to_sub_control_area",
            cim_role="To_SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="to_flowgate",
            aggregation="none",
        )
    )
    generating_unit_dynamic_values: Many[GeneratingUnitDynamicValues] = Many(
        EndMeta(
            name="generating_unit_dynamic_values",
            cim_role="GeneratingUnitDynamicValues",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.generating_unit_dynamic_values:GeneratingUnitDynamicValues",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    transmission_capacity: Many[TransmissionCapacity] = Many(
        EndMeta(
            name="transmission_capacity",
            cim_role="TransmissionCapacity",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_capacity:TransmissionCapacity",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    mkt_line: Many[MktLine] = Many(
        EndMeta(
            name="mkt_line",
            cim_role="MktLine",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_line:MktLine",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    host_control_area: One[HostControlArea] = One(
        EndMeta(
            name="host_control_area",
            cim_role="HostControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area:HostControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="flowgate",
            aggregation="none",
        )
    )
    registered_inter_tie: Many[RegisteredInterTie] = Many(
        EndMeta(
            name="registered_inter_tie",
            cim_role="RegisteredInterTie",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_inter_tie:RegisteredInterTie",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    congestion_revenue_right: One[CongestionRevenueRight] = One(
        EndMeta(
            name="congestion_revenue_right",
            cim_role="CongestionRevenueRight",
            target="cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.congestion_revenue_right:CongestionRevenueRight",
            many=False,
            lower=0,
            upper=1,
            inverse="flowgate",
            aggregation="none",
        )
    )
    security_constraints: One[SecurityConstraints] = One(
        EndMeta(
            name="security_constraints",
            cim_role="SecurityConstraints",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraints:SecurityConstraints",
            many=False,
            lower=0,
            upper=1,
            inverse="flowgate",
            aggregation="none",
        )
    )
    generic_constraints: One[GenericConstraints] = One(
        EndMeta(
            name="generic_constraints",
            cim_role="GenericConstraints",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.generic_constraints:GenericConstraints",
            many=False,
            lower=0,
            upper=1,
            inverse="flowgate",
            aggregation="none",
        )
    )
    ftrs: Many[FTR] = Many(
        EndMeta(
            name="ftrs",
            cim_role="FTRs",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_congestion_revenue_rights.ftr:FTR",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    mkt_terminal: Many[MktTerminal] = Many(
        EndMeta(
            name="mkt_terminal",
            cim_role="MktTerminal",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_terminal:MktTerminal",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    mkt_power_transformer: Many[MktPowerTransformer] = Many(
        EndMeta(
            name="mkt_power_transformer",
            cim_role="MktPowerTransformer",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_power_transformer:MktPowerTransformer",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    inter_tie_results: Many[InterTieResults] = Many(
        EndMeta(
            name="inter_tie_results",
            cim_role="InterTieResults",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_market_results.inter_tie_results:InterTieResults",
            many=True,
            lower=1,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )
    flowgate_relief: Many[FlowgateRelief] = Many(
        EndMeta(
            name="flowgate_relief",
            cim_role="FlowgateRelief",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate_relief:FlowgateRelief",
            many=True,
            lower=0,
            upper=None,
            inverse="flowgate",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Flowgate",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{A0EA95BA-8681-46f8-A5DB-DF7003A7734A}",
        attributes=(
            AttrMeta("direction", "direction", "InterTieDirection", 0, 1, "enumeration"),
            AttrMeta("export_mw_rating", "exportMWRating", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("import_mw_rating", "importMWRating", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            inter_tie.meta,
            from_sub_control_area.meta,
            constraint_results.meta,
            flowgate_value.meta,
            contract_distribution_factor.meta,
            tranmission_right_entitlement.meta,
            violation_limits.meta,
            to_sub_control_area.meta,
            generating_unit_dynamic_values.meta,
            transmission_capacity.meta,
            mkt_line.meta,
            host_control_area.meta,
            registered_inter_tie.meta,
            congestion_revenue_right.meta,
            security_constraints.meta,
            generic_constraints.meta,
            ftrs.meta,
            mkt_terminal.meta,
            mkt_power_transformer.meta,
            inter_tie_results.meta,
            flowgate_relief.meta,
        ),
    )

    def __init__(
        self,
        *,
        direction: InterTieDirection | None = None,
        export_mw_rating: float | None = None,
        import_mw_rating: float | None = None,
        inter_tie: Iterable[SchedulingPoint] | None = None,
        from_sub_control_area: SubControlArea | None = None,
        constraint_results: Iterable[ConstraintResults] | None = None,
        flowgate_value: Iterable[FlowgateValue] | None = None,
        contract_distribution_factor: Iterable[ContractDistributionFactor] | None = None,
        tranmission_right_entitlement: Iterable[TransmissionInterfaceRightEntitlement]
        | None = None,
        violation_limits: Iterable[ViolationLimit] | None = None,
        to_sub_control_area: SubControlArea | None = None,
        generating_unit_dynamic_values: Iterable[GeneratingUnitDynamicValues] | None = None,
        transmission_capacity: Iterable[TransmissionCapacity] | None = None,
        mkt_line: Iterable[MktLine] | None = None,
        host_control_area: HostControlArea | None = None,
        registered_inter_tie: Iterable[RegisteredInterTie] | None = None,
        congestion_revenue_right: CongestionRevenueRight | None = None,
        security_constraints: SecurityConstraints | None = None,
        generic_constraints: GenericConstraints | None = None,
        ftrs: Iterable[FTR] | None = None,
        mkt_terminal: Iterable[MktTerminal] | None = None,
        mkt_power_transformer: Iterable[MktPowerTransformer] | None = None,
        inter_tie_results: Iterable[InterTieResults] | None = None,
        flowgate_relief: Iterable[FlowgateRelief] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.direction = direction
        self.export_mw_rating = export_mw_rating
        self.import_mw_rating = import_mw_rating
        if inter_tie is not None:
            Flowgate.inter_tie.extend(self, inter_tie)
        if from_sub_control_area is not None:
            self.from_sub_control_area = from_sub_control_area
        if constraint_results is not None:
            Flowgate.constraint_results.extend(self, constraint_results)
        if flowgate_value is not None:
            Flowgate.flowgate_value.extend(self, flowgate_value)
        if contract_distribution_factor is not None:
            Flowgate.contract_distribution_factor.extend(self, contract_distribution_factor)
        if tranmission_right_entitlement is not None:
            Flowgate.tranmission_right_entitlement.extend(self, tranmission_right_entitlement)
        if violation_limits is not None:
            Flowgate.violation_limits.extend(self, violation_limits)
        if to_sub_control_area is not None:
            self.to_sub_control_area = to_sub_control_area
        if generating_unit_dynamic_values is not None:
            Flowgate.generating_unit_dynamic_values.extend(self, generating_unit_dynamic_values)
        if transmission_capacity is not None:
            Flowgate.transmission_capacity.extend(self, transmission_capacity)
        if mkt_line is not None:
            Flowgate.mkt_line.extend(self, mkt_line)
        if host_control_area is not None:
            self.host_control_area = host_control_area
        if registered_inter_tie is not None:
            Flowgate.registered_inter_tie.extend(self, registered_inter_tie)
        if congestion_revenue_right is not None:
            self.congestion_revenue_right = congestion_revenue_right
        if security_constraints is not None:
            self.security_constraints = security_constraints
        if generic_constraints is not None:
            self.generic_constraints = generic_constraints
        if ftrs is not None:
            Flowgate.ftrs.extend(self, ftrs)
        if mkt_terminal is not None:
            Flowgate.mkt_terminal.extend(self, mkt_terminal)
        if mkt_power_transformer is not None:
            Flowgate.mkt_power_transformer.extend(self, mkt_power_transformer)
        if inter_tie_results is not None:
            Flowgate.inter_tie_results.extend(self, inter_tie_results)
        if flowgate_relief is not None:
            Flowgate.flowgate_relief.extend(self, flowgate_relief)

    def add_inter_tie(self, inter_tie: SchedulingPoint) -> Self:
        return Flowgate.inter_tie.add(self, inter_tie)

    def remove_inter_tie(self, inter_tie: SchedulingPoint) -> Self:
        return Flowgate.inter_tie.remove(self, inter_tie)

    def clear_inter_tie(self) -> Self:
        return Flowgate.inter_tie.clear(self)

    def num_inter_tie(self) -> int:
        return Flowgate.inter_tie.count(self)

    def get_inter_tie_by_mrid(self, mrid: str) -> SchedulingPoint | None:
        return Flowgate.inter_tie.get_by_mrid(self, mrid)

    def add_constraint_result(self, constraint_result: ConstraintResults) -> Self:
        return Flowgate.constraint_results.add(self, constraint_result)

    def remove_constraint_result(self, constraint_result: ConstraintResults) -> Self:
        return Flowgate.constraint_results.remove(self, constraint_result)

    def clear_constraint_results(self) -> Self:
        return Flowgate.constraint_results.clear(self)

    def num_constraint_result(self) -> int:
        return Flowgate.constraint_results.count(self)

    def get_constraint_result_by_mrid(self, mrid: str) -> ConstraintResults | None:
        return Flowgate.constraint_results.get_by_mrid(self, mrid)

    def add_flowgate_value(self, flowgate_value: FlowgateValue) -> Self:
        return Flowgate.flowgate_value.add(self, flowgate_value)

    def remove_flowgate_value(self, flowgate_value: FlowgateValue) -> Self:
        return Flowgate.flowgate_value.remove(self, flowgate_value)

    def clear_flowgate_value(self) -> Self:
        return Flowgate.flowgate_value.clear(self)

    def num_flowgate_value(self) -> int:
        return Flowgate.flowgate_value.count(self)

    def add_contract_distribution_factor(
        self, contract_distribution_factor: ContractDistributionFactor
    ) -> Self:
        return Flowgate.contract_distribution_factor.add(self, contract_distribution_factor)

    def remove_contract_distribution_factor(
        self, contract_distribution_factor: ContractDistributionFactor
    ) -> Self:
        return Flowgate.contract_distribution_factor.remove(self, contract_distribution_factor)

    def clear_contract_distribution_factor(self) -> Self:
        return Flowgate.contract_distribution_factor.clear(self)

    def num_contract_distribution_factor(self) -> int:
        return Flowgate.contract_distribution_factor.count(self)

    def add_tranmission_right_entitlement(
        self, tranmission_right_entitlement: TransmissionInterfaceRightEntitlement
    ) -> Self:
        return Flowgate.tranmission_right_entitlement.add(self, tranmission_right_entitlement)

    def remove_tranmission_right_entitlement(
        self, tranmission_right_entitlement: TransmissionInterfaceRightEntitlement
    ) -> Self:
        return Flowgate.tranmission_right_entitlement.remove(self, tranmission_right_entitlement)

    def clear_tranmission_right_entitlement(self) -> Self:
        return Flowgate.tranmission_right_entitlement.clear(self)

    def num_tranmission_right_entitlement(self) -> int:
        return Flowgate.tranmission_right_entitlement.count(self)

    def add_violation_limit(self, violation_limit: ViolationLimit) -> Self:
        return Flowgate.violation_limits.add(self, violation_limit)

    def remove_violation_limit(self, violation_limit: ViolationLimit) -> Self:
        return Flowgate.violation_limits.remove(self, violation_limit)

    def clear_violation_limits(self) -> Self:
        return Flowgate.violation_limits.clear(self)

    def num_violation_limit(self) -> int:
        return Flowgate.violation_limits.count(self)

    def get_violation_limit_by_mrid(self, mrid: str) -> ViolationLimit | None:
        return Flowgate.violation_limits.get_by_mrid(self, mrid)

    def add_generating_unit_dynamic_value(
        self, generating_unit_dynamic_value: GeneratingUnitDynamicValues
    ) -> Self:
        return Flowgate.generating_unit_dynamic_values.add(self, generating_unit_dynamic_value)

    def remove_generating_unit_dynamic_value(
        self, generating_unit_dynamic_value: GeneratingUnitDynamicValues
    ) -> Self:
        return Flowgate.generating_unit_dynamic_values.remove(self, generating_unit_dynamic_value)

    def clear_generating_unit_dynamic_values(self) -> Self:
        return Flowgate.generating_unit_dynamic_values.clear(self)

    def num_generating_unit_dynamic_value(self) -> int:
        return Flowgate.generating_unit_dynamic_values.count(self)

    def add_transmission_capacity(self, transmission_capacity: TransmissionCapacity) -> Self:
        return Flowgate.transmission_capacity.add(self, transmission_capacity)

    def remove_transmission_capacity(self, transmission_capacity: TransmissionCapacity) -> Self:
        return Flowgate.transmission_capacity.remove(self, transmission_capacity)

    def clear_transmission_capacity(self) -> Self:
        return Flowgate.transmission_capacity.clear(self)

    def num_transmission_capacity(self) -> int:
        return Flowgate.transmission_capacity.count(self)

    def add_mkt_line(self, mkt_line: MktLine) -> Self:
        return Flowgate.mkt_line.add(self, mkt_line)

    def remove_mkt_line(self, mkt_line: MktLine) -> Self:
        return Flowgate.mkt_line.remove(self, mkt_line)

    def clear_mkt_line(self) -> Self:
        return Flowgate.mkt_line.clear(self)

    def num_mkt_line(self) -> int:
        return Flowgate.mkt_line.count(self)

    def get_mkt_line_by_mrid(self, mrid: str) -> MktLine | None:
        return Flowgate.mkt_line.get_by_mrid(self, mrid)

    def add_registered_inter_tie(self, registered_inter_tie: RegisteredInterTie) -> Self:
        return Flowgate.registered_inter_tie.add(self, registered_inter_tie)

    def remove_registered_inter_tie(self, registered_inter_tie: RegisteredInterTie) -> Self:
        return Flowgate.registered_inter_tie.remove(self, registered_inter_tie)

    def clear_registered_inter_tie(self) -> Self:
        return Flowgate.registered_inter_tie.clear(self)

    def num_registered_inter_tie(self) -> int:
        return Flowgate.registered_inter_tie.count(self)

    def get_registered_inter_tie_by_mrid(self, mrid: str) -> RegisteredInterTie | None:
        return Flowgate.registered_inter_tie.get_by_mrid(self, mrid)

    def add_ftr(self, ftr: FTR) -> Self:
        return Flowgate.ftrs.add(self, ftr)

    def remove_ftr(self, ftr: FTR) -> Self:
        return Flowgate.ftrs.remove(self, ftr)

    def clear_ftrs(self) -> Self:
        return Flowgate.ftrs.clear(self)

    def num_ftr(self) -> int:
        return Flowgate.ftrs.count(self)

    def get_ftr_by_mrid(self, mrid: str) -> FTR | None:
        return Flowgate.ftrs.get_by_mrid(self, mrid)

    def add_mkt_terminal(self, mkt_terminal: MktTerminal) -> Self:
        return Flowgate.mkt_terminal.add(self, mkt_terminal)

    def remove_mkt_terminal(self, mkt_terminal: MktTerminal) -> Self:
        return Flowgate.mkt_terminal.remove(self, mkt_terminal)

    def clear_mkt_terminal(self) -> Self:
        return Flowgate.mkt_terminal.clear(self)

    def num_mkt_terminal(self) -> int:
        return Flowgate.mkt_terminal.count(self)

    def get_mkt_terminal_by_mrid(self, mrid: str) -> MktTerminal | None:
        return Flowgate.mkt_terminal.get_by_mrid(self, mrid)

    def add_mkt_power_transformer(self, mkt_power_transformer: MktPowerTransformer) -> Self:
        return Flowgate.mkt_power_transformer.add(self, mkt_power_transformer)

    def remove_mkt_power_transformer(self, mkt_power_transformer: MktPowerTransformer) -> Self:
        return Flowgate.mkt_power_transformer.remove(self, mkt_power_transformer)

    def clear_mkt_power_transformer(self) -> Self:
        return Flowgate.mkt_power_transformer.clear(self)

    def num_mkt_power_transformer(self) -> int:
        return Flowgate.mkt_power_transformer.count(self)

    def get_mkt_power_transformer_by_mrid(self, mrid: str) -> MktPowerTransformer | None:
        return Flowgate.mkt_power_transformer.get_by_mrid(self, mrid)

    def add_inter_tie_result(self, inter_tie_result: InterTieResults) -> Self:
        return Flowgate.inter_tie_results.add(self, inter_tie_result)

    def remove_inter_tie_result(self, inter_tie_result: InterTieResults) -> Self:
        return Flowgate.inter_tie_results.remove(self, inter_tie_result)

    def clear_inter_tie_results(self) -> Self:
        return Flowgate.inter_tie_results.clear(self)

    def num_inter_tie_result(self) -> int:
        return Flowgate.inter_tie_results.count(self)

    def add_flowgate_relief(self, flowgate_relief: FlowgateRelief) -> Self:
        return Flowgate.flowgate_relief.add(self, flowgate_relief)

    def remove_flowgate_relief(self, flowgate_relief: FlowgateRelief) -> Self:
        return Flowgate.flowgate_relief.remove(self, flowgate_relief)

    def clear_flowgate_relief(self) -> Self:
        return Flowgate.flowgate_relief.clear(self)

    def num_flowgate_relief(self) -> int:
        return Flowgate.flowgate_relief.count(self)
