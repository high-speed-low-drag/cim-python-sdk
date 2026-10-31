"""CIM class DesignLocation (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_bom_item_data import (
        ErpBomItemData,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.condition_factor import ConditionFactor
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design import Design
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu import (
        DesignLocationCU,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.misc_cost_item import MiscCostItem
    from cim_python_sdk.model.iec61968.work.work_location import WorkLocation


class DesignLocation(WorkIdentifiedObject):
    """A logical part of the design (e.g., pole and all equipment on a pole). This includes
    points and spans."""

    __slots__ = (
        "_condition_factors",
        "_design_location_cus",
        "_designs",
        "_erp_bom_item_datas",
        "_misc_cost_items",
        "_work_locations",
        "span_length",
        "status",
    )

    span_length: float | None  # Length
    status: Status | None

    condition_factors: Many[ConditionFactor] = Many(
        EndMeta(
            name="condition_factors",
            cim_role="ConditionFactors",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.condition_factor:ConditionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="design_locations",
            aggregation="none",
        )
    )
    erp_bom_item_datas: Many[ErpBomItemData] = Many(
        EndMeta(
            name="erp_bom_item_datas",
            cim_role="ErpBomItemDatas",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_bom_item_data:ErpBomItemData",
            many=True,
            lower=0,
            upper=None,
            inverse="design_location",
            aggregation="none",
        )
    )
    designs: Many[Design] = Many(
        EndMeta(
            name="designs",
            cim_role="Designs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design:Design",
            many=True,
            lower=1,
            upper=None,
            inverse="design_locations",
            aggregation="none",
        )
    )
    design_location_cus: Many[DesignLocationCU] = Many(
        EndMeta(
            name="design_location_cus",
            cim_role="DesignLocationCUs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu:DesignLocationCU",
            many=True,
            lower=0,
            upper=None,
            inverse="design_location",
            aggregation="none",
        )
    )
    work_locations: Many[WorkLocation] = Many(
        EndMeta(
            name="work_locations",
            cim_role="WorkLocations",
            target="cim_python_sdk.model.iec61968.work.work_location:WorkLocation",
            many=True,
            lower=1,
            upper=None,
            inverse="design_locations",
            aggregation="none",
        )
    )
    misc_cost_items: Many[MiscCostItem] = Many(
        EndMeta(
            name="misc_cost_items",
            cim_role="MiscCostItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.misc_cost_item:MiscCostItem",
            many=True,
            lower=0,
            upper=None,
            inverse="design_location",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DesignLocation",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{19C5D8E2-644A-4ab7-9057-3D46A6538905}",
        attributes=(
            AttrMeta("span_length", "spanLength", "Length", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            condition_factors.meta,
            erp_bom_item_datas.meta,
            designs.meta,
            design_location_cus.meta,
            work_locations.meta,
            misc_cost_items.meta,
        ),
    )

    def __init__(
        self,
        *,
        span_length: float | None = None,
        status: Status | None = None,
        condition_factors: Iterable[ConditionFactor] | None = None,
        erp_bom_item_datas: Iterable[ErpBomItemData] | None = None,
        designs: Iterable[Design] | None = None,
        design_location_cus: Iterable[DesignLocationCU] | None = None,
        work_locations: Iterable[WorkLocation] | None = None,
        misc_cost_items: Iterable[MiscCostItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.span_length = span_length
        self.status = status
        if condition_factors is not None:
            DesignLocation.condition_factors.extend(self, condition_factors)
        if erp_bom_item_datas is not None:
            DesignLocation.erp_bom_item_datas.extend(self, erp_bom_item_datas)
        if designs is not None:
            DesignLocation.designs.extend(self, designs)
        if design_location_cus is not None:
            DesignLocation.design_location_cus.extend(self, design_location_cus)
        if work_locations is not None:
            DesignLocation.work_locations.extend(self, work_locations)
        if misc_cost_items is not None:
            DesignLocation.misc_cost_items.extend(self, misc_cost_items)

    def add_condition_factor(self, condition_factor: ConditionFactor) -> Self:
        return DesignLocation.condition_factors.add(self, condition_factor)

    def remove_condition_factor(self, condition_factor: ConditionFactor) -> Self:
        return DesignLocation.condition_factors.remove(self, condition_factor)

    def clear_condition_factors(self) -> Self:
        return DesignLocation.condition_factors.clear(self)

    def num_condition_factor(self) -> int:
        return DesignLocation.condition_factors.count(self)

    def get_condition_factor_by_mrid(self, mrid: str) -> ConditionFactor | None:
        return DesignLocation.condition_factors.get_by_mrid(self, mrid)

    def add_erp_bom_item_data(self, erp_bom_item_data: ErpBomItemData) -> Self:
        return DesignLocation.erp_bom_item_datas.add(self, erp_bom_item_data)

    def remove_erp_bom_item_data(self, erp_bom_item_data: ErpBomItemData) -> Self:
        return DesignLocation.erp_bom_item_datas.remove(self, erp_bom_item_data)

    def clear_erp_bom_item_datas(self) -> Self:
        return DesignLocation.erp_bom_item_datas.clear(self)

    def num_erp_bom_item_data(self) -> int:
        return DesignLocation.erp_bom_item_datas.count(self)

    def get_erp_bom_item_data_by_mrid(self, mrid: str) -> ErpBomItemData | None:
        return DesignLocation.erp_bom_item_datas.get_by_mrid(self, mrid)

    def add_design(self, design: Design) -> Self:
        return DesignLocation.designs.add(self, design)

    def remove_design(self, design: Design) -> Self:
        return DesignLocation.designs.remove(self, design)

    def clear_designs(self) -> Self:
        return DesignLocation.designs.clear(self)

    def num_design(self) -> int:
        return DesignLocation.designs.count(self)

    def get_design_by_mrid(self, mrid: str) -> Design | None:
        return DesignLocation.designs.get_by_mrid(self, mrid)

    def add_design_location_cu(self, design_location_cu: DesignLocationCU) -> Self:
        return DesignLocation.design_location_cus.add(self, design_location_cu)

    def remove_design_location_cu(self, design_location_cu: DesignLocationCU) -> Self:
        return DesignLocation.design_location_cus.remove(self, design_location_cu)

    def clear_design_location_cus(self) -> Self:
        return DesignLocation.design_location_cus.clear(self)

    def num_design_location_cu(self) -> int:
        return DesignLocation.design_location_cus.count(self)

    def get_design_location_cu_by_mrid(self, mrid: str) -> DesignLocationCU | None:
        return DesignLocation.design_location_cus.get_by_mrid(self, mrid)

    def add_work_location(self, work_location: WorkLocation) -> Self:
        return DesignLocation.work_locations.add(self, work_location)

    def remove_work_location(self, work_location: WorkLocation) -> Self:
        return DesignLocation.work_locations.remove(self, work_location)

    def clear_work_locations(self) -> Self:
        return DesignLocation.work_locations.clear(self)

    def num_work_location(self) -> int:
        return DesignLocation.work_locations.count(self)

    def get_work_location_by_mrid(self, mrid: str) -> WorkLocation | None:
        return DesignLocation.work_locations.get_by_mrid(self, mrid)

    def add_misc_cost_item(self, misc_cost_item: MiscCostItem) -> Self:
        return DesignLocation.misc_cost_items.add(self, misc_cost_item)

    def remove_misc_cost_item(self, misc_cost_item: MiscCostItem) -> Self:
        return DesignLocation.misc_cost_items.remove(self, misc_cost_item)

    def clear_misc_cost_items(self) -> Self:
        return DesignLocation.misc_cost_items.clear(self)

    def num_misc_cost_item(self) -> int:
        return DesignLocation.misc_cost_items.count(self)

    def get_misc_cost_item_by_mrid(self, mrid: str) -> MiscCostItem | None:
        return DesignLocation.misc_cost_items.get_by_mrid(self, mrid)
