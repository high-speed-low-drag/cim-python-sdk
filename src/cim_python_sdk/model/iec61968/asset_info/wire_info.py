"""CIM class WireInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.wire_insulation_kind import WireInsulationKind
    from cim_python_sdk.model.iec61968.asset_info.wire_material_kind import WireMaterialKind
    from cim_python_sdk.model.iec61968.asset_info.wire_phase_info import WirePhaseInfo
    from cim_python_sdk.model.iec61970.base.wires.ac_line_segment_phase import ACLineSegmentPhase


class WireInfo(AssetInfo):
    """Wire data that can be specified per line segment phase, or for the line segment as a
    whole in case its phases all have the same wire characteristics."""

    __slots__ = (
        "_ac_line_segment_phase",
        "_wire_phase_info",
        "core_radius",
        "core_strand_count",
        "gmr",
        "insulated",
        "insulation_material",
        "insulation_thickness",
        "material",
        "r_ac25",
        "r_ac50",
        "r_ac75",
        "r_dc20",
        "radius",
        "rated_current",
        "size_description",
        "strand_count",
    )

    insulated: bool | None
    insulation_material: WireInsulationKind | None
    insulation_thickness: float | None  # Length
    material: WireMaterialKind | None
    size_description: str | None
    radius: float | None  # Length
    strand_count: int | None
    core_radius: float | None  # Length
    core_strand_count: int | None
    gmr: float | None  # Length
    rated_current: float | None  # CurrentFlow
    r_ac25: float | None  # ResistancePerLength
    r_ac50: float | None  # ResistancePerLength
    r_ac75: float | None  # ResistancePerLength
    r_dc20: float | None  # ResistancePerLength

    ac_line_segment_phase: Many[ACLineSegmentPhase] = Many(
        EndMeta(
            name="ac_line_segment_phase",
            cim_role="ACLineSegmentPhase",
            target="cim_python_sdk.model.iec61970.base.wires.ac_line_segment_phase:ACLineSegmentPhase",
            many=True,
            lower=0,
            upper=None,
            inverse="wire_info",
            aggregation="none",
        )
    )
    wire_phase_info: Many[WirePhaseInfo] = Many(
        EndMeta(
            name="wire_phase_info",
            cim_role="WirePhaseInfo",
            target="cim_python_sdk.model.iec61968.asset_info.wire_phase_info:WirePhaseInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="wire_info",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WireInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{4C4D8C3D-A5C2-4fec-B9AF-1E5CDB329B44}",
        attributes=(
            AttrMeta("insulated", "insulated", "bool", 0, 1, "primitive"),
            AttrMeta(
                "insulation_material",
                "insulationMaterial",
                "WireInsulationKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("insulation_thickness", "insulationThickness", "Length", 0, 1, "cimdatatype"),
            AttrMeta("material", "material", "WireMaterialKind", 0, 1, "enumeration"),
            AttrMeta("size_description", "sizeDescription", "str", 0, 1, "primitive"),
            AttrMeta("radius", "radius", "Length", 0, 1, "cimdatatype"),
            AttrMeta("strand_count", "strandCount", "int", 0, 1, "primitive"),
            AttrMeta("core_radius", "coreRadius", "Length", 0, 1, "cimdatatype"),
            AttrMeta("core_strand_count", "coreStrandCount", "int", 0, 1, "primitive"),
            AttrMeta("gmr", "gmr", "Length", 0, 1, "cimdatatype"),
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("r_ac25", "rAC25", "ResistancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("r_ac50", "rAC50", "ResistancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("r_ac75", "rAC75", "ResistancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("r_dc20", "rDC20", "ResistancePerLength", 0, 1, "cimdatatype"),
        ),
        ends=(
            ac_line_segment_phase.meta,
            wire_phase_info.meta,
        ),
    )

    def __init__(
        self,
        *,
        insulated: bool | None = None,
        insulation_material: WireInsulationKind | None = None,
        insulation_thickness: float | None = None,
        material: WireMaterialKind | None = None,
        size_description: str | None = None,
        radius: float | None = None,
        strand_count: int | None = None,
        core_radius: float | None = None,
        core_strand_count: int | None = None,
        gmr: float | None = None,
        rated_current: float | None = None,
        r_ac25: float | None = None,
        r_ac50: float | None = None,
        r_ac75: float | None = None,
        r_dc20: float | None = None,
        ac_line_segment_phase: Iterable[ACLineSegmentPhase] | None = None,
        wire_phase_info: Iterable[WirePhaseInfo] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.insulated = insulated
        self.insulation_material = insulation_material
        self.insulation_thickness = insulation_thickness
        self.material = material
        self.size_description = size_description
        self.radius = radius
        self.strand_count = strand_count
        self.core_radius = core_radius
        self.core_strand_count = core_strand_count
        self.gmr = gmr
        self.rated_current = rated_current
        self.r_ac25 = r_ac25
        self.r_ac50 = r_ac50
        self.r_ac75 = r_ac75
        self.r_dc20 = r_dc20
        if ac_line_segment_phase is not None:
            WireInfo.ac_line_segment_phase.extend(self, ac_line_segment_phase)
        if wire_phase_info is not None:
            WireInfo.wire_phase_info.extend(self, wire_phase_info)

    def add_ac_line_segment_phase(self, ac_line_segment_phase: ACLineSegmentPhase) -> Self:
        return WireInfo.ac_line_segment_phase.add(self, ac_line_segment_phase)

    def remove_ac_line_segment_phase(self, ac_line_segment_phase: ACLineSegmentPhase) -> Self:
        return WireInfo.ac_line_segment_phase.remove(self, ac_line_segment_phase)

    def clear_ac_line_segment_phase(self) -> Self:
        return WireInfo.ac_line_segment_phase.clear(self)

    def num_ac_line_segment_phase(self) -> int:
        return WireInfo.ac_line_segment_phase.count(self)

    def get_ac_line_segment_phase_by_mrid(self, mrid: str) -> ACLineSegmentPhase | None:
        return WireInfo.ac_line_segment_phase.get_by_mrid(self, mrid)

    def add_wire_phase_info(self, wire_phase_info: WirePhaseInfo) -> Self:
        return WireInfo.wire_phase_info.add(self, wire_phase_info)

    def remove_wire_phase_info(self, wire_phase_info: WirePhaseInfo) -> Self:
        return WireInfo.wire_phase_info.remove(self, wire_phase_info)

    def clear_wire_phase_info(self) -> Self:
        return WireInfo.wire_phase_info.clear(self)

    def num_wire_phase_info(self) -> int:
        return WireInfo.wire_phase_info.count(self)
