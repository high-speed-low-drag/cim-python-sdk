"""CIM class WireSegment (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.conductor import Conductor

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.wire_segment_phase import WireSegmentPhase


class WireSegment(Conductor):
    """A two terminal and power conducting device of negligible impedance and length
    represented as zero impedance device that can be used to connect auxiliary equipment to
    its terminals."""

    __slots__ = ("_wire_segment_phases",)

    wire_segment_phases: Many[WireSegmentPhase] = Many(
        EndMeta(
            name="wire_segment_phases",
            cim_role="WireSegmentPhases",
            target="cim_python_sdk.model.iec61970.base.wires.wire_segment_phase:WireSegmentPhase",
            many=True,
            lower=0,
            upper=None,
            inverse="wire_segment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WireSegment",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{56BC76FE-5834-43c3-A34B-B9749293629D}",
        ends=(wire_segment_phases.meta,),
    )

    def __init__(
        self,
        *,
        wire_segment_phases: Iterable[WireSegmentPhase] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wire_segment_phases is not None:
            WireSegment.wire_segment_phases.extend(self, wire_segment_phases)

    def add_wire_segment_phase(self, wire_segment_phase: WireSegmentPhase) -> Self:
        return WireSegment.wire_segment_phases.add(self, wire_segment_phase)

    def remove_wire_segment_phase(self, wire_segment_phase: WireSegmentPhase) -> Self:
        return WireSegment.wire_segment_phases.remove(self, wire_segment_phase)

    def clear_wire_segment_phases(self) -> Self:
        return WireSegment.wire_segment_phases.clear(self)

    def num_wire_segment_phase(self) -> int:
        return WireSegment.wire_segment_phases.count(self)

    def get_wire_segment_phase_by_mrid(self, mrid: str) -> WireSegmentPhase | None:
        return WireSegment.wire_segment_phases.get_by_mrid(self, mrid)
