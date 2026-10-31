"""CIM class EnvironmentalInformation (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.environmental.environmental_analog import EnvironmentalAnalog
    from cim_python_sdk.model.iec62325.environmental.environmental_data_provider import (
        EnvironmentalDataProvider,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_discrete import (
        EnvironmentalDiscrete,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_event import EnvironmentalEvent
    from cim_python_sdk.model.iec62325.environmental.environmental_phenomenon import (
        EnvironmentalPhenomenon,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_string_measurement import (
        EnvironmentalStringMeasurement,
    )


class EnvironmentalInformation(IdentifiedObject):
    """Abstract class (with concrete child classes of Observation and Forecast) that groups
    phenomenon and/or environmental value sets."""

    __slots__ = (
        "_environmental_analog",
        "_environmental_data_provider",
        "_environmental_discrete",
        "_environmental_event",
        "_environmental_phenomenon",
        "_environmental_string_measurement",
        "created",
    )

    created: _dt.datetime | None

    environmental_string_measurement: Many[EnvironmentalStringMeasurement] = Many(
        EndMeta(
            name="environmental_string_measurement",
            cim_role="EnvironmentalStringMeasurement",
            target="cim_python_sdk.model.iec62325.environmental.environmental_string_measurement:EnvironmentalStringMeasurement",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_information",
            aggregation="none",
        )
    )
    environmental_analog: Many[EnvironmentalAnalog] = Many(
        EndMeta(
            name="environmental_analog",
            cim_role="EnvironmentalAnalog",
            target="cim_python_sdk.model.iec62325.environmental.environmental_analog:EnvironmentalAnalog",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_information",
            aggregation="none",
        )
    )
    environmental_event: Many[EnvironmentalEvent] = Many(
        EndMeta(
            name="environmental_event",
            cim_role="EnvironmentalEvent",
            target="cim_python_sdk.model.iec62325.environmental.environmental_event:EnvironmentalEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_information",
            aggregation="none",
        )
    )
    environmental_discrete: Many[EnvironmentalDiscrete] = Many(
        EndMeta(
            name="environmental_discrete",
            cim_role="EnvironmentalDiscrete",
            target="cim_python_sdk.model.iec62325.environmental.environmental_discrete:EnvironmentalDiscrete",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_information",
            aggregation="none",
        )
    )
    environmental_phenomenon: Many[EnvironmentalPhenomenon] = Many(
        EndMeta(
            name="environmental_phenomenon",
            cim_role="EnvironmentalPhenomenon",
            target="cim_python_sdk.model.iec62325.environmental.environmental_phenomenon:EnvironmentalPhenomenon",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_information",
            aggregation="none",
        )
    )
    environmental_data_provider: One[EnvironmentalDataProvider] = One(
        EndMeta(
            name="environmental_data_provider",
            cim_role="EnvironmentalDataProvider",
            target="cim_python_sdk.model.iec62325.environmental.environmental_data_provider:EnvironmentalDataProvider",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_information",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalInformation",
        package="TC57CIM/IEC62325/Environmental",
        guid="{E0E65339-6D6D-49ff-846C-6A2A175C0504}",
        attributes=(AttrMeta("created", "created", "datetime", 0, 1, "primitive"),),
        ends=(
            environmental_string_measurement.meta,
            environmental_analog.meta,
            environmental_event.meta,
            environmental_discrete.meta,
            environmental_phenomenon.meta,
            environmental_data_provider.meta,
        ),
    )

    def __init__(
        self,
        *,
        created: _dt.datetime | None = None,
        environmental_string_measurement: Iterable[EnvironmentalStringMeasurement] | None = None,
        environmental_analog: Iterable[EnvironmentalAnalog] | None = None,
        environmental_event: Iterable[EnvironmentalEvent] | None = None,
        environmental_discrete: Iterable[EnvironmentalDiscrete] | None = None,
        environmental_phenomenon: Iterable[EnvironmentalPhenomenon] | None = None,
        environmental_data_provider: EnvironmentalDataProvider | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.created = created
        if environmental_string_measurement is not None:
            EnvironmentalInformation.environmental_string_measurement.extend(
                self, environmental_string_measurement
            )
        if environmental_analog is not None:
            EnvironmentalInformation.environmental_analog.extend(self, environmental_analog)
        if environmental_event is not None:
            EnvironmentalInformation.environmental_event.extend(self, environmental_event)
        if environmental_discrete is not None:
            EnvironmentalInformation.environmental_discrete.extend(self, environmental_discrete)
        if environmental_phenomenon is not None:
            EnvironmentalInformation.environmental_phenomenon.extend(self, environmental_phenomenon)
        if environmental_data_provider is not None:
            self.environmental_data_provider = environmental_data_provider

    def add_environmental_string_measurement(
        self, environmental_string_measurement: EnvironmentalStringMeasurement
    ) -> Self:
        return EnvironmentalInformation.environmental_string_measurement.add(
            self, environmental_string_measurement
        )

    def remove_environmental_string_measurement(
        self, environmental_string_measurement: EnvironmentalStringMeasurement
    ) -> Self:
        return EnvironmentalInformation.environmental_string_measurement.remove(
            self, environmental_string_measurement
        )

    def clear_environmental_string_measurement(self) -> Self:
        return EnvironmentalInformation.environmental_string_measurement.clear(self)

    def num_environmental_string_measurement(self) -> int:
        return EnvironmentalInformation.environmental_string_measurement.count(self)

    def get_environmental_string_measurement_by_mrid(
        self, mrid: str
    ) -> EnvironmentalStringMeasurement | None:
        return EnvironmentalInformation.environmental_string_measurement.get_by_mrid(self, mrid)

    def add_environmental_analog(self, environmental_analog: EnvironmentalAnalog) -> Self:
        return EnvironmentalInformation.environmental_analog.add(self, environmental_analog)

    def remove_environmental_analog(self, environmental_analog: EnvironmentalAnalog) -> Self:
        return EnvironmentalInformation.environmental_analog.remove(self, environmental_analog)

    def clear_environmental_analog(self) -> Self:
        return EnvironmentalInformation.environmental_analog.clear(self)

    def num_environmental_analog(self) -> int:
        return EnvironmentalInformation.environmental_analog.count(self)

    def get_environmental_analog_by_mrid(self, mrid: str) -> EnvironmentalAnalog | None:
        return EnvironmentalInformation.environmental_analog.get_by_mrid(self, mrid)

    def add_environmental_event(self, environmental_event: EnvironmentalEvent) -> Self:
        return EnvironmentalInformation.environmental_event.add(self, environmental_event)

    def remove_environmental_event(self, environmental_event: EnvironmentalEvent) -> Self:
        return EnvironmentalInformation.environmental_event.remove(self, environmental_event)

    def clear_environmental_event(self) -> Self:
        return EnvironmentalInformation.environmental_event.clear(self)

    def num_environmental_event(self) -> int:
        return EnvironmentalInformation.environmental_event.count(self)

    def get_environmental_event_by_mrid(self, mrid: str) -> EnvironmentalEvent | None:
        return EnvironmentalInformation.environmental_event.get_by_mrid(self, mrid)

    def add_environmental_discrete(self, environmental_discrete: EnvironmentalDiscrete) -> Self:
        return EnvironmentalInformation.environmental_discrete.add(self, environmental_discrete)

    def remove_environmental_discrete(self, environmental_discrete: EnvironmentalDiscrete) -> Self:
        return EnvironmentalInformation.environmental_discrete.remove(self, environmental_discrete)

    def clear_environmental_discrete(self) -> Self:
        return EnvironmentalInformation.environmental_discrete.clear(self)

    def num_environmental_discrete(self) -> int:
        return EnvironmentalInformation.environmental_discrete.count(self)

    def get_environmental_discrete_by_mrid(self, mrid: str) -> EnvironmentalDiscrete | None:
        return EnvironmentalInformation.environmental_discrete.get_by_mrid(self, mrid)

    def add_environmental_phenomenon(
        self, environmental_phenomenon: EnvironmentalPhenomenon
    ) -> Self:
        return EnvironmentalInformation.environmental_phenomenon.add(self, environmental_phenomenon)

    def remove_environmental_phenomenon(
        self, environmental_phenomenon: EnvironmentalPhenomenon
    ) -> Self:
        return EnvironmentalInformation.environmental_phenomenon.remove(
            self, environmental_phenomenon
        )

    def clear_environmental_phenomenon(self) -> Self:
        return EnvironmentalInformation.environmental_phenomenon.clear(self)

    def num_environmental_phenomenon(self) -> int:
        return EnvironmentalInformation.environmental_phenomenon.count(self)
