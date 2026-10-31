"""CIM class CutAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.temp_equip_action_kind import TempEquipActionKind
    from cim_python_sdk.model.iec61970.base.wires.cut import Cut


class CutAction(SwitchingAction):
    """Action on cut as a switching step."""

    __slots__ = ("_cut", "kind")

    kind: TempEquipActionKind | None

    cut: One[Cut] = One(
        EndMeta(
            name="cut",
            cim_role="Cut",
            target="cim_python_sdk.model.iec61970.base.wires.cut:Cut",
            many=False,
            lower=0,
            upper=1,
            inverse="cut_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CutAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{40FB11D9-C203-4534-89FA-28F98BB3DC72}",
        attributes=(AttrMeta("kind", "kind", "TempEquipActionKind", 0, 1, "enumeration"),),
        ends=(cut.meta,),
    )

    def __init__(
        self,
        *,
        kind: TempEquipActionKind | None = None,
        cut: Cut | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if cut is not None:
            self.cut = cut
