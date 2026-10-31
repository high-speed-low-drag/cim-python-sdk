"""CIM class AltGeneratingUnitMeas (TC57CIM/IEC61970/Base/ControlArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.control_area.control_area_generating_unit import (
        ControlAreaGeneratingUnit,
    )
    from cim_python_sdk.model.iec61970.base.meas.analog_value import AnalogValue


class AltGeneratingUnitMeas(IdentifiedObject):
    """A prioritized measurement to be used for the generating unit in the control area
    specification."""

    __slots__ = ("_analog_value", "_control_area_generating_unit", "priority")

    priority: int | None

    analog_value: One[AnalogValue] = One(
        EndMeta(
            name="analog_value",
            cim_role="AnalogValue",
            target="cim_python_sdk.model.iec61970.base.meas.analog_value:AnalogValue",
            many=False,
            lower=1,
            upper=1,
            inverse="alt_generating_unit",
            aggregation="none",
        )
    )
    control_area_generating_unit: One[ControlAreaGeneratingUnit] = One(
        EndMeta(
            name="control_area_generating_unit",
            cim_role="ControlAreaGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.control_area.control_area_generating_unit:ControlAreaGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="alt_generating_unit_meas",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AltGeneratingUnitMeas",
        package="TC57CIM/IEC61970/Base/ControlArea",
        guid="{73E925B7-6B4A-45b9-B03E-3EE2FA3C1837}",
        attributes=(AttrMeta("priority", "priority", "int", 0, 1, "primitive"),),
        ends=(
            analog_value.meta,
            control_area_generating_unit.meta,
        ),
    )

    def __init__(
        self,
        *,
        priority: int | None = None,
        analog_value: AnalogValue | None = None,
        control_area_generating_unit: ControlAreaGeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.priority = priority
        if analog_value is not None:
            self.analog_value = analog_value
        if control_area_generating_unit is not None:
            self.control_area_generating_unit = control_area_generating_unit
