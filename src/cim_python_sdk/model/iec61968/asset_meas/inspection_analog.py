"""CIM class InspectionAnalog (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_analog import AssetAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.inspection_analog_kind import InspectionAnalogKind


class InspectionAnalog(AssetAnalog):
    """Asset inspection type of analog."""

    __slots__ = ("kind",)

    kind: InspectionAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="InspectionAnalog",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{A9A741B5-E772-424b-A705-77F294FAC685}",
        attributes=(AttrMeta("kind", "kind", "InspectionAnalogKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: InspectionAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
