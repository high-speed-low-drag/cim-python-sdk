"""CIM class RemoteControl (TC57CIM/IEC61970/Base/SCADA). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.scada.remote_point import RemotePoint

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.control import Control


class RemoteControl(RemotePoint):
    """Remote controls are outputs that are sent by the remote unit to actuators in the
    process."""

    __slots__ = ("_control", "actuator_maximum", "actuator_minimum", "remote_controlled")

    remote_controlled: bool | None
    actuator_maximum: float | None
    actuator_minimum: float | None

    control: One[Control] = One(
        EndMeta(
            name="control",
            cim_role="Control",
            target="cim_python_sdk.model.iec61970.base.meas.control:Control",
            many=False,
            lower=1,
            upper=1,
            inverse="remote_control",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RemoteControl",
        package="TC57CIM/IEC61970/Base/SCADA",
        guid="{5B096850-E749-4b88-AC9B-AB0EFD66A72F}",
        attributes=(
            AttrMeta("remote_controlled", "remoteControlled", "bool", 0, 1, "primitive"),
            AttrMeta("actuator_maximum", "actuatorMaximum", "float", 0, 1, "primitive"),
            AttrMeta("actuator_minimum", "actuatorMinimum", "float", 0, 1, "primitive"),
        ),
        ends=(control.meta,),
    )

    def __init__(
        self,
        *,
        remote_controlled: bool | None = None,
        actuator_maximum: float | None = None,
        actuator_minimum: float | None = None,
        control: Control | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.remote_controlled = remote_controlled
        self.actuator_maximum = actuator_maximum
        self.actuator_minimum = actuator_minimum
        if control is not None:
            self.control = control
