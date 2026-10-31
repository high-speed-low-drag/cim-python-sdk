"""CIM class WirePosition (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.wire_phase_info import WirePhaseInfo
    from cim_python_sdk.model.iec61968.asset_info.wire_spacing_info import WireSpacingInfo


class WirePosition(IdentifiedObject):
    """Identification, spacing and configuration of the wires of a conductor with respect to a
    structure."""

    __slots__ = ("_wire_phase_info", "_wire_spacing_info", "sequence_number", "x_coord", "y_coord")

    x_coord: float | None  # Displacement
    y_coord: float | None  # Displacement
    sequence_number: int | None

    wire_phase_info: Many[WirePhaseInfo] = Many(
        EndMeta(
            name="wire_phase_info",
            cim_role="WirePhaseInfo",
            target="cim_python_sdk.model.iec61968.asset_info.wire_phase_info:WirePhaseInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="wire_position",
            aggregation="none",
        )
    )
    wire_spacing_info: One[WireSpacingInfo] = One(
        EndMeta(
            name="wire_spacing_info",
            cim_role="WireSpacingInfo",
            target="cim_python_sdk.model.iec61968.asset_info.wire_spacing_info:WireSpacingInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="wire_positions",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WirePosition",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{B62996D7-5A21-437d-9C1C-FCC061733196}",
        attributes=(
            AttrMeta("x_coord", "xCoord", "Displacement", 0, 1, "cimdatatype"),
            AttrMeta("y_coord", "yCoord", "Displacement", 0, 1, "cimdatatype"),
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
        ),
        ends=(
            wire_phase_info.meta,
            wire_spacing_info.meta,
        ),
    )

    def __init__(
        self,
        *,
        x_coord: float | None = None,
        y_coord: float | None = None,
        sequence_number: int | None = None,
        wire_phase_info: Iterable[WirePhaseInfo] | None = None,
        wire_spacing_info: WireSpacingInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.sequence_number = sequence_number
        if wire_phase_info is not None:
            WirePosition.wire_phase_info.extend(self, wire_phase_info)
        if wire_spacing_info is not None:
            self.wire_spacing_info = wire_spacing_info

    def add_wire_phase_info(self, wire_phase_info: WirePhaseInfo) -> Self:
        return WirePosition.wire_phase_info.add(self, wire_phase_info)

    def remove_wire_phase_info(self, wire_phase_info: WirePhaseInfo) -> Self:
        return WirePosition.wire_phase_info.remove(self, wire_phase_info)

    def clear_wire_phase_info(self) -> Self:
        return WirePosition.wire_phase_info.clear(self)

    def num_wire_phase_info(self) -> int:
        return WirePosition.wire_phase_info.count(self)
