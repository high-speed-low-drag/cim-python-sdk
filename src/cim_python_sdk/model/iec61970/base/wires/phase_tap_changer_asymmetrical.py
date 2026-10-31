"""CIM class PhaseTapChangerAsymmetrical (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.phase_tap_changer_non_linear import (
    PhaseTapChangerNonLinear,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PhaseTapChangerAsymmetrical(PhaseTapChangerNonLinear):
    """Describes the tap model for an asymmetrical phase shifting transformer in which the
    difference voltage vector adds to the in-phase winding. The out-of-phase winding is the
    transformer end where the tap changer is located. The angle between the in-phase and
    out-of-phase windings is named the winding connection angle. The phase shift depends on
    both the difference voltage magnitude and the winding connection angle."""

    __slots__ = ("winding_connection_angle",)

    winding_connection_angle: float | None  # AngleDegrees

    _cim_meta = ClassMeta(
        cim_name="PhaseTapChangerAsymmetrical",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{4161A809-7542-4c92-A7D0-99AE5682E89C}",
        attributes=(
            AttrMeta(
                "winding_connection_angle",
                "windingConnectionAngle",
                "AngleDegrees",
                0,
                1,
                "cimdatatype",
            ),
        ),
    )

    def __init__(
        self,
        *,
        winding_connection_angle: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.winding_connection_angle = winding_connection_angle
