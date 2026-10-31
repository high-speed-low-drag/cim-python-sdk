"""CIM class Facility (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_container import AssetContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Facility(AssetContainer):
    """A facility may contain buildings, storage facilities, switching facilities, power
    generation, manufacturing facilities, maintenance facilities, etc."""

    __slots__ = ()

    # overrides Asset.kind (AssetKind) with an incompatible type
    kind: str | None  # type: ignore[assignment]

    _cim_meta = ClassMeta(
        cim_name="Facility",
        package="TC57CIM/IEC61968/Assets",
        guid="{ABD0F5AB-6E76-47cc-AB57-87BF50E45DDF}",
        attributes=(AttrMeta("kind", "kind", "str", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        kind: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
