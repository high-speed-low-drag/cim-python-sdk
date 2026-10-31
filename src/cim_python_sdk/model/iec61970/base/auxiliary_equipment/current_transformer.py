"""CIM class CurrentTransformer (TC57CIM/IEC61970/Base/AuxiliaryEquipment). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.auxiliary_equipment.sensor import Sensor

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class CurrentTransformer(Sensor):
    """Instrument transformer used to measure electrical qualities of the circuit that is being
    protected and/or monitored. Typically used as current transducer for the purpose of
    metering or protection. A typical secondary current rating would be 5A."""

    __slots__ = ("accuracy_class", "accuracy_limit", "core_burden", "ct_class", "usage")

    accuracy_class: str | None
    accuracy_limit: float | None  # PerCent
    ct_class: str | None
    usage: str | None
    core_burden: float | None  # ActivePower

    _cim_meta = ClassMeta(
        cim_name="CurrentTransformer",
        package="TC57CIM/IEC61970/Base/AuxiliaryEquipment",
        guid="{24CFE1CD-BFCC-4212-A1F0-CB492DAA61EC}",
        attributes=(
            AttrMeta("accuracy_class", "accuracyClass", "str", 0, 1, "primitive"),
            AttrMeta("accuracy_limit", "accuracyLimit", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("ct_class", "ctClass", "str", 0, 1, "primitive"),
            AttrMeta("usage", "usage", "str", 0, 1, "primitive"),
            AttrMeta("core_burden", "coreBurden", "ActivePower", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        accuracy_class: str | None = None,
        accuracy_limit: float | None = None,
        ct_class: str | None = None,
        usage: str | None = None,
        core_burden: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.accuracy_class = accuracy_class
        self.accuracy_limit = accuracy_limit
        self.ct_class = ct_class
        self.usage = usage
        self.core_burden = core_burden
