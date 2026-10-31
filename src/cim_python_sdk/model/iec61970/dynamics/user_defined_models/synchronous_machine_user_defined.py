"""CIM class SynchronousMachineUserDefined (TC57CIM/IEC61970/Dynamics/UserDefinedModels). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics import (
    SynchronousMachineDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.proprietary_parameter_dynamics import (
        ProprietaryParameterDynamics,
    )


class SynchronousMachineUserDefined(SynchronousMachineDynamics):
    """Synchronous machine whose dynamic behaviour is described by a user-defined model."""

    __slots__ = ("_proprietary_parameter_dynamics", "proprietary")

    proprietary: bool | None

    proprietary_parameter_dynamics: Many[ProprietaryParameterDynamics] = Many(
        EndMeta(
            name="proprietary_parameter_dynamics",
            cim_role="ProprietaryParameterDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.proprietary_parameter_dynamics:ProprietaryParameterDynamics",
            many=True,
            lower=0,
            upper=None,
            inverse="synchronous_machine_user_defined",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SynchronousMachineUserDefined",
        package="TC57CIM/IEC61970/Dynamics/UserDefinedModels",
        guid="{37B233FC-B7CB-49cd-8AB3-4618A5FA3250}",
        attributes=(AttrMeta("proprietary", "proprietary", "bool", 0, 1, "primitive"),),
        ends=(proprietary_parameter_dynamics.meta,),
    )

    def __init__(
        self,
        *,
        proprietary: bool | None = None,
        proprietary_parameter_dynamics: Iterable[ProprietaryParameterDynamics] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.proprietary = proprietary
        if proprietary_parameter_dynamics is not None:
            SynchronousMachineUserDefined.proprietary_parameter_dynamics.extend(
                self, proprietary_parameter_dynamics
            )

    def add_proprietary_parameter_dynamics(
        self, proprietary_parameter_dynamics: ProprietaryParameterDynamics
    ) -> Self:
        return SynchronousMachineUserDefined.proprietary_parameter_dynamics.add(
            self, proprietary_parameter_dynamics
        )

    def remove_proprietary_parameter_dynamics(
        self, proprietary_parameter_dynamics: ProprietaryParameterDynamics
    ) -> Self:
        return SynchronousMachineUserDefined.proprietary_parameter_dynamics.remove(
            self, proprietary_parameter_dynamics
        )

    def clear_proprietary_parameter_dynamics(self) -> Self:
        return SynchronousMachineUserDefined.proprietary_parameter_dynamics.clear(self)

    def num_proprietary_parameter_dynamics(self) -> int:
        return SynchronousMachineUserDefined.proprietary_parameter_dynamics.count(self)
