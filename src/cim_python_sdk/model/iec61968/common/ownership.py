"""CIM class Ownership (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.asset_owner import AssetOwner


class Ownership(IdentifiedObject):
    """Ownership of e.g. asset."""

    __slots__ = ("_asset", "_asset_owner", "share")

    share: float | None  # PerCent

    asset_owner: One[AssetOwner] = One(
        EndMeta(
            name="asset_owner",
            cim_role="AssetOwner",
            target="cim_python_sdk.model.iec61968.assets.asset_owner:AssetOwner",
            many=False,
            lower=0,
            upper=1,
            inverse="ownerships",
            aggregation="none",
        )
    )
    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="ownerships",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Ownership",
        package="TC57CIM/IEC61968/Common",
        guid="{28F059EF-408D-4bde-93EE-0173ABC67D39}",
        attributes=(AttrMeta("share", "share", "PerCent", 0, 1, "cimdatatype"),),
        ends=(
            asset_owner.meta,
            asset.meta,
        ),
    )

    def __init__(
        self,
        *,
        share: float | None = None,
        asset_owner: AssetOwner | None = None,
        asset: Asset | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.share = share
        if asset_owner is not None:
            self.asset_owner = asset_owner
        if asset is not None:
            self.asset = asset
