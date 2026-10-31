"""CIM class EnergyGroup (TC57CIM/IEC61970/InfIEC61970/EnergyArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.control_area.control_area import ControlArea
    from cim_python_sdk.model.iec61970.base.state_variables.sv_power_flow import SvPowerFlow
    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.block_dispatch_instruction import (
        BlockDispatchInstruction,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_component import (
        EnergyComponent,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_type_reference import (
        EnergyTypeReference,
    )


class EnergyGroup(PowerSystemResource):
    """CIM class EnergyGroup."""

    __slots__ = (
        "_block_dispatch_instructions",
        "_control_area",
        "_energy_components",
        "_energy_type_reference",
        "_sv_power_flows",
        "is_slack",
        "p",
    )

    p: float | None  # ActivePower
    is_slack: bool | None

    energy_type_reference: One[EnergyTypeReference] = One(
        EndMeta(
            name="energy_type_reference",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_type_reference:EnergyTypeReference",
            many=False,
            lower=1,
            upper=1,
            inverse="energy_groups",
            aggregation="none",
        )
    )
    block_dispatch_instructions: Many[BlockDispatchInstruction] = Many(
        EndMeta(
            name="block_dispatch_instructions",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.block_dispatch_instruction:BlockDispatchInstruction",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_group",
            aggregation="none",
        )
    )
    energy_components: Many[EnergyComponent] = Many(
        EndMeta(
            name="energy_components",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_component:EnergyComponent",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_group",
            aggregation="none",
        )
    )
    sv_power_flows: Many[SvPowerFlow] = Many(
        EndMeta(
            name="sv_power_flows",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.base.state_variables.sv_power_flow:SvPowerFlow",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_group",
            aggregation="none",
        )
    )
    control_area: One[ControlArea] = One(
        EndMeta(
            name="control_area",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.base.control_area.control_area:ControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="energy_groups",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyGroup",
        package="TC57CIM/IEC61970/InfIEC61970/EnergyArea",
        guid="{13F95157-0F4C-4040-B1E9-C83D5F382D52}",
        attributes=(
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("is_slack", "isSlack", "bool", 0, 1, "primitive"),
        ),
        ends=(
            energy_type_reference.meta,
            block_dispatch_instructions.meta,
            energy_components.meta,
            sv_power_flows.meta,
            control_area.meta,
        ),
    )

    def __init__(
        self,
        *,
        p: float | None = None,
        is_slack: bool | None = None,
        energy_type_reference: EnergyTypeReference | None = None,
        block_dispatch_instructions: Iterable[BlockDispatchInstruction] | None = None,
        energy_components: Iterable[EnergyComponent] | None = None,
        sv_power_flows: Iterable[SvPowerFlow] | None = None,
        control_area: ControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.p = p
        self.is_slack = is_slack
        if energy_type_reference is not None:
            self.energy_type_reference = energy_type_reference
        if block_dispatch_instructions is not None:
            EnergyGroup.block_dispatch_instructions.extend(self, block_dispatch_instructions)
        if energy_components is not None:
            EnergyGroup.energy_components.extend(self, energy_components)
        if sv_power_flows is not None:
            EnergyGroup.sv_power_flows.extend(self, sv_power_flows)
        if control_area is not None:
            self.control_area = control_area

    def add_block_dispatch_instruction(
        self, block_dispatch_instruction: BlockDispatchInstruction
    ) -> Self:
        return EnergyGroup.block_dispatch_instructions.add(self, block_dispatch_instruction)

    def remove_block_dispatch_instruction(
        self, block_dispatch_instruction: BlockDispatchInstruction
    ) -> Self:
        return EnergyGroup.block_dispatch_instructions.remove(self, block_dispatch_instruction)

    def clear_block_dispatch_instructions(self) -> Self:
        return EnergyGroup.block_dispatch_instructions.clear(self)

    def num_block_dispatch_instruction(self) -> int:
        return EnergyGroup.block_dispatch_instructions.count(self)

    def get_block_dispatch_instruction_by_mrid(self, mrid: str) -> BlockDispatchInstruction | None:
        return EnergyGroup.block_dispatch_instructions.get_by_mrid(self, mrid)

    def add_energy_component(self, energy_component: EnergyComponent) -> Self:
        return EnergyGroup.energy_components.add(self, energy_component)

    def remove_energy_component(self, energy_component: EnergyComponent) -> Self:
        return EnergyGroup.energy_components.remove(self, energy_component)

    def clear_energy_components(self) -> Self:
        return EnergyGroup.energy_components.clear(self)

    def num_energy_component(self) -> int:
        return EnergyGroup.energy_components.count(self)

    def get_energy_component_by_mrid(self, mrid: str) -> EnergyComponent | None:
        return EnergyGroup.energy_components.get_by_mrid(self, mrid)

    def add_sv_power_flow(self, sv_power_flow: SvPowerFlow) -> Self:
        return EnergyGroup.sv_power_flows.add(self, sv_power_flow)

    def remove_sv_power_flow(self, sv_power_flow: SvPowerFlow) -> Self:
        return EnergyGroup.sv_power_flows.remove(self, sv_power_flow)

    def clear_sv_power_flows(self) -> Self:
        return EnergyGroup.sv_power_flows.clear(self)

    def num_sv_power_flow(self) -> int:
        return EnergyGroup.sv_power_flows.count(self)
