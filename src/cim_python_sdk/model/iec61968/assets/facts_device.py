"""CIM class FACTSDevice (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.facts_device_kind import (
        FACTSDeviceKind,
    )


class FACTSDevice(Asset):
    """FACTS device asset."""

    __slots__ = ()

    kind: FACTSDeviceKind | None  # type: ignore[assignment]

    _cim_meta = ClassMeta(
        cim_name="FACTSDevice",
        package="TC57CIM/IEC61968/Assets",
        guid="{72F6944F-86AC-4777-B060-132006C88993}",
        attributes=(AttrMeta("kind", "kind", "FACTSDeviceKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: FACTSDeviceKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
