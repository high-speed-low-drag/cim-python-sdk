"""CIM class RightOfWay (TC57CIM/IEC61968/InfIEC61968/InfLocations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.agreement import Agreement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property import LandProperty


class RightOfWay(Agreement):
    """A right-of-way (ROW) is for land where it is lawful to use for a public road, an
    electric power line, etc. Note that the association to Location, Asset, Organisation,
    etc. for the Grant is inherited from Agreement, a type of Document."""

    __slots__ = ("_land_properties", "property_data")

    property_data: str | None

    land_properties: Many[LandProperty] = Many(
        EndMeta(
            name="land_properties",
            cim_role="LandProperties",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property:LandProperty",
            many=True,
            lower=0,
            upper=None,
            inverse="right_of_ways",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RightOfWay",
        package="TC57CIM/IEC61968/InfIEC61968/InfLocations",
        guid="{44FBA225-6F53-4b26-BF4C-7792D077AFF2}",
        attributes=(AttrMeta("property_data", "propertyData", "str", 0, 1, "primitive"),),
        ends=(land_properties.meta,),
    )

    def __init__(
        self,
        *,
        property_data: str | None = None,
        land_properties: Iterable[LandProperty] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.property_data = property_data
        if land_properties is not None:
            RightOfWay.land_properties.extend(self, land_properties)

    def add_land_property(self, land_property: LandProperty) -> Self:
        return RightOfWay.land_properties.add(self, land_property)

    def remove_land_property(self, land_property: LandProperty) -> Self:
        return RightOfWay.land_properties.remove(self, land_property)

    def clear_land_properties(self) -> Self:
        return RightOfWay.land_properties.clear(self)

    def num_land_property(self) -> int:
        return RightOfWay.land_properties.count(self)

    def get_land_property_by_mrid(self, mrid: str) -> LandProperty | None:
        return RightOfWay.land_properties.get_by_mrid(self, mrid)
