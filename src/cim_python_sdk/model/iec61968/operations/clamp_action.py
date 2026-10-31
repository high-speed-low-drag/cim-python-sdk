"""CIM class ClampAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.temp_equip_action_kind import TempEquipActionKind
    from cim_python_sdk.model.iec61970.base.wires.clamp import Clamp


class ClampAction(SwitchingAction):
    """Action on Clamp as a switching step"""

    __slots__ = ("_clamp", "kind")

    kind: TempEquipActionKind | None

    clamp: One[Clamp] = One(
        EndMeta(
            name="clamp",
            cim_role="Clamp",
            target="cim_python_sdk.model.iec61970.base.wires.clamp:Clamp",
            many=False,
            lower=0,
            upper=1,
            inverse="clamp_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ClampAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{1A877B96-636E-4f6d-9F3D-CB43E3082464}",
        attributes=(AttrMeta("kind", "kind", "TempEquipActionKind", 0, 1, "enumeration"),),
        ends=(clamp.meta,),
    )

    def __init__(
        self,
        *,
        kind: TempEquipActionKind | None = None,
        clamp: Clamp | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if clamp is not None:
            self.clamp = clamp
