"""CIM class MiscCostItem (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location import DesignLocation
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail
    from cim_python_sdk.model.iec61970.base.domain.integer_quantity import IntegerQuantity


class MiscCostItem(WorkIdentifiedObject):
    """Various cost items that are not associated with compatible units. Examples include
    rental equipment, labor, materials, contractor costs, permits - anything not covered in
    a CU."""

    __slots__ = (
        "_design_location",
        "_work_cost_detail",
        "_work_task",
        "account",
        "cost_per_unit",
        "cost_type",
        "external_ref_id",
        "quantity",
        "status",
    )

    quantity: IntegerQuantity | None
    cost_per_unit: _decimal.Decimal | None  # Money
    cost_type: str | None
    account: str | None
    external_ref_id: str | None
    status: Status | None

    work_task: One[OldWorkTask] = One(
        EndMeta(
            name="work_task",
            cim_role="WorkTask",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task:OldWorkTask",
            many=False,
            lower=0,
            upper=1,
            inverse="misc_cost_items",
            aggregation="none",
        )
    )
    work_cost_detail: One[WorkCostDetail] = One(
        EndMeta(
            name="work_cost_detail",
            cim_role="WorkCostDetail",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail:WorkCostDetail",
            many=False,
            lower=0,
            upper=1,
            inverse="misc_cost_items",
            aggregation="none",
        )
    )
    design_location: One[DesignLocation] = One(
        EndMeta(
            name="design_location",
            cim_role="DesignLocation",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location:DesignLocation",
            many=False,
            lower=0,
            upper=1,
            inverse="misc_cost_items",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MiscCostItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{4026BBE0-4EDE-4a88-9540-4BEE474CA739}",
        attributes=(
            AttrMeta("quantity", "quantity", "IntegerQuantity", 0, 1, "compound"),
            AttrMeta("cost_per_unit", "costPerUnit", "Money", 0, 1, "cimdatatype"),
            AttrMeta("cost_type", "costType", "str", 0, 1, "primitive"),
            AttrMeta("account", "account", "str", 0, 1, "primitive"),
            AttrMeta("external_ref_id", "externalRefID", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            work_task.meta,
            work_cost_detail.meta,
            design_location.meta,
        ),
    )

    def __init__(
        self,
        *,
        quantity: IntegerQuantity | None = None,
        cost_per_unit: _decimal.Decimal | None = None,
        cost_type: str | None = None,
        account: str | None = None,
        external_ref_id: str | None = None,
        status: Status | None = None,
        work_task: OldWorkTask | None = None,
        work_cost_detail: WorkCostDetail | None = None,
        design_location: DesignLocation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit
        self.cost_type = cost_type
        self.account = account
        self.external_ref_id = external_ref_id
        self.status = status
        if work_task is not None:
            self.work_task = work_task
        if work_cost_detail is not None:
            self.work_cost_detail = work_cost_detail
        if design_location is not None:
            self.design_location = design_location
