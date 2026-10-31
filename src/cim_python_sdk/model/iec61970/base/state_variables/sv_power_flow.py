"""CIM class SvPowerFlow (TC57CIM/IEC61970/Base/StateVariables). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.state_variables.state_variable import StateVariable

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind
    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_group import EnergyGroup


class SvPowerFlow(StateVariable):
    """State variable for power flow. Load convention is used for flow direction. This means
    flow out from the TopologicalNode into the equipment is positive."""

    __slots__ = ("_energy_group", "_terminal", "p", "phase", "q")

    p: float | None  # ActivePower
    phase: SinglePhaseKind | None
    q: float | None  # ReactivePower

    terminal: One[Terminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=1,
            upper=1,
            inverse="sv_power_flow",
            aggregation="none",
        )
    )
    energy_group: One[EnergyGroup] = One(
        EndMeta(
            name="energy_group",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_group:EnergyGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="sv_power_flows",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SvPowerFlow",
        package="TC57CIM/IEC61970/Base/StateVariables",
        guid="{0289223C-1161-4047-84EC-201D00A0CD92}",
        attributes=(
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("q", "q", "ReactivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            terminal.meta,
            energy_group.meta,
        ),
    )

    def __init__(
        self,
        *,
        p: float | None = None,
        phase: SinglePhaseKind | None = None,
        q: float | None = None,
        terminal: Terminal | None = None,
        energy_group: EnergyGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.p = p
        self.phase = phase
        self.q = q
        if terminal is not None:
            self.terminal = terminal
        if energy_group is not None:
            self.energy_group = energy_group
