"""CIM class EnergyConsumer (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.wires.energy_connection import EnergyConnection

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.energy_consumer_action import EnergyConsumerAction
    from cim_python_sdk.model.iec61970.base.load_model.load_response_characteristic import (
        LoadResponseCharacteristic,
    )
    from cim_python_sdk.model.iec61970.base.load_model.power_cut_zone import PowerCutZone
    from cim_python_sdk.model.iec61970.base.wires.energy_consumer_phase import EnergyConsumerPhase
    from cim_python_sdk.model.iec61970.base.wires.phase_shunt_connection_kind import (
        PhaseShuntConnectionKind,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_dynamics import (
        LoadDynamics,
    )


class EnergyConsumer(EnergyConnection):
    """Generic user of energy - a point of consumption on the power system model.

    EnergyConsumer.pfixed, .qfixed, .pfixedPct and .qfixedPct have meaning only if there is
    no LoadResponseCharacteristic associated with EnergyConsumer or if
    LoadResponseCharacteristic.exponentModel is set to False."""

    __slots__ = (
        "_energy_consumer_action",
        "_energy_consumer_phase",
        "_load_dynamics",
        "_load_response",
        "_power_cut_zone",
        "customer_count",
        "grounded",
        "p",
        "pfixed",
        "pfixed_pct",
        "phase_connection",
        "q",
        "qfixed",
        "qfixed_pct",
    )

    customer_count: int | None
    grounded: bool | None
    pfixed: float | None  # ActivePower
    pfixed_pct: float | None  # PerCent
    phase_connection: PhaseShuntConnectionKind | None
    qfixed: float | None  # ReactivePower
    qfixed_pct: float | None  # PerCent
    p: float | None  # ActivePower
    q: float | None  # ReactivePower

    power_cut_zone: One[PowerCutZone] = One(
        EndMeta(
            name="power_cut_zone",
            cim_role="PowerCutZone",
            target="cim_python_sdk.model.iec61970.base.load_model.power_cut_zone:PowerCutZone",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_consumers",
            aggregation="none",
        )
    )
    load_dynamics: One[LoadDynamics] = One(
        EndMeta(
            name="load_dynamics",
            cim_role="LoadDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_dynamics:LoadDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_consumer",
            aggregation="none",
        )
    )
    load_response: One[LoadResponseCharacteristic] = One(
        EndMeta(
            name="load_response",
            cim_role="LoadResponse",
            target="cim_python_sdk.model.iec61970.base.load_model.load_response_characteristic:LoadResponseCharacteristic",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_consumer",
            aggregation="none",
        )
    )
    energy_consumer_phase: Many[EnergyConsumerPhase] = Many(
        EndMeta(
            name="energy_consumer_phase",
            cim_role="EnergyConsumerPhase",
            target="cim_python_sdk.model.iec61970.base.wires.energy_consumer_phase:EnergyConsumerPhase",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_consumer",
            aggregation="none",
        )
    )
    energy_consumer_action: One[EnergyConsumerAction] = One(
        EndMeta(
            name="energy_consumer_action",
            cim_role="EnergyConsumerAction",
            target="cim_python_sdk.model.iec61968.operations.energy_consumer_action:EnergyConsumerAction",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_consumer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyConsumer",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{BCEC7EE8-7294-4b50-8216-0286C31A035C}",
        attributes=(
            AttrMeta("customer_count", "customerCount", "int", 0, 1, "primitive"),
            AttrMeta("grounded", "grounded", "bool", 0, 1, "primitive"),
            AttrMeta("pfixed", "pfixed", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("pfixed_pct", "pfixedPct", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta(
                "phase_connection",
                "phaseConnection",
                "PhaseShuntConnectionKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("qfixed", "qfixed", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("qfixed_pct", "qfixedPct", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("q", "q", "ReactivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            power_cut_zone.meta,
            load_dynamics.meta,
            load_response.meta,
            energy_consumer_phase.meta,
            energy_consumer_action.meta,
        ),
    )

    def __init__(
        self,
        *,
        customer_count: int | None = None,
        grounded: bool | None = None,
        pfixed: float | None = None,
        pfixed_pct: float | None = None,
        phase_connection: PhaseShuntConnectionKind | None = None,
        qfixed: float | None = None,
        qfixed_pct: float | None = None,
        p: float | None = None,
        q: float | None = None,
        power_cut_zone: PowerCutZone | None = None,
        load_dynamics: LoadDynamics | None = None,
        load_response: LoadResponseCharacteristic | None = None,
        energy_consumer_phase: Iterable[EnergyConsumerPhase] | None = None,
        energy_consumer_action: EnergyConsumerAction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.customer_count = customer_count
        self.grounded = grounded
        self.pfixed = pfixed
        self.pfixed_pct = pfixed_pct
        self.phase_connection = phase_connection
        self.qfixed = qfixed
        self.qfixed_pct = qfixed_pct
        self.p = p
        self.q = q
        if power_cut_zone is not None:
            self.power_cut_zone = power_cut_zone
        if load_dynamics is not None:
            self.load_dynamics = load_dynamics
        if load_response is not None:
            self.load_response = load_response
        if energy_consumer_phase is not None:
            EnergyConsumer.energy_consumer_phase.extend(self, energy_consumer_phase)
        if energy_consumer_action is not None:
            self.energy_consumer_action = energy_consumer_action

    def add_energy_consumer_phase(self, energy_consumer_phase: EnergyConsumerPhase) -> Self:
        return EnergyConsumer.energy_consumer_phase.add(self, energy_consumer_phase)

    def remove_energy_consumer_phase(self, energy_consumer_phase: EnergyConsumerPhase) -> Self:
        return EnergyConsumer.energy_consumer_phase.remove(self, energy_consumer_phase)

    def clear_energy_consumer_phase(self) -> Self:
        return EnergyConsumer.energy_consumer_phase.clear(self)

    def num_energy_consumer_phase(self) -> int:
        return EnergyConsumer.energy_consumer_phase.count(self)

    def get_energy_consumer_phase_by_mrid(self, mrid: str) -> EnergyConsumerPhase | None:
        return EnergyConsumer.energy_consumer_phase.get_by_mrid(self, mrid)
