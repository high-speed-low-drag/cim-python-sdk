"""CIM class CommodityPrice (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval
    from cim_python_sdk.model.iec62325.market_operations.market_plan.commodity_definition import (
        CommodityDefinition,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pnode_clearing import (
        PnodeClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.price_descriptor import (
        PriceDescriptor,
    )


class CommodityPrice(CimObject):
    """The CommodityPrice class is used to define the price of a commodity during a given time
    interval. The interval may be long, e.g. a year, or very short, e.g. 5 minutes. There
    will be many instances of the CommodityPrice class for each instance of the
    CommodityDefinition to which it is associated. Note that there may be more than once
    price associated with a given interval and these variances are described by the
    association (or associations) with the PriceDescriptor class."""

    __slots__ = (
        "_commodity_definition",
        "_pnode_clearing",
        "_price_descriptor",
        "time_interval_period",
        "value",
    )

    time_interval_period: DateTimeInterval | None
    value: float | None

    price_descriptor: One[PriceDescriptor] = One(
        EndMeta(
            name="price_descriptor",
            cim_role="PriceDescriptor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.price_descriptor:PriceDescriptor",
            many=False,
            lower=1,
            upper=1,
            inverse="commodity_price",
            aggregation="none",
        )
    )
    pnode_clearing: One[PnodeClearing] = One(
        EndMeta(
            name="pnode_clearing",
            cim_role="PnodeClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pnode_clearing:PnodeClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="commodity_price",
            aggregation="none",
        )
    )
    commodity_definition: One[CommodityDefinition] = One(
        EndMeta(
            name="commodity_definition",
            cim_role="CommodityDefinition",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.commodity_definition:CommodityDefinition",
            many=False,
            lower=1,
            upper=1,
            inverse="commodity_price",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CommodityPrice",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{968B606D-5FCF-4d80-86A4-66E5C19020BE}",
        attributes=(
            AttrMeta(
                "time_interval_period", "timeIntervalPeriod", "DateTimeInterval", 0, 1, "compound"
            ),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
        ends=(
            price_descriptor.meta,
            pnode_clearing.meta,
            commodity_definition.meta,
        ),
    )

    def __init__(
        self,
        *,
        time_interval_period: DateTimeInterval | None = None,
        value: float | None = None,
        price_descriptor: PriceDescriptor | None = None,
        pnode_clearing: PnodeClearing | None = None,
        commodity_definition: CommodityDefinition | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.time_interval_period = time_interval_period
        self.value = value
        if price_descriptor is not None:
            self.price_descriptor = price_descriptor
        if pnode_clearing is not None:
            self.pnode_clearing = pnode_clearing
        if commodity_definition is not None:
            self.commodity_definition = commodity_definition
