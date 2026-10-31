"""CIM class PssSH (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PssSH(PowerSystemStabilizerDynamics):
    """SiemensTM “H infinity” power system stabilizer with generator electrical power input.

    [Footnote: Siemens "H infinity" power system stabilizers are an example of suitable
    products available commercially. This information is given for the convenience of users
    of this document and does not constitute an endorsement by IEC of these products.]"""

    __slots__ = ("k", "k0", "k1", "k2", "k3", "k4", "t1", "t2", "t3", "t4", "td", "vsmax", "vsmin")

    k: float | None  # PU
    k0: float | None  # PU
    k1: float | None  # PU
    k2: float | None  # PU
    k3: float | None  # PU
    k4: float | None  # PU
    td: float | None  # Seconds
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    vsmax: float | None  # PU
    vsmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PssSH",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{462F11AB-EED2-487a-9FB4-9224CB7FCC4A}",
        attributes=(
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k0", "k0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k1", "k1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k2", "k2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k3", "k3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k4", "k4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vsmax", "vsmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vsmin", "vsmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        k: float | None = None,
        k0: float | None = None,
        k1: float | None = None,
        k2: float | None = None,
        k3: float | None = None,
        k4: float | None = None,
        td: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        vsmax: float | None = None,
        vsmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.k = k
        self.k0 = k0
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.td = td
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.vsmax = vsmax
        self.vsmin = vsmin
