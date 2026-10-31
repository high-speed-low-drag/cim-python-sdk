"""CIM class Circuit (TC57CIM/IEC61970/InfIEC61970/Feeder). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.line import Line

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.bay import Bay
    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal


class Circuit(Line):
    """CIM class Circuit."""

    __slots__ = ("_end_bay", "_end_terminal")

    end_bay: Many[Bay] = Many(
        EndMeta(
            name="end_bay",
            cim_role="EndBay",
            target="cim_python_sdk.model.iec61970.base.core.bay:Bay",
            many=True,
            lower=0,
            upper=None,
            inverse="circuit",
            aggregation="none",
        )
    )
    end_terminal: Many[Terminal] = Many(
        EndMeta(
            name="end_terminal",
            cim_role="EndTerminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=True,
            lower=0,
            upper=None,
            inverse="circuit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Circuit",
        package="TC57CIM/IEC61970/InfIEC61970/Feeder",
        guid="{E27D9368-509B-4ea8-9C6C-99D10F5B57E1}",
        ends=(
            end_bay.meta,
            end_terminal.meta,
        ),
    )

    def __init__(
        self,
        *,
        end_bay: Iterable[Bay] | None = None,
        end_terminal: Iterable[Terminal] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if end_bay is not None:
            Circuit.end_bay.extend(self, end_bay)
        if end_terminal is not None:
            Circuit.end_terminal.extend(self, end_terminal)

    def add_end_bay(self, end_bay: Bay) -> Self:
        return Circuit.end_bay.add(self, end_bay)

    def remove_end_bay(self, end_bay: Bay) -> Self:
        return Circuit.end_bay.remove(self, end_bay)

    def clear_end_bay(self) -> Self:
        return Circuit.end_bay.clear(self)

    def num_end_bay(self) -> int:
        return Circuit.end_bay.count(self)

    def get_end_bay_by_mrid(self, mrid: str) -> Bay | None:
        return Circuit.end_bay.get_by_mrid(self, mrid)

    def add_end_terminal(self, end_terminal: Terminal) -> Self:
        return Circuit.end_terminal.add(self, end_terminal)

    def remove_end_terminal(self, end_terminal: Terminal) -> Self:
        return Circuit.end_terminal.remove(self, end_terminal)

    def clear_end_terminal(self) -> Self:
        return Circuit.end_terminal.clear(self)

    def num_end_terminal(self) -> int:
        return Circuit.end_terminal.count(self)

    def get_end_terminal_by_mrid(self, mrid: str) -> Terminal | None:
        return Circuit.end_terminal.get_by_mrid(self, mrid)
