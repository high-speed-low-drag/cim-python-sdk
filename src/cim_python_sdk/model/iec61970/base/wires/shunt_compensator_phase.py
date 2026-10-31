"""CIM class ShuntCompensatorPhase (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.shunt_compensator import ShuntCompensator
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class ShuntCompensatorPhase(PowerSystemResource):
    """Single phase of a multi-phase shunt compensator when its attributes might be different
    per phase."""

    __slots__ = ("_shunt_compensator", "maximum_sections", "normal_sections", "phase", "sections")

    maximum_sections: int | None
    normal_sections: int | None
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
            inverse="shunt_compensator_phase",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ShuntCompensatorPhase",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{081B186A-D45B-44d1-81DF-94EE3918A4D5}",
        attributes=(
            AttrMeta("maximum_sections", "maximumSections", "int", 0, 1, "primitive"),
            AttrMeta("normal_sections", "normalSections", "int", 0, 1, "primitive"),
            AttrMeta("sections", "sections", "float", 0, 1, "primitive"),
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
        ),
        ends=(shunt_compensator.meta,),
    )

    def __init__(
        self,
        *,
        maximum_sections: int | None = None,
        normal_sections: int | None = None,
        sections: float | None = None,
        phase: SinglePhaseKind | None = None,
        shunt_compensator: ShuntCompensator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.maximum_sections = maximum_sections
        self.normal_sections = normal_sections
        self.sections = sections
        self.phase = phase
        if shunt_compensator is not None:
            self.shunt_compensator = shunt_compensator
