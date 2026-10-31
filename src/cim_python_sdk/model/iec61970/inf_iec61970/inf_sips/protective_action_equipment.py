"""CIM class ProtectiveActionEquipment (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action import ProtectiveAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment


class ProtectiveActionEquipment(ProtectiveAction):
    """Protective action to put an Equipment in-service/out-of-service."""

    __slots__ = ("_equipment", "in_service")

    in_service: bool | None

    equipment: One[Equipment] = One(
        EndMeta(
            name="equipment",
            cim_role="Equipment",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=False,
            lower=1,
            upper=1,
            inverse="protective_action_equipment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProtectiveActionEquipment",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{FC41A9D7-3388-4465-847F-47FA8090CE1F}",
        attributes=(AttrMeta("in_service", "inService", "bool", 0, 1, "primitive"),),
        ends=(equipment.meta,),
    )

    def __init__(
        self,
        *,
        in_service: bool | None = None,
        equipment: Equipment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.in_service = in_service
        if equipment is not None:
            self.equipment = equipment
