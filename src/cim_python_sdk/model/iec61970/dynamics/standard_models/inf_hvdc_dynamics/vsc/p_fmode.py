"""CIM class PFmode (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/VSC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay import Delay
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.vs_ctype1 import (
        VSCtype1,
    )


class PFmode(CimObject):
    """CIM class PFmode."""

    __slots__ = ("_delay", "_vs_ctype1")

    delay: One[Delay] = One(
        EndMeta(
            name="delay",
            cim_role="Delay",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay:Delay",
            many=False,
            lower=1,
            upper=1,
            inverse="p_fmode",
            aggregation="none",
        )
    )
    vs_ctype1: One[VSCtype1] = One(
        EndMeta(
            name="vs_ctype1",
            cim_role="VSCtype1",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.vs_ctype1:VSCtype1",
            many=False,
            lower=0,
            upper=1,
            inverse="p_fmodel",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PFmode",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/VSC",
        guid="{8EBE7C53-0C0F-48e0-B638-C4D33AA22148}",
        ends=(
            delay.meta,
            vs_ctype1.meta,
        ),
    )

    def __init__(
        self,
        *,
        delay: Delay | None = None,
        vs_ctype1: VSCtype1 | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if delay is not None:
            self.delay = delay
        if vs_ctype1 is not None:
            self.vs_ctype1 = vs_ctype1
