"""CIM class AssetLocationHazard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.hazard import Hazard

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset_hazard_kind import AssetHazardKind
    from cim_python_sdk.model.iec61968.common.location import Location


class AssetLocationHazard(Hazard):
    """Potential hazard related to the location of an asset. Examples are trees growing under
    overhead power lines, a park being located by a substation (i.e., children climb fence
    to recover a ball), a lake near an overhead distribution line (fishing pole/line
    contacting power lines), dangerous neighbour, etc."""

    __slots__ = ("_locations", "kind")

    kind: AssetHazardKind | None

    locations: Many[Location] = Many(
        EndMeta(
            name="locations",
            cim_role="Locations",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=True,
            lower=0,
            upper=None,
            inverse="hazards",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetLocationHazard",
        package="TC57CIM/IEC61968/Assets",
        guid="{B4AC24E1-04E8-4237-9AE9-A81876210B6E}",
        attributes=(AttrMeta("kind", "kind", "AssetHazardKind", 0, 1, "enumeration"),),
        ends=(locations.meta,),
    )

    def __init__(
        self,
        *,
        kind: AssetHazardKind | None = None,
        locations: Iterable[Location] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if locations is not None:
            AssetLocationHazard.locations.extend(self, locations)

    def add_location(self, location: Location) -> Self:
        return AssetLocationHazard.locations.add(self, location)

    def remove_location(self, location: Location) -> Self:
        return AssetLocationHazard.locations.remove(self, location)

    def clear_locations(self) -> Self:
        return AssetLocationHazard.locations.clear(self)

    def num_location(self) -> int:
        return AssetLocationHazard.locations.count(self)

    def get_location_by_mrid(self, mrid: str) -> Location | None:
        return AssetLocationHazard.locations.get_by_mrid(self, mrid)
