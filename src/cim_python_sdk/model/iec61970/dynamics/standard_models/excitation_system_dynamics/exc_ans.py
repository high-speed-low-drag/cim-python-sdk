"""CIM class ExcANS (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcANS(ExcitationSystemDynamics):
    """Italian excitation system. It represents static field voltage or excitation current
    feedback excitation system."""

    __slots__ = (
        "blint",
        "ifmn",
        "ifmx",
        "k2",
        "k3",
        "kce",
        "krvecc",
        "kvfif",
        "t1",
        "t2",
        "t3",
        "tb",
        "vrmn",
        "vrmx",
    )

    blint: int | None
    ifmn: float | None  # PU
    ifmx: float | None  # PU
    k2: float | None
    k3: float | None
    kce: float | None
    krvecc: int | None
    kvfif: int | None
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    tb: float | None  # Seconds
    vrmn: float | None  # PU
    vrmx: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcANS",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{D95B626D-AAD0-4551-B642-BD8E8040992C}",
        attributes=(
            AttrMeta("blint", "blint", "int", 0, 1, "primitive"),
            AttrMeta("ifmn", "ifmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ifmx", "ifmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k2", "k2", "float", 0, 1, "primitive"),
            AttrMeta("k3", "k3", "float", 0, 1, "primitive"),
            AttrMeta("kce", "kce", "float", 0, 1, "primitive"),
            AttrMeta("krvecc", "krvecc", "int", 0, 1, "primitive"),
            AttrMeta("kvfif", "kvfif", "int", 0, 1, "primitive"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmn", "vrmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmx", "vrmx", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        blint: int | None = None,
        ifmn: float | None = None,
        ifmx: float | None = None,
        k2: float | None = None,
        k3: float | None = None,
        kce: float | None = None,
        krvecc: int | None = None,
        kvfif: int | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        tb: float | None = None,
        vrmn: float | None = None,
        vrmx: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.blint = blint
        self.ifmn = ifmn
        self.ifmx = ifmx
        self.k2 = k2
        self.k3 = k3
        self.kce = kce
        self.krvecc = krvecc
        self.kvfif = kvfif
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.tb = tb
        self.vrmn = vrmn
        self.vrmx = vrmx
