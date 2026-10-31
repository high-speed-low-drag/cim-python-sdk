"""CIM class SvInjection (TC57CIM/IEC61970/Base/StateVariables). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.state_variables.state_variable import StateVariable

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.topology.topological_node import TopologicalNode
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class SvInjection(StateVariable):
    """The SvInjection reports the calculated bus injection minus the sum of the terminal
    flows. The terminal flow is positive out from the bus (load sign convention) and bus
    injection has positive flow into the bus. SvInjection may have the remainder after state
    estimation or slack after power flow calculation."""

    __slots__ = ("_topological_node", "p_injection", "phase", "q_injection")

    phase: SinglePhaseKind | None
    p_injection: float | None  # ActivePower
    q_injection: float | None  # ReactivePower

    topological_node: One[TopologicalNode] = One(
        EndMeta(
            name="topological_node",
            cim_role="TopologicalNode",
            target="cim_python_sdk.model.iec61970.base.topology.topological_node:TopologicalNode",
            many=False,
            lower=1,
            upper=1,
            inverse="sv_injection",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SvInjection",
        package="TC57CIM/IEC61970/Base/StateVariables",
        guid="{067C680D-D749-4c6a-891E-0DE4CAAD8451}",
        attributes=(
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("p_injection", "pInjection", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("q_injection", "qInjection", "ReactivePower", 0, 1, "cimdatatype"),
        ),
        ends=(topological_node.meta,),
    )

    def __init__(
        self,
        *,
        phase: SinglePhaseKind | None = None,
        p_injection: float | None = None,
        q_injection: float | None = None,
        topological_node: TopologicalNode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.phase = phase
        self.p_injection = p_injection
        self.q_injection = q_injection
        if topological_node is not None:
            self.topological_node = topological_node
