"""CIM class SynchrocheckRelay (TC57CIM/IEC61970/Base/Protection). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.protection.protection_equipment import ProtectionEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class SynchrocheckRelay(ProtectionEquipment):
    """A device that operates when two AC circuits are within the desired limits of frequency,
    phase angle, and voltage, to permit or to cause the paralleling of these two circuits.
    Used to prevent the paralleling of non-synchronous topological islands."""

    __slots__ = ("max_angle_diff", "max_freq_diff", "max_volt_diff")

    max_angle_diff: float | None  # AngleRadians
    max_freq_diff: float | None  # Frequency
    max_volt_diff: float | None  # Voltage

    _cim_meta = ClassMeta(
        cim_name="SynchrocheckRelay",
        package="TC57CIM/IEC61970/Base/Protection",
        guid="{B00D97A5-F7E7-44ad-A2C8-EEE11DCF1F42}",
        attributes=(
            AttrMeta("max_angle_diff", "maxAngleDiff", "AngleRadians", 0, 1, "cimdatatype"),
            AttrMeta("max_freq_diff", "maxFreqDiff", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("max_volt_diff", "maxVoltDiff", "Voltage", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        max_angle_diff: float | None = None,
        max_freq_diff: float | None = None,
        max_volt_diff: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_angle_diff = max_angle_diff
        self.max_freq_diff = max_freq_diff
        self.max_volt_diff = max_volt_diff
