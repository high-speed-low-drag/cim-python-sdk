"""CIM class PowerSystemStabilizerUserDefined (TC57CIM/IEC61970/Dynamics/UserDefinedModels). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.proprietary_parameter_dynamics import (
        ProprietaryParameterDynamics,
    )


class PowerSystemStabilizerUserDefined(PowerSystemStabilizerDynamics):
    """Power system stabilizer function block whose dynamic behaviour is described by a
    user-defined model."""

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
            inverse="power_system_stabilizer_user_defined",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerSystemStabilizerUserDefined",
        package="TC57CIM/IEC61970/Dynamics/UserDefinedModels",
        guid="{65A4611C-F5C6-4f93-80E8-5FC8D45C5BCC}",
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
            PowerSystemStabilizerUserDefined.proprietary_parameter_dynamics.extend(
                self, proprietary_parameter_dynamics
            )

    def add_proprietary_parameter_dynamics(
        self, proprietary_parameter_dynamics: ProprietaryParameterDynamics
    ) -> Self:
        return PowerSystemStabilizerUserDefined.proprietary_parameter_dynamics.add(
            self, proprietary_parameter_dynamics
        )

    def remove_proprietary_parameter_dynamics(
        self, proprietary_parameter_dynamics: ProprietaryParameterDynamics
    ) -> Self:
        return PowerSystemStabilizerUserDefined.proprietary_parameter_dynamics.remove(
            self, proprietary_parameter_dynamics
        )

    def clear_proprietary_parameter_dynamics(self) -> Self:
        return PowerSystemStabilizerUserDefined.proprietary_parameter_dynamics.clear(self)

    def num_proprietary_parameter_dynamics(self) -> int:
        return PowerSystemStabilizerUserDefined.proprietary_parameter_dynamics.count(self)
