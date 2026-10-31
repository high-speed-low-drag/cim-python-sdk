"""CIM class WorkAsset (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.assets.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.crew import Crew
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_work_equipment_item import (
        CUWorkEquipmentItem,
    )


class WorkAsset(Asset):
    """Asset used to perform work."""

    __slots__ = ("_crew", "_cu_work_equipment_asset")

    crew: One[Crew] = One(
        EndMeta(
            name="crew",
            cim_role="Crew",
            target="cim_python_sdk.model.iec61968.common.crew:Crew",
            many=False,
            lower=0,
            upper=1,
            inverse="work_assets",
            aggregation="none",
        )
    )
    cu_work_equipment_asset: One[CUWorkEquipmentItem] = One(
        EndMeta(
            name="cu_work_equipment_asset",
            cim_role="CUWorkEquipmentAsset",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_work_equipment_item:CUWorkEquipmentItem",
            many=False,
            lower=0,
            upper=1,
            inverse="type_asset",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WorkAsset",
        package="TC57CIM/IEC61968/Work",
        guid="{D6ADD1A2-0860-4d9d-AEDC-78818C208396}",
        ends=(
            crew.meta,
            cu_work_equipment_asset.meta,
        ),
    )

    def __init__(
        self,
        *,
        crew: Crew | None = None,
        cu_work_equipment_asset: CUWorkEquipmentItem | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if crew is not None:
            self.crew = crew
        if cu_work_equipment_asset is not None:
            self.cu_work_equipment_asset = cu_work_equipment_asset
