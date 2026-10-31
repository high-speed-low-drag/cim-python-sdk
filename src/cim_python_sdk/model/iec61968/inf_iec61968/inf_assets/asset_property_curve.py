"""CIM class AssetPropertyCurve (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification import Specification


class AssetPropertyCurve(Curve):
    """An Asset Property that is described through curves rather than as a data point. The
    relationship is to be defined between an independent variable (X-axis) and one or two
    dependent variables (Y1-axis and Y2-axis)."""

    __slots__ = ("_assets", "_specification")

    specification: One[Specification] = One(
        EndMeta(
            name="specification",
            cim_role="Specification",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification:Specification",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_property_curves",
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
            inverse="asset_property_curves",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetPropertyCurve",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{908D87FF-0DB8-400f-9203-3C586099255A}",
        ends=(
            specification.meta,
            assets.meta,
        ),
    )

    def __init__(
        self,
        *,
        specification: Specification | None = None,
        assets: Iterable[Asset] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if specification is not None:
            self.specification = specification
        if assets is not None:
            AssetPropertyCurve.assets.extend(self, assets)

    def add_asset(self, asset: Asset) -> Self:
        return AssetPropertyCurve.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return AssetPropertyCurve.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return AssetPropertyCurve.assets.clear(self)

    def num_asset(self) -> int:
        return AssetPropertyCurve.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return AssetPropertyCurve.assets.get_by_mrid(self, mrid)
