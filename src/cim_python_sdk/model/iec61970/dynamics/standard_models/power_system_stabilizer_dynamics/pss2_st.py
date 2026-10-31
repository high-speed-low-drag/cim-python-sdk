"""CIM class Pss2ST (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

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


class Pss2ST(PowerSystemStabilizerDynamics):
    """PTI microprocessor-based stabilizer type 1."""

    __slots__ = (
        "input_signal1_type",
        "input_signal2_type",
        "k1",
        "k2",
        "lsmax",
        "lsmin",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",
        "t7",
        "t8",
        "t9",
        "t10",
        "vcl",
        "vcu",
    )

    input_signal1_type: InputSignalKind | None
    input_signal2_type: InputSignalKind | None
    k1: float | None  # PU
    k2: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    t5: float | None  # Seconds
    t6: float | None  # Seconds
    t7: float | None  # Seconds
    t8: float | None  # Seconds
    t9: float | None  # Seconds
    t10: float | None  # Seconds
    lsmax: float | None  # PU
    lsmin: float | None  # PU
    vcu: float | None  # PU
    vcl: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="Pss2ST",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{499441DD-F189-4833-9878-B0179B101011}",
        attributes=(
            AttrMeta(
                "input_signal1_type", "inputSignal1Type", "InputSignalKind", 0, 1, "enumeration"
            ),
            AttrMeta(
                "input_signal2_type", "inputSignal2Type", "InputSignalKind", 0, 1, "enumeration"
            ),
            AttrMeta("k1", "k1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k2", "k2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t7", "t7", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t8", "t8", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t9", "t9", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t10", "t10", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("lsmax", "lsmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("lsmin", "lsmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vcu", "vcu", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vcl", "vcl", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        input_signal1_type: InputSignalKind | None = None,
        input_signal2_type: InputSignalKind | None = None,
        k1: float | None = None,
        k2: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        t5: float | None = None,
        t6: float | None = None,
        t7: float | None = None,
        t8: float | None = None,
        t9: float | None = None,
        t10: float | None = None,
        lsmax: float | None = None,
        lsmin: float | None = None,
        vcu: float | None = None,
        vcl: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.input_signal1_type = input_signal1_type
        self.input_signal2_type = input_signal2_type
        self.k1 = k1
        self.k2 = k2
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8
        self.t9 = t9
        self.t10 = t10
        self.lsmax = lsmax
        self.lsmin = lsmin
        self.vcu = vcu
        self.vcl = vcl
