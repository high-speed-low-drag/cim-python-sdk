"""CIM class Pss1A (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.input_signal_kind import (
        InputSignalKind,
    )


class Pss1A(PowerSystemStabilizerDynamics):
    """Single input power system stabilizer. It is a modified version in order to allow
    representation of various vendors' implementations on PSS type 1A."""

    __slots__ = (
        "a1",
        "a2",
        "a3",
        "a4",
        "a5",
        "a6",
        "a7",
        "a8",
        "input_signal_type",
        "kd",
        "ks",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",
        "tdelay",
        "vcl",
        "vcu",
        "vrmax",
        "vrmin",
    )

    input_signal_type: InputSignalKind | None
    a1: float | None  # PU
    a2: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    t5: float | None  # Seconds
    t6: float | None  # Seconds
    ks: float | None  # PU
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    vcu: float | None  # PU
    vcl: float | None  # PU
    a3: float | None  # PU
    a4: float | None  # PU
    a5: float | None  # PU
    a6: float | None  # PU
    a7: float | None  # PU
    a8: float | None  # PU
    kd: bool | None
    tdelay: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="Pss1A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{90B120AE-6659-477b-821A-516EE39E9EDD}",
        attributes=(
            AttrMeta(
                "input_signal_type", "inputSignalType", "InputSignalKind", 0, 1, "enumeration"
            ),
            AttrMeta("a1", "a1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a2", "a2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vcu", "vcu", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vcl", "vcl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a3", "a3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a4", "a4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a5", "a5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a6", "a6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a7", "a7", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a8", "a8", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "bool", 0, 1, "primitive"),
            AttrMeta("tdelay", "tdelay", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        input_signal_type: InputSignalKind | None = None,
        a1: float | None = None,
        a2: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        t5: float | None = None,
        t6: float | None = None,
        ks: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        vcu: float | None = None,
        vcl: float | None = None,
        a3: float | None = None,
        a4: float | None = None,
        a5: float | None = None,
        a6: float | None = None,
        a7: float | None = None,
        a8: float | None = None,
        kd: bool | None = None,
        tdelay: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.input_signal_type = input_signal_type
        self.a1 = a1
        self.a2 = a2
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.ks = ks
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.vcu = vcu
        self.vcl = vcl
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8
        self.kd = kd
        self.tdelay = tdelay
