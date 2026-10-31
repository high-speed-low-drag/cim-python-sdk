"""CIM class TransformerTankInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.power_transformer_info import PowerTransformerInfo
    from cim_python_sdk.model.iec61968.asset_info.transformer_end_info import TransformerEndInfo


class TransformerTankInfo(AssetInfo):
    """Set of transformer tank data, from an equipment library."""

    __slots__ = ("_power_transformer_info", "_transformer_end_infos")

    transformer_end_infos: Many[TransformerEndInfo] = Many(
        EndMeta(
            name="transformer_end_infos",
            cim_role="TransformerEndInfos",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_end_info:TransformerEndInfo",
            many=True,
            lower=1,
            upper=None,
            inverse="transformer_tank_info",
            aggregation="none",
        )
    )
    power_transformer_info: One[PowerTransformerInfo] = One(
        EndMeta(
            name="power_transformer_info",
            cim_role="PowerTransformerInfo",
            target="cim_python_sdk.model.iec61968.asset_info.power_transformer_info:PowerTransformerInfo",
            many=False,
            lower=1,
            upper=1,
            inverse="transformer_tank_infos",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransformerTankInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{C4D8C511-0532-4ac2-8888-61C0D77D4BE7}",
        ends=(
            transformer_end_infos.meta,
            power_transformer_info.meta,
        ),
    )

    def __init__(
        self,
        *,
        transformer_end_infos: Iterable[TransformerEndInfo] | None = None,
        power_transformer_info: PowerTransformerInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if transformer_end_infos is not None:
            TransformerTankInfo.transformer_end_infos.extend(self, transformer_end_infos)
        if power_transformer_info is not None:
            self.power_transformer_info = power_transformer_info

    def add_transformer_end_info(self, transformer_end_info: TransformerEndInfo) -> Self:
        return TransformerTankInfo.transformer_end_infos.add(self, transformer_end_info)

    def remove_transformer_end_info(self, transformer_end_info: TransformerEndInfo) -> Self:
        return TransformerTankInfo.transformer_end_infos.remove(self, transformer_end_info)

    def clear_transformer_end_infos(self) -> Self:
        return TransformerTankInfo.transformer_end_infos.clear(self)

    def num_transformer_end_info(self) -> int:
        return TransformerTankInfo.transformer_end_infos.count(self)

    def get_transformer_end_info_by_mrid(self, mrid: str) -> TransformerEndInfo | None:
        return TransformerTankInfo.transformer_end_infos.get_by_mrid(self, mrid)
