"""CIM class CCAinverter (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cs_ctype1 import (
        CSCtype1,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay import Delay


class CCAinverter(CimObject):
    """CIM class CCAinverter."""

    __slots__ = ("_cs_ctype1", "_delay")

    cs_ctype1: One[CSCtype1] = One(
        EndMeta(
            name="cs_ctype1",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cs_ctype1:CSCtype1",
            many=False,
            lower=0,
            upper=1,
            inverse="cc_ainverter",
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
            inverse="cc_ainverter",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CCAinverter",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC",
        guid="{099FB680-0560-4201-A6A6-39B3500DAC97}",
        ends=(
            cs_ctype1.meta,
            delay.meta,
        ),
    )

    def __init__(
        self,
        *,
        cs_ctype1: CSCtype1 | None = None,
        delay: Delay | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if cs_ctype1 is not None:
            self.cs_ctype1 = cs_ctype1
        if delay is not None:
            self.delay = delay
