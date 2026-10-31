"""CIM class SvVoltage (TC57CIM/IEC61970/Base/StateVariables). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.state_variables.state_variable import StateVariable

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.topology.topological_node import TopologicalNode
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class SvVoltage(StateVariable):
    """State variable for voltage."""

    __slots__ = ("_topological_node", "angle", "phase", "v")

    angle: float | None  # AngleDegrees
    phase: SinglePhaseKind | None
    v: float | None  # Voltage

    topological_node: One[TopologicalNode] = One(
        EndMeta(
            name="topological_node",
            cim_role="TopologicalNode",
            target="cim_python_sdk.model.iec61970.base.topology.topological_node:TopologicalNode",
            many=False,
            lower=1,
            upper=1,
            inverse="sv_voltage",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SvVoltage",
        package="TC57CIM/IEC61970/Base/StateVariables",
        guid="{22A26B24-0A8E-402a-895E-AFAE18292542}",
        attributes=(
            AttrMeta("angle", "angle", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("v", "v", "Voltage", 0, 1, "cimdatatype"),
        ),
        ends=(topological_node.meta,),
    )

    def __init__(
        self,
        *,
        angle: float | None = None,
        phase: SinglePhaseKind | None = None,
        v: float | None = None,
        topological_node: TopologicalNode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.angle = angle
        self.phase = phase
        self.v = v
        if topological_node is not None:
            self.topological_node = topological_node
