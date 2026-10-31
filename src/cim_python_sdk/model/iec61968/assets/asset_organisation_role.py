"""CIM class AssetOrganisationRole (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset


class AssetOrganisationRole(OrganisationRole):
    """Role an organisation plays with respect to asset."""

    __slots__ = ("_assets",)

    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="organisation_roles",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetOrganisationRole",
        package="TC57CIM/IEC61968/Assets",
        guid="{67516A27-FDD6-42da-91E3-3A99CD80A662}",
        ends=(assets.meta,),
    )

    def __init__(
        self,
        *,
        assets: Iterable[Asset] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if assets is not None:
            AssetOrganisationRole.assets.extend(self, assets)

    def add_asset(self, asset: Asset) -> Self:
        return AssetOrganisationRole.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return AssetOrganisationRole.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return AssetOrganisationRole.assets.clear(self)

    def num_asset(self) -> int:
        return AssetOrganisationRole.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return AssetOrganisationRole.assets.get_by_mrid(self, mrid)
