"""CIM class PssIEEE4B (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PssIEEE4B(PowerSystemStabilizerDynamics):
    """IEEE 421.5-2005 type PSS4B power system stabilizer. The PSS4B model represents a
    structure based on multiple working frequency bands. Three separate bands, respectively
    dedicated to the low-, intermediate- and high-frequency modes of oscillations, are used
    in this delta omega (speed input) PSS.

    There is an error in the in IEEE 421.5-2005 PSS4B model: the Pe input should read –Pe.
    This implies that the input Pe needs to be multiplied by -1.

    Reference: IEEE 4B 421.5-2005, 8.4.

    Parameter details:

    This model has 2 input signals. They have the following fixed types (expressed in terms
    of InputSignalKind values): the first one is of rotorAngleFrequencyDeviation type and
    the second one is of generatorElectricalPower type."""

    __slots__ = (
        "bwh1",
        "bwh2",
        "bwl1",
        "bwl2",
        "kh",
        "kh1",
        "kh2",
        "kh11",
        "kh17",
        "ki",
        "ki1",
        "ki2",
        "ki11",
        "ki17",
        "kl",
        "kl1",
        "kl2",
        "kl11",
        "kl17",
        "omeganh1",
        "omeganh2",
        "omeganl1",
        "omeganl2",
        "th1",
        "th2",
        "th3",
        "th4",
        "th5",
        "th6",
        "th7",
        "th8",
        "th9",
        "th10",
        "th11",
        "th12",
        "ti1",
        "ti2",
        "ti3",
        "ti4",
        "ti5",
        "ti6",
        "ti7",
        "ti8",
        "ti9",
        "ti10",
        "ti11",
        "ti12",
        "tl1",
        "tl2",
        "tl3",
        "tl4",
        "tl5",
        "tl6",
        "tl7",
        "tl8",
        "tl9",
        "tl10",
        "tl11",
        "tl12",
        "vhmax",
        "vhmin",
        "vimax",
        "vimin",
        "vlmax",
        "vlmin",
        "vstmax",
        "vstmin",
    )

    bwh1: float | None
    bwh2: float | None
    bwl1: float | None
    bwl2: float | None
    kh: float | None  # PU
    kh1: float | None  # PU
    kh11: float | None  # PU
    kh17: float | None  # PU
    kh2: float | None  # PU
    ki: float | None  # PU
    ki1: float | None  # PU
    ki11: float | None  # PU
    ki17: float | None  # PU
    ki2: float | None  # PU
    kl: float | None  # PU
    kl1: float | None  # PU
    kl11: float | None  # PU
    kl17: float | None  # PU
    kl2: float | None  # PU
    omeganh1: float | None
    omeganh2: float | None
    omeganl1: float | None
    omeganl2: float | None
    th1: float | None  # Seconds
    th10: float | None  # Seconds
    th11: float | None  # Seconds
    th12: float | None  # Seconds
    th2: float | None  # Seconds
    th3: float | None  # Seconds
    th4: float | None  # Seconds
    th5: float | None  # Seconds
    th6: float | None  # Seconds
    th7: float | None  # Seconds
    th8: float | None  # Seconds
    th9: float | None  # Seconds
    ti1: float | None  # Seconds
    ti10: float | None  # Seconds
    ti11: float | None  # Seconds
    ti12: float | None  # Seconds
    ti2: float | None  # Seconds
    ti3: float | None  # Seconds
    ti4: float | None  # Seconds
    ti5: float | None  # Seconds
    ti6: float | None  # Seconds
    ti7: float | None  # Seconds
    ti8: float | None  # Seconds
    ti9: float | None  # Seconds
    tl1: float | None  # Seconds
    tl10: float | None  # Seconds
    tl11: float | None  # Seconds
    tl12: float | None  # Seconds
    tl2: float | None  # Seconds
    tl3: float | None  # Seconds
    tl4: float | None  # Seconds
    tl5: float | None  # Seconds
    tl6: float | None  # Seconds
    tl7: float | None  # Seconds
    tl8: float | None  # Seconds
    tl9: float | None  # Seconds
    vhmax: float | None  # PU
    vhmin: float | None  # PU
    vimax: float | None  # PU
    vimin: float | None  # PU
    vlmax: float | None  # PU
    vlmin: float | None  # PU
    vstmax: float | None  # PU
    vstmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PssIEEE4B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{C6556415-B3C7-4b4c-B73C-A37F295680DA}",
        attributes=(
            AttrMeta("bwh1", "bwh1", "float", 0, 1, "primitive"),
            AttrMeta("bwh2", "bwh2", "float", 0, 1, "primitive"),
            AttrMeta("bwl1", "bwl1", "float", 0, 1, "primitive"),
            AttrMeta("bwl2", "bwl2", "float", 0, 1, "primitive"),
            AttrMeta("kh", "kh", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kh1", "kh1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kh11", "kh11", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kh17", "kh17", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kh2", "kh2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki1", "ki1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki11", "ki11", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki17", "ki17", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki2", "ki2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kl", "kl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kl1", "kl1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kl11", "kl11", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kl17", "kl17", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kl2", "kl2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("omeganh1", "omeganh1", "float", 0, 1, "primitive"),
            AttrMeta("omeganh2", "omeganh2", "float", 0, 1, "primitive"),
            AttrMeta("omeganl1", "omeganl1", "float", 0, 1, "primitive"),
            AttrMeta("omeganl2", "omeganl2", "float", 0, 1, "primitive"),
            AttrMeta("th1", "th1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th10", "th10", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th11", "th11", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th12", "th12", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th2", "th2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th3", "th3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th4", "th4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th5", "th5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th6", "th6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th7", "th7", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th8", "th8", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th9", "th9", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti1", "ti1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti10", "ti10", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti11", "ti11", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti12", "ti12", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti2", "ti2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti3", "ti3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti4", "ti4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti5", "ti5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti6", "ti6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti7", "ti7", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti8", "ti8", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti9", "ti9", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl1", "tl1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl10", "tl10", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl11", "tl11", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl12", "tl12", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl2", "tl2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl3", "tl3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl4", "tl4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl5", "tl5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl6", "tl6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl7", "tl7", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl8", "tl8", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl9", "tl9", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vhmax", "vhmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vhmin", "vhmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimax", "vimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimin", "vimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vlmax", "vlmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vlmin", "vlmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vstmax", "vstmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vstmin", "vstmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        bwh1: float | None = None,
        bwh2: float | None = None,
        bwl1: float | None = None,
        bwl2: float | None = None,
        kh: float | None = None,
        kh1: float | None = None,
        kh11: float | None = None,
        kh17: float | None = None,
        kh2: float | None = None,
        ki: float | None = None,
        ki1: float | None = None,
        ki11: float | None = None,
        ki17: float | None = None,
        ki2: float | None = None,
        kl: float | None = None,
        kl1: float | None = None,
        kl11: float | None = None,
        kl17: float | None = None,
        kl2: float | None = None,
        omeganh1: float | None = None,
        omeganh2: float | None = None,
        omeganl1: float | None = None,
        omeganl2: float | None = None,
        th1: float | None = None,
        th10: float | None = None,
        th11: float | None = None,
        th12: float | None = None,
        th2: float | None = None,
        th3: float | None = None,
        th4: float | None = None,
        th5: float | None = None,
        th6: float | None = None,
        th7: float | None = None,
        th8: float | None = None,
        th9: float | None = None,
        ti1: float | None = None,
        ti10: float | None = None,
        ti11: float | None = None,
        ti12: float | None = None,
        ti2: float | None = None,
        ti3: float | None = None,
        ti4: float | None = None,
        ti5: float | None = None,
        ti6: float | None = None,
        ti7: float | None = None,
        ti8: float | None = None,
        ti9: float | None = None,
        tl1: float | None = None,
        tl10: float | None = None,
        tl11: float | None = None,
        tl12: float | None = None,
        tl2: float | None = None,
        tl3: float | None = None,
        tl4: float | None = None,
        tl5: float | None = None,
        tl6: float | None = None,
        tl7: float | None = None,
        tl8: float | None = None,
        tl9: float | None = None,
        vhmax: float | None = None,
        vhmin: float | None = None,
        vimax: float | None = None,
        vimin: float | None = None,
        vlmax: float | None = None,
        vlmin: float | None = None,
        vstmax: float | None = None,
        vstmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bwh1 = bwh1
        self.bwh2 = bwh2
        self.bwl1 = bwl1
        self.bwl2 = bwl2
        self.kh = kh
        self.kh1 = kh1
        self.kh11 = kh11
        self.kh17 = kh17
        self.kh2 = kh2
        self.ki = ki
        self.ki1 = ki1
        self.ki11 = ki11
        self.ki17 = ki17
        self.ki2 = ki2
        self.kl = kl
        self.kl1 = kl1
        self.kl11 = kl11
        self.kl17 = kl17
        self.kl2 = kl2
        self.omeganh1 = omeganh1
        self.omeganh2 = omeganh2
        self.omeganl1 = omeganl1
        self.omeganl2 = omeganl2
        self.th1 = th1
        self.th10 = th10
        self.th11 = th11
        self.th12 = th12
        self.th2 = th2
        self.th3 = th3
        self.th4 = th4
        self.th5 = th5
        self.th6 = th6
        self.th7 = th7
        self.th8 = th8
        self.th9 = th9
        self.ti1 = ti1
        self.ti10 = ti10
        self.ti11 = ti11
        self.ti12 = ti12
        self.ti2 = ti2
        self.ti3 = ti3
        self.ti4 = ti4
        self.ti5 = ti5
        self.ti6 = ti6
        self.ti7 = ti7
        self.ti8 = ti8
        self.ti9 = ti9
        self.tl1 = tl1
        self.tl10 = tl10
        self.tl11 = tl11
        self.tl12 = tl12
        self.tl2 = tl2
        self.tl3 = tl3
        self.tl4 = tl4
        self.tl5 = tl5
        self.tl6 = tl6
        self.tl7 = tl7
        self.tl8 = tl8
        self.tl9 = tl9
        self.vhmax = vhmax
        self.vhmin = vhmin
        self.vimax = vimax
        self.vimin = vimin
        self.vlmax = vlmax
        self.vlmin = vlmin
        self.vstmax = vstmax
        self.vstmin = vstmin
