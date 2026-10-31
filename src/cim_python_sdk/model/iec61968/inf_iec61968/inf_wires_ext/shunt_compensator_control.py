"""CIM class ShuntCompensatorControl (TC57CIM/IEC61968/InfIEC61968/InfWiresExt). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.regulating_control import RegulatingControl

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_info.shunt_compensator_info import ShuntCompensatorInfo
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.regulation_branch_kind import (
        RegulationBranchKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.shunt_impedance_control_kind import (
        ShuntImpedanceControlKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.shunt_impedance_local_control_kind import (
        ShuntImpedanceLocalControlKind,
    )
    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode


class ShuntCompensatorControl(RegulatingControl):
    """Distribution capacitor bank control settings."""

    __slots__ = (
        "_shunt_compensator_info",
        "branch_direct",
        "cell_size",
        "control_kind",
        "high_voltage_override",
        "local_control_kind",
        "local_off_level",
        "local_on_level",
        "local_override",
        "low_voltage_override",
        "max_switch_operation_count",
        "normal_open",
        "reg_branch",
        "reg_branch_end",
        "reg_branch_kind",
        "sensing_phase_code",
        "switch_operation_cycle",
        "v_reg_line_line",
    )

    control_kind: ShuntImpedanceControlKind | None
    local_control_kind: ShuntImpedanceLocalControlKind | None
    local_on_level: str | None
    local_off_level: str | None
    max_switch_operation_count: int | None
    switch_operation_cycle: float | None  # Hours
    normal_open: bool | None
    sensing_phase_code: PhaseCode | None
    v_reg_line_line: bool | None
    reg_branch: str | None
    reg_branch_kind: RegulationBranchKind | None
    branch_direct: int | None
    reg_branch_end: int | None
    local_override: bool | None
    low_voltage_override: float | None  # PU
    high_voltage_override: float | None  # PU
    cell_size: float | None  # ReactivePower

    shunt_compensator_info: One[ShuntCompensatorInfo] = One(
        EndMeta(
            name="shunt_compensator_info",
            cim_role="ShuntCompensatorInfo",
            target="cim_python_sdk.model.iec61968.asset_info.shunt_compensator_info:ShuntCompensatorInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="shunt_compensator_control",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ShuntCompensatorControl",
        package="TC57CIM/IEC61968/InfIEC61968/InfWiresExt",
        guid="{5FFFB760-AFCE-495a-8F94-95B84D23690E}",
        attributes=(
            AttrMeta(
                "control_kind", "controlKind", "ShuntImpedanceControlKind", 0, 1, "enumeration"
            ),
            AttrMeta(
                "local_control_kind",
                "localControlKind",
                "ShuntImpedanceLocalControlKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("local_on_level", "localOnLevel", "str", 0, 1, "primitive"),
            AttrMeta("local_off_level", "localOffLevel", "str", 0, 1, "primitive"),
            AttrMeta(
                "max_switch_operation_count", "maxSwitchOperationCount", "int", 0, 1, "primitive"
            ),
            AttrMeta(
                "switch_operation_cycle", "switchOperationCycle", "Hours", 0, 1, "cimdatatype"
            ),
            AttrMeta("normal_open", "normalOpen", "bool", 0, 1, "primitive"),
            AttrMeta("sensing_phase_code", "sensingPhaseCode", "PhaseCode", 0, 1, "enumeration"),
            AttrMeta("v_reg_line_line", "vRegLineLine", "bool", 0, 1, "primitive"),
            AttrMeta("reg_branch", "regBranch", "str", 0, 1, "primitive"),
            AttrMeta(
                "reg_branch_kind", "regBranchKind", "RegulationBranchKind", 0, 1, "enumeration"
            ),
            AttrMeta("branch_direct", "branchDirect", "int", 0, 1, "primitive"),
            AttrMeta("reg_branch_end", "regBranchEnd", "int", 0, 1, "primitive"),
            AttrMeta("local_override", "localOverride", "bool", 0, 1, "primitive"),
            AttrMeta("low_voltage_override", "lowVoltageOverride", "PU", 0, 1, "cimdatatype"),
            AttrMeta("high_voltage_override", "highVoltageOverride", "PU", 0, 1, "cimdatatype"),
            AttrMeta("cell_size", "cellSize", "ReactivePower", 0, 1, "cimdatatype"),
        ),
        ends=(shunt_compensator_info.meta,),
    )

    def __init__(
        self,
        *,
        control_kind: ShuntImpedanceControlKind | None = None,
        local_control_kind: ShuntImpedanceLocalControlKind | None = None,
        local_on_level: str | None = None,
        local_off_level: str | None = None,
        max_switch_operation_count: int | None = None,
        switch_operation_cycle: float | None = None,
        normal_open: bool | None = None,
        sensing_phase_code: PhaseCode | None = None,
        v_reg_line_line: bool | None = None,
        reg_branch: str | None = None,
        reg_branch_kind: RegulationBranchKind | None = None,
        branch_direct: int | None = None,
        reg_branch_end: int | None = None,
        local_override: bool | None = None,
        low_voltage_override: float | None = None,
        high_voltage_override: float | None = None,
        cell_size: float | None = None,
        shunt_compensator_info: ShuntCompensatorInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.control_kind = control_kind
        self.local_control_kind = local_control_kind
        self.local_on_level = local_on_level
        self.local_off_level = local_off_level
        self.max_switch_operation_count = max_switch_operation_count
        self.switch_operation_cycle = switch_operation_cycle
        self.normal_open = normal_open
        self.sensing_phase_code = sensing_phase_code
        self.v_reg_line_line = v_reg_line_line
        self.reg_branch = reg_branch
        self.reg_branch_kind = reg_branch_kind
        self.branch_direct = branch_direct
        self.reg_branch_end = reg_branch_end
        self.local_override = local_override
        self.low_voltage_override = low_voltage_override
        self.high_voltage_override = high_voltage_override
        self.cell_size = cell_size
        if shunt_compensator_info is not None:
            self.shunt_compensator_info = shunt_compensator_info
