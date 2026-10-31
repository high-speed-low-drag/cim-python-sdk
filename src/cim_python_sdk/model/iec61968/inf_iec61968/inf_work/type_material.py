"""CIM class TypeMaterial (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_issue_inventory import (
        ErpIssueInventory,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_req_line_item import (
        ErpReqLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_material_item import CUMaterialItem
    from cim_python_sdk.model.iec61968.work.material_item import MaterialItem


class TypeMaterial(WorkDocument):
    """Documentation for a generic material item that may be used for design, work and other
    purposes. Any number of MaterialItems manufactured by various vendors may be used to
    perform this TypeMaterial.

    Note that class analagous to "AssetModel" is not used for material items. This is
    because in some cases, for example, a utility sets up a Master material record for a 3
    inch long half inch diameter steel bolt and they do not necessarily care what specific
    supplier is providing the material item. As different vendors are used to supply the
    part, the Stock Code of the material item can stay the same. In other cases, each time
    the vendor changes, a new stock code is set up so they can track material used by
    vendor. Therefore a Material Item "Model" is not typically needed."""

    __slots__ = (
        "_cu_material_items",
        "_erp_issue_inventories",
        "_erp_req_line_items",
        "_material_items",
        "cost_type",
        "est_unit_cost",
        "quantity",
        "stock_item",
    )

    stock_item: bool | None
    est_unit_cost: _decimal.Decimal | None  # Money
    quantity: str | None
    cost_type: str | None

    material_items: Many[MaterialItem] = Many(
        EndMeta(
            name="material_items",
            cim_role="MaterialItems",
            target="cim_python_sdk.model.iec61968.work.material_item:MaterialItem",
            many=True,
            lower=0,
            upper=None,
            inverse="type_material",
            aggregation="none",
        )
    )
    erp_req_line_items: Many[ErpReqLineItem] = Many(
        EndMeta(
            name="erp_req_line_items",
            cim_role="ErpReqLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_req_line_item:ErpReqLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="type_material",
            aggregation="none",
        )
    )
    erp_issue_inventories: Many[ErpIssueInventory] = Many(
        EndMeta(
            name="erp_issue_inventories",
            cim_role="ErpIssueInventories",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_issue_inventory:ErpIssueInventory",
            many=True,
            lower=0,
            upper=None,
            inverse="type_material",
            aggregation="none",
        )
    )
    cu_material_items: Many[CUMaterialItem] = Many(
        EndMeta(
            name="cu_material_items",
            cim_role="CUMaterialItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_material_item:CUMaterialItem",
            many=True,
            lower=0,
            upper=None,
            inverse="type_material",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TypeMaterial",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{EC640844-2A38-430d-AF20-D32909547B2A}",
        attributes=(
            AttrMeta("stock_item", "stockItem", "bool", 0, 1, "primitive"),
            AttrMeta("est_unit_cost", "estUnitCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("quantity", "quantity", "str", 0, 1, "primitive"),
            AttrMeta("cost_type", "costType", "str", 0, 1, "primitive"),
        ),
        ends=(
            material_items.meta,
            erp_req_line_items.meta,
            erp_issue_inventories.meta,
            cu_material_items.meta,
        ),
    )

    def __init__(
        self,
        *,
        stock_item: bool | None = None,
        est_unit_cost: _decimal.Decimal | None = None,
        quantity: str | None = None,
        cost_type: str | None = None,
        material_items: Iterable[MaterialItem] | None = None,
        erp_req_line_items: Iterable[ErpReqLineItem] | None = None,
        erp_issue_inventories: Iterable[ErpIssueInventory] | None = None,
        cu_material_items: Iterable[CUMaterialItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.stock_item = stock_item
        self.est_unit_cost = est_unit_cost
        self.quantity = quantity
        self.cost_type = cost_type
        if material_items is not None:
            TypeMaterial.material_items.extend(self, material_items)
        if erp_req_line_items is not None:
            TypeMaterial.erp_req_line_items.extend(self, erp_req_line_items)
        if erp_issue_inventories is not None:
            TypeMaterial.erp_issue_inventories.extend(self, erp_issue_inventories)
        if cu_material_items is not None:
            TypeMaterial.cu_material_items.extend(self, cu_material_items)

    def add_material_item(self, material_item: MaterialItem) -> Self:
        return TypeMaterial.material_items.add(self, material_item)

    def remove_material_item(self, material_item: MaterialItem) -> Self:
        return TypeMaterial.material_items.remove(self, material_item)

    def clear_material_items(self) -> Self:
        return TypeMaterial.material_items.clear(self)

    def num_material_item(self) -> int:
        return TypeMaterial.material_items.count(self)

    def get_material_item_by_mrid(self, mrid: str) -> MaterialItem | None:
        return TypeMaterial.material_items.get_by_mrid(self, mrid)

    def add_erp_req_line_item(self, erp_req_line_item: ErpReqLineItem) -> Self:
        return TypeMaterial.erp_req_line_items.add(self, erp_req_line_item)

    def remove_erp_req_line_item(self, erp_req_line_item: ErpReqLineItem) -> Self:
        return TypeMaterial.erp_req_line_items.remove(self, erp_req_line_item)

    def clear_erp_req_line_items(self) -> Self:
        return TypeMaterial.erp_req_line_items.clear(self)

    def num_erp_req_line_item(self) -> int:
        return TypeMaterial.erp_req_line_items.count(self)

    def get_erp_req_line_item_by_mrid(self, mrid: str) -> ErpReqLineItem | None:
        return TypeMaterial.erp_req_line_items.get_by_mrid(self, mrid)

    def add_erp_issue_inventory(self, erp_issue_inventory: ErpIssueInventory) -> Self:
        return TypeMaterial.erp_issue_inventories.add(self, erp_issue_inventory)

    def remove_erp_issue_inventory(self, erp_issue_inventory: ErpIssueInventory) -> Self:
        return TypeMaterial.erp_issue_inventories.remove(self, erp_issue_inventory)

    def clear_erp_issue_inventories(self) -> Self:
        return TypeMaterial.erp_issue_inventories.clear(self)

    def num_erp_issue_inventory(self) -> int:
        return TypeMaterial.erp_issue_inventories.count(self)

    def get_erp_issue_inventory_by_mrid(self, mrid: str) -> ErpIssueInventory | None:
        return TypeMaterial.erp_issue_inventories.get_by_mrid(self, mrid)

    def add_cu_material_item(self, cu_material_item: CUMaterialItem) -> Self:
        return TypeMaterial.cu_material_items.add(self, cu_material_item)

    def remove_cu_material_item(self, cu_material_item: CUMaterialItem) -> Self:
        return TypeMaterial.cu_material_items.remove(self, cu_material_item)

    def clear_cu_material_items(self) -> Self:
        return TypeMaterial.cu_material_items.clear(self)

    def num_cu_material_item(self) -> int:
        return TypeMaterial.cu_material_items.count(self)

    def get_cu_material_item_by_mrid(self, mrid: str) -> CUMaterialItem | None:
        return TypeMaterial.cu_material_items.get_by_mrid(self, mrid)
