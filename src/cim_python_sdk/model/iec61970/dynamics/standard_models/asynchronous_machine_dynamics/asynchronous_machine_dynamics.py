"""CIM class AsynchronousMachineDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/AsynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.rotating_machine_dynamics import (
    RotatingMachineDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.asynchronous_machine import AsynchronousMachine
    from cim_python_sdk.model.iec61970.dynamics.standard_models.mechanical_load_dynamics.mechanical_load_dynamics import (
        MechanicalLoadDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
        TurbineGovernorDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_dynamics import (
        WindTurbineType1or2Dynamics,
    )


class AsynchronousMachineDynamics(RotatingMachineDynamics):
    """Asynchronous machine whose behaviour is described by reference to a standard model
    expressed in either time constant reactance form or equivalent circuit form or by
    definition of a user-defined model.

    Parameter details:

    - Asynchronous machine parameters such as Xl, Xs, etc. are actually used as inductances
    in the model, but are commonly referred to as reactances since, at nominal frequency,
    the PU values are the same. However, some references use the symbol L instead of X."""

    __slots__ = (
        "_asynchronous_machine",
        "_mechanical_load_dynamics",
        "_turbine_governor_dynamics",
        "_wind_turbine_type1or2_dynamics",
    )

    wind_turbine_type1or2_dynamics: One[WindTurbineType1or2Dynamics] = One(
        EndMeta(
            name="wind_turbine_type1or2_dynamics",
            cim_role="WindTurbineType1or2Dynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_dynamics:WindTurbineType1or2Dynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="asynchronous_machine_dynamics",
            aggregation="none",
        )
    )
    mechanical_load_dynamics: One[MechanicalLoadDynamics] = One(
        EndMeta(
            name="mechanical_load_dynamics",
            cim_role="MechanicalLoadDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.mechanical_load_dynamics.mechanical_load_dynamics:MechanicalLoadDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="asynchronous_machine_dynamics",
            aggregation="none",
        )
    )
    turbine_governor_dynamics: One[TurbineGovernorDynamics] = One(
        EndMeta(
            name="turbine_governor_dynamics",
            cim_role="TurbineGovernorDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics:TurbineGovernorDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="asynchronous_machine_dynamics",
            aggregation="none",
        )
    )
    asynchronous_machine: One[AsynchronousMachine] = One(
        EndMeta(
            name="asynchronous_machine",
            cim_role="AsynchronousMachine",
            target="cim_python_sdk.model.iec61970.base.wires.asynchronous_machine:AsynchronousMachine",
            many=False,
            lower=1,
            upper=1,
            inverse="asynchronous_machine_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AsynchronousMachineDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/AsynchronousMachineDynamics",
        guid="{3459C70D-B2B9-4da0-93C9-AEC975B7B46C}",
        ends=(
            wind_turbine_type1or2_dynamics.meta,
            mechanical_load_dynamics.meta,
            turbine_governor_dynamics.meta,
            asynchronous_machine.meta,
        ),
    )

    def __init__(
        self,
        *,
        wind_turbine_type1or2_dynamics: WindTurbineType1or2Dynamics | None = None,
        mechanical_load_dynamics: MechanicalLoadDynamics | None = None,
        turbine_governor_dynamics: TurbineGovernorDynamics | None = None,
        asynchronous_machine: AsynchronousMachine | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_turbine_type1or2_dynamics is not None:
            self.wind_turbine_type1or2_dynamics = wind_turbine_type1or2_dynamics
        if mechanical_load_dynamics is not None:
            self.mechanical_load_dynamics = mechanical_load_dynamics
        if turbine_governor_dynamics is not None:
            self.turbine_governor_dynamics = turbine_governor_dynamics
        if asynchronous_machine is not None:
            self.asynchronous_machine = asynchronous_machine
