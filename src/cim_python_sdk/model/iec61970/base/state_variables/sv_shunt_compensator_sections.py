"""CIM class SvShuntCompensatorSections (TC57CIM/IEC61970/Base/StateVariables). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.state_variables.state_variable import StateVariable

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.shunt_compensator import ShuntCompensator
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class SvShuntCompensatorSections(StateVariable):
    """State variable for the number of sections in service for a shunt compensator."""

    __slots__ = ("_shunt_compensator", "phase", "sections")

    sections: float | None
    phase: SinglePhaseKind | None

    shunt_compensator: One[ShuntCompensator] = One(
        EndMeta(
            name="shunt_compensator",
            cim_role="ShuntCompensator",
            target="cim_python_sdk.model.iec61970.base.wires.shunt_compensator:ShuntCompensator",
            many=False,
            lower=1,
            upper=1,
            inverse="sv_shunt_compensator_sections",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SvShuntCompensatorSections",
        package="TC57CIM/IEC61970/Base/StateVariables",
        guid="{BC85044F-2D85-462a-AE9A-CC3E1D541D44}",
        attributes=(
            AttrMeta("sections", "sections", "float", 0, 1, "primitive"),
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
        ),
        ends=(shunt_compensator.meta,),
    )

    def __init__(
        self,
        *,
        sections: float | None = None,
        phase: SinglePhaseKind | None = None,
        shunt_compensator: ShuntCompensator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sections = sections
        self.phase = phase
        if shunt_compensator is not None:
            self.shunt_compensator = shunt_compensator
