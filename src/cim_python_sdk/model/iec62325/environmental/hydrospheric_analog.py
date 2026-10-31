"""CIM class HydrosphericAnalog (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.environmental_analog import EnvironmentalAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.env_domain.hydrospheric_analog_kind import (
        HydrosphericAnalogKind,
    )


class HydrosphericAnalog(EnvironmentalAnalog):
    """Analog (float) measuring a hydrospheric condition."""

    __slots__ = ("kind",)

    kind: HydrosphericAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="HydrosphericAnalog",
        package="TC57CIM/IEC62325/Environmental",
        guid="{0E591614-B81B-4ea6-B1CD-FC9F1637E35C}",
        attributes=(AttrMeta("kind", "kind", "HydrosphericAnalogKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: HydrosphericAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
