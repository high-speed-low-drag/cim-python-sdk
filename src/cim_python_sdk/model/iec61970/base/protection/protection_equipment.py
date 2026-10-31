"""CIM class ProtectionEquipment (TC57CIM/IEC61970/Base/Protection). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.equipment import Equipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol
    from cim_python_sdk.model.iec61970.base.wires.protected_switch import ProtectedSwitch
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action import (
        ProtectiveAction,
    )


class ProtectionEquipment(Equipment):
    """An electrical device designed to respond to input conditions in a prescribed manner and
    after specified conditions are met to cause contact operation or similar abrupt change
    in associated electric control circuits, or simply to display the detected condition.
    Protection equipment is associated with conducting equipment and usually operate circuit
    breakers."""

    __slots__ = (
        "_conducting_equipments",
        "_protected_switches",
        "_protective_action",
        "high_limit",
        "low_limit",
        "power_direction_flag",
        "relay_delay_time",
        "unit_multiplier",
        "unit_symbol",
    )

    relay_delay_time: float | None  # Seconds
    high_limit: float | None
    low_limit: float | None
    power_direction_flag: bool | None
    unit_symbol: UnitSymbol | None
    unit_multiplier: UnitMultiplier | None

    conducting_equipments: Many[ConductingEquipment] = Many(
        EndMeta(
            name="conducting_equipments",
            cim_role="ConductingEquipments",
            target="cim_python_sdk.model.iec61970.base.core.conducting_equipment:ConductingEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="protection_equipments",
            aggregation="none",
        )
    )
    protected_switches: Many[ProtectedSwitch] = Many(
        EndMeta(
            name="protected_switches",
            cim_role="ProtectedSwitches",
            target="cim_python_sdk.model.iec61970.base.wires.protected_switch:ProtectedSwitch",
            many=True,
            lower=0,
            upper=None,
            inverse="operated_by_protection_equipment",
            aggregation="none",
        )
    )
    protective_action: Many[ProtectiveAction] = Many(
        EndMeta(
            name="protective_action",
            cim_role="ProtectiveAction",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action:ProtectiveAction",
            many=True,
            lower=0,
            upper=None,
            inverse="protection_equipment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProtectionEquipment",
        package="TC57CIM/IEC61970/Base/Protection",
        guid="{9EAE8A03-D411-432a-AC39-38ACEC6B1FAD}",
        attributes=(
            AttrMeta("relay_delay_time", "relayDelayTime", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("high_limit", "highLimit", "float", 0, 1, "primitive"),
            AttrMeta("low_limit", "lowLimit", "float", 0, 1, "primitive"),
            AttrMeta("power_direction_flag", "powerDirectionFlag", "bool", 0, 1, "primitive"),
            AttrMeta("unit_symbol", "unitSymbol", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta("unit_multiplier", "unitMultiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
        ends=(
            conducting_equipments.meta,
            protected_switches.meta,
            protective_action.meta,
        ),
    )

    def __init__(
        self,
        *,
        relay_delay_time: float | None = None,
        high_limit: float | None = None,
        low_limit: float | None = None,
        power_direction_flag: bool | None = None,
        unit_symbol: UnitSymbol | None = None,
        unit_multiplier: UnitMultiplier | None = None,
        conducting_equipments: Iterable[ConductingEquipment] | None = None,
        protected_switches: Iterable[ProtectedSwitch] | None = None,
        protective_action: Iterable[ProtectiveAction] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.relay_delay_time = relay_delay_time
        self.high_limit = high_limit
        self.low_limit = low_limit
        self.power_direction_flag = power_direction_flag
        self.unit_symbol = unit_symbol
        self.unit_multiplier = unit_multiplier
        if conducting_equipments is not None:
            ProtectionEquipment.conducting_equipments.extend(self, conducting_equipments)
        if protected_switches is not None:
            ProtectionEquipment.protected_switches.extend(self, protected_switches)
        if protective_action is not None:
            ProtectionEquipment.protective_action.extend(self, protective_action)

    def add_conducting_equipment(self, conducting_equipment: ConductingEquipment) -> Self:
        return ProtectionEquipment.conducting_equipments.add(self, conducting_equipment)

    def remove_conducting_equipment(self, conducting_equipment: ConductingEquipment) -> Self:
        return ProtectionEquipment.conducting_equipments.remove(self, conducting_equipment)

    def clear_conducting_equipments(self) -> Self:
        return ProtectionEquipment.conducting_equipments.clear(self)

    def num_conducting_equipment(self) -> int:
        return ProtectionEquipment.conducting_equipments.count(self)

    def get_conducting_equipment_by_mrid(self, mrid: str) -> ConductingEquipment | None:
        return ProtectionEquipment.conducting_equipments.get_by_mrid(self, mrid)

    def add_protected_switche(self, protected_switche: ProtectedSwitch) -> Self:
        return ProtectionEquipment.protected_switches.add(self, protected_switche)

    def remove_protected_switche(self, protected_switche: ProtectedSwitch) -> Self:
        return ProtectionEquipment.protected_switches.remove(self, protected_switche)

    def clear_protected_switches(self) -> Self:
        return ProtectionEquipment.protected_switches.clear(self)

    def num_protected_switche(self) -> int:
        return ProtectionEquipment.protected_switches.count(self)

    def get_protected_switche_by_mrid(self, mrid: str) -> ProtectedSwitch | None:
        return ProtectionEquipment.protected_switches.get_by_mrid(self, mrid)

    def add_protective_action(self, protective_action: ProtectiveAction) -> Self:
        return ProtectionEquipment.protective_action.add(self, protective_action)

    def remove_protective_action(self, protective_action: ProtectiveAction) -> Self:
        return ProtectionEquipment.protective_action.remove(self, protective_action)

    def clear_protective_action(self) -> Self:
        return ProtectionEquipment.protective_action.clear(self)

    def num_protective_action(self) -> int:
        return ProtectionEquipment.protective_action.count(self)

    def get_protective_action_by_mrid(self, mrid: str) -> ProtectiveAction | None:
        return ProtectionEquipment.protective_action.get_by_mrid(self, mrid)
