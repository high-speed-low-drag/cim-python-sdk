"""CIM class AssetTemperaturePressureAnalog (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_analog import AssetAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.asset_temperature_pressure_analog_kind import (
        AssetTemperaturePressureAnalogKind,
    )


class AssetTemperaturePressureAnalog(AssetAnalog):
    """Temperature or pressure type of asset analog."""

    __slots__ = ("kind",)

    kind: AssetTemperaturePressureAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="AssetTemperaturePressureAnalog",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{209F5C9F-32CE-4ac6-9D01-9FAD6305692B}",
        attributes=(
            AttrMeta("kind", "kind", "AssetTemperaturePressureAnalogKind", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        kind: AssetTemperaturePressureAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
