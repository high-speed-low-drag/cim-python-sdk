"""CIM class EnvironmentalCodedValue (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.meas.string_measurement_value import StringMeasurementValue

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.env_domain.coverage_code_kind import (
        CoverageCodeKind,
    )
    from cim_python_sdk.model.iec62325.environmental.env_domain.intensity_code_kind import (
        IntensityCodeKind,
    )
    from cim_python_sdk.model.iec62325.environmental.env_domain.weather_code_kind import (
        WeatherCodeKind,
    )


class EnvironmentalCodedValue(StringMeasurementValue):
    """An environmental value described using a coded value. A triplicate of enumerated values
    representing intensity, coverage, type of weather is used. These may be concatenated
    into the string value."""

    __slots__ = ("coverage_kind", "intensity_kind", "probability_percent", "weather_kind")

    coverage_kind: CoverageCodeKind | None
    intensity_kind: IntensityCodeKind | None
    probability_percent: float | None  # PerCent
    weather_kind: WeatherCodeKind | None

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalCodedValue",
        package="TC57CIM/IEC62325/Environmental",
        guid="{8FF33878-EEAD-4243-86A6-7FB65DB71D18}",
        attributes=(
            AttrMeta("coverage_kind", "coverageKind", "CoverageCodeKind", 0, 1, "enumeration"),
            AttrMeta("intensity_kind", "intensityKind", "IntensityCodeKind", 0, 1, "enumeration"),
            AttrMeta("probability_percent", "probabilityPercent", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("weather_kind", "weatherKind", "WeatherCodeKind", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        coverage_kind: CoverageCodeKind | None = None,
        intensity_kind: IntensityCodeKind | None = None,
        probability_percent: float | None = None,
        weather_kind: WeatherCodeKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.coverage_kind = coverage_kind
        self.intensity_kind = intensity_kind
        self.probability_percent = probability_percent
        self.weather_kind = weather_kind
