"""CIM class Ground (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.ground_action import GroundAction


class Ground(ConductingEquipment):
    """A point where the system is grounded used for connecting conducting equipment to ground.
    The power system model can have any number of grounds."""

    __slots__ = ("_ground_action",)

    ground_action: One[GroundAction] = One(
        EndMeta(
            name="ground_action",
            cim_role="GroundAction",
            target="cim_python_sdk.model.iec61968.operations.ground_action:GroundAction",
            many=False,
            lower=0,
            upper=1,
            inverse="ground",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Ground",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{437ABFFA-B6B0-47fd-BFE2-76ACD0B7FFDC}",
        ends=(ground_action.meta,),
    )

    def __init__(
        self,
        *,
        ground_action: GroundAction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if ground_action is not None:
            self.ground_action = ground_action
