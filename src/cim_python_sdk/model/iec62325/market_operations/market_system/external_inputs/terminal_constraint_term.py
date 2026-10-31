"""CIM class TerminalConstraintTerm (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.constraint_term import (
    ConstraintTerm,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_terminal import (
        MktTerminal,
    )


class TerminalConstraintTerm(ConstraintTerm):
    """A constraint term associated with a specific terminal on a physical piece of equipment."""

    __slots__ = ("_mkt_terminal",)

    mkt_terminal: One[MktTerminal] = One(
        EndMeta(
            name="mkt_terminal",
            cim_role="MktTerminal",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_terminal:MktTerminal",
            many=False,
            lower=1,
            upper=1,
            inverse="terminal_constraint_term",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TerminalConstraintTerm",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{4705BCBF-E616-4d1c-8CA4-3AD2BD777401}",
        ends=(mkt_terminal.meta,),
    )

    def __init__(
        self,
        *,
        mkt_terminal: MktTerminal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if mkt_terminal is not None:
            self.mkt_terminal = mkt_terminal
