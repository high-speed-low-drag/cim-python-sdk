"""CIM class Pss1 (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Pss1(PowerSystemStabilizerDynamics):
    """Italian PSS with three inputs (speed, frequency, power)."""

    __slots__ = (
        "kf",
        "komega",
        "kpe",
        "ks",
        "pmin",
        "t5",
        "t6",
        "t7",
        "t8",
        "t9",
        "t10",
        "tpe",
        "vadat",
        "vsmn",
        "vsmx",
    )

    komega: float | None
    kf: float | None
    kpe: float | None
    pmin: float | None  # PU
    ks: float | None
    vsmn: float | None  # PU
    vsmx: float | None  # PU
    tpe: float | None  # Seconds
    t5: float | None  # Seconds
    t6: float | None  # Seconds
    t7: float | None  # Seconds
    t8: float | None  # Seconds
    t9: float | None  # Seconds
    t10: float | None  # Seconds
    vadat: bool | None

    _cim_meta = ClassMeta(
        cim_name="Pss1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{61359006-B6EA-4d44-88D5-037172A02902}",
        attributes=(
            AttrMeta("komega", "komega", "float", 0, 1, "primitive"),
            AttrMeta("kf", "kf", "float", 0, 1, "primitive"),
            AttrMeta("kpe", "kpe", "float", 0, 1, "primitive"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "float", 0, 1, "primitive"),
            AttrMeta("vsmn", "vsmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vsmx", "vsmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tpe", "tpe", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t7", "t7", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t8", "t8", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t9", "t9", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t10", "t10", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vadat", "vadat", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        komega: float | None = None,
        kf: float | None = None,
        kpe: float | None = None,
        pmin: float | None = None,
        ks: float | None = None,
        vsmn: float | None = None,
        vsmx: float | None = None,
        tpe: float | None = None,
        t5: float | None = None,
        t6: float | None = None,
        t7: float | None = None,
        t8: float | None = None,
        t9: float | None = None,
        t10: float | None = None,
        vadat: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.komega = komega
        self.kf = kf
        self.kpe = kpe
        self.pmin = pmin
        self.ks = ks
        self.vsmn = vsmn
        self.vsmx = vsmx
        self.tpe = tpe
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8
        self.t9 = t9
        self.t10 = t10
        self.vadat = vadat
