"""CIM class Forecast (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.environmental_information import (
    EnvironmentalInformation,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class Forecast(EnvironmentalInformation):
    """A forecast group of value sets and/or phenomena characteristics."""

    __slots__ = ("valid_for",)

    valid_for: DateTimeInterval | None

    _cim_meta = ClassMeta(
        cim_name="Forecast",
        package="TC57CIM/IEC62325/Environmental",
        guid="{4D1FE60B-DA7E-465f-B2D5-CD008A89A5E8}",
        attributes=(AttrMeta("valid_for", "validFor", "DateTimeInterval", 0, 1, "compound"),),
    )

    def __init__(
        self,
        *,
        valid_for: DateTimeInterval | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.valid_for = valid_for
