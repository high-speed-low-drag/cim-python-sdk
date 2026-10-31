"""CIM class AnalogValue (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.control_area.alt_generating_unit_meas import (
        AltGeneratingUnitMeas,
    )
    from cim_python_sdk.model.iec61970.base.control_area.alt_tie_meas import AltTieMeas
    from cim_python_sdk.model.iec61970.base.meas.analog import Analog
    from cim_python_sdk.model.iec61970.base.meas.analog_control import AnalogControl


class AnalogValue(MeasurementValue):
    """AnalogValue represents an analog MeasurementValue."""

    __slots__ = ("_alt_generating_unit", "_alt_tie_meas", "_analog", "_analog_control", "value")

    value: float | None

    alt_generating_unit: Many[AltGeneratingUnitMeas] = Many(
        EndMeta(
            name="alt_generating_unit",
            cim_role="AltGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.control_area.alt_generating_unit_meas:AltGeneratingUnitMeas",
            many=True,
            lower=0,
            upper=None,
            inverse="analog_value",
            aggregation="none",
        )
    )
    analog: One[Analog] = One(
        EndMeta(
            name="analog",
            cim_role="Analog",
            target="cim_python_sdk.model.iec61970.base.meas.analog:Analog",
            many=False,
            lower=1,
            upper=1,
            inverse="analog_values",
            aggregation="none",
        )
    )
    analog_control: One[AnalogControl] = One(
        EndMeta(
            name="analog_control",
            cim_role="AnalogControl",
            target="cim_python_sdk.model.iec61970.base.meas.analog_control:AnalogControl",
            many=False,
            lower=0,
            upper=1,
            inverse="analog_value",
            aggregation="none",
        )
    )
    alt_tie_meas: Many[AltTieMeas] = Many(
        EndMeta(
            name="alt_tie_meas",
            cim_role="AltTieMeas",
            target="cim_python_sdk.model.iec61970.base.control_area.alt_tie_meas:AltTieMeas",
            many=True,
            lower=0,
            upper=None,
            inverse="analog_value",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AnalogValue",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{E8AD2B41-94FA-40e5-A1DC-96B7E0A8025C}",
        attributes=(AttrMeta("value", "value", "float", 0, 1, "primitive"),),
        ends=(
            alt_generating_unit.meta,
            analog.meta,
            analog_control.meta,
            alt_tie_meas.meta,
        ),
    )

    def __init__(
        self,
        *,
        value: float | None = None,
        alt_generating_unit: Iterable[AltGeneratingUnitMeas] | None = None,
        analog: Analog | None = None,
        analog_control: AnalogControl | None = None,
        alt_tie_meas: Iterable[AltTieMeas] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
        if alt_generating_unit is not None:
            AnalogValue.alt_generating_unit.extend(self, alt_generating_unit)
        if analog is not None:
            self.analog = analog
        if analog_control is not None:
            self.analog_control = analog_control
        if alt_tie_meas is not None:
            AnalogValue.alt_tie_meas.extend(self, alt_tie_meas)

    def add_alt_generating_unit(self, alt_generating_unit: AltGeneratingUnitMeas) -> Self:
        return AnalogValue.alt_generating_unit.add(self, alt_generating_unit)

    def remove_alt_generating_unit(self, alt_generating_unit: AltGeneratingUnitMeas) -> Self:
        return AnalogValue.alt_generating_unit.remove(self, alt_generating_unit)

    def clear_alt_generating_unit(self) -> Self:
        return AnalogValue.alt_generating_unit.clear(self)

    def num_alt_generating_unit(self) -> int:
        return AnalogValue.alt_generating_unit.count(self)

    def get_alt_generating_unit_by_mrid(self, mrid: str) -> AltGeneratingUnitMeas | None:
        return AnalogValue.alt_generating_unit.get_by_mrid(self, mrid)

    def add_alt_tie_mea(self, alt_tie_mea: AltTieMeas) -> Self:
        return AnalogValue.alt_tie_meas.add(self, alt_tie_mea)

    def remove_alt_tie_mea(self, alt_tie_mea: AltTieMeas) -> Self:
        return AnalogValue.alt_tie_meas.remove(self, alt_tie_mea)

    def clear_alt_tie_meas(self) -> Self:
        return AnalogValue.alt_tie_meas.clear(self)

    def num_alt_tie_mea(self) -> int:
        return AnalogValue.alt_tie_meas.count(self)

    def get_alt_tie_mea_by_mrid(self, mrid: str) -> AltTieMeas | None:
        return AnalogValue.alt_tie_meas.get_by_mrid(self, mrid)
