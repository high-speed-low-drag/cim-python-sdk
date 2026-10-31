"""CIM class BasicIntervalSchedule (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class BasicIntervalSchedule(IdentifiedObject):
    """Schedule of values at points in time."""

    __slots__ = (
        "start_time",
        "value1_multiplier",
        "value1_unit",
        "value2_multiplier",
        "value2_unit",
    )

    start_time: _dt.datetime | None
    value1_multiplier: UnitMultiplier | None
    value1_unit: UnitSymbol | None
    value2_multiplier: UnitMultiplier | None
    value2_unit: UnitSymbol | None

    _cim_meta = ClassMeta(
        cim_name="BasicIntervalSchedule",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{848DEDB2-99A8-44ec-8319-F7629519D147}",
        attributes=(
            AttrMeta("start_time", "startTime", "datetime", 0, 1, "primitive"),
            AttrMeta(
                "value1_multiplier", "value1Multiplier", "UnitMultiplier", 0, 1, "enumeration"
            ),
            AttrMeta("value1_unit", "value1Unit", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta(
                "value2_multiplier", "value2Multiplier", "UnitMultiplier", 0, 1, "enumeration"
            ),
            AttrMeta("value2_unit", "value2Unit", "UnitSymbol", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        start_time: _dt.datetime | None = None,
        value1_multiplier: UnitMultiplier | None = None,
        value1_unit: UnitSymbol | None = None,
        value2_multiplier: UnitMultiplier | None = None,
        value2_unit: UnitSymbol | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.start_time = start_time
        self.value1_multiplier = value1_multiplier
        self.value1_unit = value1_unit
        self.value2_multiplier = value2_multiplier
        self.value2_unit = value2_unit
