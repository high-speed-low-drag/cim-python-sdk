"""CIM class BasePower (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class BasePower(IdentifiedObject):
    """The BasePower class defines the base power used in the per unit calculations."""

    __slots__ = ("base_power",)

    base_power: float | None  # ApparentPower

    _cim_meta = ClassMeta(
        cim_name="BasePower",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{A10836E5-09FC-4862-B3C3-96D52298E21B}",
        attributes=(AttrMeta("base_power", "basePower", "ApparentPower", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        base_power: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.base_power = base_power
