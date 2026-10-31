"""CIM class CsConverter (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.dc.acdc_converter import ACDCConverter

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.dc.cs_operating_mode_kind import CsOperatingModeKind
    from cim_python_sdk.model.iec61970.base.dc.cs_ppcc_control_kind import CsPpccControlKind
    from cim_python_sdk.model.iec61970.dynamics.standard_models.hvdc_dynamics.csc_dynamics import (
        CSCDynamics,
    )


class CsConverter(ACDCConverter):
    """DC side of the current source converter (CSC).

    The firing angle controls the dc voltage at the converter, both for rectifier and
    inverter. The difference between the dc voltages of the rectifier and inverter
    determines the dc current. The extinction angle is used to limit the dc voltage at the
    inverter, if needed, and is not used in active power control. The firing angle,
    transformer tap position and number of connected filters are the primary means to
    control a current source dc line. Higher level controls are built on top, e.g. dc
    voltage, dc current and active power. From a steady state perspective it is sufficient
    to specify the wanted active power transfer (ACDCConverter.targetPpcc) and the control
    functions will set the dc voltage, dc current, firing angle, transformer tap position
    and number of connected filters to meet this. Therefore attributes targetAlpha and
    targetGamma are not applicable in this case.

    The reactive power consumed by the converter is a function of the firing angle,
    transformer tap position and number of connected filter, which can be approximated with
    half of the active power. The losses is a function of the dc voltage and dc current.

    The attributes minAlpha and maxAlpha define the range of firing angles for rectifier
    operation between which no discrete tap changer action takes place. The range is
    typically 10-18 degrees.

    The attributes minGamma and maxGamma define the range of extinction angles for inverter
    operation between which no discrete tap changer action takes place. The range is
    typically 17-20 degrees."""

    __slots__ = (
        "_csc_dynamics",
        "alpha",
        "gamma",
        "max_alpha",
        "max_gamma",
        "max_idc",
        "min_alpha",
        "min_gamma",
        "min_idc",
        "operating_mode",
        "p_pcc_control",
        "rated_idc",
        "target_alpha",
        "target_gamma",
        "target_idc",
    )

    alpha: float | None  # AngleDegrees
    gamma: float | None  # AngleDegrees
    max_alpha: float | None  # AngleDegrees
    max_gamma: float | None  # AngleDegrees
    max_idc: float | None  # CurrentFlow
    min_alpha: float | None  # AngleDegrees
    min_gamma: float | None  # AngleDegrees
    min_idc: float | None  # CurrentFlow
    operating_mode: CsOperatingModeKind | None
    p_pcc_control: CsPpccControlKind | None
    rated_idc: float | None  # CurrentFlow
    target_alpha: float | None  # AngleDegrees
    target_gamma: float | None  # AngleDegrees
    target_idc: float | None  # CurrentFlow

    csc_dynamics: One[CSCDynamics] = One(
        EndMeta(
            name="csc_dynamics",
            cim_role="CSCDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.hvdc_dynamics.csc_dynamics:CSCDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="cs_converter",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CsConverter",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{A4B7CE00-5051-45cf-B107-CD62C2FF3B81}",
        attributes=(
            AttrMeta("alpha", "alpha", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("gamma", "gamma", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("max_alpha", "maxAlpha", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("max_gamma", "maxGamma", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("max_idc", "maxIdc", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("min_alpha", "minAlpha", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("min_gamma", "minGamma", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("min_idc", "minIdc", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("operating_mode", "operatingMode", "CsOperatingModeKind", 0, 1, "enumeration"),
            AttrMeta("p_pcc_control", "pPccControl", "CsPpccControlKind", 0, 1, "enumeration"),
            AttrMeta("rated_idc", "ratedIdc", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("target_alpha", "targetAlpha", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("target_gamma", "targetGamma", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("target_idc", "targetIdc", "CurrentFlow", 0, 1, "cimdatatype"),
        ),
        ends=(csc_dynamics.meta,),
    )

    def __init__(
        self,
        *,
        alpha: float | None = None,
        gamma: float | None = None,
        max_alpha: float | None = None,
        max_gamma: float | None = None,
        max_idc: float | None = None,
        min_alpha: float | None = None,
        min_gamma: float | None = None,
        min_idc: float | None = None,
        operating_mode: CsOperatingModeKind | None = None,
        p_pcc_control: CsPpccControlKind | None = None,
        rated_idc: float | None = None,
        target_alpha: float | None = None,
        target_gamma: float | None = None,
        target_idc: float | None = None,
        csc_dynamics: CSCDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.alpha = alpha
        self.gamma = gamma
        self.max_alpha = max_alpha
        self.max_gamma = max_gamma
        self.max_idc = max_idc
        self.min_alpha = min_alpha
        self.min_gamma = min_gamma
        self.min_idc = min_idc
        self.operating_mode = operating_mode
        self.p_pcc_control = p_pcc_control
        self.rated_idc = rated_idc
        self.target_alpha = target_alpha
        self.target_gamma = target_gamma
        self.target_idc = target_idc
        if csc_dynamics is not None:
            self.csc_dynamics = csc_dynamics
