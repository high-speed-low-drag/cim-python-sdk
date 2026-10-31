"""CIM class NonlinearShuntCompensatorPoint (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.nonlinear_shunt_compensator import (
        NonlinearShuntCompensator,
    )


class NonlinearShuntCompensatorPoint(CimObject):
    """A non linear shunt compensator bank or section admittance value. The number of
    NonlinearShuntCompenstorPoint instances associated with a NonlinearShuntCompensator
    shall be equal to ShuntCompensator.maximumSections. ShuntCompensator.sections shall only
    be set to one of the NonlinearShuntCompenstorPoint.sectionNumber. There is no
    interpolation between NonlinearShuntCompenstorPoint-s."""

    __slots__ = ("_nonlinear_shunt_compensator", "b", "b0", "g", "g0", "section_number")

    b: float | None  # Susceptance
    b0: float | None  # Susceptance
    g: float | None  # Conductance
    g0: float | None  # Conductance
    section_number: int | None

    nonlinear_shunt_compensator: One[NonlinearShuntCompensator] = One(
        EndMeta(
            name="nonlinear_shunt_compensator",
            cim_role="NonlinearShuntCompensator",
            target="cim_python_sdk.model.iec61970.base.wires.nonlinear_shunt_compensator:NonlinearShuntCompensator",
            many=False,
            lower=1,
            upper=1,
            inverse="nonlinear_shunt_compensator_points",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NonlinearShuntCompensatorPoint",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{96F8BB1B-2776-413c-A4AF-63924395C921}",
        attributes=(
            AttrMeta("b", "b", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("b0", "b0", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("g", "g", "Conductance", 0, 1, "cimdatatype"),
            AttrMeta("g0", "g0", "Conductance", 0, 1, "cimdatatype"),
            AttrMeta("section_number", "sectionNumber", "int", 0, 1, "primitive"),
        ),
        ends=(nonlinear_shunt_compensator.meta,),
    )

    def __init__(
        self,
        *,
        b: float | None = None,
        b0: float | None = None,
        g: float | None = None,
        g0: float | None = None,
        section_number: int | None = None,
        nonlinear_shunt_compensator: NonlinearShuntCompensator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b = b
        self.b0 = b0
        self.g = g
        self.g0 = g0
        self.section_number = section_number
        if nonlinear_shunt_compensator is not None:
            self.nonlinear_shunt_compensator = nonlinear_shunt_compensator
