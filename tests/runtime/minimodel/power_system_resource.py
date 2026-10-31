"""CIM class PowerSystemResource (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from tests.runtime.minimodel.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from tests.runtime.minimodel.asset import Asset


class PowerSystemResource(IdentifiedObject):
    """A power system resource (PSR) can be an item of equipment such as a switch, an
    equipment container containing many individual items of equipment such as a substation,
    or an organisational entity such as sub-control area."""

    __slots__ = ("_assets", "_children", "_parent")

    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="tests.runtime.minimodel.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_resources",
            aggregation="none",
        )
    )
    children: Many[PowerSystemResource] = Many(
        EndMeta(
            name="children",
            cim_role="Children",
            target="tests.runtime.minimodel.power_system_resource:PowerSystemResource",
            many=True,
            lower=0,
            upper=2,
            inverse="parent",
            aggregation="none",
        )
    )
    parent: One[PowerSystemResource] = One(
        EndMeta(
            name="parent",
            cim_role="Parent",
            target="tests.runtime.minimodel.power_system_resource:PowerSystemResource",
            many=False,
            lower=0,
            upper=1,
            inverse="children",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerSystemResource",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{00000000-0000-0000-0000-00000000C002}",
        ends=(assets.meta, children.meta, parent.meta),
    )

    def __init__(
        self,
        *,
        assets: Iterable[Asset] | None = None,
        children: Iterable[PowerSystemResource] | None = None,
        parent: PowerSystemResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if assets is not None:
            PowerSystemResource.assets.extend(self, assets)
        if children is not None:
            PowerSystemResource.children.extend(self, children)
        if parent is not None:
            self.parent = parent

    def add_asset(self, asset: Asset) -> Self:
        return PowerSystemResource.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return PowerSystemResource.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return PowerSystemResource.assets.clear(self)

    def num_asset(self) -> int:
        return PowerSystemResource.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return PowerSystemResource.assets.get_by_mrid(self, mrid)

    def add_child(self, child: PowerSystemResource) -> Self:
        return PowerSystemResource.children.add(self, child)

    def remove_child(self, child: PowerSystemResource) -> Self:
        return PowerSystemResource.children.remove(self, child)

    def clear_children(self) -> Self:
        return PowerSystemResource.children.clear(self)

    def num_child(self) -> int:
        return PowerSystemResource.children.count(self)

    def get_child_by_mrid(self, mrid: str) -> PowerSystemResource | None:
        return PowerSystemResource.children.get_by_mrid(self, mrid)
