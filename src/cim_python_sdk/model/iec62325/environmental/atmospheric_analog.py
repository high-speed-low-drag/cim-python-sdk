"""CIM class AtmosphericAnalog (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.environmental_analog import EnvironmentalAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.env_domain.atmospheric_analog_kind import (
        AtmosphericAnalogKind,
    )


class AtmosphericAnalog(EnvironmentalAnalog):
    """Analog (float) measuring an atmospheric condition."""

    __slots__ = ("kind",)

    kind: AtmosphericAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="AtmosphericAnalog",
        package="TC57CIM/IEC62325/Environmental",
        guid="{0EE3CCDF-F8A8-42d5-9B94-142D58F87739}",
        attributes=(AttrMeta("kind", "kind", "AtmosphericAnalogKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: AtmosphericAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
