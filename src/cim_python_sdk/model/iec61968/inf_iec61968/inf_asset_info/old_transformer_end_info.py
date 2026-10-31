"""CIM class OldTransformerEndInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_info.transformer_end_info import TransformerEndInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.winding_insulation_kind import (
        WindingInsulationKind,
    )


class OldTransformerEndInfo(TransformerEndInfo):
    """CIM class OldTransformerEndInfo."""

    __slots__ = (
        "day_over_load_rating",
        "hour_over_load_rating",
        "solid_insulation_weight",
        "winding_insulation_kind",
    )

    winding_insulation_kind: WindingInsulationKind | None
    solid_insulation_weight: float | None  # Mass
    hour_over_load_rating: float | None  # ApparentPower
    day_over_load_rating: float | None  # ApparentPower

    _cim_meta = ClassMeta(
        cim_name="OldTransformerEndInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{81DF1954-79FE-4b6f-BFB6-E760D899C702}",
        attributes=(
            AttrMeta(
                "winding_insulation_kind",
                "windingInsulationKind",
                "WindingInsulationKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "solid_insulation_weight", "solidInsulationWeight", "Mass", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "hour_over_load_rating", "hourOverLoadRating", "ApparentPower", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "day_over_load_rating", "dayOverLoadRating", "ApparentPower", 0, 1, "cimdatatype"
            ),
        ),
    )

    def __init__(
        self,
        *,
        winding_insulation_kind: WindingInsulationKind | None = None,
        solid_insulation_weight: float | None = None,
        hour_over_load_rating: float | None = None,
        day_over_load_rating: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.winding_insulation_kind = winding_insulation_kind
        self.solid_insulation_weight = solid_insulation_weight
        self.hour_over_load_rating = hour_over_load_rating
        self.day_over_load_rating = day_over_load_rating
