"""CIM class Hurricane (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.cyclone import Cyclone

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Hurricane(Cyclone):
    """A hurricane, a subtype of cyclone occurring in the North Atlantic Ocean or North-eastern
    Pacific Ocean whose intensity is measured using the Saffir-Simpson Hurricane Scale."""

    __slots__ = ("category",)

    category: int | None

    _cim_meta = ClassMeta(
        cim_name="Hurricane",
        package="TC57CIM/IEC62325/Environmental",
        guid="{078BAC7C-F2F4-4b92-9819-A4B0A9B51AFA}",
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
