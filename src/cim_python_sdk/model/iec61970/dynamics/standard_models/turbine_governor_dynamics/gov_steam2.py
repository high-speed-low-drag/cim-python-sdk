"""CIM class GovSteam2 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovSteam2(TurbineGovernorDynamics):
    """Simplified governor."""

    __slots__ = ("dbf", "k", "mnef", "mxef", "pmax", "pmin", "t1", "t2")

    k: float | None
    dbf: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    pmax: float | None  # PU
    pmin: float | None  # PU
    mxef: float | None  # PU
    mnef: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovSteam2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{21648324-C0D1-4125-855B-CCCA46600E7B}",
        attributes=(
            AttrMeta("k", "k", "float", 0, 1, "primitive"),
            AttrMeta("dbf", "dbf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mxef", "mxef", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mnef", "mnef", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        k: float | None = None,
        dbf: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        pmax: float | None = None,
        pmin: float | None = None,
        mxef: float | None = None,
        mnef: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.k = k
        self.dbf = dbf
        self.t1 = t1
        self.t2 = t2
        self.pmax = pmax
        self.pmin = pmin
        self.mxef = mxef
        self.mnef = mnef
