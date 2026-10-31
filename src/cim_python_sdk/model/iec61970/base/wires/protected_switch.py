"""CIM class ProtectedSwitch (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.switch import Switch

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.protection.protection_equipment import (
        ProtectionEquipment,
    )
    from cim_python_sdk.model.iec61970.base.protection.reclose_sequence import RecloseSequence


class ProtectedSwitch(Switch):
    """A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment."""

    __slots__ = ("_operated_by_protection_equipment", "_reclose_sequences", "breaking_capacity")

    breaking_capacity: float | None  # CurrentFlow

    reclose_sequences: Many[RecloseSequence] = Many(
        EndMeta(
            name="reclose_sequences",
            cim_role="RecloseSequences",
            target="cim_python_sdk.model.iec61970.base.protection.reclose_sequence:RecloseSequence",
            many=True,
            lower=0,
            upper=None,
            inverse="protected_switch",
            aggregation="shared",
        )
    )
    operated_by_protection_equipment: Many[ProtectionEquipment] = Many(
        EndMeta(
            name="operated_by_protection_equipment",
            cim_role="OperatedByProtectionEquipment",
            target="cim_python_sdk.model.iec61970.base.protection.protection_equipment:ProtectionEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="protected_switches",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProtectedSwitch",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{BADE2A18-37F4-49bf-87BC-A087E4D2E4F7}",
        attributes=(
            AttrMeta("breaking_capacity", "breakingCapacity", "CurrentFlow", 0, 1, "cimdatatype"),
        ),
        ends=(
            reclose_sequences.meta,
            operated_by_protection_equipment.meta,
        ),
    )

    def __init__(
        self,
        *,
        breaking_capacity: float | None = None,
        reclose_sequences: Iterable[RecloseSequence] | None = None,
        operated_by_protection_equipment: Iterable[ProtectionEquipment] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.breaking_capacity = breaking_capacity
        if reclose_sequences is not None:
            ProtectedSwitch.reclose_sequences.extend(self, reclose_sequences)
        if operated_by_protection_equipment is not None:
            ProtectedSwitch.operated_by_protection_equipment.extend(
                self, operated_by_protection_equipment
            )

    def add_reclose_sequence(self, reclose_sequence: RecloseSequence) -> Self:
        return ProtectedSwitch.reclose_sequences.add(self, reclose_sequence)

    def remove_reclose_sequence(self, reclose_sequence: RecloseSequence) -> Self:
        return ProtectedSwitch.reclose_sequences.remove(self, reclose_sequence)

    def clear_reclose_sequences(self) -> Self:
        return ProtectedSwitch.reclose_sequences.clear(self)

    def num_reclose_sequence(self) -> int:
        return ProtectedSwitch.reclose_sequences.count(self)

    def get_reclose_sequence_by_mrid(self, mrid: str) -> RecloseSequence | None:
        return ProtectedSwitch.reclose_sequences.get_by_mrid(self, mrid)

    def add_operated_by_protection_equipment(
        self, operated_by_protection_equipment: ProtectionEquipment
    ) -> Self:
        return ProtectedSwitch.operated_by_protection_equipment.add(
            self, operated_by_protection_equipment
        )

    def remove_operated_by_protection_equipment(
        self, operated_by_protection_equipment: ProtectionEquipment
    ) -> Self:
        return ProtectedSwitch.operated_by_protection_equipment.remove(
            self, operated_by_protection_equipment
        )

    def clear_operated_by_protection_equipment(self) -> Self:
        return ProtectedSwitch.operated_by_protection_equipment.clear(self)

    def num_operated_by_protection_equipment(self) -> int:
        return ProtectedSwitch.operated_by_protection_equipment.count(self)

    def get_operated_by_protection_equipment_by_mrid(self, mrid: str) -> ProtectionEquipment | None:
        return ProtectedSwitch.operated_by_protection_equipment.get_by_mrid(self, mrid)
