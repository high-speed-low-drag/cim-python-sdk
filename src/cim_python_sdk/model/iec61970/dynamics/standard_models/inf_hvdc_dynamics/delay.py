"""CIM class Delay (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

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
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.vdcol import (
        VDCOL,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.blocking_function import (
        BlockingFunction,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.d_cvoltage_control import (
        DCvoltageControl,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.p_fmode import (
        PFmode,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.pcontrol import (
        Pcontrol,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qlimiter import (
        Qlimiter,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qmode import (
        Qmode,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qregulator import (
        Qregulator,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.umode import (
        Umode,
    )


class Delay(CimObject):
    """All the measurements are filtered by a first lag element with a time constant TM."""

    __slots__ = (
        "_blocking_function",
        "_cc_ainverter",
        "_cc_arectifier_control",
        "_d_cvoltage_control",
        "_idc_inverter_control",
        "_p_fmode",
        "_pcontrol",
        "_qlimiter",
        "_qmode",
        "_qregulator",
        "_umode",
        "_vdcol",
        "tm",
    )

    tm: float | None  # Seconds

    p_fmode: One[PFmode] = One(
        EndMeta(
            name="p_fmode",
            cim_role="PFmode",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.p_fmode:PFmode",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    qmode: One[Qmode] = One(
        EndMeta(
            name="qmode",
            cim_role="Qmode",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qmode:Qmode",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    blocking_function: One[BlockingFunction] = One(
        EndMeta(
            name="blocking_function",
            cim_role="BlockingFunction",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.blocking_function:BlockingFunction",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    qlimiter: One[Qlimiter] = One(
        EndMeta(
            name="qlimiter",
            cim_role="Qlimiter",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qlimiter:Qlimiter",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    umode: One[Umode] = One(
        EndMeta(
            name="umode",
            cim_role="Umode",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.umode:Umode",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    d_cvoltage_control: One[DCvoltageControl] = One(
        EndMeta(
            name="d_cvoltage_control",
            cim_role="DCvoltageControl",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.d_cvoltage_control:DCvoltageControl",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    cc_arectifier_control: One[CCArectifierControl] = One(
        EndMeta(
            name="cc_arectifier_control",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cc_arectifier_control:CCArectifierControl",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    qregulator: One[Qregulator] = One(
        EndMeta(
            name="qregulator",
            cim_role="Qregulator",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qregulator:Qregulator",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    pcontrol: One[Pcontrol] = One(
        EndMeta(
            name="pcontrol",
            cim_role="Pcontrol",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.pcontrol:Pcontrol",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    cc_ainverter: One[CCAinverter] = One(
        EndMeta(
            name="cc_ainverter",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cc_ainverter:CCAinverter",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    vdcol: One[VDCOL] = One(
        EndMeta(
            name="vdcol",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.vdcol:VDCOL",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )
    idc_inverter_control: One[IdcInverterControl] = One(
        EndMeta(
            name="idc_inverter_control",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.idc_inverter_control:IdcInverterControl",
            many=False,
            lower=0,
            upper=1,
            inverse="delay",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Delay",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics",
        guid="{3A73496A-9549-4898-A98E-E7A51B9B8A6B}",
        attributes=(AttrMeta("tm", "tm", "Seconds", 0, 1, "cimdatatype"),),
        ends=(
            p_fmode.meta,
            qmode.meta,
            blocking_function.meta,
            qlimiter.meta,
            umode.meta,
            d_cvoltage_control.meta,
            cc_arectifier_control.meta,
            qregulator.meta,
            pcontrol.meta,
            cc_ainverter.meta,
            vdcol.meta,
            idc_inverter_control.meta,
        ),
    )

    def __init__(
        self,
        *,
        tm: float | None = None,
        p_fmode: PFmode | None = None,
        qmode: Qmode | None = None,
        blocking_function: BlockingFunction | None = None,
        qlimiter: Qlimiter | None = None,
        umode: Umode | None = None,
        d_cvoltage_control: DCvoltageControl | None = None,
        cc_arectifier_control: CCArectifierControl | None = None,
        qregulator: Qregulator | None = None,
        pcontrol: Pcontrol | None = None,
        cc_ainverter: CCAinverter | None = None,
        vdcol: VDCOL | None = None,
        idc_inverter_control: IdcInverterControl | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tm = tm
        if p_fmode is not None:
            self.p_fmode = p_fmode
        if qmode is not None:
            self.qmode = qmode
        if blocking_function is not None:
            self.blocking_function = blocking_function
        if qlimiter is not None:
            self.qlimiter = qlimiter
        if umode is not None:
            self.umode = umode
        if d_cvoltage_control is not None:
            self.d_cvoltage_control = d_cvoltage_control
        if cc_arectifier_control is not None:
            self.cc_arectifier_control = cc_arectifier_control
        if qregulator is not None:
            self.qregulator = qregulator
        if pcontrol is not None:
            self.pcontrol = pcontrol
        if cc_ainverter is not None:
            self.cc_ainverter = cc_ainverter
        if vdcol is not None:
            self.vdcol = vdcol
        if idc_inverter_control is not None:
            self.idc_inverter_control = idc_inverter_control
