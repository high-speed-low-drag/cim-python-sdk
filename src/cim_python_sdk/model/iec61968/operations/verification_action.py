"""CIM class VerificationAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource


class VerificationAction(SwitchingAction):
    """Verification of a switch position or other condition as a switching step"""

    __slots__ = ("_power_system_resource", "verification_condition")

    verification_condition: str | None

    power_system_resource: One[PowerSystemResource] = One(
        EndMeta(
            name="power_system_resource",
            cim_role="PowerSystemResource",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=False,
            lower=0,
            upper=1,
            inverse="verification_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VerificationAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{D7D96493-B36A-45b9-9FC4-D765897756EF}",
        attributes=(
            AttrMeta("verification_condition", "verificationCondition", "str", 0, 1, "primitive"),
        ),
        ends=(power_system_resource.meta,),
    )

    def __init__(
        self,
        *,
        verification_condition: str | None = None,
        power_system_resource: PowerSystemResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.verification_condition = verification_condition
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource
