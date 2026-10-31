"""CIM class Pss5 (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Pss5(PowerSystemStabilizerDynamics):
    """Detailed Italian PSS."""

    __slots__ = (
        "ctw2",
        "deadband",
        "isfreq",
        "kf",
        "kpe",
        "kpss",
        "pmin",
        "tl1",
        "tl2",
        "tl3",
        "tl4",
        "tpe",
        "tw1",
        "tw2",
        "vadat",
        "vsmn",
        "vsmx",
    )

    kpe: float | None
    kf: float | None
    isfreq: bool | None
    kpss: float | None
    ctw2: bool | None
    tw1: float | None  # Seconds
    tw2: float | None  # Seconds
    tl1: float | None  # Seconds
    tl2: float | None  # Seconds
    tl3: float | None  # Seconds
    tl4: float | None  # Seconds
    vsmn: float | None  # PU
    vsmx: float | None  # PU
    tpe: float | None  # Seconds
    pmin: float | None  # PU
    deadband: float | None  # PU
    vadat: bool | None

    _cim_meta = ClassMeta(
        cim_name="Pss5",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{63072F6E-933B-4719-923E-7FADA9019D79}",
        attributes=(
            AttrMeta("kpe", "kpe", "float", 0, 1, "primitive"),
            AttrMeta("kf", "kf", "float", 0, 1, "primitive"),
            AttrMeta("isfreq", "isfreq", "bool", 0, 1, "primitive"),
            AttrMeta("kpss", "kpss", "float", 0, 1, "primitive"),
            AttrMeta("ctw2", "ctw2", "bool", 0, 1, "primitive"),
            AttrMeta("tw1", "tw1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tw2", "tw2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl1", "tl1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl2", "tl2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl3", "tl3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl4", "tl4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vsmn", "vsmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vsmx", "vsmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tpe", "tpe", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("deadband", "deadband", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vadat", "vadat", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        kpe: float | None = None,
        kf: float | None = None,
        isfreq: bool | None = None,
        kpss: float | None = None,
        ctw2: bool | None = None,
        tw1: float | None = None,
        tw2: float | None = None,
        tl1: float | None = None,
        tl2: float | None = None,
        tl3: float | None = None,
        tl4: float | None = None,
        vsmn: float | None = None,
        vsmx: float | None = None,
        tpe: float | None = None,
        pmin: float | None = None,
        deadband: float | None = None,
        vadat: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kpe = kpe
        self.kf = kf
        self.isfreq = isfreq
        self.kpss = kpss
        self.ctw2 = ctw2
        self.tw1 = tw1
        self.tw2 = tw2
        self.tl1 = tl1
        self.tl2 = tl2
        self.tl3 = tl3
        self.tl4 = tl4
        self.vsmn = vsmn
        self.vsmx = vsmx
        self.tpe = tpe
        self.pmin = pmin
        self.deadband = deadband
        self.vadat = vadat
