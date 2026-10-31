"""CIM class ExcIEEEST5B (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEST5B(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type ST5B model. The type ST5B excitation system is a variation of the
    type ST1A model, with alternative overexcitation and underexcitation inputs and
    additional limits.

    The block diagram in the IEEE 421.5 standard has input signal Vc and does not indicate
    the summation point with Vref. The implementation of the ExcIEEEST5B shall consider
    summation point with Vref.

    Reference: IEEE 421.5-2005, 7.5."""

    __slots__ = (
        "kc",
        "kr",
        "t1",
        "tb1",
        "tb2",
        "tc1",
        "tc2",
        "tob1",
        "tob2",
        "toc1",
        "toc2",
        "tub1",
        "tub2",
        "tuc1",
        "tuc2",
        "vrmax",
        "vrmin",
    )

    kr: float | None  # PU
    t1: float | None  # Seconds
    kc: float | None  # PU
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    tc1: float | None  # Seconds
    tb1: float | None  # Seconds
    tc2: float | None  # Seconds
    tb2: float | None  # Seconds
    toc1: float | None  # Seconds
    tob1: float | None  # Seconds
    toc2: float | None  # Seconds
    tob2: float | None  # Seconds
    tuc1: float | None  # Seconds
    tub1: float | None  # Seconds
    tuc2: float | None  # Seconds
    tub2: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEST5B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{A3248F33-3B25-4879-9B29-C0E09FAF8695}",
        attributes=(
            AttrMeta("kr", "kr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tc1", "tc1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb1", "tb1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc2", "tc2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb2", "tb2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("toc1", "toc1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tob1", "tob1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("toc2", "toc2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tob2", "tob2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tuc1", "tuc1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tub1", "tub1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tuc2", "tuc2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tub2", "tub2", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        kr: float | None = None,
        t1: float | None = None,
        kc: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        tc1: float | None = None,
        tb1: float | None = None,
        tc2: float | None = None,
        tb2: float | None = None,
        toc1: float | None = None,
        tob1: float | None = None,
        toc2: float | None = None,
        tob2: float | None = None,
        tuc1: float | None = None,
        tub1: float | None = None,
        tuc2: float | None = None,
        tub2: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kr = kr
        self.t1 = t1
        self.kc = kc
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.tc1 = tc1
        self.tb1 = tb1
        self.tc2 = tc2
        self.tb2 = tb2
        self.toc1 = toc1
        self.tob1 = tob1
        self.toc2 = toc2
        self.tob2 = tob2
        self.tuc1 = tuc1
        self.tub1 = tub1
        self.tuc2 = tuc2
        self.tub2 = tub2
