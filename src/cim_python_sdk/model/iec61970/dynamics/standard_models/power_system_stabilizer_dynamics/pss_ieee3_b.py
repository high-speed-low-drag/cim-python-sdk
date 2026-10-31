"""CIM class PssIEEE3B (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PssIEEE3B(PowerSystemStabilizerDynamics):
    """IEEE 421.5-2005 type PSS3B power system stabilizer model. The PSS model PSS3B has dual
    inputs of electrical power and rotor angular frequency deviation. The signals are used
    to derive an equivalent mechanical power signal.

    This model has 2 input signals. They have the following fixed types (expressed in terms
    of InputSignalKind values): the first one is of rotorAngleFrequencyDeviation type and
    the second one is of generatorElectricalPower type.

    Reference: IEEE 3B 421.5-2005, 8.3."""

    __slots__ = (
        "a1",
        "a2",
        "a3",
        "a4",
        "a5",
        "a6",
        "a7",
        "a8",
        "ks1",
        "ks2",
        "t1",
        "t2",
        "tw1",
        "tw2",
        "tw3",
        "vstmax",
        "vstmin",
    )

    t1: float | None  # Seconds
    t2: float | None  # Seconds
    tw1: float | None  # Seconds
    tw2: float | None  # Seconds
    tw3: float | None  # Seconds
    ks1: float | None  # PU
    ks2: float | None  # PU
    a1: float | None  # PU
    a2: float | None  # PU
    a3: float | None  # PU
    a4: float | None  # PU
    a5: float | None  # PU
    a6: float | None  # PU
    a7: float | None  # PU
    a8: float | None  # PU
    vstmax: float | None  # PU
    vstmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PssIEEE3B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{F7C38135-ADBE-4f67-A7B3-2A7BF378835A}",
        attributes=(
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tw1", "tw1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tw2", "tw2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tw3", "tw3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ks1", "ks1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks2", "ks2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a1", "a1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a2", "a2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a3", "a3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a4", "a4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a5", "a5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a6", "a6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a7", "a7", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a8", "a8", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vstmax", "vstmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vstmin", "vstmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        t1: float | None = None,
        t2: float | None = None,
        tw1: float | None = None,
        tw2: float | None = None,
        tw3: float | None = None,
        ks1: float | None = None,
        ks2: float | None = None,
        a1: float | None = None,
        a2: float | None = None,
        a3: float | None = None,
        a4: float | None = None,
        a5: float | None = None,
        a6: float | None = None,
        a7: float | None = None,
        a8: float | None = None,
        vstmax: float | None = None,
        vstmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.t1 = t1
        self.t2 = t2
        self.tw1 = tw1
        self.tw2 = tw2
        self.tw3 = tw3
        self.ks1 = ks1
        self.ks2 = ks2
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8
        self.vstmax = vstmax
        self.vstmin = vstmin
