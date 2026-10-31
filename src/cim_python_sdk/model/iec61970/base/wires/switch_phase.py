"""CIM class SwitchPhase (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind
    from cim_python_sdk.model.iec61970.base.wires.switch import Switch


class SwitchPhase(PowerSystemResource):
    """Single phase of a multi-phase switch when its attributes might be different per phase."""

    __slots__ = ("_switch", "closed", "normal_open", "phase_side1", "phase_side2", "rated_current")

    normal_open: bool | None
    phase_side1: SinglePhaseKind | None
    phase_side2: SinglePhaseKind | None
    closed: bool | None
    rated_current: float | None  # CurrentFlow

    switch: One[Switch] = One(
        EndMeta(
            name="switch",
            cim_role="Switch",
            target="cim_python_sdk.model.iec61970.base.wires.switch:Switch",
            many=False,
            lower=1,
            upper=1,
            inverse="switch_phase",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchPhase",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{4BAF4C19-5181-41b2-B690-9758DB9D4F8B}",
        attributes=(
            AttrMeta("normal_open", "normalOpen", "bool", 0, 1, "primitive"),
            AttrMeta("phase_side1", "phaseSide1", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("phase_side2", "phaseSide2", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("closed", "closed", "bool", 0, 1, "primitive"),
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
        ),
        ends=(switch.meta,),
    )

    def __init__(
        self,
        *,
        normal_open: bool | None = None,
        phase_side1: SinglePhaseKind | None = None,
        phase_side2: SinglePhaseKind | None = None,
        closed: bool | None = None,
        rated_current: float | None = None,
        switch: Switch | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.normal_open = normal_open
        self.phase_side1 = phase_side1
        self.phase_side2 = phase_side2
        self.closed = closed
        self.rated_current = rated_current
        if switch is not None:
            self.switch = switch
