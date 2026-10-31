"""CIM class Asset (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from tests.runtime.minimodel.asset_kind import AssetKind
from tests.runtime.minimodel.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from tests.runtime.minimodel.location import Location
    from tests.runtime.minimodel.power_system_resource import PowerSystemResource


class Asset(IdentifiedObject):
    """Tangible resource of the utility, including power system equipment."""

    __slots__ = ("_location", "_power_system_resources", "date", "kind")

    date: _dt.date | None
    kind: AssetKind | None

    location: One[Location] = One(
        EndMeta(
            name="location",
            cim_role="Location",
            target="tests.runtime.minimodel.location:Location",
            many=False,
            lower=0,
            upper=1,
            inverse="asset",
            aggregation="none",
        )
    )
    power_system_resources: Many[PowerSystemResource] = Many(
        EndMeta(
            name="power_system_resources",
            cim_role="PowerSystemResources",
            target="tests.runtime.minimodel.power_system_resource:PowerSystemResource",
            many=True,
            lower=1,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Asset",
        package="TC57CIM/IEC61968/Assets",
        guid="{00000000-0000-0000-0000-00000000C005}",
        attributes=(
            AttrMeta("date", "date", "date", 0, 1, "primitive"),
            AttrMeta("kind", "kind", "AssetKind", 0, 1, "enumeration", AssetKind.other),
        ),
        ends=(location.meta, power_system_resources.meta),
    )

    def __init__(
        self,
        *,
        date: _dt.date | None = None,
        kind: AssetKind | None = AssetKind.other,
        location: Location | None = None,
        power_system_resources: Iterable[PowerSystemResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.date = date
        self.kind = kind
        if location is not None:
            self.location = location
        if power_system_resources is not None:
            Asset.power_system_resources.extend(self, power_system_resources)

    def add_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return Asset.power_system_resources.add(self, power_system_resource)

    def remove_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return Asset.power_system_resources.remove(self, power_system_resource)

    def clear_power_system_resources(self) -> Self:
        return Asset.power_system_resources.clear(self)

    def num_power_system_resource(self) -> int:
        return Asset.power_system_resources.count(self)

    def get_power_system_resource_by_mrid(self, mrid: str) -> PowerSystemResource | None:
        return Asset.power_system_resources.get_by_mrid(self, mrid)
