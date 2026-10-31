"""CIM class ContingencyEquipment (TC57CIM/IEC61970/Base/Contingency). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.contingency.contingency_element import ContingencyElement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.contingency.contingency_equipment_status_kind import (
        ContingencyEquipmentStatusKind,
    )
    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment


class ContingencyEquipment(ContingencyElement):
    """Equipment whose in service status is to change, such as a power transformer or AC line
    segment."""

    __slots__ = ("_equipment", "contingent_status")

    contingent_status: ContingencyEquipmentStatusKind | None

    equipment: One[Equipment] = One(
        EndMeta(
            name="equipment",
            cim_role="Equipment",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=False,
            lower=1,
            upper=1,
            inverse="contingency_equipment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ContingencyEquipment",
        package="TC57CIM/IEC61970/Base/Contingency",
        guid="{1ED472A0-8419-4547-A0B3-86DBCB9831B4}",
        attributes=(
            AttrMeta(
                "contingent_status",
                "contingentStatus",
                "ContingencyEquipmentStatusKind",
                0,
                1,
                "enumeration",
            ),
        ),
        ends=(equipment.meta,),
    )

    def __init__(
        self,
        *,
        contingent_status: ContingencyEquipmentStatusKind | None = None,
        equipment: Equipment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.contingent_status = contingent_status
        if equipment is not None:
            self.equipment = equipment
