"""CIM class EnvironmentalPhenomenon (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval
    from cim_python_sdk.model.iec62325.environmental.environmental_information import (
        EnvironmentalInformation,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_location_type import (
        EnvironmentalLocationType,
    )
    from cim_python_sdk.model.iec62325.environmental.phenomenon_classification import (
        PhenomenonClassification,
    )


class EnvironmentalPhenomenon(CimObject):
    """The actual or forecast characteristics of an environmental phenomenon at a specific
    point in time (or during a specific time interval) that may have both a center and
    area/line location."""

    __slots__ = (
        "_environmental_information",
        "_environmental_location_kind",
        "_phenomenon_classification",
        "time_interval",
    )

    time_interval: DateTimeInterval | None

    environmental_location_kind: Many[EnvironmentalLocationType] = Many(
        EndMeta(
            name="environmental_location_kind",
            cim_role="EnvironmentalLocationKind",
            target="cim_python_sdk.model.iec62325.environmental.environmental_location_type:EnvironmentalLocationType",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_phenomenon",
            aggregation="none",
        )
    )
    phenomenon_classification: One[PhenomenonClassification] = One(
        EndMeta(
            name="phenomenon_classification",
            cim_role="PhenomenonClassification",
            target="cim_python_sdk.model.iec62325.environmental.phenomenon_classification:PhenomenonClassification",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_phenomenon",
            aggregation="none",
        )
    )
    environmental_information: One[EnvironmentalInformation] = One(
        EndMeta(
            name="environmental_information",
            cim_role="EnvironmentalInformation",
            target="cim_python_sdk.model.iec62325.environmental.environmental_information:EnvironmentalInformation",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_phenomenon",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalPhenomenon",
        package="TC57CIM/IEC62325/Environmental",
        guid="{E5CAB7F1-22D3-4dd1-AAE4-FD2DA5C91BF2}",
        attributes=(
            AttrMeta("time_interval", "timeInterval", "DateTimeInterval", 0, 1, "compound"),
        ),
        ends=(
            environmental_location_kind.meta,
            phenomenon_classification.meta,
            environmental_information.meta,
        ),
    )

    def __init__(
        self,
        *,
        time_interval: DateTimeInterval | None = None,
        environmental_location_kind: Iterable[EnvironmentalLocationType] | None = None,
        phenomenon_classification: PhenomenonClassification | None = None,
        environmental_information: EnvironmentalInformation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.time_interval = time_interval
        if environmental_location_kind is not None:
            EnvironmentalPhenomenon.environmental_location_kind.extend(
                self, environmental_location_kind
            )
        if phenomenon_classification is not None:
            self.phenomenon_classification = phenomenon_classification
        if environmental_information is not None:
            self.environmental_information = environmental_information

    def add_environmental_location_kind(
        self, environmental_location_kind: EnvironmentalLocationType
    ) -> Self:
        return EnvironmentalPhenomenon.environmental_location_kind.add(
            self, environmental_location_kind
        )

    def remove_environmental_location_kind(
        self, environmental_location_kind: EnvironmentalLocationType
    ) -> Self:
        return EnvironmentalPhenomenon.environmental_location_kind.remove(
            self, environmental_location_kind
        )

    def clear_environmental_location_kind(self) -> Self:
        return EnvironmentalPhenomenon.environmental_location_kind.clear(self)

    def num_environmental_location_kind(self) -> int:
        return EnvironmentalPhenomenon.environmental_location_kind.count(self)
