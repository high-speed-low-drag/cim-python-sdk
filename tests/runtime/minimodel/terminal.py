"""CIM class Terminal (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from tests.runtime.minimodel.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from tests.runtime.minimodel.conducting_equipment import ConductingEquipment


class Terminal(IdentifiedObject):
    """An AC electrical connection point to a piece of conducting equipment."""

    __slots__ = ("_conducting_equipment", "sequence_number")

    sequence_number: int | None

    conducting_equipment: One[ConductingEquipment] = One(
        EndMeta(
            name="conducting_equipment",
            cim_role="ConductingEquipment",
            target="tests.runtime.minimodel.conducting_equipment:ConductingEquipment",
            many=False,
            lower=1,
            upper=1,
            inverse="terminals",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Terminal",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{00000000-0000-0000-0000-00000000C004}",
        attributes=(AttrMeta("sequence_number", "sequenceNumber", "int", 1, 1, "primitive"),),
        ends=(conducting_equipment.meta,),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        conducting_equipment: ConductingEquipment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        if conducting_equipment is not None:
            self.conducting_equipment = conducting_equipment
