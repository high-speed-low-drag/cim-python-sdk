"""CIM class Participation (TC57CIM/IEC62325/InfIEC62325/InfMarketOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Participation(IdentifiedObject):
    """Participation level of a given Pnode in a given AggregatePnode."""

    __slots__ = ("factor",)

    factor: float | None

    _cim_meta = ClassMeta(
        cim_name="Participation",
        package="TC57CIM/IEC62325/InfIEC62325/InfMarketOperations",
        guid="{029E0A30-B136-4cf2-91E5-8DE0DD57F07C}",
        attributes=(AttrMeta("factor", "factor", "float", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        factor: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.factor = factor
