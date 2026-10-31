"""CIM class ControlAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.control import Control


class ControlAction(SwitchingAction):
    """Control executed as a switching step."""

    __slots__ = ("_control", "analog_value", "discrete_value")

    analog_value: float | None
    discrete_value: int | None

    control: One[Control] = One(
        EndMeta(
            name="control",
            cim_role="Control",
            target="cim_python_sdk.model.iec61970.base.meas.control:Control",
            many=False,
            lower=0,
            upper=1,
            inverse="control_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ControlAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{F90EA179-BE05-4f82-9287-CCF839EF5869}",
        attributes=(
            AttrMeta("analog_value", "analogValue", "float", 0, 1, "primitive"),
            AttrMeta("discrete_value", "discreteValue", "int", 0, 1, "primitive"),
        ),
        ends=(control.meta,),
    )

    def __init__(
        self,
        *,
        analog_value: float | None = None,
        discrete_value: int | None = None,
        control: Control | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.analog_value = analog_value
        self.discrete_value = discrete_value
        if control is not None:
            self.control = control
