"""CIM class Medium (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.medium_kind import MediumKind
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification import Specification


class Medium(IdentifiedObject):
    """A substance that either (1) provides the means of transmission of a force or effect,
    such as hydraulic fluid, or (2) is used for a surrounding or enveloping substance, such
    as oil in a transformer or circuit breaker."""

    __slots__ = ("_asset", "_specification", "kind", "volume_spec")

    kind: MediumKind | None
    volume_spec: float | None  # Volume

    asset: Many[Asset] = Many(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="medium",
            aggregation="none",
        )
    )
    specification: One[Specification] = One(
        EndMeta(
            name="specification",
            cim_role="Specification",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification:Specification",
            many=False,
            lower=0,
            upper=1,
            inverse="mediums",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Medium",
        package="TC57CIM/IEC61968/Assets",
        guid="{EE7BBAF4-7FC2-4777-BCB7-2C0CC47C4899}",
        attributes=(
            AttrMeta("kind", "kind", "MediumKind", 0, 1, "enumeration"),
            AttrMeta("volume_spec", "volumeSpec", "Volume", 0, 1, "cimdatatype"),
        ),
        ends=(
            asset.meta,
            specification.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: MediumKind | None = None,
        volume_spec: float | None = None,
        asset: Iterable[Asset] | None = None,
        specification: Specification | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.volume_spec = volume_spec
        if asset is not None:
            Medium.asset.extend(self, asset)
        if specification is not None:
            self.specification = specification

    def add_asset(self, asset: Asset) -> Self:
        return Medium.asset.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return Medium.asset.remove(self, asset)

    def clear_asset(self) -> Self:
        return Medium.asset.clear(self)

    def num_asset(self) -> int:
        return Medium.asset.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return Medium.asset.get_by_mrid(self, mrid)
