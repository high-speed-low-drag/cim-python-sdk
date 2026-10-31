"""CIM class AssetContainer (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.seal import Seal
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property import LandProperty


class AssetContainer(Asset):
    """Asset that is aggregation of other assets such as conductors, transformers, switchgear,
    land, fences, buildings, equipment, vehicles, etc."""

    __slots__ = ("_assets", "_land_properties", "_seals")

    land_properties: Many[LandProperty] = Many(
        EndMeta(
            name="land_properties",
            cim_role="LandProperties",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property:LandProperty",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_containers",
            aggregation="none",
        )
    )
    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_container",
            aggregation="none",
        )
    )
    seals: Many[Seal] = Many(
        EndMeta(
            name="seals",
            cim_role="Seals",
            target="cim_python_sdk.model.iec61968.assets.seal:Seal",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_container",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetContainer",
        package="TC57CIM/IEC61968/Assets",
        guid="{C871BF41-2266-4e8c-B45A-1534C39F8633}",
        ends=(
            land_properties.meta,
            assets.meta,
            seals.meta,
        ),
    )

    def __init__(
        self,
        *,
        land_properties: Iterable[LandProperty] | None = None,
        assets: Iterable[Asset] | None = None,
        seals: Iterable[Seal] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if land_properties is not None:
            AssetContainer.land_properties.extend(self, land_properties)
        if assets is not None:
            AssetContainer.assets.extend(self, assets)
        if seals is not None:
            AssetContainer.seals.extend(self, seals)

    def add_land_property(self, land_property: LandProperty) -> Self:
        return AssetContainer.land_properties.add(self, land_property)

    def remove_land_property(self, land_property: LandProperty) -> Self:
        return AssetContainer.land_properties.remove(self, land_property)

    def clear_land_properties(self) -> Self:
        return AssetContainer.land_properties.clear(self)

    def num_land_property(self) -> int:
        return AssetContainer.land_properties.count(self)

    def get_land_property_by_mrid(self, mrid: str) -> LandProperty | None:
        return AssetContainer.land_properties.get_by_mrid(self, mrid)

    def add_asset(self, asset: Asset) -> Self:
        return AssetContainer.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return AssetContainer.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return AssetContainer.assets.clear(self)

    def num_asset(self) -> int:
        return AssetContainer.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return AssetContainer.assets.get_by_mrid(self, mrid)

    def add_seal(self, seal: Seal) -> Self:
        return AssetContainer.seals.add(self, seal)

    def remove_seal(self, seal: Seal) -> Self:
        return AssetContainer.seals.remove(self, seal)

    def clear_seals(self) -> Self:
        return AssetContainer.seals.clear(self)

    def num_seal(self) -> int:
        return AssetContainer.seals.count(self)

    def get_seal_by_mrid(self, mrid: str) -> Seal | None:
        return AssetContainer.seals.get_by_mrid(self, mrid)
