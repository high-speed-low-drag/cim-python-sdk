"""CIM class EndDeviceInfo (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.end_device import EndDevice
    from cim_python_sdk.model.iec61968.metering.end_device_capability import EndDeviceCapability


class EndDeviceInfo(AssetInfo):
    """End device data."""

    __slots__ = (
        "_end_devices",
        "capability",
        "is_solid_state",
        "phase_count",
        "rated_current",
        "rated_voltage",
    )

    capability: EndDeviceCapability | None
    phase_count: int | None
    rated_current: float | None  # CurrentFlow
    rated_voltage: float | None  # Voltage
    is_solid_state: bool | None

    end_devices: Many[EndDevice] = Many(
        EndMeta(
            name="end_devices",
            cim_role="EndDevices",
            target="cim_python_sdk.model.iec61968.metering.end_device:EndDevice",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_info",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EndDeviceInfo",
        package="TC57CIM/IEC61968/Metering",
        guid="{99DD997C-F77C-4153-BD29-301334A613CA}",
        attributes=(
            AttrMeta("capability", "capability", "EndDeviceCapability", 0, 1, "compound"),
            AttrMeta("phase_count", "phaseCount", "int", 0, 1, "primitive"),
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("rated_voltage", "ratedVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("is_solid_state", "isSolidState", "bool", 0, 1, "primitive"),
        ),
        ends=(end_devices.meta,),
    )

    def __init__(
        self,
        *,
        capability: EndDeviceCapability | None = None,
        phase_count: int | None = None,
        rated_current: float | None = None,
        rated_voltage: float | None = None,
        is_solid_state: bool | None = None,
        end_devices: Iterable[EndDevice] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.capability = capability
        self.phase_count = phase_count
        self.rated_current = rated_current
        self.rated_voltage = rated_voltage
        self.is_solid_state = is_solid_state
        if end_devices is not None:
            EndDeviceInfo.end_devices.extend(self, end_devices)

    def add_end_device(self, end_device: EndDevice) -> Self:
        return EndDeviceInfo.end_devices.add(self, end_device)

    def remove_end_device(self, end_device: EndDevice) -> Self:
        return EndDeviceInfo.end_devices.remove(self, end_device)

    def clear_end_devices(self) -> Self:
        return EndDeviceInfo.end_devices.clear(self)

    def num_end_device(self) -> int:
        return EndDeviceInfo.end_devices.count(self)

    def get_end_device_by_mrid(self, mrid: str) -> EndDevice | None:
        return EndDeviceInfo.end_devices.get_by_mrid(self, mrid)
