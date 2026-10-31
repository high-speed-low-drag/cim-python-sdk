"""CIM class TransformerTest (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class TransformerTest(IdentifiedObject):
    """Test result for transformer ends, such as short-circuit, open-circuit (excitation) or
    no-load test."""

    __slots__ = ("base_power", "temperature")

    base_power: float | None  # ApparentPower
    temperature: float | None  # Temperature

    _cim_meta = ClassMeta(
        cim_name="TransformerTest",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{6882227B-F7AD-48fd-A7C6-9C6A08A41979}",
        attributes=(
            AttrMeta("base_power", "basePower", "ApparentPower", 0, 1, "cimdatatype"),
            AttrMeta("temperature", "temperature", "Temperature", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        base_power: float | None = None,
        temperature: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.base_power = base_power
        self.temperature = temperature
