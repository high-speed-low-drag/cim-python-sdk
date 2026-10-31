"""CIM class EnvironmentalStringMeasurement (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.string_measurement import StringMeasurement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.classification_condition import (
        ClassificationCondition,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_information import (
        EnvironmentalInformation,
    )


class EnvironmentalStringMeasurement(StringMeasurement):
    """String measurement of relevance in the environmental domain."""

    __slots__ = ("_classification_condition", "_environmental_information")

    environmental_information: One[EnvironmentalInformation] = One(
        EndMeta(
            name="environmental_information",
            cim_role="EnvironmentalInformation",
            target="cim_python_sdk.model.iec62325.environmental.environmental_information:EnvironmentalInformation",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_string_measurement",
            aggregation="none",
        )
    )
    classification_condition: One[ClassificationCondition] = One(
        EndMeta(
            name="classification_condition",
            cim_role="ClassificationCondition",
            target="cim_python_sdk.model.iec62325.environmental.classification_condition:ClassificationCondition",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_string_measurement",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalStringMeasurement",
        package="TC57CIM/IEC62325/Environmental",
        guid="{45D363CC-9B36-4fc4-9E55-C5550D9BAF23}",
        ends=(
            environmental_information.meta,
            classification_condition.meta,
        ),
    )

    def __init__(
        self,
        *,
        environmental_information: EnvironmentalInformation | None = None,
        classification_condition: ClassificationCondition | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if environmental_information is not None:
            self.environmental_information = environmental_information
        if classification_condition is not None:
            self.classification_condition = classification_condition
