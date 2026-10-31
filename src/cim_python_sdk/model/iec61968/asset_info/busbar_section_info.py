"""CIM class BusbarSectionInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class BusbarSectionInfo(AssetInfo):
    """Busbar section data."""

    __slots__ = ("rated_current", "rated_voltage")

    rated_voltage: float | None  # Voltage
    rated_current: float | None  # CurrentFlow

    _cim_meta = ClassMeta(
        cim_name="BusbarSectionInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{95039B97-087A-444e-9A08-E301D7CE84C7}",
        attributes=(
            AttrMeta("rated_voltage", "ratedVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        rated_voltage: float | None = None,
        rated_current: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rated_voltage = rated_voltage
        self.rated_current = rated_current
