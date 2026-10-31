"""CIM compound EndDeviceTiming (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.metering.randomisation_kind import RandomisationKind
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class EndDeviceTiming(CimCompound):
    """Timing for the control actions of end devices."""

    __slots__ = ("duration", "duration_indefinite", "interval", "randomisation")

    duration: float | None  # Minutes
    duration_indefinite: bool | None
    interval: DateTimeInterval | None
    randomisation: RandomisationKind | None

    _cim_meta = ClassMeta(
        cim_name="EndDeviceTiming",
        package="TC57CIM/IEC61968/Metering",
        guid="{BD68DA41-C97B-4bf3-B2E3-614107744D35}",
        kind="compound",
        attributes=(
            AttrMeta("duration", "duration", "Minutes", 0, 1, "cimdatatype"),
            AttrMeta("duration_indefinite", "durationIndefinite", "bool", 0, 1, "primitive"),
            AttrMeta("interval", "interval", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("randomisation", "randomisation", "RandomisationKind", 0, 1, "enumeration"),
        ),
    )
