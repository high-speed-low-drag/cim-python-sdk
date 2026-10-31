"""CIM class PFVArControllerType2UserDefined (TC57CIM/IEC61970/Dynamics/UserDefinedModels). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type2_dynamics.pfv_ar_controller_type2_dynamics import (
    PFVArControllerType2Dynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.proprietary_parameter_dynamics import (
        ProprietaryParameterDynamics,
    )


class PFVArControllerType2UserDefined(PFVArControllerType2Dynamics):
    """Power factor or VAr controller type 2 function block whose dynamic behaviour is
    described by a user-defined model."""

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
            inverse="pfv_ar_controller_type2_user_defined",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PFVArControllerType2UserDefined",
        package="TC57CIM/IEC61970/Dynamics/UserDefinedModels",
        guid="{B6706B2D-7D88-4378-AA62-CB2E3A61F31F}",
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
            PFVArControllerType2UserDefined.proprietary_parameter_dynamics.extend(
                self, proprietary_parameter_dynamics
            )

    def add_proprietary_parameter_dynamics(
        self, proprietary_parameter_dynamics: ProprietaryParameterDynamics
    ) -> Self:
        return PFVArControllerType2UserDefined.proprietary_parameter_dynamics.add(
            self, proprietary_parameter_dynamics
        )

    def remove_proprietary_parameter_dynamics(
        self, proprietary_parameter_dynamics: ProprietaryParameterDynamics
    ) -> Self:
        return PFVArControllerType2UserDefined.proprietary_parameter_dynamics.remove(
            self, proprietary_parameter_dynamics
        )

    def clear_proprietary_parameter_dynamics(self) -> Self:
        return PFVArControllerType2UserDefined.proprietary_parameter_dynamics.clear(self)

    def num_proprietary_parameter_dynamics(self) -> int:
        return PFVArControllerType2UserDefined.proprietary_parameter_dynamics.count(self)
