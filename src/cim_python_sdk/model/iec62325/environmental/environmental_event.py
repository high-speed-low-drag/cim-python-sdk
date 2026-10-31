"""CIM class EnvironmentalEvent (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.environmental.environmental_information import (
        EnvironmentalInformation,
    )


class EnvironmentalEvent(ActivityRecord):
    """An environmental event to which one or more forecasts or observations may be tied and
    which may relate to or affect one or more assets.

    This class is intended to be used as a means of grouping forecasts and/or observations
    and could be used for a variety of purposes, including:

    - to define a 'named' event like Hurricane Katrina and allow the historic (or forecast)
    values for phenomena and measurements (precipitation, temperature) across time to be
    associated with it

    - to identify assets that were (or are forecast to be) affected by a phenomenon or set
    of measurements"""

    __slots__ = ("_environmental_information",)

    environmental_information: Many[EnvironmentalInformation] = Many(
        EndMeta(
            name="environmental_information",
            cim_role="EnvironmentalInformation",
            target="cim_python_sdk.model.iec62325.environmental.environmental_information:EnvironmentalInformation",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_event",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalEvent",
        package="TC57CIM/IEC62325/Environmental",
        guid="{FFCF28A6-7F47-4970-A6D0-E39F622CC21A}",
        ends=(environmental_information.meta,),
    )

    def __init__(
        self,
        *,
        environmental_information: Iterable[EnvironmentalInformation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if environmental_information is not None:
            EnvironmentalEvent.environmental_information.extend(self, environmental_information)

    def add_environmental_information(
        self, environmental_information: EnvironmentalInformation
    ) -> Self:
        return EnvironmentalEvent.environmental_information.add(self, environmental_information)

    def remove_environmental_information(
        self, environmental_information: EnvironmentalInformation
    ) -> Self:
        return EnvironmentalEvent.environmental_information.remove(self, environmental_information)

    def clear_environmental_information(self) -> Self:
        return EnvironmentalEvent.environmental_information.clear(self)

    def num_environmental_information(self) -> int:
        return EnvironmentalEvent.environmental_information.count(self)

    def get_environmental_information_by_mrid(self, mrid: str) -> EnvironmentalInformation | None:
        return EnvironmentalEvent.environmental_information.get_by_mrid(self, mrid)
