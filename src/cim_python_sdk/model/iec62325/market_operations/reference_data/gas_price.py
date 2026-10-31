"""CIM class GasPrice (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.fuel_region import (
        FuelRegion,
    )


class GasPrice(CimObject):
    """Price of gas in monetary units."""

    __slots__ = ("_fuel_region", "gas_price_index")

    gas_price_index: float | None

    fuel_region: One[FuelRegion] = One(
        EndMeta(
            name="fuel_region",
            cim_role="FuelRegion",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.fuel_region:FuelRegion",
            many=False,
            lower=1,
            upper=1,
            inverse="gas_price",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GasPrice",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{EDD07EC7-2D92-44a4-B07F-EDF75A6C744E}",
        attributes=(AttrMeta("gas_price_index", "gasPriceIndex", "float", 0, 1, "primitive"),),
        ends=(fuel_region.meta,),
    )

    def __init__(
        self,
        *,
        gas_price_index: float | None = None,
        fuel_region: FuelRegion | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.gas_price_index = gas_price_index
        if fuel_region is not None:
            self.fuel_region = fuel_region
