"""CIM class PerLengthDCLineParameter (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.per_length_line_parameter import (
    PerLengthLineParameter,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.dc.dc_line_segment import DCLineSegment


class PerLengthDCLineParameter(PerLengthLineParameter):
    """Common type for per-length electrical catalogues describing DC line parameters."""

    __slots__ = ("_dc_line_segments", "capacitance", "inductance", "resistance")

    capacitance: float | None  # CapacitancePerLength
    inductance: float | None  # InductancePerLength
    resistance: float | None  # ResistancePerLength

    dc_line_segments: Many[DCLineSegment] = Many(
        EndMeta(
            name="dc_line_segments",
            cim_role="DCLineSegments",
            target="cim_python_sdk.model.iec61970.base.dc.dc_line_segment:DCLineSegment",
            many=True,
            lower=0,
            upper=None,
            inverse="per_length_parameter",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PerLengthDCLineParameter",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{5D15EC24-6829-4038-80A3-6C8F1C58EE75}",
        attributes=(
            AttrMeta("capacitance", "capacitance", "CapacitancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("inductance", "inductance", "InductancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("resistance", "resistance", "ResistancePerLength", 0, 1, "cimdatatype"),
        ),
        ends=(dc_line_segments.meta,),
    )

    def __init__(
        self,
        *,
        capacitance: float | None = None,
        inductance: float | None = None,
        resistance: float | None = None,
        dc_line_segments: Iterable[DCLineSegment] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.capacitance = capacitance
        self.inductance = inductance
        self.resistance = resistance
        if dc_line_segments is not None:
            PerLengthDCLineParameter.dc_line_segments.extend(self, dc_line_segments)

    def add_dc_line_segment(self, dc_line_segment: DCLineSegment) -> Self:
        return PerLengthDCLineParameter.dc_line_segments.add(self, dc_line_segment)

    def remove_dc_line_segment(self, dc_line_segment: DCLineSegment) -> Self:
        return PerLengthDCLineParameter.dc_line_segments.remove(self, dc_line_segment)

    def clear_dc_line_segments(self) -> Self:
        return PerLengthDCLineParameter.dc_line_segments.clear(self)

    def num_dc_line_segment(self) -> int:
        return PerLengthDCLineParameter.dc_line_segments.count(self)

    def get_dc_line_segment_by_mrid(self, mrid: str) -> DCLineSegment | None:
        return PerLengthDCLineParameter.dc_line_segments.get_by_mrid(self, mrid)
