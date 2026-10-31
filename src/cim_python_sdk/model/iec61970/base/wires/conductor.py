"""CIM class Conductor (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Conductor(ConductingEquipment):
    """Combination of conducting material with consistent electrical characteristics, building
    a single electrical system, used to carry current between points in the power system."""

    __slots__ = ("length",)

    length: float | None  # Length

    _cim_meta = ClassMeta(
        cim_name="Conductor",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{C435D1A4-31AE-46ef-BCF8-7932F0785DA9}",
        attributes=(AttrMeta("length", "length", "Length", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        length: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.length = length
