"""CIM class CCArectifierControl (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cs_ctype1 import (
        CSCtype1,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay import Delay


class CCArectifierControl(CimObject):
    """CIM class CCArectifierControl."""

    __slots__ = ("_cs_ctype1", "_delay")

    delay: One[Delay] = One(
        EndMeta(
            name="delay",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay:Delay",
            many=False,
            lower=1,
            upper=1,
            inverse="cc_arectifier_control",
            aggregation="none",
        )
    )
    cs_ctype1: One[CSCtype1] = One(
        EndMeta(
            name="cs_ctype1",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cs_ctype1:CSCtype1",
            many=False,
            lower=0,
            upper=1,
            inverse="cc_arectifier_control",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CCArectifierControl",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC",
        guid="{90A5831E-597B-44bf-8364-261D3C6C6B20}",
        ends=(
            delay.meta,
            cs_ctype1.meta,
        ),
    )

    def __init__(
        self,
        *,
        delay: Delay | None = None,
        cs_ctype1: CSCtype1 | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if delay is not None:
            self.delay = delay
        if cs_ctype1 is not None:
            self.cs_ctype1 = cs_ctype1
