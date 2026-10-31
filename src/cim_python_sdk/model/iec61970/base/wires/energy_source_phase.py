"""CIM class EnergySourcePhase (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.energy_source import EnergySource
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class EnergySourcePhase(PowerSystemResource):
    """Represents the single phase information of an unbalanced energy source."""

    __slots__ = ("_energy_source", "phase")

    phase: SinglePhaseKind | None

    energy_source: One[EnergySource] = One(
        EndMeta(
            name="energy_source",
            cim_role="EnergySource",
            target="cim_python_sdk.model.iec61970.base.wires.energy_source:EnergySource",
            many=False,
            lower=1,
            upper=1,
            inverse="energy_source_phase",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergySourcePhase",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{1EABE5E1-F61A-4758-ADFC-E9C816E97063}",
        attributes=(AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),),
        ends=(energy_source.meta,),
    )

    def __init__(
        self,
        *,
        phase: SinglePhaseKind | None = None,
        energy_source: EnergySource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.phase = phase
        if energy_source is not None:
            self.energy_source = energy_source
