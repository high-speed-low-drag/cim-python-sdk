"""CIM class DiscExcContIEEEDEC3A (TC57CIM/IEC61970/Dynamics/StandardModels/DiscontinuousExcitationControlDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.discontinuous_excitation_control_dynamics.discontinuous_excitation_control_dynamics import (
    DiscontinuousExcitationControlDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
    """IEEE type DEC3A model. In some systems, the stabilizer output is disconnected from the
    regulator immediately following a severe fault to prevent the stabilizer from competing
    with action of voltage regulator during the first swing.

    Reference: IEEE 421.5-2005 12.4."""

    __slots__ = ("tdr", "vtmin")

    vtmin: float | None  # PU
    tdr: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="DiscExcContIEEEDEC3A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/DiscontinuousExcitationControlDynamics",
        guid="{7D872155-7DE6-4dab-93A2-294AEC702FEB}",
        attributes=(
            AttrMeta("vtmin", "vtmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tdr", "tdr", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        vtmin: float | None = None,
        tdr: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.vtmin = vtmin
        self.tdr = tdr
