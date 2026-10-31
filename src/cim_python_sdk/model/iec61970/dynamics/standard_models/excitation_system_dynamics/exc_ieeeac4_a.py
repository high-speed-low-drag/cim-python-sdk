"""CIM class ExcIEEEAC4A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEAC4A(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type AC4A model. The model represents type AC4A alternator-supplied
    controlled-rectifier excitation system which is quite different from the other types of
    AC systems. This high initial response excitation system utilizes a full thyristor
    bridge in the exciter output circuit. The voltage regulator controls the firing of the
    thyristor bridges. The exciter alternator uses an independent voltage regulator to
    control its output voltage to a constant value. These effects are not modelled; however,
    transient loading effects on the exciter alternator are included.

    Reference: IEEE 421.5-2005, 6.4."""

    __slots__ = ("ka", "kc", "ta", "tb", "tc", "vimax", "vimin", "vrmax", "vrmin")

    vimax: float | None  # PU
    vimin: float | None  # PU
    tc: float | None  # Seconds
    tb: float | None  # Seconds
    ka: float | None  # PU
    ta: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    kc: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEAC4A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{A19ECF3E-99EC-46c1-A2E0-892E351F1F79}",
        attributes=(
            AttrMeta("vimax", "vimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimin", "vimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        vimax: float | None = None,
        vimin: float | None = None,
        tc: float | None = None,
        tb: float | None = None,
        ka: float | None = None,
        ta: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        kc: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.vimax = vimax
        self.vimin = vimin
        self.tc = tc
        self.tb = tb
        self.ka = ka
        self.ta = ta
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.kc = kc
