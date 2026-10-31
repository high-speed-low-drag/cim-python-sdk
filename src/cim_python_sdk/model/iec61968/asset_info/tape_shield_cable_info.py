"""CIM class TapeShieldCableInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_info.cable_info import CableInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class TapeShieldCableInfo(CableInfo):
    """Tape shield cable data."""

    __slots__ = ("tape_lap", "tape_thickness")

    tape_lap: float | None  # PerCent
    tape_thickness: float | None  # Length

    _cim_meta = ClassMeta(
        cim_name="TapeShieldCableInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{A8752772-CFD3-4eb2-9456-73B15504040D}",
        attributes=(
            AttrMeta("tape_lap", "tapeLap", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("tape_thickness", "tapeThickness", "Length", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        tape_lap: float | None = None,
        tape_thickness: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tape_lap = tape_lap
        self.tape_thickness = tape_thickness
