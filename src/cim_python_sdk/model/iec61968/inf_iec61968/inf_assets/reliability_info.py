"""CIM class ReliabilityInfo (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification import Specification


class ReliabilityInfo(IdentifiedObject):
    """Information regarding the experienced and expected reliability of a specific asset, type
    of asset, or asset model."""

    __slots__ = ("_assets", "_specification", "m_ttr", "mom_failure_rate")

    mom_failure_rate: float | None  # PerCent
    m_ttr: float | None  # Hours

    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="reliability_infos",
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
            inverse="reliability_infos",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReliabilityInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{A482ED74-2DA2-44d4-B516-615598573052}",
        attributes=(
            AttrMeta("mom_failure_rate", "momFailureRate", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("m_ttr", "mTTR", "Hours", 0, 1, "cimdatatype"),
        ),
        ends=(
            assets.meta,
            specification.meta,
        ),
    )

    def __init__(
        self,
        *,
        mom_failure_rate: float | None = None,
        m_ttr: float | None = None,
        assets: Iterable[Asset] | None = None,
        specification: Specification | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mom_failure_rate = mom_failure_rate
        self.m_ttr = m_ttr
        if assets is not None:
            ReliabilityInfo.assets.extend(self, assets)
        if specification is not None:
            self.specification = specification

    def add_asset(self, asset: Asset) -> Self:
        return ReliabilityInfo.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return ReliabilityInfo.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return ReliabilityInfo.assets.clear(self)

    def num_asset(self) -> int:
        return ReliabilityInfo.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return ReliabilityInfo.assets.get_by_mrid(self, mrid)
