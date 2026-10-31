"""CIM class ShuntCompensator (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.wires.regulating_cond_eq import RegulatingCondEq

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.shunt_compensator_action import (
        ShuntCompensatorAction,
    )
    from cim_python_sdk.model.iec61970.base.state_variables.sv_shunt_compensator_sections import (
        SvShuntCompensatorSections,
    )
    from cim_python_sdk.model.iec61970.base.wires.phase_shunt_connection_kind import (
        PhaseShuntConnectionKind,
    )
    from cim_python_sdk.model.iec61970.base.wires.shunt_compensator_phase import (
        ShuntCompensatorPhase,
    )


class ShuntCompensator(RegulatingCondEq):
    """A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A
    section of a shunt compensator is an individual capacitor or reactor. A negative value
    for bPerSection indicates that the compensator is a reactor. ShuntCompensator is a
    single terminal device. Ground is implied."""

    __slots__ = (
        "_shunt_compensator_action",
        "_shunt_compensator_phase",
        "_sv_shunt_compensator_sections",
        "a_vr_delay",
        "grounded",
        "maximum_sections",
        "nom_u",
        "normal_sections",
        "phase_connection",
        "sections",
        "switch_on_count",
        "switch_on_date",
        "voltage_sensitivity",
    )

    a_vr_delay: float | None  # Seconds
    grounded: bool | None
    maximum_sections: int | None
    nom_u: float | None  # Voltage
    normal_sections: int | None
    phase_connection: PhaseShuntConnectionKind | None
    switch_on_count: int | None
    switch_on_date: _dt.datetime | None
    voltage_sensitivity: float | None  # VoltagePerReactivePower
    sections: float | None

    shunt_compensator_action: One[ShuntCompensatorAction] = One(
        EndMeta(
            name="shunt_compensator_action",
            cim_role="ShuntCompensatorAction",
            target="cim_python_sdk.model.iec61968.operations.shunt_compensator_action:ShuntCompensatorAction",
            many=False,
            lower=0,
            upper=1,
            inverse="shunt_compensator",
            aggregation="none",
        )
    )
    shunt_compensator_phase: Many[ShuntCompensatorPhase] = Many(
        EndMeta(
            name="shunt_compensator_phase",
            cim_role="ShuntCompensatorPhase",
            target="cim_python_sdk.model.iec61970.base.wires.shunt_compensator_phase:ShuntCompensatorPhase",
            many=True,
            lower=0,
            upper=None,
            inverse="shunt_compensator",
            aggregation="none",
        )
    )
    sv_shunt_compensator_sections: Many[SvShuntCompensatorSections] = Many(
        EndMeta(
            name="sv_shunt_compensator_sections",
            cim_role="SvShuntCompensatorSections",
            target="cim_python_sdk.model.iec61970.base.state_variables.sv_shunt_compensator_sections:SvShuntCompensatorSections",
            many=True,
            lower=0,
            upper=None,
            inverse="shunt_compensator",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ShuntCompensator",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{92B30569-5ED0-4fc0-B796-984D9BF75453}",
        attributes=(
            AttrMeta("a_vr_delay", "aVRDelay", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("grounded", "grounded", "bool", 0, 1, "primitive"),
            AttrMeta("maximum_sections", "maximumSections", "int", 0, 1, "primitive"),
            AttrMeta("nom_u", "nomU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("normal_sections", "normalSections", "int", 0, 1, "primitive"),
            AttrMeta(
                "phase_connection",
                "phaseConnection",
                "PhaseShuntConnectionKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("switch_on_count", "switchOnCount", "int", 0, 1, "primitive", deprecated=True),
            AttrMeta(
                "switch_on_date", "switchOnDate", "datetime", 0, 1, "primitive", deprecated=True
            ),
            AttrMeta(
                "voltage_sensitivity",
                "voltageSensitivity",
                "VoltagePerReactivePower",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("sections", "sections", "float", 0, 1, "primitive"),
        ),
        ends=(
            shunt_compensator_action.meta,
            shunt_compensator_phase.meta,
            sv_shunt_compensator_sections.meta,
        ),
    )

    def __init__(
        self,
        *,
        a_vr_delay: float | None = None,
        grounded: bool | None = None,
        maximum_sections: int | None = None,
        nom_u: float | None = None,
        normal_sections: int | None = None,
        phase_connection: PhaseShuntConnectionKind | None = None,
        switch_on_count: int | None = None,
        switch_on_date: _dt.datetime | None = None,
        voltage_sensitivity: float | None = None,
        sections: float | None = None,
        shunt_compensator_action: ShuntCompensatorAction | None = None,
        shunt_compensator_phase: Iterable[ShuntCompensatorPhase] | None = None,
        sv_shunt_compensator_sections: Iterable[SvShuntCompensatorSections] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.a_vr_delay = a_vr_delay
        self.grounded = grounded
        self.maximum_sections = maximum_sections
        self.nom_u = nom_u
        self.normal_sections = normal_sections
        self.phase_connection = phase_connection
        self.switch_on_count = switch_on_count
        self.switch_on_date = switch_on_date
        self.voltage_sensitivity = voltage_sensitivity
        self.sections = sections
        if shunt_compensator_action is not None:
            self.shunt_compensator_action = shunt_compensator_action
        if shunt_compensator_phase is not None:
            ShuntCompensator.shunt_compensator_phase.extend(self, shunt_compensator_phase)
        if sv_shunt_compensator_sections is not None:
            ShuntCompensator.sv_shunt_compensator_sections.extend(
                self, sv_shunt_compensator_sections
            )

    def add_shunt_compensator_phase(self, shunt_compensator_phase: ShuntCompensatorPhase) -> Self:
        return ShuntCompensator.shunt_compensator_phase.add(self, shunt_compensator_phase)

    def remove_shunt_compensator_phase(
        self, shunt_compensator_phase: ShuntCompensatorPhase
    ) -> Self:
        return ShuntCompensator.shunt_compensator_phase.remove(self, shunt_compensator_phase)

    def clear_shunt_compensator_phase(self) -> Self:
        return ShuntCompensator.shunt_compensator_phase.clear(self)

    def num_shunt_compensator_phase(self) -> int:
        return ShuntCompensator.shunt_compensator_phase.count(self)

    def get_shunt_compensator_phase_by_mrid(self, mrid: str) -> ShuntCompensatorPhase | None:
        return ShuntCompensator.shunt_compensator_phase.get_by_mrid(self, mrid)

    def add_sv_shunt_compensator_section(
        self, sv_shunt_compensator_section: SvShuntCompensatorSections
    ) -> Self:
        return ShuntCompensator.sv_shunt_compensator_sections.add(
            self, sv_shunt_compensator_section
        )

    def remove_sv_shunt_compensator_section(
        self, sv_shunt_compensator_section: SvShuntCompensatorSections
    ) -> Self:
        return ShuntCompensator.sv_shunt_compensator_sections.remove(
            self, sv_shunt_compensator_section
        )

    def clear_sv_shunt_compensator_sections(self) -> Self:
        return ShuntCompensator.sv_shunt_compensator_sections.clear(self)

    def num_sv_shunt_compensator_section(self) -> int:
        return ShuntCompensator.sv_shunt_compensator_sections.count(self)
