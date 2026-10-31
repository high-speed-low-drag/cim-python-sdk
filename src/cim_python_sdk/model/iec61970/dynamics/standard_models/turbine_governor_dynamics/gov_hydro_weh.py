"""CIM class GovHydroWEH (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovHydroWEH(TurbineGovernorDynamics):
    """WoodwardTM electric hydro governor.

    [Footnote: Woodward electric hydro governors are an example of suitable products
    available commercially. This information is given for the convenience of users of this
    document and does not constitute an endorsement by IEC of these products.]"""

    __slots__ = (
        "db",
        "dicn",
        "dpv",
        "dturb",
        "feedback_signal",
        "fl1",
        "fl2",
        "fl3",
        "fl4",
        "fl5",
        "fp1",
        "fp2",
        "fp3",
        "fp4",
        "fp5",
        "fp6",
        "fp7",
        "fp8",
        "fp9",
        "fp10",
        "gmax",
        "gmin",
        "gtmxcl",
        "gtmxop",
        "gv1",
        "gv2",
        "gv3",
        "gv4",
        "gv5",
        "kd",
        "ki",
        "kp",
        "mwbase",
        "pmss1",
        "pmss2",
        "pmss3",
        "pmss4",
        "pmss5",
        "pmss6",
        "pmss7",
        "pmss8",
        "pmss9",
        "pmss10",
        "rpg",
        "rpp",
        "td",
        "tdv",
        "tg",
        "tp",
        "tpe",
        "tw",
    )

    mwbase: float | None  # ActivePower
    rpg: float | None
    rpp: float | None
    tpe: float | None  # Seconds
    kp: float | None  # PU
    ki: float | None  # PU
    kd: float | None  # PU
    td: float | None  # Seconds
    tp: float | None  # Seconds
    tdv: float | None  # Seconds
    tg: float | None  # Seconds
    gtmxop: float | None  # PU
    gtmxcl: float | None  # PU
    gmax: float | None  # PU
    gmin: float | None  # PU
    dturb: float | None  # PU
    tw: float | None  # Seconds
    db: float | None  # PU
    dpv: float | None  # PU
    dicn: float | None  # PU
    feedback_signal: bool | None
    gv1: float | None  # PU
    gv2: float | None  # PU
    gv3: float | None  # PU
    gv4: float | None  # PU
    gv5: float | None  # PU
    fl1: float | None  # PU
    fl2: float | None  # PU
    fl3: float | None  # PU
    fl4: float | None  # PU
    fl5: float | None  # PU
    fp1: float | None  # PU
    fp2: float | None  # PU
    fp3: float | None  # PU
    fp4: float | None  # PU
    fp5: float | None  # PU
    fp6: float | None  # PU
    fp7: float | None  # PU
    fp8: float | None  # PU
    fp9: float | None  # PU
    fp10: float | None  # PU
    pmss1: float | None  # PU
    pmss2: float | None  # PU
    pmss3: float | None  # PU
    pmss4: float | None  # PU
    pmss5: float | None  # PU
    pmss6: float | None  # PU
    pmss7: float | None  # PU
    pmss8: float | None  # PU
    pmss9: float | None  # PU
    pmss10: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovHydroWEH",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{44F7E8EE-7150-4a8b-B451-EB756B45B2C3}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("rpg", "rpg", "float", 0, 1, "primitive"),
            AttrMeta("rpp", "rpp", "float", 0, 1, "primitive"),
            AttrMeta("tpe", "tpe", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tdv", "tdv", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tg", "tg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("gtmxop", "gtmxop", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gtmxcl", "gtmxcl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gmax", "gmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gmin", "gmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dturb", "dturb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tw", "tw", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("db", "db", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dpv", "dpv", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dicn", "dicn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("feedback_signal", "feedbackSignal", "bool", 0, 1, "primitive"),
            AttrMeta("gv1", "gv1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv2", "gv2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv3", "gv3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv4", "gv4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv5", "gv5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fl1", "fl1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fl2", "fl2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fl3", "fl3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fl4", "fl4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fl5", "fl5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fp1", "fp1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fp2", "fp2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fp3", "fp3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fp4", "fp4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fp5", "fp5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fp6", "fp6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fp7", "fp7", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fp8", "fp8", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fp9", "fp9", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fp10", "fp10", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmss1", "pmss1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmss2", "pmss2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmss3", "pmss3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmss4", "pmss4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmss5", "pmss5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmss6", "pmss6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmss7", "pmss7", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmss8", "pmss8", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmss9", "pmss9", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmss10", "pmss10", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        rpg: float | None = None,
        rpp: float | None = None,
        tpe: float | None = None,
        kp: float | None = None,
        ki: float | None = None,
        kd: float | None = None,
        td: float | None = None,
        tp: float | None = None,
        tdv: float | None = None,
        tg: float | None = None,
        gtmxop: float | None = None,
        gtmxcl: float | None = None,
        gmax: float | None = None,
        gmin: float | None = None,
        dturb: float | None = None,
        tw: float | None = None,
        db: float | None = None,
        dpv: float | None = None,
        dicn: float | None = None,
        feedback_signal: bool | None = None,
        gv1: float | None = None,
        gv2: float | None = None,
        gv3: float | None = None,
        gv4: float | None = None,
        gv5: float | None = None,
        fl1: float | None = None,
        fl2: float | None = None,
        fl3: float | None = None,
        fl4: float | None = None,
        fl5: float | None = None,
        fp1: float | None = None,
        fp2: float | None = None,
        fp3: float | None = None,
        fp4: float | None = None,
        fp5: float | None = None,
        fp6: float | None = None,
        fp7: float | None = None,
        fp8: float | None = None,
        fp9: float | None = None,
        fp10: float | None = None,
        pmss1: float | None = None,
        pmss2: float | None = None,
        pmss3: float | None = None,
        pmss4: float | None = None,
        pmss5: float | None = None,
        pmss6: float | None = None,
        pmss7: float | None = None,
        pmss8: float | None = None,
        pmss9: float | None = None,
        pmss10: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.rpg = rpg
        self.rpp = rpp
        self.tpe = tpe
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.td = td
        self.tp = tp
        self.tdv = tdv
        self.tg = tg
        self.gtmxop = gtmxop
        self.gtmxcl = gtmxcl
        self.gmax = gmax
        self.gmin = gmin
        self.dturb = dturb
        self.tw = tw
        self.db = db
        self.dpv = dpv
        self.dicn = dicn
        self.feedback_signal = feedback_signal
        self.gv1 = gv1
        self.gv2 = gv2
        self.gv3 = gv3
        self.gv4 = gv4
        self.gv5 = gv5
        self.fl1 = fl1
        self.fl2 = fl2
        self.fl3 = fl3
        self.fl4 = fl4
        self.fl5 = fl5
        self.fp1 = fp1
        self.fp2 = fp2
        self.fp3 = fp3
        self.fp4 = fp4
        self.fp5 = fp5
        self.fp6 = fp6
        self.fp7 = fp7
        self.fp8 = fp8
        self.fp9 = fp9
        self.fp10 = fp10
        self.pmss1 = pmss1
        self.pmss2 = pmss2
        self.pmss3 = pmss3
        self.pmss4 = pmss4
        self.pmss5 = pmss5
        self.pmss6 = pmss6
        self.pmss7 = pmss7
        self.pmss8 = pmss8
        self.pmss9 = pmss9
        self.pmss10 = pmss10
