"""CIM class IdcInverterControl (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cs_ctype1 import (
        CSCtype1,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.vdcol import (
        VDCOL,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay import Delay


class IdcInverterControl(CimObject):
    """CIM class IdcInverterControl."""

    __slots__ = ("_cs_ctype1", "_delay", "_vdcol")

    cs_ctype1: One[CSCtype1] = One(
        EndMeta(
            name="cs_ctype1",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cs_ctype1:CSCtype1",
            many=False,
            lower=0,
            upper=1,
            inverse="idc_inverter_control",
            aggregation="none",
        )
    )
    vdcol: One[VDCOL] = One(
        EndMeta(
            name="vdcol",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.vdcol:VDCOL",
            many=False,
            lower=1,
            upper=1,
            inverse="idc_inverter_control",
            aggregation="none",
        )
    )
    delay: One[Delay] = One(
        EndMeta(
            name="delay",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay:Delay",
            many=False,
            lower=1,
            upper=1,
            inverse="idc_inverter_control",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IdcInverterControl",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC",
        guid="{6A534873-94AB-429f-B19A-50F1C3309772}",
        ends=(
            cs_ctype1.meta,
            vdcol.meta,
            delay.meta,
        ),
    )

    def __init__(
        self,
        *,
        cs_ctype1: CSCtype1 | None = None,
        vdcol: VDCOL | None = None,
        delay: Delay | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if cs_ctype1 is not None:
            self.cs_ctype1 = cs_ctype1
        if vdcol is not None:
            self.vdcol = vdcol
        if delay is not None:
            self.delay = delay
