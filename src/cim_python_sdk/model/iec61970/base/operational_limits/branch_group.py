"""CIM class BranchGroup (TC57CIM/IEC61970/Base/OperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.operational_limits.branch_group_terminal import (
        BranchGroupTerminal,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_branch_group import PinBranchGroup


class BranchGroup(IdentifiedObject):
    """A group of branch terminals whose directed flow summation is to be monitored. A branch
    group need not form a cutset of the network."""

    __slots__ = (
        "_branch_group_terminal",
        "_pin_branch_group",
        "maximum_active_power",
        "maximum_reactive_power",
        "minimum_active_power",
        "minimum_reactive_power",
        "monitor_active_power",
        "monitor_reactive_power",
    )

    maximum_active_power: float | None  # ActivePower
    maximum_reactive_power: float | None  # ReactivePower
    minimum_active_power: float | None  # ActivePower
    minimum_reactive_power: float | None  # ReactivePower
    monitor_active_power: bool | None
    monitor_reactive_power: bool | None

    branch_group_terminal: Many[BranchGroupTerminal] = Many(
        EndMeta(
            name="branch_group_terminal",
            cim_role="BranchGroupTerminal",
            target="cim_python_sdk.model.iec61970.base.operational_limits.branch_group_terminal:BranchGroupTerminal",
            many=True,
            lower=0,
            upper=None,
            inverse="branch_group",
            aggregation="shared",
        )
    )
    pin_branch_group: Many[PinBranchGroup] = Many(
        EndMeta(
            name="pin_branch_group",
            cim_role="PinBranchGroup",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_branch_group:PinBranchGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="branch_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BranchGroup",
        package="TC57CIM/IEC61970/Base/OperationalLimits",
        guid="{A795B546-34EE-419f-B392-039926A2C6E3}",
        attributes=(
            AttrMeta(
                "maximum_active_power", "maximumActivePower", "ActivePower", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "maximum_reactive_power",
                "maximumReactivePower",
                "ReactivePower",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "minimum_active_power", "minimumActivePower", "ActivePower", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "minimum_reactive_power",
                "minimumReactivePower",
                "ReactivePower",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("monitor_active_power", "monitorActivePower", "bool", 0, 1, "primitive"),
            AttrMeta("monitor_reactive_power", "monitorReactivePower", "bool", 0, 1, "primitive"),
        ),
        ends=(
            branch_group_terminal.meta,
            pin_branch_group.meta,
        ),
    )

    def __init__(
        self,
        *,
        maximum_active_power: float | None = None,
        maximum_reactive_power: float | None = None,
        minimum_active_power: float | None = None,
        minimum_reactive_power: float | None = None,
        monitor_active_power: bool | None = None,
        monitor_reactive_power: bool | None = None,
        branch_group_terminal: Iterable[BranchGroupTerminal] | None = None,
        pin_branch_group: Iterable[PinBranchGroup] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.maximum_active_power = maximum_active_power
        self.maximum_reactive_power = maximum_reactive_power
        self.minimum_active_power = minimum_active_power
        self.minimum_reactive_power = minimum_reactive_power
        self.monitor_active_power = monitor_active_power
        self.monitor_reactive_power = monitor_reactive_power
        if branch_group_terminal is not None:
            BranchGroup.branch_group_terminal.extend(self, branch_group_terminal)
        if pin_branch_group is not None:
            BranchGroup.pin_branch_group.extend(self, pin_branch_group)

    def add_branch_group_terminal(self, branch_group_terminal: BranchGroupTerminal) -> Self:
        return BranchGroup.branch_group_terminal.add(self, branch_group_terminal)

    def remove_branch_group_terminal(self, branch_group_terminal: BranchGroupTerminal) -> Self:
        return BranchGroup.branch_group_terminal.remove(self, branch_group_terminal)

    def clear_branch_group_terminal(self) -> Self:
        return BranchGroup.branch_group_terminal.clear(self)

    def num_branch_group_terminal(self) -> int:
        return BranchGroup.branch_group_terminal.count(self)

    def add_pin_branch_group(self, pin_branch_group: PinBranchGroup) -> Self:
        return BranchGroup.pin_branch_group.add(self, pin_branch_group)

    def remove_pin_branch_group(self, pin_branch_group: PinBranchGroup) -> Self:
        return BranchGroup.pin_branch_group.remove(self, pin_branch_group)

    def clear_pin_branch_group(self) -> Self:
        return BranchGroup.pin_branch_group.clear(self)

    def num_pin_branch_group(self) -> int:
        return BranchGroup.pin_branch_group.count(self)

    def get_pin_branch_group_by_mrid(self, mrid: str) -> PinBranchGroup | None:
        return BranchGroup.pin_branch_group.get_by_mrid(self, mrid)
