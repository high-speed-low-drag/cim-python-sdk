"""CIM class OilAnalysisFluidAnalog (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_analog import AssetAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.oil_analysis_fluid_analog_kind import (
        OilAnalysisFluidAnalogKind,
    )


class OilAnalysisFluidAnalog(AssetAnalog):
    """Asset oil analysis fluid test type of analog.

    ."""

    __slots__ = ("kind",)

    kind: OilAnalysisFluidAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="OilAnalysisFluidAnalog",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{54A4C289-DCC4-4b33-92D8-5D30BF2336D8}",
        attributes=(AttrMeta("kind", "kind", "OilAnalysisFluidAnalogKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: OilAnalysisFluidAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
