"""CIM class TriggerCondition (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate import Gate
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.remedial_action_scheme import (
        RemedialActionScheme,
    )


class TriggerCondition(IdentifiedObject):
    """A conditions that can trigger remedial actions."""

    __slots__ = ("_gate_trigger", "_remedial_action_scheme")

    gate_trigger: One[Gate] = One(
        EndMeta(
            name="gate_trigger",
            cim_role="GateTrigger",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate:Gate",
            many=False,
            lower=1,
            upper=1,
            inverse="trigger_condition",
            aggregation="none",
        )
    )
    remedial_action_scheme: One[RemedialActionScheme] = One(
        EndMeta(
            name="remedial_action_scheme",
            cim_role="RemedialActionScheme",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.remedial_action_scheme:RemedialActionScheme",
            many=False,
            lower=1,
            upper=1,
            inverse="trigger_condition",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TriggerCondition",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{D3318288-1811-4c7a-98FC-DB3D4585AC89}",
        ends=(
            gate_trigger.meta,
            remedial_action_scheme.meta,
        ),
    )

    def __init__(
        self,
        *,
        gate_trigger: Gate | None = None,
        remedial_action_scheme: RemedialActionScheme | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if gate_trigger is not None:
            self.gate_trigger = gate_trigger
        if remedial_action_scheme is not None:
            self.remedial_action_scheme = remedial_action_scheme
