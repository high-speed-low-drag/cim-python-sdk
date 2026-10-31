"""CIM class WireSpacingInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.wire_position import WirePosition
    from cim_python_sdk.model.iec61968.asset_info.wire_usage_kind import WireUsageKind
    from cim_python_sdk.model.iec61968.assets.duct_bank import DuctBank
    from cim_python_sdk.model.iec61968.assets.structure import Structure
    from cim_python_sdk.model.iec61970.base.wires.ac_line_segment import ACLineSegment


class WireSpacingInfo(AssetInfo):
    """Wire spacing data that associates multiple wire positions with the line segment, and
    allows to calculate line segment impedances. Number of phases can be derived from the
    number of associated wire positions whose phase is not neutral."""

    __slots__ = (
        "_ac_line_segment",
        "_duct_bank",
        "_structures",
        "_wire_positions",
        "is_cable",
        "phase_wire_count",
        "phase_wire_spacing",
        "usage",
    )

    is_cable: bool | None
    phase_wire_count: int | None
    phase_wire_spacing: float | None  # Length
    usage: WireUsageKind | None

    duct_bank: One[DuctBank] = One(
        EndMeta(
            name="duct_bank",
            cim_role="DuctBank",
            target="cim_python_sdk.model.iec61968.assets.duct_bank:DuctBank",
            many=False,
            lower=0,
            upper=1,
            inverse="wire_spacing_infos",
            aggregation="none",
        )
    )
    structures: Many[Structure] = Many(
        EndMeta(
            name="structures",
            cim_role="Structures",
            target="cim_python_sdk.model.iec61968.assets.structure:Structure",
            many=True,
            lower=0,
            upper=None,
            inverse="wire_spacing_infos",
            aggregation="none",
        )
    )
    wire_positions: Many[WirePosition] = Many(
        EndMeta(
            name="wire_positions",
            cim_role="WirePositions",
            target="cim_python_sdk.model.iec61968.asset_info.wire_position:WirePosition",
            many=True,
            lower=1,
            upper=None,
            inverse="wire_spacing_info",
            aggregation="none",
        )
    )
    ac_line_segment: Many[ACLineSegment] = Many(
        EndMeta(
            name="ac_line_segment",
            cim_role="ACLineSegment",
            target="cim_python_sdk.model.iec61970.base.wires.ac_line_segment:ACLineSegment",
            many=True,
            lower=0,
            upper=None,
            inverse="wire_spacing_info",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WireSpacingInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{B035BD42-43E8-49f5-9685-B4ECF92364A4}",
        attributes=(
            AttrMeta("is_cable", "isCable", "bool", 0, 1, "primitive"),
            AttrMeta("phase_wire_count", "phaseWireCount", "int", 0, 1, "primitive"),
            AttrMeta("phase_wire_spacing", "phaseWireSpacing", "Length", 0, 1, "cimdatatype"),
            AttrMeta("usage", "usage", "WireUsageKind", 0, 1, "enumeration"),
        ),
        ends=(
            duct_bank.meta,
            structures.meta,
            wire_positions.meta,
            ac_line_segment.meta,
        ),
    )

    def __init__(
        self,
        *,
        is_cable: bool | None = None,
        phase_wire_count: int | None = None,
        phase_wire_spacing: float | None = None,
        usage: WireUsageKind | None = None,
        duct_bank: DuctBank | None = None,
        structures: Iterable[Structure] | None = None,
        wire_positions: Iterable[WirePosition] | None = None,
        ac_line_segment: Iterable[ACLineSegment] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_cable = is_cable
        self.phase_wire_count = phase_wire_count
        self.phase_wire_spacing = phase_wire_spacing
        self.usage = usage
        if duct_bank is not None:
            self.duct_bank = duct_bank
        if structures is not None:
            WireSpacingInfo.structures.extend(self, structures)
        if wire_positions is not None:
            WireSpacingInfo.wire_positions.extend(self, wire_positions)
        if ac_line_segment is not None:
            WireSpacingInfo.ac_line_segment.extend(self, ac_line_segment)

    def add_structure(self, structure: Structure) -> Self:
        return WireSpacingInfo.structures.add(self, structure)

    def remove_structure(self, structure: Structure) -> Self:
        return WireSpacingInfo.structures.remove(self, structure)

    def clear_structures(self) -> Self:
        return WireSpacingInfo.structures.clear(self)

    def num_structure(self) -> int:
        return WireSpacingInfo.structures.count(self)

    def get_structure_by_mrid(self, mrid: str) -> Structure | None:
        return WireSpacingInfo.structures.get_by_mrid(self, mrid)

    def add_wire_position(self, wire_position: WirePosition) -> Self:
        return WireSpacingInfo.wire_positions.add(self, wire_position)

    def remove_wire_position(self, wire_position: WirePosition) -> Self:
        return WireSpacingInfo.wire_positions.remove(self, wire_position)

    def clear_wire_positions(self) -> Self:
        return WireSpacingInfo.wire_positions.clear(self)

    def num_wire_position(self) -> int:
        return WireSpacingInfo.wire_positions.count(self)

    def get_wire_position_by_mrid(self, mrid: str) -> WirePosition | None:
        return WireSpacingInfo.wire_positions.get_by_mrid(self, mrid)

    def add_ac_line_segment(self, ac_line_segment: ACLineSegment) -> Self:
        return WireSpacingInfo.ac_line_segment.add(self, ac_line_segment)

    def remove_ac_line_segment(self, ac_line_segment: ACLineSegment) -> Self:
        return WireSpacingInfo.ac_line_segment.remove(self, ac_line_segment)

    def clear_ac_line_segment(self) -> Self:
        return WireSpacingInfo.ac_line_segment.clear(self)

    def num_ac_line_segment(self) -> int:
        return WireSpacingInfo.ac_line_segment.count(self)

    def get_ac_line_segment_by_mrid(self, mrid: str) -> ACLineSegment | None:
        return WireSpacingInfo.ac_line_segment.get_by_mrid(self, mrid)
