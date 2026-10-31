"""CIM class ResourceCapacity (TC57CIM/IEC62325/MarketCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol
    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.resource_capacity_type import (
        ResourceCapacityType,
    )


class ResourceCapacity(CimObject):
    """This class model the various capacities of a resource. A resource may have numbers of
    capacities related to operating, ancillary services, energy trade and so forth.
    Capacities may be defined for active power or reactive power."""

    __slots__ = (
        "_registered_resource",
        "capacity_type",
        "default_capacity",
        "maximum_capacity",
        "minimum_capacity",
        "unit_symbol",
    )

    capacity_type: ResourceCapacityType | None
    default_capacity: _decimal.Decimal | None
    maximum_capacity: _decimal.Decimal | None
    minimum_capacity: _decimal.Decimal | None
    unit_symbol: UnitSymbol | None

    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="resource_capacity",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceCapacity",
        package="TC57CIM/IEC62325/MarketCommon",
        guid="{3E84F6F8-797E-4e4c-8901-DA7E5B1DFB67}",
        attributes=(
            AttrMeta("capacity_type", "capacityType", "ResourceCapacityType", 0, 1, "enumeration"),
            AttrMeta("default_capacity", "defaultCapacity", "Decimal", 0, 1, "primitive"),
            AttrMeta("maximum_capacity", "maximumCapacity", "Decimal", 0, 1, "primitive"),
            AttrMeta("minimum_capacity", "minimumCapacity", "Decimal", 0, 1, "primitive"),
            AttrMeta("unit_symbol", "unitSymbol", "UnitSymbol", 0, 1, "enumeration"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        capacity_type: ResourceCapacityType | None = None,
        default_capacity: _decimal.Decimal | None = None,
        maximum_capacity: _decimal.Decimal | None = None,
        minimum_capacity: _decimal.Decimal | None = None,
        unit_symbol: UnitSymbol | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.capacity_type = capacity_type
        self.default_capacity = default_capacity
        self.maximum_capacity = maximum_capacity
        self.minimum_capacity = minimum_capacity
        self.unit_symbol = unit_symbol
        if registered_resource is not None:
            ResourceCapacity.registered_resource.extend(self, registered_resource)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return ResourceCapacity.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return ResourceCapacity.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return ResourceCapacity.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return ResourceCapacity.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return ResourceCapacity.registered_resource.get_by_mrid(self, mrid)
