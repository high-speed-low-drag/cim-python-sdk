"""CIM class SynchronousMachine (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.wires.rotating_machine import RotatingMachine

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.prime_mover import (
        PrimeMover,
    )
    from cim_python_sdk.model.iec61970.base.wires.coolant_type import CoolantType
    from cim_python_sdk.model.iec61970.base.wires.reactive_capability_curve import (
        ReactiveCapabilityCurve,
    )
    from cim_python_sdk.model.iec61970.base.wires.short_circuit_rotor_kind import (
        ShortCircuitRotorKind,
    )
    from cim_python_sdk.model.iec61970.base.wires.synchronous_machine_kind import (
        SynchronousMachineKind,
    )
    from cim_python_sdk.model.iec61970.base.wires.synchronous_machine_operating_mode import (
        SynchronousMachineOperatingMode,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics import (
        SynchronousMachineDynamics,
    )


class SynchronousMachine(RotatingMachine):
    """An electromechanical device that operates with shaft rotating synchronously with the
    network. It is a single machine operating either as a generator or synchronous condenser
    or pump."""

    __slots__ = (
        "_initial_reactive_capability_curve",
        "_prime_movers",
        "_reactive_capability_curves",
        "_synchronous_machine_dynamics",
        "a_vr_to_manual_lag",
        "a_vr_to_manual_lead",
        "base_q",
        "condenser_p",
        "coolant_condition",
        "coolant_type",
        "earthing",
        "earthing_star_point_r",
        "earthing_star_point_x",
        "ikk",
        "manual_to_avr",
        "max_q",
        "max_u",
        "min_q",
        "min_u",
        "mu",
        "operating_mode",
        "q_percent",
        "r",
        "r0",
        "r2",
        "reference_priority",
        "sat_direct_subtrans_x",
        "sat_direct_sync_x",
        "sat_direct_trans_x",
        "short_circuit_rotor_type",
        "type",
        "voltage_regulation_range",
        "x0",
        "x2",
    )

    a_vr_to_manual_lag: float | None  # Seconds
    a_vr_to_manual_lead: float | None  # Seconds
    base_q: float | None  # ReactivePower
    condenser_p: float | None  # ActivePower
    coolant_condition: float | None
    coolant_type: CoolantType | None
    earthing: bool | None
    earthing_star_point_r: float | None  # Resistance
    earthing_star_point_x: float | None  # Reactance
    ikk: float | None  # CurrentFlow
    manual_to_avr: float | None  # Seconds
    max_q: float | None  # ReactivePower
    max_u: float | None  # Voltage
    min_q: float | None  # ReactivePower
    min_u: float | None  # Voltage
    mu: float | None
    operating_mode: SynchronousMachineOperatingMode | None
    q_percent: float | None  # PerCent
    r: float | None  # Resistance
    r0: float | None  # Resistance
    r2: float | None  # Resistance
    reference_priority: int | None
    sat_direct_subtrans_x: float | None  # PU
    sat_direct_sync_x: float | None  # PU
    sat_direct_trans_x: float | None  # PU
    short_circuit_rotor_type: ShortCircuitRotorKind | None
    type: SynchronousMachineKind | None
    voltage_regulation_range: float | None  # PerCent
    x0: float | None  # Reactance
    x2: float | None  # Reactance

    reactive_capability_curves: Many[ReactiveCapabilityCurve] = Many(
        EndMeta(
            name="reactive_capability_curves",
            cim_role="ReactiveCapabilityCurves",
            target="cim_python_sdk.model.iec61970.base.wires.reactive_capability_curve:ReactiveCapabilityCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="synchronous_machines",
            aggregation="none",
        )
    )
    initial_reactive_capability_curve: One[ReactiveCapabilityCurve] = One(
        EndMeta(
            name="initial_reactive_capability_curve",
            cim_role="InitialReactiveCapabilityCurve",
            target="cim_python_sdk.model.iec61970.base.wires.reactive_capability_curve:ReactiveCapabilityCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="initially_used_by_synchronous_machines",
            aggregation="none",
        )
    )
    prime_movers: Many[PrimeMover] = Many(
        EndMeta(
            name="prime_movers",
            cim_role="PrimeMovers",
            target="cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.prime_mover:PrimeMover",
            many=True,
            lower=0,
            upper=None,
            inverse="synchronous_machines",
            aggregation="none",
        )
    )
    synchronous_machine_dynamics: One[SynchronousMachineDynamics] = One(
        EndMeta(
            name="synchronous_machine_dynamics",
            cim_role="SynchronousMachineDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics:SynchronousMachineDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="synchronous_machine",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SynchronousMachine",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{7862E21E-F054-4a33-949F-04B8B4690D49}",
        attributes=(
            AttrMeta("a_vr_to_manual_lag", "aVRToManualLag", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("a_vr_to_manual_lead", "aVRToManualLead", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("base_q", "baseQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("condenser_p", "condenserP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("coolant_condition", "coolantCondition", "float", 0, 1, "primitive"),
            AttrMeta("coolant_type", "coolantType", "CoolantType", 0, 1, "enumeration"),
            AttrMeta("earthing", "earthing", "bool", 0, 1, "primitive"),
            AttrMeta(
                "earthing_star_point_r", "earthingStarPointR", "Resistance", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "earthing_star_point_x", "earthingStarPointX", "Reactance", 0, 1, "cimdatatype"
            ),
            AttrMeta("ikk", "ikk", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("manual_to_avr", "manualToAVR", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("max_q", "maxQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_u", "maxU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("min_q", "minQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_u", "minU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("mu", "mu", "float", 0, 1, "primitive"),
            AttrMeta(
                "operating_mode",
                "operatingMode",
                "SynchronousMachineOperatingMode",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("q_percent", "qPercent", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r0", "r0", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r2", "r2", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("reference_priority", "referencePriority", "int", 0, 1, "primitive"),
            AttrMeta("sat_direct_subtrans_x", "satDirectSubtransX", "PU", 0, 1, "cimdatatype"),
            AttrMeta("sat_direct_sync_x", "satDirectSyncX", "PU", 0, 1, "cimdatatype"),
            AttrMeta("sat_direct_trans_x", "satDirectTransX", "PU", 0, 1, "cimdatatype"),
            AttrMeta(
                "short_circuit_rotor_type",
                "shortCircuitRotorType",
                "ShortCircuitRotorKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("type", "type", "SynchronousMachineKind", 0, 1, "enumeration"),
            AttrMeta(
                "voltage_regulation_range", "voltageRegulationRange", "PerCent", 0, 1, "cimdatatype"
            ),
            AttrMeta("x0", "x0", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x2", "x2", "Reactance", 0, 1, "cimdatatype"),
        ),
        ends=(
            reactive_capability_curves.meta,
            initial_reactive_capability_curve.meta,
            prime_movers.meta,
            synchronous_machine_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        a_vr_to_manual_lag: float | None = None,
        a_vr_to_manual_lead: float | None = None,
        base_q: float | None = None,
        condenser_p: float | None = None,
        coolant_condition: float | None = None,
        coolant_type: CoolantType | None = None,
        earthing: bool | None = None,
        earthing_star_point_r: float | None = None,
        earthing_star_point_x: float | None = None,
        ikk: float | None = None,
        manual_to_avr: float | None = None,
        max_q: float | None = None,
        max_u: float | None = None,
        min_q: float | None = None,
        min_u: float | None = None,
        mu: float | None = None,
        operating_mode: SynchronousMachineOperatingMode | None = None,
        q_percent: float | None = None,
        r: float | None = None,
        r0: float | None = None,
        r2: float | None = None,
        reference_priority: int | None = None,
        sat_direct_subtrans_x: float | None = None,
        sat_direct_sync_x: float | None = None,
        sat_direct_trans_x: float | None = None,
        short_circuit_rotor_type: ShortCircuitRotorKind | None = None,
        type: SynchronousMachineKind | None = None,
        voltage_regulation_range: float | None = None,
        x0: float | None = None,
        x2: float | None = None,
        reactive_capability_curves: Iterable[ReactiveCapabilityCurve] | None = None,
        initial_reactive_capability_curve: ReactiveCapabilityCurve | None = None,
        prime_movers: Iterable[PrimeMover] | None = None,
        synchronous_machine_dynamics: SynchronousMachineDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.a_vr_to_manual_lag = a_vr_to_manual_lag
        self.a_vr_to_manual_lead = a_vr_to_manual_lead
        self.base_q = base_q
        self.condenser_p = condenser_p
        self.coolant_condition = coolant_condition
        self.coolant_type = coolant_type
        self.earthing = earthing
        self.earthing_star_point_r = earthing_star_point_r
        self.earthing_star_point_x = earthing_star_point_x
        self.ikk = ikk
        self.manual_to_avr = manual_to_avr
        self.max_q = max_q
        self.max_u = max_u
        self.min_q = min_q
        self.min_u = min_u
        self.mu = mu
        self.operating_mode = operating_mode
        self.q_percent = q_percent
        self.r = r
        self.r0 = r0
        self.r2 = r2
        self.reference_priority = reference_priority
        self.sat_direct_subtrans_x = sat_direct_subtrans_x
        self.sat_direct_sync_x = sat_direct_sync_x
        self.sat_direct_trans_x = sat_direct_trans_x
        self.short_circuit_rotor_type = short_circuit_rotor_type
        self.type = type
        self.voltage_regulation_range = voltage_regulation_range
        self.x0 = x0
        self.x2 = x2
        if reactive_capability_curves is not None:
            SynchronousMachine.reactive_capability_curves.extend(self, reactive_capability_curves)
        if initial_reactive_capability_curve is not None:
            self.initial_reactive_capability_curve = initial_reactive_capability_curve
        if prime_movers is not None:
            SynchronousMachine.prime_movers.extend(self, prime_movers)
        if synchronous_machine_dynamics is not None:
            self.synchronous_machine_dynamics = synchronous_machine_dynamics

    def add_reactive_capability_curve(
        self, reactive_capability_curve: ReactiveCapabilityCurve
    ) -> Self:
        return SynchronousMachine.reactive_capability_curves.add(self, reactive_capability_curve)

    def remove_reactive_capability_curve(
        self, reactive_capability_curve: ReactiveCapabilityCurve
    ) -> Self:
        return SynchronousMachine.reactive_capability_curves.remove(self, reactive_capability_curve)

    def clear_reactive_capability_curves(self) -> Self:
        return SynchronousMachine.reactive_capability_curves.clear(self)

    def num_reactive_capability_curve(self) -> int:
        return SynchronousMachine.reactive_capability_curves.count(self)

    def get_reactive_capability_curve_by_mrid(self, mrid: str) -> ReactiveCapabilityCurve | None:
        return SynchronousMachine.reactive_capability_curves.get_by_mrid(self, mrid)

    def add_prime_mover(self, prime_mover: PrimeMover) -> Self:
        return SynchronousMachine.prime_movers.add(self, prime_mover)

    def remove_prime_mover(self, prime_mover: PrimeMover) -> Self:
        return SynchronousMachine.prime_movers.remove(self, prime_mover)

    def clear_prime_movers(self) -> Self:
        return SynchronousMachine.prime_movers.clear(self)

    def num_prime_mover(self) -> int:
        return SynchronousMachine.prime_movers.count(self)

    def get_prime_mover_by_mrid(self, mrid: str) -> PrimeMover | None:
        return SynchronousMachine.prime_movers.get_by_mrid(self, mrid)
