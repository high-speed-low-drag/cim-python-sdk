"""CIM class OilSpecimen (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.specimen import Specimen

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.oil_sample_location import OilSampleLocation
    from cim_python_sdk.model.iec61968.assets.oil_temperature_source import OilTemperatureSource
    from cim_python_sdk.model.iec61968.assets.sample_container_type import SampleContainerType


class OilSpecimen(Specimen):
    """CIM class OilSpecimen."""

    __slots__ = (
        "oil_sample_taken_from",
        "oil_sample_temperature",
        "oil_temperature_source",
        "sample_container",
    )

    oil_sample_temperature: float | None  # Temperature
    oil_temperature_source: OilTemperatureSource | None
    oil_sample_taken_from: OilSampleLocation | None
    sample_container: SampleContainerType | None

    _cim_meta = ClassMeta(
        cim_name="OilSpecimen",
        package="TC57CIM/IEC61968/Assets",
        guid="{53695A93-8369-4d59-9903-81B3867E7688}",
        attributes=(
            AttrMeta(
                "oil_sample_temperature", "oilSampleTemperature", "Temperature", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "oil_temperature_source",
                "oilTemperatureSource",
                "OilTemperatureSource",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "oil_sample_taken_from",
                "oilSampleTakenFrom",
                "OilSampleLocation",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "sample_container", "sampleContainer", "SampleContainerType", 0, 1, "enumeration"
            ),
        ),
    )

    def __init__(
        self,
        *,
        oil_sample_temperature: float | None = None,
        oil_temperature_source: OilTemperatureSource | None = None,
        oil_sample_taken_from: OilSampleLocation | None = None,
        sample_container: SampleContainerType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.oil_sample_temperature = oil_sample_temperature
        self.oil_temperature_source = oil_temperature_source
        self.oil_sample_taken_from = oil_sample_taken_from
        self.sample_container = sample_container
