"""CIM class Pss2B (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Pss2B(PowerSystemStabilizerDynamics):
    """Modified IEEE PSS2B. Extra lead/lag (or rate) block added at end (up to 4 lead/lags
    total)."""

    __slots__ = (
        "a",
        "ks1",
        "ks2",
        "ks3",
        "ks4",
        "m",
        "n",
        "t1",
        "t2",
        "t3",
        "t4",
        "t6",
        "t7",
        "t8",
        "t9",
        "t10",
        "t11",
        "ta",
        "tb",
        "tw1",
        "tw2",
        "tw3",
        "tw4",
        "vsi1max",
        "vsi1min",
        "vsi2max",
        "vsi2min",
        "vstmax",
        "vstmin",
    )

    vsi1max: float | None  # PU
    vsi1min: float | None  # PU
    tw1: float | None  # Seconds
    tw2: float | None  # Seconds
    vsi2max: float | None  # PU
    vsi2min: float | None  # PU
    tw3: float | None  # Seconds
    tw4: float | None  # Seconds
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    t6: float | None  # Seconds
    t7: float | None  # Seconds
    t8: float | None  # Seconds
    t9: float | None  # Seconds
    t10: float | None  # Seconds
    t11: float | None  # Seconds
    ks1: float | None  # PU
    ks2: float | None  # PU
    ks3: float | None  # PU
    ks4: float | None  # PU
    n: int | None
    m: int | None
    vstmax: float | None  # PU
    vstmin: float | None  # PU
    a: float | None
    ta: float | None  # Seconds
    tb: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="Pss2B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{A95B2DA4-2E19-4831-82FF-AB7074ACAEC4}",
        attributes=(
            AttrMeta("vsi1max", "vsi1max", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vsi1min", "vsi1min", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tw1", "tw1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tw2", "tw2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vsi2max", "vsi2max", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vsi2min", "vsi2min", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tw3", "tw3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tw4", "tw4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t7", "t7", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t8", "t8", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t9", "t9", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t10", "t10", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t11", "t11", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ks1", "ks1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks2", "ks2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks3", "ks3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks4", "ks4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("n", "n", "int", 0, 1, "primitive"),
            AttrMeta("m", "m", "int", 0, 1, "primitive"),
            AttrMeta("vstmax", "vstmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vstmin", "vstmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a", "a", "float", 0, 1, "primitive"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        vsi1max: float | None = None,
        vsi1min: float | None = None,
        tw1: float | None = None,
        tw2: float | None = None,
        vsi2max: float | None = None,
        vsi2min: float | None = None,
        tw3: float | None = None,
        tw4: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        t6: float | None = None,
        t7: float | None = None,
        t8: float | None = None,
        t9: float | None = None,
        t10: float | None = None,
        t11: float | None = None,
        ks1: float | None = None,
        ks2: float | None = None,
        ks3: float | None = None,
        ks4: float | None = None,
        n: int | None = None,
        m: int | None = None,
        vstmax: float | None = None,
        vstmin: float | None = None,
        a: float | None = None,
        ta: float | None = None,
        tb: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.vsi1max = vsi1max
        self.vsi1min = vsi1min
        self.tw1 = tw1
        self.tw2 = tw2
        self.vsi2max = vsi2max
        self.vsi2min = vsi2min
        self.tw3 = tw3
        self.tw4 = tw4
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8
        self.t9 = t9
        self.t10 = t10
        self.t11 = t11
        self.ks1 = ks1
        self.ks2 = ks2
        self.ks3 = ks3
        self.ks4 = ks4
        self.n = n
        self.m = m
        self.vstmax = vstmax
        self.vstmin = vstmin
        self.a = a
        self.ta = ta
        self.tb = tb
