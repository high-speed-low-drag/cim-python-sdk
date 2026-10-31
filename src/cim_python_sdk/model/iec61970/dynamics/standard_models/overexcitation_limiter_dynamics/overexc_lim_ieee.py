"""CIM class OverexcLimIEEE (TC57CIM/IEC61970/Dynamics/StandardModels/OverexcitationLimiterDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.overexcitation_limiter_dynamics.overexcitation_limiter_dynamics import (
    OverexcitationLimiterDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class OverexcLimIEEE(OverexcitationLimiterDynamics):
    """The over excitation limiter model is intended to represent the significant features of
    OELs necessary for some large-scale system studies. It is the result of a pragmatic
    approach to obtain a model that can be widely applied with attainable data from
    generator owners. An attempt to include all variations in the functionality of OELs and
    duplicate how they interact with the rest of the excitation systems would likely result
    in a level of application insufficient for the studies for which they are intended.

    Reference: IEEE OEL 421.5-2005, 9."""

    __slots__ = ("hyst", "ifdlim", "ifdmax", "itfpu", "kcd", "kramp")

    itfpu: float | None  # PU
    ifdmax: float | None  # PU
    ifdlim: float | None  # PU
    hyst: float | None  # PU
    kcd: float | None  # PU
    kramp: float | None

    _cim_meta = ClassMeta(
        cim_name="OverexcLimIEEE",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/OverexcitationLimiterDynamics",
        guid="{123E0D03-692E-4567-A697-C64C50ABA7C7}",
        attributes=(
            AttrMeta("itfpu", "itfpu", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ifdmax", "ifdmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ifdlim", "ifdlim", "PU", 0, 1, "cimdatatype"),
            AttrMeta("hyst", "hyst", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kcd", "kcd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kramp", "kramp", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        itfpu: float | None = None,
        ifdmax: float | None = None,
        ifdlim: float | None = None,
        hyst: float | None = None,
        kcd: float | None = None,
        kramp: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.itfpu = itfpu
        self.ifdmax = ifdmax
        self.ifdlim = ifdlim
        self.hyst = hyst
        self.kcd = kcd
        self.kramp = kramp
