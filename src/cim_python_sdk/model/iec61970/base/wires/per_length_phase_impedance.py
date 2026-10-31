"""CIM class PerLengthPhaseImpedance (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.per_length_impedance import PerLengthImpedance

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.phase_impedance_data import PhaseImpedanceData


class PerLengthPhaseImpedance(PerLengthImpedance):
    """Impedance and admittance parameters per unit length for n-wire unbalanced lines, in
    matrix form."""

    __slots__ = ("_phase_impedance_data", "conductor_count")

    conductor_count: int | None

    phase_impedance_data: Many[PhaseImpedanceData] = Many(
        EndMeta(
            name="phase_impedance_data",
            cim_role="PhaseImpedanceData",
            target="cim_python_sdk.model.iec61970.base.wires.phase_impedance_data:PhaseImpedanceData",
            many=True,
            lower=1,
            upper=None,
            inverse="phase_impedance",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PerLengthPhaseImpedance",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{048ADD31-9C78-4fb8-93AD-0F89496AC846}",
        attributes=(AttrMeta("conductor_count", "conductorCount", "int", 0, 1, "primitive"),),
        ends=(phase_impedance_data.meta,),
    )

    def __init__(
        self,
        *,
        conductor_count: int | None = None,
        phase_impedance_data: Iterable[PhaseImpedanceData] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.conductor_count = conductor_count
        if phase_impedance_data is not None:
            PerLengthPhaseImpedance.phase_impedance_data.extend(self, phase_impedance_data)

    def add_phase_impedance_data(self, phase_impedance_data: PhaseImpedanceData) -> Self:
        return PerLengthPhaseImpedance.phase_impedance_data.add(self, phase_impedance_data)

    def remove_phase_impedance_data(self, phase_impedance_data: PhaseImpedanceData) -> Self:
        return PerLengthPhaseImpedance.phase_impedance_data.remove(self, phase_impedance_data)

    def clear_phase_impedance_data(self) -> Self:
        return PerLengthPhaseImpedance.phase_impedance_data.clear(self)

    def num_phase_impedance_data(self) -> int:
        return PerLengthPhaseImpedance.phase_impedance_data.count(self)
