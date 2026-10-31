"""CIM class PowerTransformerInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.transformer_tank_info import TransformerTankInfo


class PowerTransformerInfo(AssetInfo):
    """Set of power transformer data, from an equipment library."""

    __slots__ = ("_transformer_tank_infos",)

    transformer_tank_infos: Many[TransformerTankInfo] = Many(
        EndMeta(
            name="transformer_tank_infos",
            cim_role="TransformerTankInfos",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_tank_info:TransformerTankInfo",
            many=True,
            lower=1,
            upper=None,
            inverse="power_transformer_info",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerTransformerInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{46FF16E8-5771-4f84-BFAF-AE487FF9ED06}",
        ends=(transformer_tank_infos.meta,),
    )

    def __init__(
        self,
        *,
        transformer_tank_infos: Iterable[TransformerTankInfo] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if transformer_tank_infos is not None:
            PowerTransformerInfo.transformer_tank_infos.extend(self, transformer_tank_infos)

    def add_transformer_tank_info(self, transformer_tank_info: TransformerTankInfo) -> Self:
        return PowerTransformerInfo.transformer_tank_infos.add(self, transformer_tank_info)

    def remove_transformer_tank_info(self, transformer_tank_info: TransformerTankInfo) -> Self:
        return PowerTransformerInfo.transformer_tank_infos.remove(self, transformer_tank_info)

    def clear_transformer_tank_infos(self) -> Self:
        return PowerTransformerInfo.transformer_tank_infos.clear(self)

    def num_transformer_tank_info(self) -> int:
        return PowerTransformerInfo.transformer_tank_infos.count(self)

    def get_transformer_tank_info_by_mrid(self, mrid: str) -> TransformerTankInfo | None:
        return PowerTransformerInfo.transformer_tank_infos.get_by_mrid(self, mrid)
