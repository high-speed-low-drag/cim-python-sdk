"""CIM class OilPrice (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.fuel_region import (
        FuelRegion,
    )


class OilPrice(CimObject):
    """Price of oil in monetary units."""

    __slots__ = ("_fuel_region", "oil_price_index")

    oil_price_index: float | None

    fuel_region: One[FuelRegion] = One(
        EndMeta(
            name="fuel_region",
            cim_role="FuelRegion",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.fuel_region:FuelRegion",
            many=False,
            lower=1,
            upper=1,
            inverse="oil_price",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OilPrice",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{5BA9F9A4-622A-41b1-8951-811C4BC9E8DC}",
        attributes=(AttrMeta("oil_price_index", "oilPriceIndex", "float", 0, 1, "primitive"),),
        ends=(fuel_region.meta,),
    )

    def __init__(
        self,
        *,
        oil_price_index: float | None = None,
        fuel_region: FuelRegion | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.oil_price_index = oil_price_index
        if fuel_region is not None:
            self.fuel_region = fuel_region
