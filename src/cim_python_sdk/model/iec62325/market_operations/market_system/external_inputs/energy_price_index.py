"""CIM class EnergyPriceIndex (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.energy_price_index_type import (
        EnergyPriceIndexType,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )


class EnergyPriceIndex(IdentifiedObject):
    """An Energy Price Index for each Resource is valid for a period (e.g. daily) that is
    identified by a Valid Period Start Time and a Valid Period End Time. An Energy Price
    Index is in $/MWh."""

    __slots__ = (
        "_registered_generator",
        "energy_price_index",
        "energy_price_index_type",
        "last_modified",
        "valid_period",
    )

    energy_price_index: float | None
    energy_price_index_type: EnergyPriceIndexType | None
    last_modified: _dt.datetime | None
    valid_period: DateTimeInterval | None

    registered_generator: One[RegisteredGenerator] = One(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=False,
            lower=1,
            upper=1,
            inverse="energy_price_index",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyPriceIndex",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{63BC381D-F1F5-4881-9543-DFE3E000878E}",
        attributes=(
            AttrMeta("energy_price_index", "energyPriceIndex", "float", 0, 1, "primitive"),
            AttrMeta(
                "energy_price_index_type",
                "energyPriceIndexType",
                "EnergyPriceIndexType",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("last_modified", "lastModified", "datetime", 0, 1, "primitive"),
            AttrMeta("valid_period", "validPeriod", "DateTimeInterval", 0, 1, "compound"),
        ),
        ends=(registered_generator.meta,),
    )

    def __init__(
        self,
        *,
        energy_price_index: float | None = None,
        energy_price_index_type: EnergyPriceIndexType | None = None,
        last_modified: _dt.datetime | None = None,
        valid_period: DateTimeInterval | None = None,
        registered_generator: RegisteredGenerator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.energy_price_index = energy_price_index
        self.energy_price_index_type = energy_price_index_type
        self.last_modified = last_modified
        self.valid_period = valid_period
        if registered_generator is not None:
            self.registered_generator = registered_generator
