"""CIM class ExcBBC (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcBBC(ExcitationSystemDynamics):
    """Transformer fed static excitation system (static with ABB regulator). This model
    represents a static excitation system in which a gated thyristor bridge fed by a
    transformer at the main generator terminals feeds the main generator directly."""

    __slots__ = ("efdmax", "efdmin", "k", "switch", "t1", "t2", "t3", "t4", "vrmax", "vrmin", "xe")

    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    k: float | None  # PU
    vrmin: float | None  # PU
    vrmax: float | None  # PU
    efdmin: float | None  # PU
    efdmax: float | None  # PU
    xe: float | None  # PU
    switch: bool | None

    _cim_meta = ClassMeta(
        cim_name="ExcBBC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{A44053E0-AE0F-4cf5-A19C-801DB19B2563}",
        attributes=(
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdmin", "efdmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdmax", "efdmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xe", "xe", "PU", 0, 1, "cimdatatype"),
            AttrMeta("switch", "switch", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        k: float | None = None,
        vrmin: float | None = None,
        vrmax: float | None = None,
        efdmin: float | None = None,
        efdmax: float | None = None,
        xe: float | None = None,
        switch: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.k = k
        self.vrmin = vrmin
        self.vrmax = vrmax
        self.efdmin = efdmin
        self.efdmax = efdmax
        self.xe = xe
        self.switch = switch
