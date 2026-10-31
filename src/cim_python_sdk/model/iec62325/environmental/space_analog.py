"""CIM class SpaceAnalog (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.environmental_analog import EnvironmentalAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.env_domain.space_analog_kind import (
        SpaceAnalogKind,
    )


class SpaceAnalog(EnvironmentalAnalog):
    """Analog (float) measuring a space (extra-terrestrial) condition."""

    __slots__ = ("kind",)

    kind: SpaceAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="SpaceAnalog",
        package="TC57CIM/IEC62325/Environmental",
        guid="{218C406A-9E85-4756-BE01-2A5058AE5403}",
        attributes=(AttrMeta("kind", "kind", "SpaceAnalogKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: SpaceAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
