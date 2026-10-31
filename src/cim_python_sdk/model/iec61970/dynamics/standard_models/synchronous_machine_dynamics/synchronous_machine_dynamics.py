"""CIM class SynchronousMachineDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.rotating_machine_dynamics import (
    RotatingMachineDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.synchronous_machine import SynchronousMachine
    from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
        ExcitationSystemDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.mechanical_load_dynamics.mechanical_load_dynamics import (
        MechanicalLoadDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.cross_compound_turbine_governor_dynamics import (
        CrossCompoundTurbineGovernorDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
        TurbineGovernorDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.gen_i_compensation_for_gen_j import (
        GenICompensationForGenJ,
    )


class SynchronousMachineDynamics(RotatingMachineDynamics):
    """Synchronous machine whose behaviour is described by reference to a standard model
    expressed in one of the following forms:

    - simplified (or classical), where a group of generators or motors is not modelled in
    detail;

    - detailed, in equivalent circuit form;

    - detailed, in time constant reactance form; or

    - by definition of a user-defined model.

    It is a common practice to represent small generators by a negative load rather than by
    a dynamic generator model when performing dynamics simulations. In this case, a
    SynchronousMachine in the static model is not represented by anything in the dynamics
    model, instead it is treated as an ordinary load.

    Parameter details:

    - Synchronous machine parameters such as Xl, Xd, Xp etc. are actually used as
    inductances in the models, but are commonly referred to as reactances since, at nominal
    frequency, the PU values are the same. However, some references use the symbol L instead
    of X."""

    __slots__ = (
        "_cross_compound_turbine_governor_dyanmics",
        "_cross_compound_turbine_governor_dynamics",
        "_excitation_system_dynamics",
        "_gen_i_compensation_for_gen_j",
        "_mechanical_load_dynamics",
        "_synchronous_machine",
        "_turbine_governor_dynamics",
    )

    mechanical_load_dynamics: One[MechanicalLoadDynamics] = One(
        EndMeta(
            name="mechanical_load_dynamics",
            cim_role="MechanicalLoadDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.mechanical_load_dynamics.mechanical_load_dynamics:MechanicalLoadDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="synchronous_machine_dynamics",
            aggregation="none",
        )
    )
    cross_compound_turbine_governor_dyanmics: One[CrossCompoundTurbineGovernorDynamics] = One(
        EndMeta(
            name="cross_compound_turbine_governor_dyanmics",
            cim_role="CrossCompoundTurbineGovernorDyanmics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.cross_compound_turbine_governor_dynamics:CrossCompoundTurbineGovernorDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="high_pressure_synchronous_machine_dynamics",
            aggregation="none",
        )
    )
    turbine_governor_dynamics: Many[TurbineGovernorDynamics] = Many(
        EndMeta(
            name="turbine_governor_dynamics",
            cim_role="TurbineGovernorDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics:TurbineGovernorDynamics",
            many=True,
            lower=0,
            upper=None,
            inverse="synchronous_machine_dynamics",
            aggregation="none",
        )
    )
    cross_compound_turbine_governor_dynamics: One[CrossCompoundTurbineGovernorDynamics] = One(
        EndMeta(
            name="cross_compound_turbine_governor_dynamics",
            cim_role="CrossCompoundTurbineGovernorDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.cross_compound_turbine_governor_dynamics:CrossCompoundTurbineGovernorDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="low_pressure_synchronous_machine_dynamics",
            aggregation="none",
        )
    )
    excitation_system_dynamics: One[ExcitationSystemDynamics] = One(
        EndMeta(
            name="excitation_system_dynamics",
            cim_role="ExcitationSystemDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics:ExcitationSystemDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="synchronous_machine_dynamics",
            aggregation="none",
        )
    )
    gen_i_compensation_for_gen_j: Many[GenICompensationForGenJ] = Many(
        EndMeta(
            name="gen_i_compensation_for_gen_j",
            cim_role="GenICompensationForGenJ",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.gen_i_compensation_for_gen_j:GenICompensationForGenJ",
            many=True,
            lower=0,
            upper=None,
            inverse="synchronous_machine_dynamics",
            aggregation="none",
        )
    )
    synchronous_machine: One[SynchronousMachine] = One(
        EndMeta(
            name="synchronous_machine",
            cim_role="SynchronousMachine",
            target="cim_python_sdk.model.iec61970.base.wires.synchronous_machine:SynchronousMachine",
            many=False,
            lower=1,
            upper=1,
            inverse="synchronous_machine_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SynchronousMachineDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics",
        guid="{575BECE2-4C08-40c3-9B81-1C8E6F4FCF8C}",
        ends=(
            mechanical_load_dynamics.meta,
            cross_compound_turbine_governor_dyanmics.meta,
            turbine_governor_dynamics.meta,
            cross_compound_turbine_governor_dynamics.meta,
            excitation_system_dynamics.meta,
            gen_i_compensation_for_gen_j.meta,
            synchronous_machine.meta,
        ),
    )

    def __init__(
        self,
        *,
        mechanical_load_dynamics: MechanicalLoadDynamics | None = None,
        cross_compound_turbine_governor_dyanmics: CrossCompoundTurbineGovernorDynamics
        | None = None,
        turbine_governor_dynamics: Iterable[TurbineGovernorDynamics] | None = None,
        cross_compound_turbine_governor_dynamics: CrossCompoundTurbineGovernorDynamics
        | None = None,
        excitation_system_dynamics: ExcitationSystemDynamics | None = None,
        gen_i_compensation_for_gen_j: Iterable[GenICompensationForGenJ] | None = None,
        synchronous_machine: SynchronousMachine | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if mechanical_load_dynamics is not None:
            self.mechanical_load_dynamics = mechanical_load_dynamics
        if cross_compound_turbine_governor_dyanmics is not None:
            self.cross_compound_turbine_governor_dyanmics = cross_compound_turbine_governor_dyanmics
        if turbine_governor_dynamics is not None:
            SynchronousMachineDynamics.turbine_governor_dynamics.extend(
                self, turbine_governor_dynamics
            )
        if cross_compound_turbine_governor_dynamics is not None:
            self.cross_compound_turbine_governor_dynamics = cross_compound_turbine_governor_dynamics
        if excitation_system_dynamics is not None:
            self.excitation_system_dynamics = excitation_system_dynamics
        if gen_i_compensation_for_gen_j is not None:
            SynchronousMachineDynamics.gen_i_compensation_for_gen_j.extend(
                self, gen_i_compensation_for_gen_j
            )
        if synchronous_machine is not None:
            self.synchronous_machine = synchronous_machine

    def add_turbine_governor_dynamics(
        self, turbine_governor_dynamics: TurbineGovernorDynamics
    ) -> Self:
        return SynchronousMachineDynamics.turbine_governor_dynamics.add(
            self, turbine_governor_dynamics
        )

    def remove_turbine_governor_dynamics(
        self, turbine_governor_dynamics: TurbineGovernorDynamics
    ) -> Self:
        return SynchronousMachineDynamics.turbine_governor_dynamics.remove(
            self, turbine_governor_dynamics
        )

    def clear_turbine_governor_dynamics(self) -> Self:
        return SynchronousMachineDynamics.turbine_governor_dynamics.clear(self)

    def num_turbine_governor_dynamics(self) -> int:
        return SynchronousMachineDynamics.turbine_governor_dynamics.count(self)

    def get_turbine_governor_dynamics_by_mrid(self, mrid: str) -> TurbineGovernorDynamics | None:
        return SynchronousMachineDynamics.turbine_governor_dynamics.get_by_mrid(self, mrid)

    def add_gen_i_compensation_for_gen_j(
        self, gen_i_compensation_for_gen_j: GenICompensationForGenJ
    ) -> Self:
        return SynchronousMachineDynamics.gen_i_compensation_for_gen_j.add(
            self, gen_i_compensation_for_gen_j
        )

    def remove_gen_i_compensation_for_gen_j(
        self, gen_i_compensation_for_gen_j: GenICompensationForGenJ
    ) -> Self:
        return SynchronousMachineDynamics.gen_i_compensation_for_gen_j.remove(
            self, gen_i_compensation_for_gen_j
        )

    def clear_gen_i_compensation_for_gen_j(self) -> Self:
        return SynchronousMachineDynamics.gen_i_compensation_for_gen_j.clear(self)

    def num_gen_i_compensation_for_gen_j(self) -> int:
        return SynchronousMachineDynamics.gen_i_compensation_for_gen_j.count(self)

    def get_gen_i_compensation_for_gen_j_by_mrid(self, mrid: str) -> GenICompensationForGenJ | None:
        return SynchronousMachineDynamics.gen_i_compensation_for_gen_j.get_by_mrid(self, mrid)
