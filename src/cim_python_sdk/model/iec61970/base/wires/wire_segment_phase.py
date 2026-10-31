"""CIM class WireSegmentPhase (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind
    from cim_python_sdk.model.iec61970.base.wires.wire_segment import WireSegment


class WireSegmentPhase(PowerSystemResource):
    """Represents a single wire of an alternating current wire segment."""

    __slots__ = ("_wire_segment", "phase", "sequence_number")

    phase: SinglePhaseKind | None
    sequence_number: int | None

    wire_segment: One[WireSegment] = One(
        EndMeta(
            name="wire_segment",
            cim_role="WireSegment",
            target="cim_python_sdk.model.iec61970.base.wires.wire_segment:WireSegment",
            many=False,
            lower=1,
            upper=1,
            inverse="wire_segment_phases",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WireSegmentPhase",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{91BE148F-E7B0-4687-B275-4A9FF1797051}",
        attributes=(
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
        ),
        ends=(wire_segment.meta,),
    )

    def __init__(
        self,
        *,
        phase: SinglePhaseKind | None = None,
        sequence_number: int | None = None,
        wire_segment: WireSegment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.phase = phase
        self.sequence_number = sequence_number
        if wire_segment is not None:
            self.wire_segment = wire_segment
