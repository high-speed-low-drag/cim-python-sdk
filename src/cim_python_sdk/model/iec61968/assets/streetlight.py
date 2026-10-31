"""CIM class Streetlight (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.assets.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.pole import Pole
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.streetlight_lamp_kind import (
        StreetlightLampKind,
    )


class Streetlight(Asset):
    """Streetlight asset."""

    __slots__ = ("_pole", "arm_length", "lamp_kind", "light_rating")

    light_rating: float | None  # ActivePower
    lamp_kind: StreetlightLampKind | None
    arm_length: float | None  # Length

    pole: One[Pole] = One(
        EndMeta(
            name="pole",
            cim_role="Pole",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.pole:Pole",
            many=False,
            lower=0,
            upper=1,
            inverse="streetlights",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Streetlight",
        package="TC57CIM/IEC61968/Assets",
        guid="{265BB5FA-D760-4500-BDD8-734847324F48}",
        attributes=(
            AttrMeta("light_rating", "lightRating", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("lamp_kind", "lampKind", "StreetlightLampKind", 0, 1, "enumeration"),
            AttrMeta("arm_length", "armLength", "Length", 0, 1, "cimdatatype"),
        ),
        ends=(pole.meta,),
    )

    def __init__(
        self,
        *,
        light_rating: float | None = None,
        lamp_kind: StreetlightLampKind | None = None,
        arm_length: float | None = None,
        pole: Pole | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.light_rating = light_rating
        self.lamp_kind = lamp_kind
        self.arm_length = arm_length
        if pole is not None:
            self.pole = pole
