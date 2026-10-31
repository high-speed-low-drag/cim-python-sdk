"""CIM class GovSteamCC (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.cross_compound_turbine_governor_dynamics import (
    CrossCompoundTurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovSteamCC(CrossCompoundTurbineGovernorDynamics):
    """Cross compound turbine governor. Unlike tandem compound units, cross compound units are
    not on the same shaft."""

    __slots__ = (
        "dhp",
        "dlp",
        "fhp",
        "flp",
        "mwbase",
        "pmaxhp",
        "pmaxlp",
        "rhp",
        "rlp",
        "t1hp",
        "t1lp",
        "t3hp",
        "t3lp",
        "t4hp",
        "t4lp",
        "t5hp",
        "t5lp",
    )

    mwbase: float | None  # ActivePower
    pmaxhp: float | None  # PU
    rhp: float | None  # PU
    t1hp: float | None  # Seconds
    t3hp: float | None  # Seconds
    t4hp: float | None  # Seconds
    t5hp: float | None  # Seconds
    fhp: float | None  # PU
    dhp: float | None  # PU
    pmaxlp: float | None  # PU
    rlp: float | None  # PU
    t1lp: float | None  # Seconds
    t3lp: float | None  # Seconds
    t4lp: float | None  # Seconds
    t5lp: float | None  # Seconds
    flp: float | None  # PU
    dlp: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovSteamCC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{710F836E-E997-4363-8621-0F02146A82A9}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("pmaxhp", "pmaxhp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rhp", "rhp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1hp", "t1hp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3hp", "t3hp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4hp", "t4hp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5hp", "t5hp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("fhp", "fhp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dhp", "dhp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmaxlp", "pmaxlp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rlp", "rlp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1lp", "t1lp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3lp", "t3lp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4lp", "t4lp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5lp", "t5lp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("flp", "flp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dlp", "dlp", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        pmaxhp: float | None = None,
        rhp: float | None = None,
        t1hp: float | None = None,
        t3hp: float | None = None,
        t4hp: float | None = None,
        t5hp: float | None = None,
        fhp: float | None = None,
        dhp: float | None = None,
        pmaxlp: float | None = None,
        rlp: float | None = None,
        t1lp: float | None = None,
        t3lp: float | None = None,
        t4lp: float | None = None,
        t5lp: float | None = None,
        flp: float | None = None,
        dlp: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.pmaxhp = pmaxhp
        self.rhp = rhp
        self.t1hp = t1hp
        self.t3hp = t3hp
        self.t4hp = t4hp
        self.t5hp = t5hp
        self.fhp = fhp
        self.dhp = dhp
        self.pmaxlp = pmaxlp
        self.rlp = rlp
        self.t1lp = t1lp
        self.t3lp = t3lp
        self.t4lp = t4lp
        self.t5lp = t5lp
        self.flp = flp
        self.dlp = dlp
