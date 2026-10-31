"""CIM class Control (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.io_point import IOPoint

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.control_action import ControlAction
    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol
    from cim_python_sdk.model.iec61970.base.scada.remote_control import RemoteControl


class Control(IOPoint):
    """Control is used for supervisory/device control. It represents control outputs that are
    used to change the state in a process, e.g. close or open breaker, a set point value or
    a raise lower command."""

    __slots__ = (
        "_control_action",
        "_power_system_resource",
        "_remote_control",
        "control_type",
        "operation_in_progress",
        "time_stamp",
        "unit_multiplier",
        "unit_symbol",
    )

    operation_in_progress: bool | None
    time_stamp: _dt.datetime | None
    unit_multiplier: UnitMultiplier | None
    unit_symbol: UnitSymbol | None
    control_type: str | None

    control_action: One[ControlAction] = One(
        EndMeta(
            name="control_action",
            cim_role="ControlAction",
            target="cim_python_sdk.model.iec61968.operations.control_action:ControlAction",
            many=False,
            lower=0,
            upper=1,
            inverse="control",
            aggregation="none",
        )
    )
    power_system_resource: One[PowerSystemResource] = One(
        EndMeta(
            name="power_system_resource",
            cim_role="PowerSystemResource",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=False,
            lower=0,
            upper=1,
            inverse="controls",
            aggregation="none",
        )
    )
    remote_control: One[RemoteControl] = One(
        EndMeta(
            name="remote_control",
            cim_role="RemoteControl",
            target="cim_python_sdk.model.iec61970.base.scada.remote_control:RemoteControl",
            many=False,
            lower=0,
            upper=1,
            inverse="control",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Control",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{4EEEE27D-42CD-4efc-8F74-3655BF703F4E}",
        attributes=(
            AttrMeta("operation_in_progress", "operationInProgress", "bool", 0, 1, "primitive"),
            AttrMeta("time_stamp", "timeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("unit_multiplier", "unitMultiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit_symbol", "unitSymbol", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta("control_type", "controlType", "str", 0, 1, "primitive"),
        ),
        ends=(
            control_action.meta,
            power_system_resource.meta,
            remote_control.meta,
        ),
    )

    def __init__(
        self,
        *,
        operation_in_progress: bool | None = None,
        time_stamp: _dt.datetime | None = None,
        unit_multiplier: UnitMultiplier | None = None,
        unit_symbol: UnitSymbol | None = None,
        control_type: str | None = None,
        control_action: ControlAction | None = None,
        power_system_resource: PowerSystemResource | None = None,
        remote_control: RemoteControl | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.operation_in_progress = operation_in_progress
        self.time_stamp = time_stamp
        self.unit_multiplier = unit_multiplier
        self.unit_symbol = unit_symbol
        self.control_type = control_type
        if control_action is not None:
            self.control_action = control_action
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource
        if remote_control is not None:
            self.remote_control = remote_control
