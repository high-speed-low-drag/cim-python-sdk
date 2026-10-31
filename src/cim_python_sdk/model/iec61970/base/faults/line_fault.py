"""CIM class LineFault (TC57CIM/IEC61970/Base/Faults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.faults.fault import Fault

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.ac_line_segment import ACLineSegment


class LineFault(Fault):
    """A fault that occurs on an AC line segment at some point along the length."""

    __slots__ = ("_ac_line_segment", "length_from_terminal1")

    length_from_terminal1: float | None  # Length

    ac_line_segment: One[ACLineSegment] = One(
        EndMeta(
            name="ac_line_segment",
            cim_role="ACLineSegment",
            target="cim_python_sdk.model.iec61970.base.wires.ac_line_segment:ACLineSegment",
            many=False,
            lower=0,
            upper=1,
            inverse="line_faults",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LineFault",
        package="TC57CIM/IEC61970/Base/Faults",
        guid="{784DAFDE-99A3-4b69-A759-169FFD08E627}",
        attributes=(
            AttrMeta("length_from_terminal1", "lengthFromTerminal1", "Length", 0, 1, "cimdatatype"),
        ),
        ends=(ac_line_segment.meta,),
    )

    def __init__(
        self,
        *,
        length_from_terminal1: float | None = None,
        ac_line_segment: ACLineSegment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.length_from_terminal1 = length_from_terminal1
        if ac_line_segment is not None:
            self.ac_line_segment = ac_line_segment
