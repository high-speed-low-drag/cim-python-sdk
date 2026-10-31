"""CIM class VSCtype1 (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/VSC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.hvdc_dynamics.vsc_dynamics import (
    VSCDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

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


class VSCtype1(VSCDynamics):
    """CIM class VSCtype1."""

    __slots__ = (
        "_blocking_function",
        "_d_cvoltage_control",
        "_p_fmodel",
        "_pcontrol",
        "_qlimiter",
        "_qmode",
        "_qregulator",
        "_umode",
    )

    qlimiter: One[Qlimiter] = One(
        EndMeta(
            name="qlimiter",
            cim_role="Qlimiter",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qlimiter:Qlimiter",
            many=False,
            lower=1,
            upper=1,
            inverse="vs_ctype1",
            aggregation="none",
        )
    )
    pcontrol: One[Pcontrol] = One(
        EndMeta(
            name="pcontrol",
            cim_role="Pcontrol",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.pcontrol:Pcontrol",
            many=False,
            lower=1,
            upper=1,
            inverse="vs_ctype1",
            aggregation="none",
        )
    )
    qmode: One[Qmode] = One(
        EndMeta(
            name="qmode",
            cim_role="Qmode",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qmode:Qmode",
            many=False,
            lower=1,
            upper=1,
            inverse="vs_ctype1",
            aggregation="none",
        )
    )
    qregulator: One[Qregulator] = One(
        EndMeta(
            name="qregulator",
            cim_role="Qregulator",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qregulator:Qregulator",
            many=False,
            lower=1,
            upper=1,
            inverse="vs_ctype1",
            aggregation="none",
        )
    )
    d_cvoltage_control: One[DCvoltageControl] = One(
        EndMeta(
            name="d_cvoltage_control",
            cim_role="DCvoltageControl",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.d_cvoltage_control:DCvoltageControl",
            many=False,
            lower=1,
            upper=1,
            inverse="vs_ctype1",
            aggregation="none",
        )
    )
    umode: One[Umode] = One(
        EndMeta(
            name="umode",
            cim_role="Umode",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.umode:Umode",
            many=False,
            lower=1,
            upper=1,
            inverse="vs_ctype1",
            aggregation="none",
        )
    )
    p_fmodel: One[PFmode] = One(
        EndMeta(
            name="p_fmodel",
            cim_role="PFmodel",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.p_fmode:PFmode",
            many=False,
            lower=1,
            upper=1,
            inverse="vs_ctype1",
            aggregation="none",
        )
    )
    blocking_function: One[BlockingFunction] = One(
        EndMeta(
            name="blocking_function",
            cim_role="BlockingFunction",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.blocking_function:BlockingFunction",
            many=False,
            lower=1,
            upper=1,
            inverse="vs_ctype1",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VSCtype1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/VSC",
        guid="{3B4C89A8-DD2D-4e68-AB68-EB6320ABD849}",
        ends=(
            qlimiter.meta,
            pcontrol.meta,
            qmode.meta,
            qregulator.meta,
            d_cvoltage_control.meta,
            umode.meta,
            p_fmodel.meta,
            blocking_function.meta,
        ),
    )

    def __init__(
        self,
        *,
        qlimiter: Qlimiter | None = None,
        pcontrol: Pcontrol | None = None,
        qmode: Qmode | None = None,
        qregulator: Qregulator | None = None,
        d_cvoltage_control: DCvoltageControl | None = None,
        umode: Umode | None = None,
        p_fmodel: PFmode | None = None,
        blocking_function: BlockingFunction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if qlimiter is not None:
            self.qlimiter = qlimiter
        if pcontrol is not None:
            self.pcontrol = pcontrol
        if qmode is not None:
            self.qmode = qmode
        if qregulator is not None:
            self.qregulator = qregulator
        if d_cvoltage_control is not None:
            self.d_cvoltage_control = d_cvoltage_control
        if umode is not None:
            self.umode = umode
        if p_fmodel is not None:
            self.p_fmodel = p_fmodel
        if blocking_function is not None:
            self.blocking_function = blocking_function
