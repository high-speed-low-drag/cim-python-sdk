"""CIM class CULaborCode (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_labor_item import CULaborItem


class CULaborCode(WorkIdentifiedObject):
    """Labor code associated with various compatible unit labor items."""

    __slots__ = ("_cu_labor_items", "code", "status")

    code: str | None
    status: Status | None

    cu_labor_items: Many[CULaborItem] = Many(
        EndMeta(
            name="cu_labor_items",
            cim_role="CULaborItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_labor_item:CULaborItem",
            many=True,
            lower=0,
            upper=None,
            inverse="cu_labor_code",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CULaborCode",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{24A4AC0F-0478-4eea-AF98-F304F6802DC2}",
        attributes=(
            AttrMeta("code", "code", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(cu_labor_items.meta,),
    )

    def __init__(
        self,
        *,
        code: str | None = None,
        status: Status | None = None,
        cu_labor_items: Iterable[CULaborItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.code = code
        self.status = status
        if cu_labor_items is not None:
            CULaborCode.cu_labor_items.extend(self, cu_labor_items)

    def add_cu_labor_item(self, cu_labor_item: CULaborItem) -> Self:
        return CULaborCode.cu_labor_items.add(self, cu_labor_item)

    def remove_cu_labor_item(self, cu_labor_item: CULaborItem) -> Self:
        return CULaborCode.cu_labor_items.remove(self, cu_labor_item)

    def clear_cu_labor_items(self) -> Self:
        return CULaborCode.cu_labor_items.clear(self)

    def num_cu_labor_item(self) -> int:
        return CULaborCode.cu_labor_items.count(self)

    def get_cu_labor_item_by_mrid(self, mrid: str) -> CULaborItem | None:
        return CULaborCode.cu_labor_items.get_by_mrid(self, mrid)
