"""CIM class Facility (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from tests.runtime.minimodel.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Facility(Asset):
    """A facility may contain buildings, storage facilities, switching facilities, etc."""

    __slots__ = ()

    # overrides Asset.kind (AssetKind) with an incompatible type
    kind: str | None  # type: ignore[assignment]

    _cim_meta = ClassMeta(
        cim_name="Facility",
        package="TC57CIM/IEC61968/Assets",
        guid="{00000000-0000-0000-0000-00000000C006}",
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
