"""CIM class GroundingImpedance (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.earth_fault_compensator import EarthFaultCompensator

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GroundingImpedance(EarthFaultCompensator):
    """A fixed impedance device used for grounding."""

    __slots__ = ("x",)

    x: float | None  # Reactance

    _cim_meta = ClassMeta(
        cim_name="GroundingImpedance",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{5E278FF4-B19F-4c63-8AA5-5DE09E2586DA}",
        attributes=(AttrMeta("x", "x", "Reactance", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        x: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.x = x
