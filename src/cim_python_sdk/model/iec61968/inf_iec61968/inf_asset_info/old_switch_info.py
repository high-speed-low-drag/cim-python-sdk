"""CIM class OldSwitchInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_info.switch_info import SwitchInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class OldSwitchInfo(SwitchInfo):
    """Properties of switch assets."""

    __slots__ = (
        "dielectric_strength",
        "load_break",
        "making_capacity",
        "minimum_current",
        "pole_count",
        "remote",
        "withstand_current",
    )

    remote: bool | None
    load_break: bool | None
    minimum_current: float | None  # CurrentFlow
    making_capacity: float | None  # CurrentFlow
    pole_count: int | None
    withstand_current: float | None  # CurrentFlow
    dielectric_strength: float | None  # Voltage

    _cim_meta = ClassMeta(
        cim_name="OldSwitchInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{DFEA6966-9F30-4ec7-81DF-D0A1F33EC95A}",
        attributes=(
            AttrMeta("remote", "remote", "bool", 0, 1, "primitive"),
            AttrMeta("load_break", "loadBreak", "bool", 0, 1, "primitive"),
            AttrMeta("minimum_current", "minimumCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("making_capacity", "makingCapacity", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("pole_count", "poleCount", "int", 0, 1, "primitive"),
            AttrMeta("withstand_current", "withstandCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("dielectric_strength", "dielectricStrength", "Voltage", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        remote: bool | None = None,
        load_break: bool | None = None,
        minimum_current: float | None = None,
        making_capacity: float | None = None,
        pole_count: int | None = None,
        withstand_current: float | None = None,
        dielectric_strength: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.remote = remote
        self.load_break = load_break
        self.minimum_current = minimum_current
        self.making_capacity = making_capacity
        self.pole_count = pole_count
        self.withstand_current = withstand_current
        self.dielectric_strength = dielectric_strength
