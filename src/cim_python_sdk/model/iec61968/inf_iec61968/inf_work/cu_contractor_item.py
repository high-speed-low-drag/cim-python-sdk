"""CIM class CUContractorItem (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit import CompatibleUnit


class CUContractorItem(WorkIdentifiedObject):
    """Compatible unit contractor item."""

    __slots__ = ("_compatible_units", "activity_code", "bid_amount", "status")

    activity_code: str | None
    bid_amount: _decimal.Decimal | None  # Money
    status: Status | None

    compatible_units: Many[CompatibleUnit] = Many(
        EndMeta(
            name="compatible_units",
            cim_role="CompatibleUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit:CompatibleUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="cu_contractor_items",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CUContractorItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{1154E13A-BB99-4075-AF1F-D572FE30B18F}",
        attributes=(
            AttrMeta("activity_code", "activityCode", "str", 0, 1, "primitive"),
            AttrMeta("bid_amount", "bidAmount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(compatible_units.meta,),
    )

    def __init__(
        self,
        *,
        activity_code: str | None = None,
        bid_amount: _decimal.Decimal | None = None,
        status: Status | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.activity_code = activity_code
        self.bid_amount = bid_amount
        self.status = status
        if compatible_units is not None:
            CUContractorItem.compatible_units.extend(self, compatible_units)

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CUContractorItem.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CUContractorItem.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return CUContractorItem.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return CUContractorItem.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return CUContractorItem.compatible_units.get_by_mrid(self, mrid)
