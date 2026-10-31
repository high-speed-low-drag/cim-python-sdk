"""CIM class AuxiliaryEquipment (TC57CIM/IEC61970/Base/AuxiliaryEquipment). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.equipment import Equipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal


class AuxiliaryEquipment(Equipment):
    """AuxiliaryEquipment describe equipment that is not performing any primary functions but
    support for the equipment performing the primary function.

    AuxiliaryEquipment is attached to primary equipment via an association with Terminal."""

    __slots__ = ("_terminal",)

    terminal: One[Terminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=1,
            upper=1,
            inverse="auxiliary_equipment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AuxiliaryEquipment",
        package="TC57CIM/IEC61970/Base/AuxiliaryEquipment",
        guid="{CB6ECCEF-5854-40ec-A5DD-6A4E884E859C}",
        ends=(terminal.meta,),
    )

    def __init__(
        self,
        *,
        terminal: Terminal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if terminal is not None:
            self.terminal = terminal
