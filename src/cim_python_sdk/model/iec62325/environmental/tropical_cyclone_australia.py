"""CIM class TropicalCycloneAustralia (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.cyclone import Cyclone

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class TropicalCycloneAustralia(Cyclone):
    """A tropical cyclone, a subtype of cyclone that forms to the east of 90°E in the Southern
    Hemisphere whose intensity is measured by the Australian tropical cyclone intensity
    scale."""

    __slots__ = ("category",)

    category: int | None

    _cim_meta = ClassMeta(
        cim_name="TropicalCycloneAustralia",
        package="TC57CIM/IEC62325/Environmental",
        guid="{C5570427-A052-4f94-85C3-410D6F383BEB}",
        attributes=(AttrMeta("category", "category", "int", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        category: int | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.category = category
