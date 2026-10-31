"""CIM class SwitchingEvent (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction


class SwitchingEvent(ActivityRecord):
    """Event indicating the completion (success or fail) of any switching action (jumper
    action, cut action, tag action, etc). The switching action may or may not be a
    consequential event in response to a request to complete the action."""

    __slots__ = ("_switching_action",)

    switching_action: One[SwitchingAction] = One(
        EndMeta(
            name="switching_action",
            cim_role="SwitchingAction",
            target="cim_python_sdk.model.iec61968.operations.switching_action:SwitchingAction",
            many=False,
            lower=1,
            upper=1,
            inverse="switching_event",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchingEvent",
        package="TC57CIM/IEC61968/Operations",
        guid="{12009FF8-FCCD-459b-8D67-9366AF32DD46}",
        ends=(switching_action.meta,),
    )

    def __init__(
        self,
        *,
        switching_action: SwitchingAction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if switching_action is not None:
            self.switching_action = switching_action
