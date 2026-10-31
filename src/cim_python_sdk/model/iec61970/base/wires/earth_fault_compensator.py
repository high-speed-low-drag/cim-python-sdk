"""CIM class EarthFaultCompensator (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class EarthFaultCompensator(ConductingEquipment):
    """A conducting equipment used to represent a connection to ground which is typically used
    to compensate earth faults. An earth fault compensator device modelled with a single
    terminal implies a second terminal solidly connected to ground. If two terminals are
    modelled, the ground is not assumed and normal connection rules apply."""

    __slots__ = ("r",)

    r: float | None  # Resistance

    _cim_meta = ClassMeta(
        cim_name="EarthFaultCompensator",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{99B51F43-C935-4382-AB8A-6352DAB082D4}",
        attributes=(AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        r: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.r = r
