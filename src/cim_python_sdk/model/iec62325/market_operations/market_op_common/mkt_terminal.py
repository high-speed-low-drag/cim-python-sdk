"""CIM class MktTerminal (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.terminal import Terminal

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.terminal_constraint_term import (
        TerminalConstraintTerm,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class MktTerminal(Terminal):
    """Subclass of IEC61970:Core:Terminal."""

    __slots__ = ("_flowgate", "_terminal_constraint_term")

    terminal_constraint_term: Many[TerminalConstraintTerm] = Many(
        EndMeta(
            name="terminal_constraint_term",
            cim_role="TerminalConstraintTerm",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.terminal_constraint_term:TerminalConstraintTerm",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_terminal",
            aggregation="none",
        )
    )
    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_terminal",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktTerminal",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{CB4EA124-E91C-4e18-97EC-1AFD85646AFE}",
        ends=(
            terminal_constraint_term.meta,
            flowgate.meta,
        ),
    )

    def __init__(
        self,
        *,
        terminal_constraint_term: Iterable[TerminalConstraintTerm] | None = None,
        flowgate: Flowgate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if terminal_constraint_term is not None:
            MktTerminal.terminal_constraint_term.extend(self, terminal_constraint_term)
        if flowgate is not None:
            self.flowgate = flowgate

    def add_terminal_constraint_term(
        self, terminal_constraint_term: TerminalConstraintTerm
    ) -> Self:
        return MktTerminal.terminal_constraint_term.add(self, terminal_constraint_term)

    def remove_terminal_constraint_term(
        self, terminal_constraint_term: TerminalConstraintTerm
    ) -> Self:
        return MktTerminal.terminal_constraint_term.remove(self, terminal_constraint_term)

    def clear_terminal_constraint_term(self) -> Self:
        return MktTerminal.terminal_constraint_term.clear(self)

    def num_terminal_constraint_term(self) -> int:
        return MktTerminal.terminal_constraint_term.count(self)

    def get_terminal_constraint_term_by_mrid(self, mrid: str) -> TerminalConstraintTerm | None:
        return MktTerminal.terminal_constraint_term.get_by_mrid(self, mrid)
