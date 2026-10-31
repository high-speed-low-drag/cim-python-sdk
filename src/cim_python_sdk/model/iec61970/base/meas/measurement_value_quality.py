"""CIM class MeasurementValueQuality (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.quality61850 import Quality61850

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue


class MeasurementValueQuality(Quality61850):
    """Measurement quality flags. Bits 0-10 are defined for substation automation in IEC
    61850-7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are
    reserved for EMS applications."""

    __slots__ = ("_measurement_value",)

    measurement_value: One[MeasurementValue] = One(
        EndMeta(
            name="measurement_value",
            cim_role="MeasurementValue",
            target="cim_python_sdk.model.iec61970.base.meas.measurement_value:MeasurementValue",
            many=False,
            lower=1,
            upper=1,
            inverse="measurement_value_quality",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeasurementValueQuality",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{D45A5712-F5C6-410e-8799-A6EEBD3DAEA2}",
        ends=(measurement_value.meta,),
    )

    def __init__(
        self,
        *,
        measurement_value: MeasurementValue | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if measurement_value is not None:
            self.measurement_value = measurement_value
