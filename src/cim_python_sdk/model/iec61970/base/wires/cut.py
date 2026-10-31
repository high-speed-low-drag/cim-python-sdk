"""CIM class Cut (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.switch import Switch

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.cut_action import CutAction
    from cim_python_sdk.model.iec61970.base.wires.ac_line_segment import ACLineSegment


class Cut(Switch):
    """A cut separates a line segment into two parts. The cut appears as a switch inserted
    between these two parts and connects them together. As the cut is normally open there is
    no galvanic connection between the two line segment parts. But it is possible to close
    the cut to get galvanic connection.

    The cut terminals are oriented towards the line segment terminals with the same sequence
    number. Hence the cut terminal with sequence number equal to 1 is oriented to the line
    segment's terminal with sequence number equal to 1.

    The cut terminals also act as connection points for jumpers and other equipment, e.g. a
    mobile generator. To enable this, connectivity nodes are placed at the cut terminals.
    Once the connectivity nodes are in place any conducting equipment can be connected at
    them."""

    __slots__ = ("_ac_line_segment", "_cut_action", "length_from_terminal1")

    length_from_terminal1: float | None  # Length

    ac_line_segment: One[ACLineSegment] = One(
        EndMeta(
            name="ac_line_segment",
            cim_role="ACLineSegment",
            target="cim_python_sdk.model.iec61970.base.wires.ac_line_segment:ACLineSegment",
            many=False,
            lower=1,
            upper=1,
            inverse="cut",
            aggregation="none",
        )
    )
    cut_action: One[CutAction] = One(
        EndMeta(
            name="cut_action",
            cim_role="CutAction",
            target="cim_python_sdk.model.iec61968.operations.cut_action:CutAction",
            many=False,
            lower=0,
            upper=1,
            inverse="cut",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Cut",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{A7BE7DB8-C02A-427a-95EE-F342693F1590}",
        attributes=(
            AttrMeta("length_from_terminal1", "lengthFromTerminal1", "Length", 0, 1, "cimdatatype"),
        ),
        ends=(
            ac_line_segment.meta,
            cut_action.meta,
        ),
    )

    def __init__(
        self,
        *,
        length_from_terminal1: float | None = None,
        ac_line_segment: ACLineSegment | None = None,
        cut_action: CutAction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.length_from_terminal1 = length_from_terminal1
        if ac_line_segment is not None:
            self.ac_line_segment = ac_line_segment
        if cut_action is not None:
            self.cut_action = cut_action
