"""CIM class LoadComposite (TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_dynamics import (
    LoadDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class LoadComposite(LoadDynamics):
    """Combined static load and induction motor load effects.

    The dynamics of the motor are simplified by linearizing the induction machine equations."""

    __slots__ = (
        "epfd",
        "epfs",
        "epvd",
        "epvs",
        "eqfd",
        "eqfs",
        "eqvd",
        "eqvs",
        "h",
        "lfac",
        "pfrac",
    )

    epvs: float | None
    epfs: float | None
    eqvs: float | None
    eqfs: float | None
    epvd: float | None
    epfd: float | None
    eqvd: float | None
    eqfd: float | None
    lfac: float | None
    h: float | None  # Seconds
    pfrac: float | None

    _cim_meta = ClassMeta(
        cim_name="LoadComposite",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics",
        guid="{BDFAC440-3B77-47a6-B8DB-C480D393299F}",
        attributes=(
            AttrMeta("epvs", "epvs", "float", 0, 1, "primitive"),
            AttrMeta("epfs", "epfs", "float", 0, 1, "primitive"),
            AttrMeta("eqvs", "eqvs", "float", 0, 1, "primitive"),
            AttrMeta("eqfs", "eqfs", "float", 0, 1, "primitive"),
            AttrMeta("epvd", "epvd", "float", 0, 1, "primitive"),
            AttrMeta("epfd", "epfd", "float", 0, 1, "primitive"),
            AttrMeta("eqvd", "eqvd", "float", 0, 1, "primitive"),
            AttrMeta("eqfd", "eqfd", "float", 0, 1, "primitive"),
            AttrMeta("lfac", "lfac", "float", 0, 1, "primitive"),
            AttrMeta("h", "h", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("pfrac", "pfrac", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        epvs: float | None = None,
        epfs: float | None = None,
        eqvs: float | None = None,
        eqfs: float | None = None,
        epvd: float | None = None,
        epfd: float | None = None,
        eqvd: float | None = None,
        eqfd: float | None = None,
        lfac: float | None = None,
        h: float | None = None,
        pfrac: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.epvs = epvs
        self.epfs = epfs
        self.eqvs = eqvs
        self.eqfs = eqfs
        self.epvd = epvd
        self.epfd = epfd
        self.eqvd = eqvd
        self.eqfd = eqfd
        self.lfac = lfac
        self.h = h
        self.pfrac = pfrac
