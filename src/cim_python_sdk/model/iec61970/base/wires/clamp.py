"""CIM class Clamp (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.clamp_action import ClampAction
    from cim_python_sdk.model.iec61968.operations.jumper_action import JumperAction
    from cim_python_sdk.model.iec61970.base.wires.ac_line_segment import ACLineSegment


class Clamp(ConductingEquipment):
    """A Clamp is a galvanic connection at a line segment where other equipment is connected. A
    Clamp does not cut the line segment.

    A Clamp is ConductingEquipment and has one Terminal with an associated ConnectivityNode.
    Any other ConductingEquipment can be connected to the Clamp ConnectivityNode."""

    __slots__ = ("_ac_line_segment", "_clamp_action", "_jumper_action", "length_from_terminal1")

    length_from_terminal1: float | None  # Length

    ac_line_segment: One[ACLineSegment] = One(
        EndMeta(
            name="ac_line_segment",
            cim_role="ACLineSegment",
            target="cim_python_sdk.model.iec61970.base.wires.ac_line_segment:ACLineSegment",
            many=False,
            lower=1,
            upper=1,
            inverse="clamp",
            aggregation="none",
        )
    )
    jumper_action: One[JumperAction] = One(
        EndMeta(
            name="jumper_action",
            cim_role="JumperAction",
            target="cim_python_sdk.model.iec61968.operations.jumper_action:JumperAction",
            many=False,
            lower=0,
            upper=1,
            inverse="clamp",
            aggregation="none",
        )
    )
    clamp_action: One[ClampAction] = One(
        EndMeta(
            name="clamp_action",
            cim_role="ClampAction",
            target="cim_python_sdk.model.iec61968.operations.clamp_action:ClampAction",
            many=False,
            lower=0,
            upper=1,
            inverse="clamp",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Clamp",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{7B0758AF-6E8E-438e-BD69-A838A56F256D}",
        attributes=(
            AttrMeta("length_from_terminal1", "lengthFromTerminal1", "Length", 0, 1, "cimdatatype"),
        ),
        ends=(
            ac_line_segment.meta,
            jumper_action.meta,
            clamp_action.meta,
        ),
    )

    def __init__(
        self,
        *,
        length_from_terminal1: float | None = None,
        ac_line_segment: ACLineSegment | None = None,
        jumper_action: JumperAction | None = None,
        clamp_action: ClampAction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.length_from_terminal1 = length_from_terminal1
        if ac_line_segment is not None:
            self.ac_line_segment = ac_line_segment
        if jumper_action is not None:
            self.jumper_action = jumper_action
        if clamp_action is not None:
            self.clamp_action = clamp_action
