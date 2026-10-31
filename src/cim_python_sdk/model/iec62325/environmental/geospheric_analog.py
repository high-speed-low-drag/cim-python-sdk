"""CIM class GeosphericAnalog (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.environmental_analog import EnvironmentalAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.env_domain.geospheric_analog_kind import (
        GeosphericAnalogKind,
    )


class GeosphericAnalog(EnvironmentalAnalog):
    """Analog (float) measuring a geospheric condition."""

    __slots__ = ("kind",)

    kind: GeosphericAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="GeosphericAnalog",
        package="TC57CIM/IEC62325/Environmental",
        guid="{5617575E-DF8A-4109-AD72-E263516214C8}",
        attributes=(AttrMeta("kind", "kind", "GeosphericAnalogKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: GeosphericAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
