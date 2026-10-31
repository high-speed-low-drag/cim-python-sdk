"""CIM class Terminal (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.acdc_terminal import ACDCTerminal

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.bushing import Bushing
    from cim_python_sdk.model.iec61970.base.auxiliary_equipment.auxiliary_equipment import (
        AuxiliaryEquipment,
    )
    from cim_python_sdk.model.iec61970.base.control_area.tie_flow import TieFlow
    from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment
    from cim_python_sdk.model.iec61970.base.core.connectivity_node import ConnectivityNode
    from cim_python_sdk.model.iec61970.base.core.feeder import Feeder
    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode
    from cim_python_sdk.model.iec61970.base.dc.acdc_converter import ACDCConverter
    from cim_python_sdk.model.iec61970.base.faults.equipment_fault import EquipmentFault
    from cim_python_sdk.model.iec61970.base.operational_limits.branch_group_terminal import (
        BranchGroupTerminal,
    )
    from cim_python_sdk.model.iec61970.base.state_variables.sv_power_flow import SvPowerFlow
    from cim_python_sdk.model.iec61970.base.topology.topological_node import TopologicalNode
    from cim_python_sdk.model.iec61970.base.wires.mutual_coupling import MutualCoupling
    from cim_python_sdk.model.iec61970.base.wires.regulating_control import RegulatingControl
    from cim_python_sdk.model.iec61970.base.wires.transformer_end import TransformerEnd
    from cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_input_signal import (
        RemoteInputSignal,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.feeder.circuit import Circuit
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_terminal import PinTerminal


class Terminal(ACDCTerminal):
    """An AC electrical connection point to a piece of conducting equipment. Terminals are
    connected at physical connection points called connectivity nodes."""

    __slots__ = (
        "_auxiliary_equipment",
        "_branch_group_terminal",
        "_bushing",
        "_circuit",
        "_conducting_equipment",
        "_connectivity_node",
        "_converter_dc_sides",
        "_equipment_faults",
        "_has_first_mutual_coupling",
        "_has_second_mutual_coupling",
        "_normal_head_feeder",
        "_pin_terminal",
        "_regulating_control",
        "_remote_input_signal",
        "_sv_power_flow",
        "_tie_flow",
        "_topological_node",
        "_transformer_end",
        "phases",
    )

    phases: PhaseCode | None

    bushing: One[Bushing] = One(
        EndMeta(
            name="bushing",
            cim_role="Bushing",
            target="cim_python_sdk.model.iec61968.assets.bushing:Bushing",
            many=False,
            lower=0,
            upper=1,
            inverse="terminal",
            aggregation="none",
        )
    )
    equipment_faults: Many[EquipmentFault] = Many(
        EndMeta(
            name="equipment_faults",
            cim_role="EquipmentFaults",
            target="cim_python_sdk.model.iec61970.base.faults.equipment_fault:EquipmentFault",
            many=True,
            lower=0,
            upper=None,
            inverse="terminal",
            aggregation="none",
        )
    )
    tie_flow: Many[TieFlow] = Many(
        EndMeta(
            name="tie_flow",
            cim_role="TieFlow",
            target="cim_python_sdk.model.iec61970.base.control_area.tie_flow:TieFlow",
            many=True,
            lower=0,
            upper=2,
            inverse="terminal",
            aggregation="none",
        )
    )
    regulating_control: Many[RegulatingControl] = Many(
        EndMeta(
            name="regulating_control",
            cim_role="RegulatingControl",
            target="cim_python_sdk.model.iec61970.base.wires.regulating_control:RegulatingControl",
            many=True,
            lower=0,
            upper=None,
            inverse="terminal",
            aggregation="none",
        )
    )
    has_second_mutual_coupling: Many[MutualCoupling] = Many(
        EndMeta(
            name="has_second_mutual_coupling",
            cim_role="HasSecondMutualCoupling",
            target="cim_python_sdk.model.iec61970.base.wires.mutual_coupling:MutualCoupling",
            many=True,
            lower=0,
            upper=None,
            inverse="second_terminal",
            aggregation="none",
        )
    )
    auxiliary_equipment: Many[AuxiliaryEquipment] = Many(
        EndMeta(
            name="auxiliary_equipment",
            cim_role="AuxiliaryEquipment",
            target="cim_python_sdk.model.iec61970.base.auxiliary_equipment.auxiliary_equipment:AuxiliaryEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="terminal",
            aggregation="none",
        )
    )
    conducting_equipment: One[ConductingEquipment] = One(
        EndMeta(
            name="conducting_equipment",
            cim_role="ConductingEquipment",
            target="cim_python_sdk.model.iec61970.base.core.conducting_equipment:ConductingEquipment",
            many=False,
            lower=1,
            upper=1,
            inverse="terminals",
            aggregation="none",
        )
    )
    sv_power_flow: Many[SvPowerFlow] = Many(
        EndMeta(
            name="sv_power_flow",
            cim_role="SvPowerFlow",
            target="cim_python_sdk.model.iec61970.base.state_variables.sv_power_flow:SvPowerFlow",
            many=True,
            lower=0,
            upper=None,
            inverse="terminal",
            aggregation="none",
        )
    )
    circuit: One[Circuit] = One(
        EndMeta(
            name="circuit",
            cim_role="Circuit",
            target="cim_python_sdk.model.iec61970.inf_iec61970.feeder.circuit:Circuit",
            many=False,
            lower=0,
            upper=1,
            inverse="end_terminal",
            aggregation="none",
        )
    )
    converter_dc_sides: Many[ACDCConverter] = Many(
        EndMeta(
            name="converter_dc_sides",
            cim_role="ConverterDCSides",
            target="cim_python_sdk.model.iec61970.base.dc.acdc_converter:ACDCConverter",
            many=True,
            lower=0,
            upper=None,
            inverse="pcc_terminal",
            aggregation="none",
        )
    )
    pin_terminal: Many[PinTerminal] = Many(
        EndMeta(
            name="pin_terminal",
            cim_role="PinTerminal",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_terminal:PinTerminal",
            many=True,
            lower=0,
            upper=None,
            inverse="terminal",
            aggregation="none",
        )
    )
    remote_input_signal: Many[RemoteInputSignal] = Many(
        EndMeta(
            name="remote_input_signal",
            cim_role="RemoteInputSignal",
            target="cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_input_signal:RemoteInputSignal",
            many=True,
            lower=0,
            upper=None,
            inverse="terminal",
            aggregation="none",
        )
    )
    normal_head_feeder: One[Feeder] = One(
        EndMeta(
            name="normal_head_feeder",
            cim_role="NormalHeadFeeder",
            target="cim_python_sdk.model.iec61970.base.core.feeder:Feeder",
            many=False,
            lower=0,
            upper=1,
            inverse="normal_head_terminal",
            aggregation="none",
        )
    )
    connectivity_node: One[ConnectivityNode] = One(
        EndMeta(
            name="connectivity_node",
            cim_role="ConnectivityNode",
            target="cim_python_sdk.model.iec61970.base.core.connectivity_node:ConnectivityNode",
            many=False,
            lower=0,
            upper=1,
            inverse="terminals",
            aggregation="none",
        )
    )
    branch_group_terminal: Many[BranchGroupTerminal] = Many(
        EndMeta(
            name="branch_group_terminal",
            cim_role="BranchGroupTerminal",
            target="cim_python_sdk.model.iec61970.base.operational_limits.branch_group_terminal:BranchGroupTerminal",
            many=True,
            lower=0,
            upper=None,
            inverse="terminal",
            aggregation="none",
        )
    )
    transformer_end: Many[TransformerEnd] = Many(
        EndMeta(
            name="transformer_end",
            cim_role="TransformerEnd",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_end:TransformerEnd",
            many=True,
            lower=0,
            upper=None,
            inverse="terminal",
            aggregation="none",
        )
    )
    has_first_mutual_coupling: Many[MutualCoupling] = Many(
        EndMeta(
            name="has_first_mutual_coupling",
            cim_role="HasFirstMutualCoupling",
            target="cim_python_sdk.model.iec61970.base.wires.mutual_coupling:MutualCoupling",
            many=True,
            lower=0,
            upper=None,
            inverse="first_terminal",
            aggregation="none",
        )
    )
    topological_node: One[TopologicalNode] = One(
        EndMeta(
            name="topological_node",
            cim_role="TopologicalNode",
            target="cim_python_sdk.model.iec61970.base.topology.topological_node:TopologicalNode",
            many=False,
            lower=0,
            upper=1,
            inverse="terminal",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Terminal",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{1A0F8321-5E77-4d68-BE29-B36FA31549DC}",
        attributes=(AttrMeta("phases", "phases", "PhaseCode", 0, 1, "enumeration"),),
        ends=(
            bushing.meta,
            equipment_faults.meta,
            tie_flow.meta,
            regulating_control.meta,
            has_second_mutual_coupling.meta,
            auxiliary_equipment.meta,
            conducting_equipment.meta,
            sv_power_flow.meta,
            circuit.meta,
            converter_dc_sides.meta,
            pin_terminal.meta,
            remote_input_signal.meta,
            normal_head_feeder.meta,
            connectivity_node.meta,
            branch_group_terminal.meta,
            transformer_end.meta,
            has_first_mutual_coupling.meta,
            topological_node.meta,
        ),
    )

    def __init__(
        self,
        *,
        phases: PhaseCode | None = None,
        bushing: Bushing | None = None,
        equipment_faults: Iterable[EquipmentFault] | None = None,
        tie_flow: Iterable[TieFlow] | None = None,
        regulating_control: Iterable[RegulatingControl] | None = None,
        has_second_mutual_coupling: Iterable[MutualCoupling] | None = None,
        auxiliary_equipment: Iterable[AuxiliaryEquipment] | None = None,
        conducting_equipment: ConductingEquipment | None = None,
        sv_power_flow: Iterable[SvPowerFlow] | None = None,
        circuit: Circuit | None = None,
        converter_dc_sides: Iterable[ACDCConverter] | None = None,
        pin_terminal: Iterable[PinTerminal] | None = None,
        remote_input_signal: Iterable[RemoteInputSignal] | None = None,
        normal_head_feeder: Feeder | None = None,
        connectivity_node: ConnectivityNode | None = None,
        branch_group_terminal: Iterable[BranchGroupTerminal] | None = None,
        transformer_end: Iterable[TransformerEnd] | None = None,
        has_first_mutual_coupling: Iterable[MutualCoupling] | None = None,
        topological_node: TopologicalNode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.phases = phases
        if bushing is not None:
            self.bushing = bushing
        if equipment_faults is not None:
            Terminal.equipment_faults.extend(self, equipment_faults)
        if tie_flow is not None:
            Terminal.tie_flow.extend(self, tie_flow)
        if regulating_control is not None:
            Terminal.regulating_control.extend(self, regulating_control)
        if has_second_mutual_coupling is not None:
            Terminal.has_second_mutual_coupling.extend(self, has_second_mutual_coupling)
        if auxiliary_equipment is not None:
            Terminal.auxiliary_equipment.extend(self, auxiliary_equipment)
        if conducting_equipment is not None:
            self.conducting_equipment = conducting_equipment
        if sv_power_flow is not None:
            Terminal.sv_power_flow.extend(self, sv_power_flow)
        if circuit is not None:
            self.circuit = circuit
        if converter_dc_sides is not None:
            Terminal.converter_dc_sides.extend(self, converter_dc_sides)
        if pin_terminal is not None:
            Terminal.pin_terminal.extend(self, pin_terminal)
        if remote_input_signal is not None:
            Terminal.remote_input_signal.extend(self, remote_input_signal)
        if normal_head_feeder is not None:
            self.normal_head_feeder = normal_head_feeder
        if connectivity_node is not None:
            self.connectivity_node = connectivity_node
        if branch_group_terminal is not None:
            Terminal.branch_group_terminal.extend(self, branch_group_terminal)
        if transformer_end is not None:
            Terminal.transformer_end.extend(self, transformer_end)
        if has_first_mutual_coupling is not None:
            Terminal.has_first_mutual_coupling.extend(self, has_first_mutual_coupling)
        if topological_node is not None:
            self.topological_node = topological_node

    def add_equipment_fault(self, equipment_fault: EquipmentFault) -> Self:
        return Terminal.equipment_faults.add(self, equipment_fault)

    def remove_equipment_fault(self, equipment_fault: EquipmentFault) -> Self:
        return Terminal.equipment_faults.remove(self, equipment_fault)

    def clear_equipment_faults(self) -> Self:
        return Terminal.equipment_faults.clear(self)

    def num_equipment_fault(self) -> int:
        return Terminal.equipment_faults.count(self)

    def get_equipment_fault_by_mrid(self, mrid: str) -> EquipmentFault | None:
        return Terminal.equipment_faults.get_by_mrid(self, mrid)

    def add_tie_flow(self, tie_flow: TieFlow) -> Self:
        return Terminal.tie_flow.add(self, tie_flow)

    def remove_tie_flow(self, tie_flow: TieFlow) -> Self:
        return Terminal.tie_flow.remove(self, tie_flow)

    def clear_tie_flow(self) -> Self:
        return Terminal.tie_flow.clear(self)

    def num_tie_flow(self) -> int:
        return Terminal.tie_flow.count(self)

    def get_tie_flow_by_mrid(self, mrid: str) -> TieFlow | None:
        return Terminal.tie_flow.get_by_mrid(self, mrid)

    def add_regulating_control(self, regulating_control: RegulatingControl) -> Self:
        return Terminal.regulating_control.add(self, regulating_control)

    def remove_regulating_control(self, regulating_control: RegulatingControl) -> Self:
        return Terminal.regulating_control.remove(self, regulating_control)

    def clear_regulating_control(self) -> Self:
        return Terminal.regulating_control.clear(self)

    def num_regulating_control(self) -> int:
        return Terminal.regulating_control.count(self)

    def get_regulating_control_by_mrid(self, mrid: str) -> RegulatingControl | None:
        return Terminal.regulating_control.get_by_mrid(self, mrid)

    def add_has_second_mutual_coupling(self, has_second_mutual_coupling: MutualCoupling) -> Self:
        return Terminal.has_second_mutual_coupling.add(self, has_second_mutual_coupling)

    def remove_has_second_mutual_coupling(self, has_second_mutual_coupling: MutualCoupling) -> Self:
        return Terminal.has_second_mutual_coupling.remove(self, has_second_mutual_coupling)

    def clear_has_second_mutual_coupling(self) -> Self:
        return Terminal.has_second_mutual_coupling.clear(self)

    def num_has_second_mutual_coupling(self) -> int:
        return Terminal.has_second_mutual_coupling.count(self)

    def get_has_second_mutual_coupling_by_mrid(self, mrid: str) -> MutualCoupling | None:
        return Terminal.has_second_mutual_coupling.get_by_mrid(self, mrid)

    def add_auxiliary_equipment(self, auxiliary_equipment: AuxiliaryEquipment) -> Self:
        return Terminal.auxiliary_equipment.add(self, auxiliary_equipment)

    def remove_auxiliary_equipment(self, auxiliary_equipment: AuxiliaryEquipment) -> Self:
        return Terminal.auxiliary_equipment.remove(self, auxiliary_equipment)

    def clear_auxiliary_equipment(self) -> Self:
        return Terminal.auxiliary_equipment.clear(self)

    def num_auxiliary_equipment(self) -> int:
        return Terminal.auxiliary_equipment.count(self)

    def get_auxiliary_equipment_by_mrid(self, mrid: str) -> AuxiliaryEquipment | None:
        return Terminal.auxiliary_equipment.get_by_mrid(self, mrid)

    def add_sv_power_flow(self, sv_power_flow: SvPowerFlow) -> Self:
        return Terminal.sv_power_flow.add(self, sv_power_flow)

    def remove_sv_power_flow(self, sv_power_flow: SvPowerFlow) -> Self:
        return Terminal.sv_power_flow.remove(self, sv_power_flow)

    def clear_sv_power_flow(self) -> Self:
        return Terminal.sv_power_flow.clear(self)

    def num_sv_power_flow(self) -> int:
        return Terminal.sv_power_flow.count(self)

    def add_converter_dc_side(self, converter_dc_side: ACDCConverter) -> Self:
        return Terminal.converter_dc_sides.add(self, converter_dc_side)

    def remove_converter_dc_side(self, converter_dc_side: ACDCConverter) -> Self:
        return Terminal.converter_dc_sides.remove(self, converter_dc_side)

    def clear_converter_dc_sides(self) -> Self:
        return Terminal.converter_dc_sides.clear(self)

    def num_converter_dc_side(self) -> int:
        return Terminal.converter_dc_sides.count(self)

    def get_converter_dc_side_by_mrid(self, mrid: str) -> ACDCConverter | None:
        return Terminal.converter_dc_sides.get_by_mrid(self, mrid)

    def add_pin_terminal(self, pin_terminal: PinTerminal) -> Self:
        return Terminal.pin_terminal.add(self, pin_terminal)

    def remove_pin_terminal(self, pin_terminal: PinTerminal) -> Self:
        return Terminal.pin_terminal.remove(self, pin_terminal)

    def clear_pin_terminal(self) -> Self:
        return Terminal.pin_terminal.clear(self)

    def num_pin_terminal(self) -> int:
        return Terminal.pin_terminal.count(self)

    def get_pin_terminal_by_mrid(self, mrid: str) -> PinTerminal | None:
        return Terminal.pin_terminal.get_by_mrid(self, mrid)

    def add_remote_input_signal(self, remote_input_signal: RemoteInputSignal) -> Self:
        return Terminal.remote_input_signal.add(self, remote_input_signal)

    def remove_remote_input_signal(self, remote_input_signal: RemoteInputSignal) -> Self:
        return Terminal.remote_input_signal.remove(self, remote_input_signal)

    def clear_remote_input_signal(self) -> Self:
        return Terminal.remote_input_signal.clear(self)

    def num_remote_input_signal(self) -> int:
        return Terminal.remote_input_signal.count(self)

    def get_remote_input_signal_by_mrid(self, mrid: str) -> RemoteInputSignal | None:
        return Terminal.remote_input_signal.get_by_mrid(self, mrid)

    def add_branch_group_terminal(self, branch_group_terminal: BranchGroupTerminal) -> Self:
        return Terminal.branch_group_terminal.add(self, branch_group_terminal)

    def remove_branch_group_terminal(self, branch_group_terminal: BranchGroupTerminal) -> Self:
        return Terminal.branch_group_terminal.remove(self, branch_group_terminal)

    def clear_branch_group_terminal(self) -> Self:
        return Terminal.branch_group_terminal.clear(self)

    def num_branch_group_terminal(self) -> int:
        return Terminal.branch_group_terminal.count(self)

    def add_transformer_end(self, transformer_end: TransformerEnd) -> Self:
        return Terminal.transformer_end.add(self, transformer_end)

    def remove_transformer_end(self, transformer_end: TransformerEnd) -> Self:
        return Terminal.transformer_end.remove(self, transformer_end)

    def clear_transformer_end(self) -> Self:
        return Terminal.transformer_end.clear(self)

    def num_transformer_end(self) -> int:
        return Terminal.transformer_end.count(self)

    def get_transformer_end_by_mrid(self, mrid: str) -> TransformerEnd | None:
        return Terminal.transformer_end.get_by_mrid(self, mrid)

    def add_has_first_mutual_coupling(self, has_first_mutual_coupling: MutualCoupling) -> Self:
        return Terminal.has_first_mutual_coupling.add(self, has_first_mutual_coupling)

    def remove_has_first_mutual_coupling(self, has_first_mutual_coupling: MutualCoupling) -> Self:
        return Terminal.has_first_mutual_coupling.remove(self, has_first_mutual_coupling)

    def clear_has_first_mutual_coupling(self) -> Self:
        return Terminal.has_first_mutual_coupling.clear(self)

    def num_has_first_mutual_coupling(self) -> int:
        return Terminal.has_first_mutual_coupling.count(self)

    def get_has_first_mutual_coupling_by_mrid(self, mrid: str) -> MutualCoupling | None:
        return Terminal.has_first_mutual_coupling.get_by_mrid(self, mrid)
