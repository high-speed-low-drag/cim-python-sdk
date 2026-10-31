"""CIM class PotentialTransformer (TC57CIM/IEC61970/Base/AuxiliaryEquipment). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.auxiliary_equipment.sensor import Sensor

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.auxiliary_equipment.potential_transformer_kind import (
        PotentialTransformerKind,
    )


class PotentialTransformer(Sensor):
    """Instrument transformer (also known as Voltage Transformer) used to measure electrical
    qualities of the circuit that is being protected and/or monitored. Typically used as
    voltage transducer for the purpose of metering, protection, or sometimes auxiliary
    substation supply. A typical secondary voltage rating would be 120V."""

    __slots__ = ("accuracy_class", "nominal_ratio", "pt_class", "type")

    accuracy_class: str | None
    nominal_ratio: float | None
    pt_class: str | None
    type: PotentialTransformerKind | None

    _cim_meta = ClassMeta(
        cim_name="PotentialTransformer",
        package="TC57CIM/IEC61970/Base/AuxiliaryEquipment",
        guid="{C23E2611-BCD6-4bba-8700-0FE573038340}",
        attributes=(
            AttrMeta("accuracy_class", "accuracyClass", "str", 0, 1, "primitive"),
            AttrMeta("nominal_ratio", "nominalRatio", "float", 0, 1, "primitive"),
            AttrMeta("pt_class", "ptClass", "str", 0, 1, "primitive"),
            AttrMeta("type", "type", "PotentialTransformerKind", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        accuracy_class: str | None = None,
        nominal_ratio: float | None = None,
        pt_class: str | None = None,
        type: PotentialTransformerKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.accuracy_class = accuracy_class
        self.nominal_ratio = nominal_ratio
        self.pt_class = pt_class
        self.type = type
