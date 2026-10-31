"""CIM class MktAnalogLimitSet (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.meas.analog_limit_set import AnalogLimitSet

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class MktAnalogLimitSet(AnalogLimitSet):
    """Subclass of IEC 61970:Meas:AnalogLimitSet."""

    __slots__ = ("rating_set",)

    rating_set: int | None

    _cim_meta = ClassMeta(
        cim_name="MktAnalogLimitSet",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{A1AC7965-7C94-45e1-B94C-207E6AA9A604}",
        attributes=(AttrMeta("rating_set", "ratingSet", "int", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        rating_set: int | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rating_set = rating_set
