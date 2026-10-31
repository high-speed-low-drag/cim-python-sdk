"""CIM class PinTerminal (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate_input_pin import GateInputPin

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_terminal_kind import (
        PinTerminalKind,
    )


class PinTerminal(GateInputPin):
    """Value associated with Terminal is used as compare."""

    __slots__ = ("_terminal", "kind")

    kind: PinTerminalKind | None

    terminal: One[Terminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=1,
            upper=1,
            inverse="pin_terminal",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PinTerminal",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{66F63EBF-9677-468b-B919-D7477FE9FBE3}",
        attributes=(AttrMeta("kind", "kind", "PinTerminalKind", 0, 1, "enumeration"),),
        ends=(terminal.meta,),
    )

    def __init__(
        self,
        *,
        kind: PinTerminalKind | None = None,
        terminal: Terminal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if terminal is not None:
            self.terminal = terminal
