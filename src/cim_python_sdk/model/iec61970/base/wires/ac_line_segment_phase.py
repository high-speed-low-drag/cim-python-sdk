"""CIM class ACLineSegmentPhase (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_info.wire_info import WireInfo
    from cim_python_sdk.model.iec61970.base.wires.ac_line_segment import ACLineSegment
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class ACLineSegmentPhase(PowerSystemResource):
    """Represents a single wire of an alternating current line segment."""

    __slots__ = ("_ac_line_segment", "_wire_info", "phase", "sequence_number")

    phase: SinglePhaseKind | None
    sequence_number: int | None

    ac_line_segment: One[ACLineSegment] = One(
        EndMeta(
            name="ac_line_segment",
            cim_role="ACLineSegment",
            target="cim_python_sdk.model.iec61970.base.wires.ac_line_segment:ACLineSegment",
            many=False,
            lower=1,
            upper=1,
            inverse="ac_line_segment_phases",
            aggregation="none",
        )
    )
    wire_info: One[WireInfo] = One(
        EndMeta(
            name="wire_info",
            cim_role="WireInfo",
            target="cim_python_sdk.model.iec61968.asset_info.wire_info:WireInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="ac_line_segment_phase",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ACLineSegmentPhase",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{84627F88-F666-4f07-890A-62622070CD0F}",
        attributes=(
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
        ),
        ends=(
            ac_line_segment.meta,
            wire_info.meta,
        ),
    )

    def __init__(
        self,
        *,
        phase: SinglePhaseKind | None = None,
        sequence_number: int | None = None,
        ac_line_segment: ACLineSegment | None = None,
        wire_info: WireInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.phase = phase
        self.sequence_number = sequence_number
        if ac_line_segment is not None:
            self.ac_line_segment = ac_line_segment
        if wire_info is not None:
            self.wire_info = wire_info
