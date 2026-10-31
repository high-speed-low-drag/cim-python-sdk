"""CIM class ConductingEquipment (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.equipment import Equipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.ground_action import GroundAction
    from cim_python_sdk.model.iec61968.operations.jumper_action import JumperAction
    from cim_python_sdk.model.iec61968.operations.outage import Outage
    from cim_python_sdk.model.iec61970.base.core.base_voltage import BaseVoltage
    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal
    from cim_python_sdk.model.iec61970.base.protection.protection_equipment import (
        ProtectionEquipment,
    )
    from cim_python_sdk.model.iec61970.base.state_variables.sv_status import SvStatus
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_adjustment import (
        ProtectiveActionAdjustment,
    )


class ConductingEquipment(Equipment):
    """The parts of the AC power system that are designed to carry current or that are
    conductively connected through terminals."""

    __slots__ = (
        "_base_voltage",
        "_grounding_action",
        "_jumping_action",
        "_outage",
        "_protection_equipments",
        "_protective_action_adjustment",
        "_sv_status",
        "_terminals",
    )

    protection_equipments: Many[ProtectionEquipment] = Many(
        EndMeta(
            name="protection_equipments",
            cim_role="ProtectionEquipments",
            target="cim_python_sdk.model.iec61970.base.protection.protection_equipment:ProtectionEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="conducting_equipments",
            aggregation="none",
        )
    )
    protective_action_adjustment: Many[ProtectiveActionAdjustment] = Many(
        EndMeta(
            name="protective_action_adjustment",
            cim_role="ProtectiveActionAdjustment",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_adjustment:ProtectiveActionAdjustment",
            many=True,
            lower=0,
            upper=None,
            inverse="conducting_equipment",
            aggregation="none",
        )
    )
    jumping_action: One[JumperAction] = One(
        EndMeta(
            name="jumping_action",
            cim_role="JumpingAction",
            target="cim_python_sdk.model.iec61968.operations.jumper_action:JumperAction",
            many=False,
            lower=0,
            upper=1,
            inverse="jumped_equipments",
            aggregation="none",
        )
    )
    terminals: Many[Terminal] = Many(
        EndMeta(
            name="terminals",
            cim_role="Terminals",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=True,
            lower=0,
            upper=None,
            inverse="conducting_equipment",
            aggregation="none",
        )
    )
    sv_status: Many[SvStatus] = Many(
        EndMeta(
            name="sv_status",
            cim_role="SvStatus",
            target="cim_python_sdk.model.iec61970.base.state_variables.sv_status:SvStatus",
            many=True,
            lower=0,
            upper=None,
            inverse="conducting_equipment",
            aggregation="none",
        )
    )
    base_voltage: One[BaseVoltage] = One(
        EndMeta(
            name="base_voltage",
            cim_role="BaseVoltage",
            target="cim_python_sdk.model.iec61970.base.core.base_voltage:BaseVoltage",
            many=False,
            lower=0,
            upper=1,
            inverse="conducting_equipment",
            aggregation="none",
        )
    )
    grounding_action: One[GroundAction] = One(
        EndMeta(
            name="grounding_action",
            cim_role="GroundingAction",
            target="cim_python_sdk.model.iec61968.operations.ground_action:GroundAction",
            many=False,
            lower=0,
            upper=1,
            inverse="grounded_equipment",
            aggregation="none",
        )
    )
    outage: One[Outage] = One(
        EndMeta(
            name="outage",
            cim_role="Outage",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=False,
            lower=0,
            upper=1,
            inverse="outage_isolation_equipment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConductingEquipment",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{7C5F19FB-5253-430c-8E53-BDCF7EBCE4C1}",
        ends=(
            protection_equipments.meta,
            protective_action_adjustment.meta,
            jumping_action.meta,
            terminals.meta,
            sv_status.meta,
            base_voltage.meta,
            grounding_action.meta,
            outage.meta,
        ),
    )

    def __init__(
        self,
        *,
        protection_equipments: Iterable[ProtectionEquipment] | None = None,
        protective_action_adjustment: Iterable[ProtectiveActionAdjustment] | None = None,
        jumping_action: JumperAction | None = None,
        terminals: Iterable[Terminal] | None = None,
        sv_status: Iterable[SvStatus] | None = None,
        base_voltage: BaseVoltage | None = None,
        grounding_action: GroundAction | None = None,
        outage: Outage | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if protection_equipments is not None:
            ConductingEquipment.protection_equipments.extend(self, protection_equipments)
        if protective_action_adjustment is not None:
            ConductingEquipment.protective_action_adjustment.extend(
                self, protective_action_adjustment
            )
        if jumping_action is not None:
            self.jumping_action = jumping_action
        if terminals is not None:
            ConductingEquipment.terminals.extend(self, terminals)
        if sv_status is not None:
            ConductingEquipment.sv_status.extend(self, sv_status)
        if base_voltage is not None:
            self.base_voltage = base_voltage
        if grounding_action is not None:
            self.grounding_action = grounding_action
        if outage is not None:
            self.outage = outage

    def add_protection_equipment(self, protection_equipment: ProtectionEquipment) -> Self:
        return ConductingEquipment.protection_equipments.add(self, protection_equipment)

    def remove_protection_equipment(self, protection_equipment: ProtectionEquipment) -> Self:
        return ConductingEquipment.protection_equipments.remove(self, protection_equipment)

    def clear_protection_equipments(self) -> Self:
        return ConductingEquipment.protection_equipments.clear(self)

    def num_protection_equipment(self) -> int:
        return ConductingEquipment.protection_equipments.count(self)

    def get_protection_equipment_by_mrid(self, mrid: str) -> ProtectionEquipment | None:
        return ConductingEquipment.protection_equipments.get_by_mrid(self, mrid)

    def add_protective_action_adjustment(
        self, protective_action_adjustment: ProtectiveActionAdjustment
    ) -> Self:
        return ConductingEquipment.protective_action_adjustment.add(
            self, protective_action_adjustment
        )

    def remove_protective_action_adjustment(
        self, protective_action_adjustment: ProtectiveActionAdjustment
    ) -> Self:
        return ConductingEquipment.protective_action_adjustment.remove(
            self, protective_action_adjustment
        )

    def clear_protective_action_adjustment(self) -> Self:
        return ConductingEquipment.protective_action_adjustment.clear(self)

    def num_protective_action_adjustment(self) -> int:
        return ConductingEquipment.protective_action_adjustment.count(self)

    def get_protective_action_adjustment_by_mrid(
        self, mrid: str
    ) -> ProtectiveActionAdjustment | None:
        return ConductingEquipment.protective_action_adjustment.get_by_mrid(self, mrid)

    def add_terminal(self, terminal: Terminal) -> Self:
        return ConductingEquipment.terminals.add(self, terminal)

    def remove_terminal(self, terminal: Terminal) -> Self:
        return ConductingEquipment.terminals.remove(self, terminal)

    def clear_terminals(self) -> Self:
        return ConductingEquipment.terminals.clear(self)

    def num_terminal(self) -> int:
        return ConductingEquipment.terminals.count(self)

    def get_terminal_by_mrid(self, mrid: str) -> Terminal | None:
        return ConductingEquipment.terminals.get_by_mrid(self, mrid)

    def add_sv_status(self, sv_status: SvStatus) -> Self:
        return ConductingEquipment.sv_status.add(self, sv_status)

    def remove_sv_status(self, sv_status: SvStatus) -> Self:
        return ConductingEquipment.sv_status.remove(self, sv_status)

    def clear_sv_status(self) -> Self:
        return ConductingEquipment.sv_status.clear(self)

    def num_sv_status(self) -> int:
        return ConductingEquipment.sv_status.count(self)
