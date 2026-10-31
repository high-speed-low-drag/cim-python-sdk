"""CIM class PinEquipment (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate_input_pin import GateInputPin

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_equipment_kind import (
        PinEquipmentKind,
    )


class PinEquipment(GateInputPin):
    """Value associated with Equipment is used as compare."""

    __slots__ = ("_equipment", "kind")

    kind: PinEquipmentKind | None

    equipment: One[Equipment] = One(
        EndMeta(
            name="equipment",
            cim_role="Equipment",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=False,
            lower=1,
            upper=1,
            inverse="pin_equipment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PinEquipment",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{0F70682A-0B2E-4542-ACC3-46F2CEBCDE73}",
        attributes=(AttrMeta("kind", "kind", "PinEquipmentKind", 0, 1, "enumeration"),),
        ends=(equipment.meta,),
    )

    def __init__(
        self,
        *,
        kind: PinEquipmentKind | None = None,
        equipment: Equipment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if equipment is not None:
            self.equipment = equipment
