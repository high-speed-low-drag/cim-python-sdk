"""CIM class MktAnalogLimit (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.meas.analog_limit import AnalogLimit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.analog_limit_type import (
        AnalogLimitType,
    )


class MktAnalogLimit(AnalogLimit):
    """Subclass of IEC 61970:Meas:AnalogLimit."""

    __slots__ = ("exceeded_limit", "limit_type")

    exceeded_limit: bool | None
    limit_type: AnalogLimitType | None

    _cim_meta = ClassMeta(
        cim_name="MktAnalogLimit",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{3CCBFC52-897B-40b2-99CD-016915C75A3D}",
        attributes=(
            AttrMeta("exceeded_limit", "exceededLimit", "bool", 0, 1, "primitive"),
            AttrMeta("limit_type", "limitType", "AnalogLimitType", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        exceeded_limit: bool | None = None,
        limit_type: AnalogLimitType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.exceeded_limit = exceeded_limit
        self.limit_type = limit_type
