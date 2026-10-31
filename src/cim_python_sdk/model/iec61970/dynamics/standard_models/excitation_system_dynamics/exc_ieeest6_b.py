"""CIM class ExcIEEEST6B (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.exc_st6_boe_lselector_kind import (
        ExcST6BOELselectorKind,
    )


class ExcIEEEST6B(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type ST6B model. This model consists of a PI voltage regulator with an
    inner loop field voltage regulator and pre-control. The field voltage regulator
    implements a proportional control. The pre-control and the delay in the feedback circuit
    increase the dynamic response.

    Reference: IEEE 421.5-2005, 7.6."""

    __slots__ = (
        "ilr",
        "kci",
        "kff",
        "kg",
        "kia",
        "klr",
        "km",
        "kpa",
        "oelin",
        "tg",
        "vamax",
        "vamin",
        "vrmax",
        "vrmin",
    )

    ilr: float | None  # PU
    kci: float | None  # PU
    kff: float | None  # PU
    kg: float | None  # PU
    kia: float | None  # PU
    klr: float | None  # PU
    km: float | None  # PU
    kpa: float | None  # PU
    oelin: ExcST6BOELselectorKind | None
    tg: float | None  # Seconds
    vamax: float | None  # PU
    vamin: float | None  # PU
    vrmax: float | None  # PU
    vrmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEST6B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{7A625070-2B4A-48c0-BB20-C7C7DD709BC5}",
        attributes=(
            AttrMeta("ilr", "ilr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kci", "kci", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kff", "kff", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kg", "kg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kia", "kia", "PU", 0, 1, "cimdatatype"),
            AttrMeta("klr", "klr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("km", "km", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpa", "kpa", "PU", 0, 1, "cimdatatype"),
            AttrMeta("oelin", "oelin", "ExcST6BOELselectorKind", 0, 1, "enumeration"),
            AttrMeta("tg", "tg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ilr: float | None = None,
        kci: float | None = None,
        kff: float | None = None,
        kg: float | None = None,
        kia: float | None = None,
        klr: float | None = None,
        km: float | None = None,
        kpa: float | None = None,
        oelin: ExcST6BOELselectorKind | None = None,
        tg: float | None = None,
        vamax: float | None = None,
        vamin: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ilr = ilr
        self.kci = kci
        self.kff = kff
        self.kg = kg
        self.kia = kia
        self.klr = klr
        self.km = km
        self.kpa = kpa
        self.oelin = oelin
        self.tg = tg
        self.vamax = vamax
        self.vamin = vamin
        self.vrmax = vrmax
        self.vrmin = vrmin
