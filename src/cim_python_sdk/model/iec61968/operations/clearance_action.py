"""CIM class ClearanceAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.clearance_action_kind import ClearanceActionKind
    from cim_python_sdk.model.iec61968.operations.clearance_document import ClearanceDocument


class ClearanceAction(SwitchingAction):
    """Action on clearance document as a switching step."""

    __slots__ = ("_clearance", "kind")

    kind: ClearanceActionKind | None

    clearance: One[ClearanceDocument] = One(
        EndMeta(
            name="clearance",
            cim_role="Clearance",
            target="cim_python_sdk.model.iec61968.operations.clearance_document:ClearanceDocument",
            many=False,
            lower=0,
            upper=1,
            inverse="clearance_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ClearanceAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{9CBAB5BD-4103-4aad-A7C8-225F07CBB230}",
        attributes=(AttrMeta("kind", "kind", "ClearanceActionKind", 0, 1, "enumeration"),),
        ends=(clearance.meta,),
    )

    def __init__(
        self,
        *,
        kind: ClearanceActionKind | None = None,
        clearance: ClearanceDocument | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if clearance is not None:
            self.clearance = clearance
