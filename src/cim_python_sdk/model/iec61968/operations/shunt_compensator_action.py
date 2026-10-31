"""CIM class ShuntCompensatorAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.temp_equip_action_kind import TempEquipActionKind
    from cim_python_sdk.model.iec61970.base.wires.shunt_compensator import ShuntCompensator


class ShuntCompensatorAction(SwitchingAction):
    """CIM class ShuntCompensatorAction."""

    __slots__ = ("_shunt_compensator", "kind")

    kind: TempEquipActionKind | None

    shunt_compensator: One[ShuntCompensator] = One(
        EndMeta(
            name="shunt_compensator",
            cim_role="ShuntCompensator",
            target="cim_python_sdk.model.iec61970.base.wires.shunt_compensator:ShuntCompensator",
            many=False,
            lower=0,
            upper=1,
            inverse="shunt_compensator_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ShuntCompensatorAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{428D6B1A-AE90-437e-8E09-3318CF951328}",
        attributes=(AttrMeta("kind", "kind", "TempEquipActionKind", 0, 1, "enumeration"),),
        ends=(shunt_compensator.meta,),
    )

    def __init__(
        self,
        *,
        kind: TempEquipActionKind | None = None,
        shunt_compensator: ShuntCompensator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if shunt_compensator is not None:
            self.shunt_compensator = shunt_compensator
