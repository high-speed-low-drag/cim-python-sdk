"""CIM class SecurityConstraintsClearing (TC57CIM/IEC62325/InfIEC62325/InfMarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from typing import Any


class SecurityConstraintsClearing(MarketFactors):
    """Binding security constrained clearing results posted for a given settlement period."""

    __slots__ = ("mw_flow", "mw_limit", "shadow_price")

    mw_limit: float | None  # ActivePower
    mw_flow: float | None  # ActivePower
    shadow_price: _decimal.Decimal | None  # Money

    _cim_meta = ClassMeta(
        cim_name="SecurityConstraintsClearing",
        package="TC57CIM/IEC62325/InfIEC62325/InfMarketResults",
        guid="{3B989922-47C7-4a9e-A793-83B152C727B3}",
        attributes=(
            AttrMeta("mw_limit", "mwLimit", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("mw_flow", "mwFlow", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("shadow_price", "shadowPrice", "Money", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mw_limit: float | None = None,
        mw_flow: float | None = None,
        shadow_price: _decimal.Decimal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mw_limit = mw_limit
        self.mw_flow = mw_flow
        self.shadow_price = shadow_price
