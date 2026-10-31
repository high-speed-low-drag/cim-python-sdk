"""CIM class FrequencyConverter (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.regulating_cond_eq import RegulatingCondEq

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class FrequencyConverter(RegulatingCondEq):
    """A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a
    pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the
    DC to F2."""

    __slots__ = ("frequency", "max_p", "max_u", "min_p", "min_u")

    frequency: float | None  # Frequency
    max_p: float | None  # ActivePower
    max_u: float | None  # Voltage
    min_p: float | None  # ActivePower
    min_u: float | None  # Voltage

    _cim_meta = ClassMeta(
        cim_name="FrequencyConverter",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{CE012E43-26BF-4af0-ABD2-68CA9BB35D60}",
        attributes=(
            AttrMeta("frequency", "frequency", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("max_p", "maxP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_u", "maxU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("min_p", "minP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_u", "minU", "Voltage", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        frequency: float | None = None,
        max_p: float | None = None,
        max_u: float | None = None,
        min_p: float | None = None,
        min_u: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.frequency = frequency
        self.max_p = max_p
        self.max_u = max_u
        self.min_p = min_p
        self.min_u = min_u
