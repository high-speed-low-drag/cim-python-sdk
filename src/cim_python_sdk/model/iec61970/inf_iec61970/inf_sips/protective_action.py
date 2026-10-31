"""CIM class ProtectiveAction (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.protection.protection_equipment import (
        ProtectionEquipment,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate import Gate
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_collection import (
        ProtectiveActionCollection,
    )


class ProtectiveAction(IdentifiedObject):
    """A protective action for supporting the integrity of the power system."""

    __slots__ = (
        "_gate_com_condition",
        "_gate_enabled_condition",
        "_protection_equipment",
        "_protective_action_collection",
        "enabled",
        "normal_enabled",
    )

    enabled: bool | None
    normal_enabled: bool | None

    protective_action_collection: One[ProtectiveActionCollection] = One(
        EndMeta(
            name="protective_action_collection",
            cim_role="ProtectiveActionCollection",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_collection:ProtectiveActionCollection",
            many=False,
            lower=1,
            upper=1,
            inverse="protective_action",
            aggregation="none",
        )
    )
    gate_enabled_condition: One[Gate] = One(
        EndMeta(
            name="gate_enabled_condition",
            cim_role="GateEnabledCondition",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate:Gate",
            many=False,
            lower=0,
            upper=1,
            inverse="protective_action_enabled",
            aggregation="none",
        )
    )
    gate_com_condition: One[Gate] = One(
        EndMeta(
            name="gate_com_condition",
            cim_role="GateComCondition",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate:Gate",
            many=False,
            lower=0,
            upper=1,
            inverse="protective_action_com",
            aggregation="none",
        )
    )
    protection_equipment: One[ProtectionEquipment] = One(
        EndMeta(
            name="protection_equipment",
            cim_role="ProtectionEquipment",
            target="cim_python_sdk.model.iec61970.base.protection.protection_equipment:ProtectionEquipment",
            many=False,
            lower=0,
            upper=1,
            inverse="protective_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProtectiveAction",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{2786E00A-6880-4d25-8D67-475403893A82}",
        attributes=(
            AttrMeta("enabled", "enabled", "bool", 0, 1, "primitive"),
            AttrMeta("normal_enabled", "normalEnabled", "bool", 0, 1, "primitive"),
        ),
        ends=(
            protective_action_collection.meta,
            gate_enabled_condition.meta,
            gate_com_condition.meta,
            protection_equipment.meta,
        ),
    )

    def __init__(
        self,
        *,
        enabled: bool | None = None,
        normal_enabled: bool | None = None,
        protective_action_collection: ProtectiveActionCollection | None = None,
        gate_enabled_condition: Gate | None = None,
        gate_com_condition: Gate | None = None,
        protection_equipment: ProtectionEquipment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.enabled = enabled
        self.normal_enabled = normal_enabled
        if protective_action_collection is not None:
            self.protective_action_collection = protective_action_collection
        if gate_enabled_condition is not None:
            self.gate_enabled_condition = gate_enabled_condition
        if gate_com_condition is not None:
            self.gate_com_condition = gate_com_condition
        if protection_equipment is not None:
            self.protection_equipment = protection_equipment
