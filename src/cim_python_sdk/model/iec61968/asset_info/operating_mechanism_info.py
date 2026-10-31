"""CIM class OperatingMechanismInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_info.operating_mechanism_kind import (
        OperatingMechanismKind,
    )


class OperatingMechanismInfo(AssetInfo):
    """Breaker operating mechanism datasheet information."""

    __slots__ = (
        "close_amps",
        "close_voltage",
        "mechanism_kind",
        "motor_run_current",
        "motor_start_current",
        "motor_voltage",
        "trip_amps",
        "trip_voltage",
    )

    mechanism_kind: OperatingMechanismKind | None
    close_voltage: float | None  # Voltage
    trip_voltage: float | None  # Voltage
    close_amps: float | None  # CurrentFlow
    trip_amps: float | None  # CurrentFlow
    motor_start_current: float | None  # CurrentFlow
    motor_run_current: float | None  # CurrentFlow
    motor_voltage: float | None  # Voltage

    _cim_meta = ClassMeta(
        cim_name="OperatingMechanismInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{2FC3E8DD-4A6F-4752-9081-0FAED4693C42}",
        attributes=(
            AttrMeta(
                "mechanism_kind", "mechanismKind", "OperatingMechanismKind", 0, 1, "enumeration"
            ),
            AttrMeta("close_voltage", "closeVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("trip_voltage", "tripVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("close_amps", "closeAmps", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("trip_amps", "tripAmps", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta(
                "motor_start_current", "motorStartCurrent", "CurrentFlow", 0, 1, "cimdatatype"
            ),
            AttrMeta("motor_run_current", "motorRunCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("motor_voltage", "motorVoltage", "Voltage", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mechanism_kind: OperatingMechanismKind | None = None,
        close_voltage: float | None = None,
        trip_voltage: float | None = None,
        close_amps: float | None = None,
        trip_amps: float | None = None,
        motor_start_current: float | None = None,
        motor_run_current: float | None = None,
        motor_voltage: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mechanism_kind = mechanism_kind
        self.close_voltage = close_voltage
        self.trip_voltage = trip_voltage
        self.close_amps = close_amps
        self.trip_amps = trip_amps
        self.motor_start_current = motor_start_current
        self.motor_run_current = motor_run_current
        self.motor_voltage = motor_voltage
