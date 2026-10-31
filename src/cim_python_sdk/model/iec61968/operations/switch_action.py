"""CIM class SwitchAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.outage import Outage
    from cim_python_sdk.model.iec61968.operations.switch_action_kind import SwitchActionKind
    from cim_python_sdk.model.iec61970.base.wires.switch import Switch


class SwitchAction(SwitchingAction):
    """Action on switch as a switching step."""

    __slots__ = ("_operated_switch", "_planned_outage", "kind")

    kind: SwitchActionKind | None

    planned_outage: One[Outage] = One(
        EndMeta(
            name="planned_outage",
            cim_role="PlannedOutage",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=False,
            lower=0,
            upper=1,
            inverse="planned_switch_actions",
            aggregation="none",
        )
    )
    operated_switch: One[Switch] = One(
        EndMeta(
            name="operated_switch",
            cim_role="OperatedSwitch",
            target="cim_python_sdk.model.iec61970.base.wires.switch:Switch",
            many=False,
            lower=0,
            upper=1,
            inverse="switch_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{4B8F56B0-FE35-4aa4-BB8B-DD756F9898AA}",
        attributes=(AttrMeta("kind", "kind", "SwitchActionKind", 0, 1, "enumeration"),),
        ends=(
            planned_outage.meta,
            operated_switch.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: SwitchActionKind | None = None,
        planned_outage: Outage | None = None,
        operated_switch: Switch | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if planned_outage is not None:
            self.planned_outage = planned_outage
        if operated_switch is not None:
            self.operated_switch = operated_switch
