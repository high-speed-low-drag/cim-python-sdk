"""CIM class ExcELIN1 (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcELIN1(ExcitationSystemDynamics):
    """Static PI transformer fed excitation system ELIN (VATECH) - simplified model. This model
    represents an all-static excitation system. A PI voltage controller establishes a
    desired field current set point for a proportional current controller. The integrator of
    the PI controller has a follow-up input to match its signal to the present field
    current. A power system stabilizer with power input is included in the model."""

    __slots__ = (
        "dpnf",
        "efmax",
        "efmin",
        "ks1",
        "ks2",
        "smax",
        "tfi",
        "tnu",
        "ts1",
        "ts2",
        "tsw",
        "vpi",
        "vpnf",
        "vpu",
        "xe",
    )

    tfi: float | None  # Seconds
    tnu: float | None  # Seconds
    vpu: float | None  # PU
    vpi: float | None  # PU
    vpnf: float | None  # PU
    dpnf: float | None  # PU
    tsw: float | None  # Seconds
    efmin: float | None  # PU
    efmax: float | None  # PU
    xe: float | None  # PU
    ks1: float | None  # PU
    ks2: float | None  # PU
    ts1: float | None  # Seconds
    ts2: float | None  # Seconds
    smax: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcELIN1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{61B64CDD-C0DC-4805-9FAE-F5CE6F84BE93}",
        attributes=(
            AttrMeta("tfi", "tfi", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tnu", "tnu", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vpu", "vpu", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vpi", "vpi", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vpnf", "vpnf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dpnf", "dpnf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tsw", "tsw", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("efmin", "efmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efmax", "efmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xe", "xe", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks1", "ks1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks2", "ks2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ts1", "ts1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ts2", "ts2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("smax", "smax", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        tfi: float | None = None,
        tnu: float | None = None,
        vpu: float | None = None,
        vpi: float | None = None,
        vpnf: float | None = None,
        dpnf: float | None = None,
        tsw: float | None = None,
        efmin: float | None = None,
        efmax: float | None = None,
        xe: float | None = None,
        ks1: float | None = None,
        ks2: float | None = None,
        ts1: float | None = None,
        ts2: float | None = None,
        smax: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tfi = tfi
        self.tnu = tnu
        self.vpu = vpu
        self.vpi = vpi
        self.vpnf = vpnf
        self.dpnf = dpnf
        self.tsw = tsw
        self.efmin = efmin
        self.efmax = efmax
        self.xe = xe
        self.ks1 = ks1
        self.ks2 = ks2
        self.ts1 = ts1
        self.ts2 = ts2
        self.smax = smax
