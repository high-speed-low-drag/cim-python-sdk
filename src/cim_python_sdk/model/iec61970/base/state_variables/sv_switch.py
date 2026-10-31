"""CIM class SvSwitch (TC57CIM/IEC61970/Base/StateVariables). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.state_variables.state_variable import StateVariable

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind
    from cim_python_sdk.model.iec61970.base.wires.switch import Switch


class SvSwitch(StateVariable):
    """State variable for switch."""

    __slots__ = ("_switch", "open", "phase")

    open: bool | None
    phase: SinglePhaseKind | None

    switch: One[Switch] = One(
        EndMeta(
            name="switch",
            cim_role="Switch",
            target="cim_python_sdk.model.iec61970.base.wires.switch:Switch",
            many=False,
            lower=1,
            upper=1,
            inverse="sv_switch",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SvSwitch",
        package="TC57CIM/IEC61970/Base/StateVariables",
        guid="{039A6EAC-2BB9-4f9a-A578-F925C2AD8468}",
        attributes=(
            AttrMeta("open", "open", "bool", 0, 1, "primitive"),
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
        ),
        ends=(switch.meta,),
    )

    def __init__(
        self,
        *,
        open: bool | None = None,
        phase: SinglePhaseKind | None = None,
        switch: Switch | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.open = open
        self.phase = phase
        if switch is not None:
            self.switch = switch
