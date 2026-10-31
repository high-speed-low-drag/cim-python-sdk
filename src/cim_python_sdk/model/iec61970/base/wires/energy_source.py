"""CIM class EnergySource (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.wires.energy_connection import EnergyConnection

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.energy_source_action import EnergySourceAction
    from cim_python_sdk.model.iec61970.base.wires.energy_scheduling_type import EnergySchedulingType
    from cim_python_sdk.model.iec61970.base.wires.energy_source_phase import EnergySourcePhase


class EnergySource(EnergyConnection):
    """A generic equivalent for an energy supplier on a transmission or distribution voltage
    level."""

    __slots__ = (
        "_energy_scheduling_type",
        "_energy_source_action",
        "_energy_source_phase",
        "active_power",
        "nominal_voltage",
        "p_max",
        "p_min",
        "r",
        "r0",
        "reactive_power",
        "rn",
        "voltage_angle",
        "voltage_magnitude",
        "x",
        "x0",
        "xn",
    )

    active_power: float | None  # ActivePower
    reactive_power: float | None  # ReactivePower
    nominal_voltage: float | None  # Voltage
    r: float | None  # Resistance
    r0: float | None  # Resistance
    rn: float | None  # Resistance
    voltage_angle: float | None  # AngleRadians
    voltage_magnitude: float | None  # Voltage
    x: float | None  # Reactance
    x0: float | None  # Reactance
    xn: float | None  # Reactance
    p_min: float | None  # ActivePower
    p_max: float | None  # ActivePower

    energy_source_action: One[EnergySourceAction] = One(
        EndMeta(
            name="energy_source_action",
            cim_role="EnergySourceAction",
            target="cim_python_sdk.model.iec61968.operations.energy_source_action:EnergySourceAction",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_source",
            aggregation="none",
        )
    )
    energy_source_phase: Many[EnergySourcePhase] = Many(
        EndMeta(
            name="energy_source_phase",
            cim_role="EnergySourcePhase",
            target="cim_python_sdk.model.iec61970.base.wires.energy_source_phase:EnergySourcePhase",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_source",
            aggregation="none",
        )
    )
    energy_scheduling_type: One[EnergySchedulingType] = One(
        EndMeta(
            name="energy_scheduling_type",
            cim_role="EnergySchedulingType",
            target="cim_python_sdk.model.iec61970.base.wires.energy_scheduling_type:EnergySchedulingType",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_source",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergySource",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{7174F78A-A2B7-457a-8EBC-4E9CBA6DA738}",
        attributes=(
            AttrMeta("active_power", "activePower", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("reactive_power", "reactivePower", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("nominal_voltage", "nominalVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r0", "r0", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("rn", "rn", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("voltage_angle", "voltageAngle", "AngleRadians", 0, 1, "cimdatatype"),
            AttrMeta("voltage_magnitude", "voltageMagnitude", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("x", "x", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x0", "x0", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("xn", "xn", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("p_min", "pMin", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("p_max", "pMax", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            energy_source_action.meta,
            energy_source_phase.meta,
            energy_scheduling_type.meta,
        ),
    )

    def __init__(
        self,
        *,
        active_power: float | None = None,
        reactive_power: float | None = None,
        nominal_voltage: float | None = None,
        r: float | None = None,
        r0: float | None = None,
        rn: float | None = None,
        voltage_angle: float | None = None,
        voltage_magnitude: float | None = None,
        x: float | None = None,
        x0: float | None = None,
        xn: float | None = None,
        p_min: float | None = None,
        p_max: float | None = None,
        energy_source_action: EnergySourceAction | None = None,
        energy_source_phase: Iterable[EnergySourcePhase] | None = None,
        energy_scheduling_type: EnergySchedulingType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.active_power = active_power
        self.reactive_power = reactive_power
        self.nominal_voltage = nominal_voltage
        self.r = r
        self.r0 = r0
        self.rn = rn
        self.voltage_angle = voltage_angle
        self.voltage_magnitude = voltage_magnitude
        self.x = x
        self.x0 = x0
        self.xn = xn
        self.p_min = p_min
        self.p_max = p_max
        if energy_source_action is not None:
            self.energy_source_action = energy_source_action
        if energy_source_phase is not None:
            EnergySource.energy_source_phase.extend(self, energy_source_phase)
        if energy_scheduling_type is not None:
            self.energy_scheduling_type = energy_scheduling_type

    def add_energy_source_phase(self, energy_source_phase: EnergySourcePhase) -> Self:
        return EnergySource.energy_source_phase.add(self, energy_source_phase)

    def remove_energy_source_phase(self, energy_source_phase: EnergySourcePhase) -> Self:
        return EnergySource.energy_source_phase.remove(self, energy_source_phase)

    def clear_energy_source_phase(self) -> Self:
        return EnergySource.energy_source_phase.clear(self)

    def num_energy_source_phase(self) -> int:
        return EnergySource.energy_source_phase.count(self)

    def get_energy_source_phase_by_mrid(self, mrid: str) -> EnergySourcePhase | None:
        return EnergySource.energy_source_phase.get_by_mrid(self, mrid)
