"""CIM class InspectionDiscrete (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_discrete import AssetDiscrete

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.inspection_discrete_kind import (
        InspectionDiscreteKind,
    )


class InspectionDiscrete(AssetDiscrete):
    """Asset inspection type of discrete."""

    __slots__ = ("kind",)

    kind: InspectionDiscreteKind | None

    _cim_meta = ClassMeta(
        cim_name="InspectionDiscrete",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{3B2DAA43-17A3-4b9a-A295-55F2F49B5E7D}",
        attributes=(AttrMeta("kind", "kind", "InspectionDiscreteKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: InspectionDiscreteKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
