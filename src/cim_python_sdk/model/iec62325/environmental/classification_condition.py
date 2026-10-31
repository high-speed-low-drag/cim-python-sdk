"""CIM class ClassificationCondition (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.environmental.env_domain.test_kind import TestKind
    from cim_python_sdk.model.iec62325.environmental.environmental_analog import EnvironmentalAnalog
    from cim_python_sdk.model.iec62325.environmental.environmental_string_measurement import (
        EnvironmentalStringMeasurement,
    )
    from cim_python_sdk.model.iec62325.environmental.phenomenon_classification import (
        PhenomenonClassification,
    )


class ClassificationCondition(IdentifiedObject):
    """A classification condition used to define preconditions that must be met by a phenomena
    classification."""

    __slots__ = (
        "_environmental_analog",
        "_environmental_string_measurement",
        "_phenomenon_classification",
        "duration",
        "test",
    )

    duration: float | None  # Seconds
    test: TestKind | None

    phenomenon_classification: One[PhenomenonClassification] = One(
        EndMeta(
            name="phenomenon_classification",
            cim_role="PhenomenonClassification",
            target="cim_python_sdk.model.iec62325.environmental.phenomenon_classification:PhenomenonClassification",
            many=False,
            lower=0,
            upper=1,
            inverse="classification_condition",
            aggregation="none",
        )
    )
    environmental_string_measurement: Many[EnvironmentalStringMeasurement] = Many(
        EndMeta(
            name="environmental_string_measurement",
            cim_role="EnvironmentalStringMeasurement",
            target="cim_python_sdk.model.iec62325.environmental.environmental_string_measurement:EnvironmentalStringMeasurement",
            many=True,
            lower=0,
            upper=None,
            inverse="classification_condition",
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
            inverse="classification_condition",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ClassificationCondition",
        package="TC57CIM/IEC62325/Environmental",
        guid="{47D315F4-9E04-40f6-B847-BAD432CD200C}",
        attributes=(
            AttrMeta("duration", "duration", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("test", "test", "TestKind", 0, 1, "enumeration"),
        ),
        ends=(
            phenomenon_classification.meta,
            environmental_string_measurement.meta,
            environmental_analog.meta,
        ),
    )

    def __init__(
        self,
        *,
        duration: float | None = None,
        test: TestKind | None = None,
        phenomenon_classification: PhenomenonClassification | None = None,
        environmental_string_measurement: Iterable[EnvironmentalStringMeasurement] | None = None,
        environmental_analog: Iterable[EnvironmentalAnalog] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.duration = duration
        self.test = test
        if phenomenon_classification is not None:
            self.phenomenon_classification = phenomenon_classification
        if environmental_string_measurement is not None:
            ClassificationCondition.environmental_string_measurement.extend(
                self, environmental_string_measurement
            )
        if environmental_analog is not None:
            ClassificationCondition.environmental_analog.extend(self, environmental_analog)

    def add_environmental_string_measurement(
        self, environmental_string_measurement: EnvironmentalStringMeasurement
    ) -> Self:
        return ClassificationCondition.environmental_string_measurement.add(
            self, environmental_string_measurement
        )

    def remove_environmental_string_measurement(
        self, environmental_string_measurement: EnvironmentalStringMeasurement
    ) -> Self:
        return ClassificationCondition.environmental_string_measurement.remove(
            self, environmental_string_measurement
        )

    def clear_environmental_string_measurement(self) -> Self:
        return ClassificationCondition.environmental_string_measurement.clear(self)

    def num_environmental_string_measurement(self) -> int:
        return ClassificationCondition.environmental_string_measurement.count(self)

    def get_environmental_string_measurement_by_mrid(
        self, mrid: str
    ) -> EnvironmentalStringMeasurement | None:
        return ClassificationCondition.environmental_string_measurement.get_by_mrid(self, mrid)

    def add_environmental_analog(self, environmental_analog: EnvironmentalAnalog) -> Self:
        return ClassificationCondition.environmental_analog.add(self, environmental_analog)

    def remove_environmental_analog(self, environmental_analog: EnvironmentalAnalog) -> Self:
        return ClassificationCondition.environmental_analog.remove(self, environmental_analog)

    def clear_environmental_analog(self) -> Self:
        return ClassificationCondition.environmental_analog.clear(self)

    def num_environmental_analog(self) -> int:
        return ClassificationCondition.environmental_analog.count(self)

    def get_environmental_analog_by_mrid(self, mrid: str) -> EnvironmentalAnalog | None:
        return ClassificationCondition.environmental_analog.get_by_mrid(self, mrid)
