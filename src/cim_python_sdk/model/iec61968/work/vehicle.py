"""CIM class Vehicle (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.work.work_asset import WorkAsset

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.work.vehicle_usage_kind import VehicleUsageKind


class Vehicle(WorkAsset):
    """Vehicle asset."""

    __slots__ = ("odometer_read_date_time", "odometer_reading", "usage_kind")

    odometer_read_date_time: _dt.datetime | None
    odometer_reading: float | None  # Length
    usage_kind: VehicleUsageKind | None

    _cim_meta = ClassMeta(
        cim_name="Vehicle",
        package="TC57CIM/IEC61968/Work",
        guid="{B7371286-9313-44c8-8D81-3FAD831ACC9B}",
        attributes=(
            AttrMeta(
                "odometer_read_date_time", "odometerReadDateTime", "datetime", 0, 1, "primitive"
            ),
            AttrMeta("odometer_reading", "odometerReading", "Length", 0, 1, "cimdatatype"),
            AttrMeta("usage_kind", "usageKind", "VehicleUsageKind", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        odometer_read_date_time: _dt.datetime | None = None,
        odometer_reading: float | None = None,
        usage_kind: VehicleUsageKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.odometer_read_date_time = odometer_read_date_time
        self.odometer_reading = odometer_reading
        self.usage_kind = usage_kind
