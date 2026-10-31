"""CIM class GenericAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource


class GenericAction(SwitchingAction):
    """An arbitrary switching step."""

    __slots__ = ("_power_system_resource",)

    power_system_resource: One[PowerSystemResource] = One(
        EndMeta(
            name="power_system_resource",
            cim_role="PowerSystemResource",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=False,
            lower=0,
            upper=1,
            inverse="generic_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GenericAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{7B245759-F49C-4c34-AEF1-F93D37992CD7}",
        ends=(power_system_resource.meta,),
    )

    def __init__(
        self,
        *,
        power_system_resource: PowerSystemResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource
