"""CIM class AltTieMeas (TC57CIM/IEC61970/Base/ControlArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.control_area.tie_flow import TieFlow
    from cim_python_sdk.model.iec61970.base.meas.analog_value import AnalogValue


class AltTieMeas(IdentifiedObject):
    """A prioritized measurement to be used for the tie flow as part of the control area
    specification."""

    __slots__ = ("_analog_value", "_tie_flow", "priority")

    priority: int | None

    analog_value: One[AnalogValue] = One(
        EndMeta(
            name="analog_value",
            cim_role="AnalogValue",
            target="cim_python_sdk.model.iec61970.base.meas.analog_value:AnalogValue",
            many=False,
            lower=1,
            upper=1,
            inverse="alt_tie_meas",
            aggregation="none",
        )
    )
    tie_flow: One[TieFlow] = One(
        EndMeta(
            name="tie_flow",
            cim_role="TieFlow",
            target="cim_python_sdk.model.iec61970.base.control_area.tie_flow:TieFlow",
            many=False,
            lower=1,
            upper=1,
            inverse="alt_tie_meas",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AltTieMeas",
        package="TC57CIM/IEC61970/Base/ControlArea",
        guid="{08FB5259-8BBB-4ca4-B812-541DCFE52997}",
        attributes=(AttrMeta("priority", "priority", "int", 0, 1, "primitive"),),
        ends=(
            analog_value.meta,
            tie_flow.meta,
        ),
    )

    def __init__(
        self,
        *,
        priority: int | None = None,
        analog_value: AnalogValue | None = None,
        tie_flow: TieFlow | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.priority = priority
        if analog_value is not None:
            self.analog_value = analog_value
        if tie_flow is not None:
            self.tie_flow = tie_flow
