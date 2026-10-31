"""CIM class EquipmentFault (TC57CIM/IEC61970/Base/Faults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.faults.fault import Fault

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal


class EquipmentFault(Fault):
    """A fault applied at the terminal, external to the equipment. This class is not used to
    specify faults internal to the equipment."""

    __slots__ = ("_terminal",)

    terminal: One[Terminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=0,
            upper=1,
            inverse="equipment_faults",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EquipmentFault",
        package="TC57CIM/IEC61970/Base/Faults",
        guid="{565ED47F-1E02-464b-8D9C-517ED5726DF3}",
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
