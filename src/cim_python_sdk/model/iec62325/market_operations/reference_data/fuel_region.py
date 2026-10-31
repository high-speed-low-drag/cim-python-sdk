"""CIM class FuelRegion (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.gas_price import GasPrice
    from cim_python_sdk.model.iec62325.market_operations.reference_data.oil_price import OilPrice
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class FuelRegion(IdentifiedObject):
    """Indication of region for fuel inventory purposes."""

    __slots__ = (
        "_gas_price",
        "_oil_price",
        "_registered_generator",
        "_rto",
        "fuel_region_type",
        "last_modified",
    )

    fuel_region_type: str | None
    last_modified: _dt.datetime | None

    gas_price: One[GasPrice] = One(
        EndMeta(
            name="gas_price",
            cim_role="GasPrice",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.gas_price:GasPrice",
            many=False,
            lower=1,
            upper=1,
            inverse="fuel_region",
            aggregation="none",
        )
    )
    registered_generator: Many[RegisteredGenerator] = Many(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=True,
            lower=0,
            upper=None,
            inverse="fuel_region",
            aggregation="none",
        )
    )
    oil_price: One[OilPrice] = One(
        EndMeta(
            name="oil_price",
            cim_role="OilPrice",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.oil_price:OilPrice",
            many=False,
            lower=1,
            upper=1,
            inverse="fuel_region",
            aggregation="none",
        )
    )
    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=1,
            upper=1,
            inverse="fuel_region",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FuelRegion",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{E8B08844-9549-4af2-BBD2-59B663583982}",
        attributes=(
            AttrMeta("fuel_region_type", "fuelRegionType", "str", 0, 1, "primitive"),
            AttrMeta("last_modified", "lastModified", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            gas_price.meta,
            registered_generator.meta,
            oil_price.meta,
            rto.meta,
        ),
    )

    def __init__(
        self,
        *,
        fuel_region_type: str | None = None,
        last_modified: _dt.datetime | None = None,
        gas_price: GasPrice | None = None,
        registered_generator: Iterable[RegisteredGenerator] | None = None,
        oil_price: OilPrice | None = None,
        rto: RTO | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.fuel_region_type = fuel_region_type
        self.last_modified = last_modified
        if gas_price is not None:
            self.gas_price = gas_price
        if registered_generator is not None:
            FuelRegion.registered_generator.extend(self, registered_generator)
        if oil_price is not None:
            self.oil_price = oil_price
        if rto is not None:
            self.rto = rto

    def add_registered_generator(self, registered_generator: RegisteredGenerator) -> Self:
        return FuelRegion.registered_generator.add(self, registered_generator)

    def remove_registered_generator(self, registered_generator: RegisteredGenerator) -> Self:
        return FuelRegion.registered_generator.remove(self, registered_generator)

    def clear_registered_generator(self) -> Self:
        return FuelRegion.registered_generator.clear(self)

    def num_registered_generator(self) -> int:
        return FuelRegion.registered_generator.count(self)

    def get_registered_generator_by_mrid(self, mrid: str) -> RegisteredGenerator | None:
        return FuelRegion.registered_generator.get_by_mrid(self, mrid)
