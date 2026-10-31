"""CIM class CSCtype1 (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.hvdc_dynamics.csc_dynamics import (
    CSCDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cc_ainverter import (
        CCAinverter,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cc_arectifier_control import (
        CCArectifierControl,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.idc_inverter_control import (
        IdcInverterControl,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.ign_angle_cont_inverter import (
        IgnAngleContInverter,
    )


class CSCtype1(CSCDynamics):
    """CIM class CSCtype1."""

    __slots__ = (
        "_cc_ainverter",
        "_cc_arectifier_control",
        "_idc_inverter_control",
        "_ign_angle_cont_inverter",
    )

    ign_angle_cont_inverter: One[IgnAngleContInverter] = One(
        EndMeta(
            name="ign_angle_cont_inverter",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.ign_angle_cont_inverter:IgnAngleContInverter",
            many=False,
            lower=1,
            upper=1,
            inverse="cs_ctype1",
            aggregation="none",
        )
    )
    idc_inverter_control: One[IdcInverterControl] = One(
        EndMeta(
            name="idc_inverter_control",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.idc_inverter_control:IdcInverterControl",
            many=False,
            lower=1,
            upper=1,
            inverse="cs_ctype1",
            aggregation="none",
        )
    )
    cc_arectifier_control: One[CCArectifierControl] = One(
        EndMeta(
            name="cc_arectifier_control",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cc_arectifier_control:CCArectifierControl",
            many=False,
            lower=1,
            upper=1,
            inverse="cs_ctype1",
            aggregation="none",
        )
    )
    cc_ainverter: One[CCAinverter] = One(
        EndMeta(
            name="cc_ainverter",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cc_ainverter:CCAinverter",
            many=False,
            lower=1,
            upper=1,
            inverse="cs_ctype1",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CSCtype1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC",
        guid="{C3AAA040-6C8A-4023-91B9-2A17211AC45F}",
        ends=(
            ign_angle_cont_inverter.meta,
            idc_inverter_control.meta,
            cc_arectifier_control.meta,
            cc_ainverter.meta,
        ),
    )

    def __init__(
        self,
        *,
        ign_angle_cont_inverter: IgnAngleContInverter | None = None,
        idc_inverter_control: IdcInverterControl | None = None,
        cc_arectifier_control: CCArectifierControl | None = None,
        cc_ainverter: CCAinverter | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if ign_angle_cont_inverter is not None:
            self.ign_angle_cont_inverter = ign_angle_cont_inverter
        if idc_inverter_control is not None:
            self.idc_inverter_control = idc_inverter_control
        if cc_arectifier_control is not None:
            self.cc_arectifier_control = cc_arectifier_control
        if cc_ainverter is not None:
            self.cc_ainverter = cc_ainverter
