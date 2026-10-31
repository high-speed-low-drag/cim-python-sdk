"""CIM class DCTerminal (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.dc.dc_base_terminal import DCBaseTerminal

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.dc.dc_conducting_equipment import DCConductingEquipment


class DCTerminal(DCBaseTerminal):
    """An electrical connection point to generic DC conducting equipment."""

    __slots__ = ("_dc_conducting_equipment",)

    dc_conducting_equipment: One[DCConductingEquipment] = One(
        EndMeta(
            name="dc_conducting_equipment",
            cim_role="DCConductingEquipment",
            target="cim_python_sdk.model.iec61970.base.dc.dc_conducting_equipment:DCConductingEquipment",
            many=False,
            lower=1,
            upper=1,
            inverse="dc_terminals",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCTerminal",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{6D3668E7-3378-46de-B0B6-9EB6724C8326}",
        ends=(dc_conducting_equipment.meta,),
    )

    def __init__(
        self,
        *,
        dc_conducting_equipment: DCConductingEquipment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dc_conducting_equipment is not None:
            self.dc_conducting_equipment = dc_conducting_equipment
