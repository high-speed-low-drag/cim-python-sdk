"""CIM class AnalogMeasurementValueQuality (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.meas.measurement_value_quality import (
    MeasurementValueQuality,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class AnalogMeasurementValueQuality(MeasurementValueQuality):
    """Measurement quality flags for Analog Values."""

    __slots__ = ("scada_quality_code",)

    scada_quality_code: str | None

    _cim_meta = ClassMeta(
        cim_name="AnalogMeasurementValueQuality",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{B2F2CD2A-A979-4ce8-ACFC-514875F2F8C2}",
        attributes=(AttrMeta("scada_quality_code", "scadaQualityCode", "str", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        scada_quality_code: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.scada_quality_code = scada_quality_code
