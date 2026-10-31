"""CIM class TieFlow (TC57CIM/IEC61970/Base/ControlArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.control_area.alt_tie_meas import AltTieMeas
    from cim_python_sdk.model.iec61970.base.control_area.control_area import ControlArea
    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal


class TieFlow(IdentifiedObject):
    """Defines the structure (in terms of location and direction) of the net interchange
    constraint for a control area. This constraint may be used by either AGC or power flow."""

    __slots__ = ("_alt_tie_meas", "_control_area", "_terminal", "positive_flow_in")

    positive_flow_in: bool | None

    terminal: One[Terminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=1,
            upper=1,
            inverse="tie_flow",
            aggregation="none",
        )
    )
    control_area: One[ControlArea] = One(
        EndMeta(
            name="control_area",
            cim_role="ControlArea",
            target="cim_python_sdk.model.iec61970.base.control_area.control_area:ControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="tie_flow",
            aggregation="none",
        )
    )
    alt_tie_meas: Many[AltTieMeas] = Many(
        EndMeta(
            name="alt_tie_meas",
            cim_role="AltTieMeas",
            target="cim_python_sdk.model.iec61970.base.control_area.alt_tie_meas:AltTieMeas",
            many=True,
            lower=0,
            upper=None,
            inverse="tie_flow",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TieFlow",
        package="TC57CIM/IEC61970/Base/ControlArea",
        guid="{AA47BC16-A18A-4beb-9CB3-5F942819B925}",
        attributes=(AttrMeta("positive_flow_in", "positiveFlowIn", "bool", 0, 1, "primitive"),),
        ends=(
            terminal.meta,
            control_area.meta,
            alt_tie_meas.meta,
        ),
    )

    def __init__(
        self,
        *,
        positive_flow_in: bool | None = None,
        terminal: Terminal | None = None,
        control_area: ControlArea | None = None,
        alt_tie_meas: Iterable[AltTieMeas] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.positive_flow_in = positive_flow_in
        if terminal is not None:
            self.terminal = terminal
        if control_area is not None:
            self.control_area = control_area
        if alt_tie_meas is not None:
            TieFlow.alt_tie_meas.extend(self, alt_tie_meas)

    def add_alt_tie_mea(self, alt_tie_mea: AltTieMeas) -> Self:
        return TieFlow.alt_tie_meas.add(self, alt_tie_mea)

    def remove_alt_tie_mea(self, alt_tie_mea: AltTieMeas) -> Self:
        return TieFlow.alt_tie_meas.remove(self, alt_tie_mea)

    def clear_alt_tie_meas(self) -> Self:
        return TieFlow.alt_tie_meas.clear(self)

    def num_alt_tie_mea(self) -> int:
        return TieFlow.alt_tie_meas.count(self)

    def get_alt_tie_mea_by_mrid(self, mrid: str) -> AltTieMeas | None:
        return TieFlow.alt_tie_meas.get_by_mrid(self, mrid)
