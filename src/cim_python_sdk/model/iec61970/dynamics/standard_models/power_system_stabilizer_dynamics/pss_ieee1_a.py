"""CIM class PssIEEE1A (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

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


class PssIEEE1A(PowerSystemStabilizerDynamics):
    """IEEE 421.5-2005 type PSS1A power system stabilizer model. PSS1A is the generalized form
    of a PSS with a single input signal.

    Reference: IEEE 1A 421.5-2005, 8.1."""

    __slots__ = (
        "a1",
        "a2",
        "input_signal_type",
        "ks",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",
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

    _cim_meta = ClassMeta(
        cim_name="PssIEEE1A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{E62CBD96-8B26-4707-8646-1587F7C2476E}",
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
