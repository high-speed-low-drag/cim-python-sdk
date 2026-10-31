"""CIM class AssetOwner (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset_organisation_role import AssetOrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.ownership import Ownership


class AssetOwner(AssetOrganisationRole):
    """Owner of the asset."""

    __slots__ = ("_ownerships",)

    ownerships: Many[Ownership] = Many(
        EndMeta(
            name="ownerships",
            cim_role="Ownerships",
            target="cim_python_sdk.model.iec61968.common.ownership:Ownership",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_owner",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetOwner",
        package="TC57CIM/IEC61968/Assets",
        guid="{780D3A9C-A59A-4516-B7EB-60C24AA5F03B}",
        ends=(ownerships.meta,),
    )

    def __init__(
        self,
        *,
        ownerships: Iterable[Ownership] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if ownerships is not None:
            AssetOwner.ownerships.extend(self, ownerships)

    def add_ownership(self, ownership: Ownership) -> Self:
        return AssetOwner.ownerships.add(self, ownership)

    def remove_ownership(self, ownership: Ownership) -> Self:
        return AssetOwner.ownerships.remove(self, ownership)

    def clear_ownerships(self) -> Self:
        return AssetOwner.ownerships.clear(self)

    def num_ownership(self) -> int:
        return AssetOwner.ownerships.count(self)

    def get_ownership_by_mrid(self, mrid: str) -> Ownership | None:
        return AssetOwner.ownerships.get_by_mrid(self, mrid)
