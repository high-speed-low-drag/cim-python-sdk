"""CIM class OldTransformerTankInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_info.transformer_tank_info import TransformerTankInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.oil_preservation_kind import (
        OilPreservationKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.transformer_construction_kind import (
        TransformerConstructionKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.transformer_core_kind import (
        TransformerCoreKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.transformer_function_kind import (
        TransformerFunctionKind,
    )


class OldTransformerTankInfo(TransformerTankInfo):
    """CIM class OldTransformerTankInfo."""

    __slots__ = (
        "construction_kind",
        "core_coils_weight",
        "core_kind",
        "function",
        "neutral_bil",
        "oil_preservation_kind",
    )

    construction_kind: TransformerConstructionKind | None
    core_kind: TransformerCoreKind | None
    function: TransformerFunctionKind | None
    oil_preservation_kind: OilPreservationKind | None
    core_coils_weight: float | None  # Mass
    neutral_bil: float | None  # Voltage

    _cim_meta = ClassMeta(
        cim_name="OldTransformerTankInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{27D05BB6-D441-4925-8E5D-8BE2039DF3E5}",
        attributes=(
            AttrMeta(
                "construction_kind",
                "constructionKind",
                "TransformerConstructionKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("core_kind", "coreKind", "TransformerCoreKind", 0, 1, "enumeration"),
            AttrMeta("function", "function", "TransformerFunctionKind", 0, 1, "enumeration"),
            AttrMeta(
                "oil_preservation_kind",
                "oilPreservationKind",
                "OilPreservationKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("core_coils_weight", "coreCoilsWeight", "Mass", 0, 1, "cimdatatype"),
            AttrMeta("neutral_bil", "neutralBIL", "Voltage", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        construction_kind: TransformerConstructionKind | None = None,
        core_kind: TransformerCoreKind | None = None,
        function: TransformerFunctionKind | None = None,
        oil_preservation_kind: OilPreservationKind | None = None,
        core_coils_weight: float | None = None,
        neutral_bil: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.construction_kind = construction_kind
        self.core_kind = core_kind
        self.function = function
        self.oil_preservation_kind = oil_preservation_kind
        self.core_coils_weight = core_coils_weight
        self.neutral_bil = neutral_bil
