"""CIM class DCvoltageControl (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/VSC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay import Delay
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.vs_ctype1 import (
        VSCtype1,
    )


class DCvoltageControl(CimObject):
    """DC voltage control used for voltage regulation."""

    __slots__ = ("_delay", "_vs_ctype1", "kivdc", "kpvdc", "vdcmax", "vdcmin")

    vdcmax: float | None  # PU
    vdcmin: float | None  # PU
    kivdc: float | None  # PU
    kpvdc: float | None  # PU

    vs_ctype1: One[VSCtype1] = One(
        EndMeta(
            name="vs_ctype1",
            cim_role="VSCtype1",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.vs_ctype1:VSCtype1",
            many=False,
            lower=0,
            upper=1,
            inverse="d_cvoltage_control",
            aggregation="none",
        )
    )
    delay: One[Delay] = One(
        EndMeta(
            name="delay",
            cim_role="Delay",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay:Delay",
            many=False,
            lower=1,
            upper=1,
            inverse="d_cvoltage_control",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCvoltageControl",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/VSC",
        guid="{8A8DDDF8-77D5-4212-9C16-9F19603AC192}",
        attributes=(
            AttrMeta("vdcmax", "vdcmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vdcmin", "vdcmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kivdc", "kivdc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpvdc", "kpvdc", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(
            vs_ctype1.meta,
            delay.meta,
        ),
    )

    def __init__(
        self,
        *,
        vdcmax: float | None = None,
        vdcmin: float | None = None,
        kivdc: float | None = None,
        kpvdc: float | None = None,
        vs_ctype1: VSCtype1 | None = None,
        delay: Delay | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.vdcmax = vdcmax
        self.vdcmin = vdcmin
        self.kivdc = kivdc
        self.kpvdc = kpvdc
        if vs_ctype1 is not None:
            self.vs_ctype1 = vs_ctype1
        if delay is not None:
            self.delay = delay
