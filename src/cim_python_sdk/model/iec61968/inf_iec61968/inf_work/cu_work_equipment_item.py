"""CIM class CUWorkEquipmentItem (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit import CompatibleUnit
    from cim_python_sdk.model.iec61968.work.work_asset import WorkAsset


class CUWorkEquipmentItem(WorkIdentifiedObject):
    """Compatible unit for various types of WorkEquipmentAssets, including vehicles."""

    __slots__ = ("_compatible_units", "_type_asset", "equip_code", "rate", "status")

    equip_code: str | None
    rate: float | None  # CostRate
    status: Status | None

    compatible_units: Many[CompatibleUnit] = Many(
        EndMeta(
            name="compatible_units",
            cim_role="CompatibleUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit:CompatibleUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="cu_work_equipment_items",
            aggregation="none",
        )
    )
    type_asset: One[WorkAsset] = One(
        EndMeta(
            name="type_asset",
            cim_role="TypeAsset",
            target="cim_python_sdk.model.iec61968.work.work_asset:WorkAsset",
            many=False,
            lower=0,
            upper=1,
            inverse="cu_work_equipment_asset",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CUWorkEquipmentItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{5A25E9C1-6C9B-453f-890A-CA0A42110858}",
        attributes=(
            AttrMeta("equip_code", "equipCode", "str", 0, 1, "primitive"),
            AttrMeta("rate", "rate", "CostRate", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            compatible_units.meta,
            type_asset.meta,
        ),
    )

    def __init__(
        self,
        *,
        equip_code: str | None = None,
        rate: float | None = None,
        status: Status | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        type_asset: WorkAsset | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.equip_code = equip_code
        self.rate = rate
        self.status = status
        if compatible_units is not None:
            CUWorkEquipmentItem.compatible_units.extend(self, compatible_units)
        if type_asset is not None:
            self.type_asset = type_asset

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CUWorkEquipmentItem.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CUWorkEquipmentItem.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return CUWorkEquipmentItem.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return CUWorkEquipmentItem.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return CUWorkEquipmentItem.compatible_units.get_by_mrid(self, mrid)
