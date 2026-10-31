"""CIM class Tornado (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.atmospheric_phenomenon import AtmosphericPhenomenon

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.env_domain.f_scale import FScale


class Tornado(AtmosphericPhenomenon):
    """A tornado, a violent destructive whirling wind accompanied by a funnel-shaped cloud that
    progresses in a narrow path over the land."""

    __slots__ = ("f_scale", "width")

    f_scale: FScale | None
    width: float | None  # Length

    _cim_meta = ClassMeta(
        cim_name="Tornado",
        package="TC57CIM/IEC62325/Environmental",
        guid="{AE09C199-6AF9-4dbf-A4D7-659755174D22}",
        attributes=(
            AttrMeta("f_scale", "fScale", "FScale", 0, 1, "enumeration"),
            AttrMeta("width", "width", "Length", 1, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        f_scale: FScale | None = None,
        width: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.f_scale = f_scale
        self.width = width
