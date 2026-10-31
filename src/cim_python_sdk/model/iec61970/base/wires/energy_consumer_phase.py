"""CIM class EnergyConsumerPhase (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.energy_consumer import EnergyConsumer
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class EnergyConsumerPhase(PowerSystemResource):
    """A single phase of an energy consumer."""

    __slots__ = (
        "_energy_consumer",
        "p",
        "pfixed",
        "pfixed_pct",
        "phase",
        "q",
        "qfixed",
        "qfixed_pct",
    )

    pfixed: float | None  # ActivePower
    pfixed_pct: float | None  # PerCent
    phase: SinglePhaseKind | None
    qfixed: float | None  # ReactivePower
    qfixed_pct: float | None  # PerCent
    p: float | None  # ActivePower
    q: float | None  # ReactivePower

    energy_consumer: One[EnergyConsumer] = One(
        EndMeta(
            name="energy_consumer",
            cim_role="EnergyConsumer",
            target="cim_python_sdk.model.iec61970.base.wires.energy_consumer:EnergyConsumer",
            many=False,
            lower=1,
            upper=1,
            inverse="energy_consumer_phase",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyConsumerPhase",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{2933FF4A-CF68-4099-B3FE-DBE8919C85AE}",
        attributes=(
            AttrMeta("pfixed", "pfixed", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("pfixed_pct", "pfixedPct", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("qfixed", "qfixed", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("qfixed_pct", "qfixedPct", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("q", "q", "ReactivePower", 0, 1, "cimdatatype"),
        ),
        ends=(energy_consumer.meta,),
    )

    def __init__(
        self,
        *,
        pfixed: float | None = None,
        pfixed_pct: float | None = None,
        phase: SinglePhaseKind | None = None,
        qfixed: float | None = None,
        qfixed_pct: float | None = None,
        p: float | None = None,
        q: float | None = None,
        energy_consumer: EnergyConsumer | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.pfixed = pfixed
        self.pfixed_pct = pfixed_pct
        self.phase = phase
        self.qfixed = qfixed
        self.qfixed_pct = qfixed_pct
        self.p = p
        self.q = q
        if energy_consumer is not None:
            self.energy_consumer = energy_consumer
