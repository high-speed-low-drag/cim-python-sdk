"""CIM class LocationGrant (TC57CIM/IEC61968/InfIEC61968/InfLocations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.agreement import Agreement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property import LandProperty


class LocationGrant(Agreement):
    """A grant provides a right, as defined by type, for a parcel of land. Note that the
    association to Location, Asset, Organisation, etc. for the Grant is inherited from
    Agreement, a type of Document."""

    __slots__ = ("_land_property", "property_data")

    property_data: str | None

    land_property: One[LandProperty] = One(
        EndMeta(
            name="land_property",
            cim_role="LandProperty",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property:LandProperty",
            many=False,
            lower=0,
            upper=1,
            inverse="location_grants",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LocationGrant",
        package="TC57CIM/IEC61968/InfIEC61968/InfLocations",
        guid="{BC7CB30C-AD3F-4ca4-B3E1-0790F9AFF07B}",
        attributes=(AttrMeta("property_data", "propertyData", "str", 0, 1, "primitive"),),
        ends=(land_property.meta,),
    )

    def __init__(
        self,
        *,
        property_data: str | None = None,
        land_property: LandProperty | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.property_data = property_data
        if land_property is not None:
            self.land_property = land_property
