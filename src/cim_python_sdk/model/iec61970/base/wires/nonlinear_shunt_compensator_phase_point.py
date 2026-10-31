"""CIM class NonlinearShuntCompensatorPhasePoint (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.nonlinear_shunt_compensator_phase import (
        NonlinearShuntCompensatorPhase,
    )


class NonlinearShuntCompensatorPhasePoint(CimObject):
    """A per phase non linear shunt compensator bank or section admittance value. The number of
    NonlinearShuntCompenstorPhasePoint instances associated with a
    NonlinearShuntCompensatorPhase shall be equal to ShuntCompensatorPhase.maximumSections.
    ShuntCompensator.sections shall only be set to one of the
    NonlinearShuntCompenstorPhasePoint.sectionNumber. There is no interpolation between
    NonlinearShuntCompenstorPhasePoint-s."""

    __slots__ = ("_nonlinear_shunt_compensator_phase", "b", "g", "section_number")

    b: float | None  # Susceptance
    g: float | None  # Conductance
    section_number: int | None

    nonlinear_shunt_compensator_phase: One[NonlinearShuntCompensatorPhase] = One(
        EndMeta(
            name="nonlinear_shunt_compensator_phase",
            cim_role="NonlinearShuntCompensatorPhase",
            target="cim_python_sdk.model.iec61970.base.wires.nonlinear_shunt_compensator_phase:NonlinearShuntCompensatorPhase",
            many=False,
            lower=1,
            upper=1,
            inverse="nonlinear_shunt_compensator_phase_points",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NonlinearShuntCompensatorPhasePoint",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{44BDEBB6-4580-4df6-9245-179240EB5058}",
        attributes=(
            AttrMeta("b", "b", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("g", "g", "Conductance", 0, 1, "cimdatatype"),
            AttrMeta("section_number", "sectionNumber", "int", 0, 1, "primitive"),
        ),
        ends=(nonlinear_shunt_compensator_phase.meta,),
    )

    def __init__(
        self,
        *,
        b: float | None = None,
        g: float | None = None,
        section_number: int | None = None,
        nonlinear_shunt_compensator_phase: NonlinearShuntCompensatorPhase | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b = b
        self.g = g
        self.section_number = section_number
        if nonlinear_shunt_compensator_phase is not None:
            self.nonlinear_shunt_compensator_phase = nonlinear_shunt_compensator_phase
