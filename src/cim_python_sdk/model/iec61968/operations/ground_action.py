"""CIM class GroundAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.temp_equip_action_kind import TempEquipActionKind
    from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment
    from cim_python_sdk.model.iec61970.base.wires.ac_line_segment import ACLineSegment
    from cim_python_sdk.model.iec61970.base.wires.ground import Ground


class GroundAction(SwitchingAction):
    """Action on ground as a switching step."""

    __slots__ = ("_along_ac_line_segment", "_ground", "_grounded_equipment", "kind")

    kind: TempEquipActionKind | None

    along_ac_line_segment: One[ACLineSegment] = One(
        EndMeta(
            name="along_ac_line_segment",
            cim_role="AlongACLineSegment",
            target="cim_python_sdk.model.iec61970.base.wires.ac_line_segment:ACLineSegment",
            many=False,
            lower=0,
            upper=1,
            inverse="line_grounding_action",
            aggregation="none",
        )
    )
    ground: One[Ground] = One(
        EndMeta(
            name="ground",
            cim_role="Ground",
            target="cim_python_sdk.model.iec61970.base.wires.ground:Ground",
            many=False,
            lower=0,
            upper=1,
            inverse="ground_action",
            aggregation="none",
        )
    )
    grounded_equipment: One[ConductingEquipment] = One(
        EndMeta(
            name="grounded_equipment",
            cim_role="GroundedEquipment",
            target="cim_python_sdk.model.iec61970.base.core.conducting_equipment:ConductingEquipment",
            many=False,
            lower=0,
            upper=1,
            inverse="grounding_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GroundAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{2EC03659-4055-4b75-AD25-BA805A479D1D}",
        attributes=(AttrMeta("kind", "kind", "TempEquipActionKind", 0, 1, "enumeration"),),
        ends=(
            along_ac_line_segment.meta,
            ground.meta,
            grounded_equipment.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: TempEquipActionKind | None = None,
        along_ac_line_segment: ACLineSegment | None = None,
        ground: Ground | None = None,
        grounded_equipment: ConductingEquipment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if along_ac_line_segment is not None:
            self.along_ac_line_segment = along_ac_line_segment
        if ground is not None:
            self.ground = ground
        if grounded_equipment is not None:
            self.grounded_equipment = grounded_equipment
