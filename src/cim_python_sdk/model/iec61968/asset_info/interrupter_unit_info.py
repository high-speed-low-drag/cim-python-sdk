"""CIM class InterrupterUnitInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_info.interrupting_medium_kind import (
        InterruptingMediumKind,
    )


class InterrupterUnitInfo(AssetInfo):
    """Interrupter datasheet information."""

    __slots__ = ("interrupting_medium",)

    interrupting_medium: InterruptingMediumKind | None

    _cim_meta = ClassMeta(
        cim_name="InterrupterUnitInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{77A86BCD-E347-4ce5-94F0-155D2B9E579B}",
        attributes=(
            AttrMeta(
                "interrupting_medium",
                "interruptingMedium",
                "InterruptingMediumKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )

    def __init__(
        self,
        *,
        interrupting_medium: InterruptingMediumKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interrupting_medium = interrupting_medium
