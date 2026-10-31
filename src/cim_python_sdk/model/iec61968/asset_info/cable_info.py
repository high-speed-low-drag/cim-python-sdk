"""CIM class CableInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_info.wire_info import WireInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_info.cable_construction_kind import (
        CableConstructionKind,
    )
    from cim_python_sdk.model.iec61968.asset_info.cable_outer_jacket_kind import (
        CableOuterJacketKind,
    )
    from cim_python_sdk.model.iec61968.asset_info.cable_shield_material_kind import (
        CableShieldMaterialKind,
    )


class CableInfo(WireInfo):
    """Cable data."""

    __slots__ = (
        "construction_kind",
        "diameter_over_core",
        "diameter_over_insulation",
        "diameter_over_jacket",
        "diameter_over_screen",
        "is_strand_fill",
        "nominal_temperature",
        "outer_jacket_kind",
        "sheath_as_neutral",
        "shield_material",
    )

    construction_kind: CableConstructionKind | None
    diameter_over_core: float | None  # Length
    diameter_over_insulation: float | None  # Length
    diameter_over_jacket: float | None  # Length
    diameter_over_screen: float | None  # Length
    nominal_temperature: float | None  # Temperature
    outer_jacket_kind: CableOuterJacketKind | None
    sheath_as_neutral: bool | None
    shield_material: CableShieldMaterialKind | None
    is_strand_fill: bool | None

    _cim_meta = ClassMeta(
        cim_name="CableInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{5AF01DB8-B1BF-4c26-8CA4-8030D36E725A}",
        attributes=(
            AttrMeta(
                "construction_kind",
                "constructionKind",
                "CableConstructionKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("diameter_over_core", "diameterOverCore", "Length", 0, 1, "cimdatatype"),
            AttrMeta(
                "diameter_over_insulation", "diameterOverInsulation", "Length", 0, 1, "cimdatatype"
            ),
            AttrMeta("diameter_over_jacket", "diameterOverJacket", "Length", 0, 1, "cimdatatype"),
            AttrMeta("diameter_over_screen", "diameterOverScreen", "Length", 0, 1, "cimdatatype"),
            AttrMeta(
                "nominal_temperature", "nominalTemperature", "Temperature", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "outer_jacket_kind", "outerJacketKind", "CableOuterJacketKind", 0, 1, "enumeration"
            ),
            AttrMeta("sheath_as_neutral", "sheathAsNeutral", "bool", 0, 1, "primitive"),
            AttrMeta(
                "shield_material", "shieldMaterial", "CableShieldMaterialKind", 0, 1, "enumeration"
            ),
            AttrMeta("is_strand_fill", "isStrandFill", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        construction_kind: CableConstructionKind | None = None,
        diameter_over_core: float | None = None,
        diameter_over_insulation: float | None = None,
        diameter_over_jacket: float | None = None,
        diameter_over_screen: float | None = None,
        nominal_temperature: float | None = None,
        outer_jacket_kind: CableOuterJacketKind | None = None,
        sheath_as_neutral: bool | None = None,
        shield_material: CableShieldMaterialKind | None = None,
        is_strand_fill: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.construction_kind = construction_kind
        self.diameter_over_core = diameter_over_core
        self.diameter_over_insulation = diameter_over_insulation
        self.diameter_over_jacket = diameter_over_jacket
        self.diameter_over_screen = diameter_over_screen
        self.nominal_temperature = nominal_temperature
        self.outer_jacket_kind = outer_jacket_kind
        self.sheath_as_neutral = sheath_as_neutral
        self.shield_material = shield_material
        self.is_strand_fill = is_strand_fill
