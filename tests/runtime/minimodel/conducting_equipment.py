"""CIM class ConductingEquipment (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from tests.runtime.minimodel.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from tests.runtime.minimodel.terminal import Terminal


class ConductingEquipment(PowerSystemResource):
    """The parts of the AC power system that are designed to carry current or that are
    conductively connected through terminals."""

    __slots__ = ("_terminals", "nominal_voltage")

    nominal_voltage: float | None  # Voltage

    terminals: Many[Terminal] = Many(
        EndMeta(
            name="terminals",
            cim_role="Terminals",
            target="tests.runtime.minimodel.terminal:Terminal",
            many=True,
            lower=0,
            upper=None,
            inverse="conducting_equipment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConductingEquipment",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{00000000-0000-0000-0000-00000000C003}",
        attributes=(AttrMeta("nominal_voltage", "nominalVoltage", "Voltage", 0, 1, "cimdatatype"),),
        ends=(terminals.meta,),
    )

    def __init__(
        self,
        *,
        nominal_voltage: float | None = None,
        terminals: Iterable[Terminal] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.nominal_voltage = nominal_voltage
        if terminals is not None:
            ConductingEquipment.terminals.extend(self, terminals)

    def add_terminal(self, terminal: Terminal) -> Self:
        return ConductingEquipment.terminals.add(self, terminal)

    def remove_terminal(self, terminal: Terminal) -> Self:
        return ConductingEquipment.terminals.remove(self, terminal)

    def clear_terminals(self) -> Self:
        return ConductingEquipment.terminals.clear(self)

    def num_terminal(self) -> int:
        return ConductingEquipment.terminals.count(self)

    def get_terminal_by_mrid(self, mrid: str) -> Terminal | None:
        return ConductingEquipment.terminals.get_by_mrid(self, mrid)
