"""CIM class PerLengthImpedance (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.per_length_line_parameter import (
    PerLengthLineParameter,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.ac_line_segment import ACLineSegment


class PerLengthImpedance(PerLengthLineParameter):
    """Common type for per-length impedance electrical catalogues."""

    __slots__ = ("_ac_line_segments",)

    ac_line_segments: Many[ACLineSegment] = Many(
        EndMeta(
            name="ac_line_segments",
            cim_role="ACLineSegments",
            target="cim_python_sdk.model.iec61970.base.wires.ac_line_segment:ACLineSegment",
            many=True,
            lower=0,
            upper=None,
            inverse="per_length_impedance",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PerLengthImpedance",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{C4C200C6-DFC4-4bec-AE5E-84B332E79E0C}",
        ends=(ac_line_segments.meta,),
    )

    def __init__(
        self,
        *,
        ac_line_segments: Iterable[ACLineSegment] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if ac_line_segments is not None:
            PerLengthImpedance.ac_line_segments.extend(self, ac_line_segments)

    def add_ac_line_segment(self, ac_line_segment: ACLineSegment) -> Self:
        return PerLengthImpedance.ac_line_segments.add(self, ac_line_segment)

    def remove_ac_line_segment(self, ac_line_segment: ACLineSegment) -> Self:
        return PerLengthImpedance.ac_line_segments.remove(self, ac_line_segment)

    def clear_ac_line_segments(self) -> Self:
        return PerLengthImpedance.ac_line_segments.clear(self)

    def num_ac_line_segment(self) -> int:
        return PerLengthImpedance.ac_line_segments.count(self)

    def get_ac_line_segment_by_mrid(self, mrid: str) -> ACLineSegment | None:
        return PerLengthImpedance.ac_line_segments.get_by_mrid(self, mrid)
