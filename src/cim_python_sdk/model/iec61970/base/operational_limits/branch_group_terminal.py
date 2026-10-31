"""CIM class BranchGroupTerminal (TC57CIM/IEC61970/Base/OperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal
    from cim_python_sdk.model.iec61970.base.operational_limits.branch_group import BranchGroup


class BranchGroupTerminal(CimObject):
    """A specific directed terminal flow for a branch group."""

    __slots__ = ("_branch_group", "_terminal", "positive_flow_in")

    positive_flow_in: bool | None

    branch_group: One[BranchGroup] = One(
        EndMeta(
            name="branch_group",
            cim_role="BranchGroup",
            target="cim_python_sdk.model.iec61970.base.operational_limits.branch_group:BranchGroup",
            many=False,
            lower=1,
            upper=1,
            inverse="branch_group_terminal",
            aggregation="none",
        )
    )
    terminal: One[Terminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=1,
            upper=1,
            inverse="branch_group_terminal",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BranchGroupTerminal",
        package="TC57CIM/IEC61970/Base/OperationalLimits",
        guid="{B0C18CF1-75AE-44f3-9466-ABD95FE287EC}",
        attributes=(AttrMeta("positive_flow_in", "positiveFlowIn", "bool", 0, 1, "primitive"),),
        ends=(
            branch_group.meta,
            terminal.meta,
        ),
    )

    def __init__(
        self,
        *,
        positive_flow_in: bool | None = None,
        branch_group: BranchGroup | None = None,
        terminal: Terminal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.positive_flow_in = positive_flow_in
        if branch_group is not None:
            self.branch_group = branch_group
        if terminal is not None:
            self.terminal = terminal
