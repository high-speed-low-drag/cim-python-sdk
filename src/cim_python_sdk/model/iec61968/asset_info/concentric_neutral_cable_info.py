"""CIM class ConcentricNeutralCableInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_info.cable_info import CableInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ConcentricNeutralCableInfo(CableInfo):
    """Concentric neutral cable data."""

    __slots__ = (
        "diameter_over_neutral",
        "neutral_strand_count",
        "neutral_strand_gmr",
        "neutral_strand_radius",
        "neutral_strand_rdc20",
    )

    diameter_over_neutral: float | None  # Length
    neutral_strand_count: int | None
    neutral_strand_radius: float | None  # Length
    neutral_strand_gmr: float | None  # Length
    neutral_strand_rdc20: float | None  # ResistancePerLength

    _cim_meta = ClassMeta(
        cim_name="ConcentricNeutralCableInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{8941D960-35C7-43ed-967C-6A75F2F2C02A}",
        attributes=(
            AttrMeta("diameter_over_neutral", "diameterOverNeutral", "Length", 0, 1, "cimdatatype"),
            AttrMeta("neutral_strand_count", "neutralStrandCount", "int", 0, 1, "primitive"),
            AttrMeta("neutral_strand_radius", "neutralStrandRadius", "Length", 0, 1, "cimdatatype"),
            AttrMeta("neutral_strand_gmr", "neutralStrandGmr", "Length", 0, 1, "cimdatatype"),
            AttrMeta(
                "neutral_strand_rdc20",
                "neutralStrandRDC20",
                "ResistancePerLength",
                0,
                1,
                "cimdatatype",
            ),
        ),
    )

    def __init__(
        self,
        *,
        diameter_over_neutral: float | None = None,
        neutral_strand_count: int | None = None,
        neutral_strand_radius: float | None = None,
        neutral_strand_gmr: float | None = None,
        neutral_strand_rdc20: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.diameter_over_neutral = diameter_over_neutral
        self.neutral_strand_count = neutral_strand_count
        self.neutral_strand_radius = neutral_strand_radius
        self.neutral_strand_gmr = neutral_strand_gmr
        self.neutral_strand_rdc20 = neutral_strand_rdc20
