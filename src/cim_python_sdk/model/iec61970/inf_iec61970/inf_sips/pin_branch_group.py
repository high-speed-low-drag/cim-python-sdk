"""CIM class PinBranchGroup (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate_input_pin import GateInputPin

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.operational_limits.branch_group import BranchGroup
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_branch_group_kind import (
        PinBranchGroupKind,
    )


class PinBranchGroup(GateInputPin):
    """Value associated with branch group is used as compare."""

    __slots__ = ("_branch_group", "kind")

    kind: PinBranchGroupKind | None

    branch_group: One[BranchGroup] = One(
        EndMeta(
            name="branch_group",
            cim_role="BranchGroup",
            target="cim_python_sdk.model.iec61970.base.operational_limits.branch_group:BranchGroup",
            many=False,
            lower=1,
            upper=1,
            inverse="pin_branch_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PinBranchGroup",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{8070DE9F-BCD5-4e30-AFEF-091F13415996}",
        attributes=(AttrMeta("kind", "kind", "PinBranchGroupKind", 0, 1, "enumeration"),),
        ends=(branch_group.meta,),
    )

    def __init__(
        self,
        *,
        kind: PinBranchGroupKind | None = None,
        branch_group: BranchGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if branch_group is not None:
            self.branch_group = branch_group
