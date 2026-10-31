"""CIM class JumperAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.temp_equip_action_kind import TempEquipActionKind
    from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment
    from cim_python_sdk.model.iec61970.base.wires.ac_line_segment import ACLineSegment
    from cim_python_sdk.model.iec61970.base.wires.clamp import Clamp
    from cim_python_sdk.model.iec61970.base.wires.jumper import Jumper


class JumperAction(SwitchingAction):
    """Action on jumper as a switching step."""

    __slots__ = ("_ac_line_segments", "_clamp", "_jumped_equipments", "_jumper", "kind")

    kind: TempEquipActionKind | None

    jumped_equipments: Many[ConductingEquipment] = Many(
        EndMeta(
            name="jumped_equipments",
            cim_role="JumpedEquipments",
            target="cim_python_sdk.model.iec61970.base.core.conducting_equipment:ConductingEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="jumping_action",
            aggregation="none",
        )
    )
    clamp: One[Clamp] = One(
        EndMeta(
            name="clamp",
            cim_role="Clamp",
            target="cim_python_sdk.model.iec61970.base.wires.clamp:Clamp",
            many=False,
            lower=0,
            upper=1,
            inverse="jumper_action",
            aggregation="none",
        )
    )
    ac_line_segments: Many[ACLineSegment] = Many(
        EndMeta(
            name="ac_line_segments",
            cim_role="ACLineSegments",
            target="cim_python_sdk.model.iec61970.base.wires.ac_line_segment:ACLineSegment",
            many=True,
            lower=0,
            upper=None,
            inverse="line_jumping_action",
            aggregation="none",
        )
    )
    jumper: One[Jumper] = One(
        EndMeta(
            name="jumper",
            cim_role="Jumper",
            target="cim_python_sdk.model.iec61970.base.wires.jumper:Jumper",
            many=False,
            lower=0,
            upper=1,
            inverse="jumper_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="JumperAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{2A90B861-B4FF-4aa8-9A3E-67859AB1303D}",
        attributes=(AttrMeta("kind", "kind", "TempEquipActionKind", 0, 1, "enumeration"),),
        ends=(
            jumped_equipments.meta,
            clamp.meta,
            ac_line_segments.meta,
            jumper.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: TempEquipActionKind | None = None,
        jumped_equipments: Iterable[ConductingEquipment] | None = None,
        clamp: Clamp | None = None,
        ac_line_segments: Iterable[ACLineSegment] | None = None,
        jumper: Jumper | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if jumped_equipments is not None:
            JumperAction.jumped_equipments.extend(self, jumped_equipments)
        if clamp is not None:
            self.clamp = clamp
        if ac_line_segments is not None:
            JumperAction.ac_line_segments.extend(self, ac_line_segments)
        if jumper is not None:
            self.jumper = jumper

    def add_jumped_equipment(self, jumped_equipment: ConductingEquipment) -> Self:
        return JumperAction.jumped_equipments.add(self, jumped_equipment)

    def remove_jumped_equipment(self, jumped_equipment: ConductingEquipment) -> Self:
        return JumperAction.jumped_equipments.remove(self, jumped_equipment)

    def clear_jumped_equipments(self) -> Self:
        return JumperAction.jumped_equipments.clear(self)

    def num_jumped_equipment(self) -> int:
        return JumperAction.jumped_equipments.count(self)

    def get_jumped_equipment_by_mrid(self, mrid: str) -> ConductingEquipment | None:
        return JumperAction.jumped_equipments.get_by_mrid(self, mrid)

    def add_ac_line_segment(self, ac_line_segment: ACLineSegment) -> Self:
        return JumperAction.ac_line_segments.add(self, ac_line_segment)

    def remove_ac_line_segment(self, ac_line_segment: ACLineSegment) -> Self:
        return JumperAction.ac_line_segments.remove(self, ac_line_segment)

    def clear_ac_line_segments(self) -> Self:
        return JumperAction.ac_line_segments.clear(self)

    def num_ac_line_segment(self) -> int:
        return JumperAction.ac_line_segments.count(self)

    def get_ac_line_segment_by_mrid(self, mrid: str) -> ACLineSegment | None:
        return JumperAction.ac_line_segments.get_by_mrid(self, mrid)
