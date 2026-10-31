"""CIM class SynchronousMachineDetailed (TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics import (
    SynchronousMachineDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.ifd_base_kind import (
        IfdBaseKind,
    )


class SynchronousMachineDetailed(SynchronousMachineDynamics):
    """All synchronous machine detailed types use a subset of the same data parameters and
    input/output variables.

    The several variations differ in the following ways:

    - the number of equivalent windings that are included;

    - the way in which saturation is incorporated into the model;

    - whether or not “subtransient saliency” (X''q not = X''d) is represented.

    It is not necessary for each simulation tool to have separate models for each of the
    model types. The same model can often be used for several types by alternative logic
    within the model. Also, differences in saturation representation might not result in
    significant model performance differences so model substitutions are often acceptable."""

    __slots__ = (
        "efd_base_ratio",
        "ifd_base_type",
        "saturation_factor120_q_axis",
        "saturation_factor_q_axis",
    )

    efd_base_ratio: float | None
    ifd_base_type: IfdBaseKind | None
    saturation_factor120_q_axis: float | None
    saturation_factor_q_axis: float | None

    _cim_meta = ClassMeta(
        cim_name="SynchronousMachineDetailed",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics",
        guid="{B272216C-A098-436d-80C8-02AD11F5B97F}",
        attributes=(
            AttrMeta("efd_base_ratio", "efdBaseRatio", "float", 0, 1, "primitive"),
            AttrMeta("ifd_base_type", "ifdBaseType", "IfdBaseKind", 0, 1, "enumeration"),
            AttrMeta(
                "saturation_factor120_q_axis",
                "saturationFactor120QAxis",
                "float",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "saturation_factor_q_axis", "saturationFactorQAxis", "float", 0, 1, "primitive"
            ),
        ),
    )

    def __init__(
        self,
        *,
        efd_base_ratio: float | None = None,
        ifd_base_type: IfdBaseKind | None = None,
        saturation_factor120_q_axis: float | None = None,
        saturation_factor_q_axis: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.efd_base_ratio = efd_base_ratio
        self.ifd_base_type = ifd_base_type
        self.saturation_factor120_q_axis = saturation_factor120_q_axis
        self.saturation_factor_q_axis = saturation_factor_q_axis
