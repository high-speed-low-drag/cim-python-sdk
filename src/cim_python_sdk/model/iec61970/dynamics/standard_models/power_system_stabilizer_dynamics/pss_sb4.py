"""CIM class PssSB4 (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PssSB4(PowerSystemStabilizerDynamics):
    """Power sensitive stabilizer model."""

    __slots__ = ("kx", "ta", "tb", "tc", "td", "te", "tt", "tx1", "tx2", "vsmax", "vsmin")

    tt: float | None  # Seconds
    kx: float | None  # PU
    tx2: float | None  # Seconds
    ta: float | None  # Seconds
    tx1: float | None  # Seconds
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    td: float | None  # Seconds
    te: float | None  # Seconds
    vsmax: float | None  # PU
    vsmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PssSB4",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{3E2172A5-0DE1-40e7-9ACC-314FCF16B78E}",
        attributes=(
            AttrMeta("tt", "tt", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kx", "kx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tx2", "tx2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tx1", "tx1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vsmax", "vsmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vsmin", "vsmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        tt: float | None = None,
        kx: float | None = None,
        tx2: float | None = None,
        ta: float | None = None,
        tx1: float | None = None,
        tb: float | None = None,
        tc: float | None = None,
        td: float | None = None,
        te: float | None = None,
        vsmax: float | None = None,
        vsmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tt = tt
        self.kx = kx
        self.tx2 = tx2
        self.ta = ta
        self.tx1 = tx1
        self.tb = tb
        self.tc = tc
        self.td = td
        self.te = te
        self.vsmax = vsmax
        self.vsmin = vsmin
