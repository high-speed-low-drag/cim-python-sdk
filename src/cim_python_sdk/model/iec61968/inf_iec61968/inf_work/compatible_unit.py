"""CIM class CompatibleUnit (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.catalog_asset_type import CatalogAssetType
    from cim_python_sdk.model.iec61968.assets.procedure import Procedure
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cost_type import CostType
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_allowable_action import (
        CUAllowableAction,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_contractor_item import (
        CUContractorItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_group import CUGroup
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_labor_item import CULaborItem
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_material_item import CUMaterialItem
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_work_equipment_item import (
        CUWorkEquipmentItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu import (
        DesignLocationCU,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.property_unit import PropertyUnit


class CompatibleUnit(WorkDocument):
    """A pre-planned job model containing labor, material, and accounting requirements for
    standardized job planning."""

    __slots__ = (
        "_cost_type",
        "_cu_allowable_action",
        "_cu_contractor_items",
        "_cu_group",
        "_cu_labor_items",
        "_cu_material_items",
        "_cu_work_equipment_items",
        "_design_location_cus",
        "_generic_asset_model",
        "_procedures",
        "_property_unit",
        "est_cost",
        "quantity",
    )

    quantity: str | None
    est_cost: _decimal.Decimal | None  # Money

    cost_type: One[CostType] = One(
        EndMeta(
            name="cost_type",
            cim_role="CostType",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cost_type:CostType",
            many=False,
            lower=0,
            upper=1,
            inverse="compatible_units",
            aggregation="none",
        )
    )
    cu_work_equipment_items: Many[CUWorkEquipmentItem] = Many(
        EndMeta(
            name="cu_work_equipment_items",
            cim_role="CUWorkEquipmentItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_work_equipment_item:CUWorkEquipmentItem",
            many=True,
            lower=0,
            upper=None,
            inverse="compatible_units",
            aggregation="none",
        )
    )
    cu_labor_items: Many[CULaborItem] = Many(
        EndMeta(
            name="cu_labor_items",
            cim_role="CULaborItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_labor_item:CULaborItem",
            many=True,
            lower=0,
            upper=None,
            inverse="compatible_units",
            aggregation="none",
        )
    )
    generic_asset_model: One[CatalogAssetType] = One(
        EndMeta(
            name="generic_asset_model",
            cim_role="GenericAssetModel",
            target="cim_python_sdk.model.iec61968.assets.catalog_asset_type:CatalogAssetType",
            many=False,
            lower=0,
            upper=1,
            inverse="compatible_units",
            aggregation="none",
        )
    )
    cu_contractor_items: Many[CUContractorItem] = Many(
        EndMeta(
            name="cu_contractor_items",
            cim_role="CUContractorItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_contractor_item:CUContractorItem",
            many=True,
            lower=0,
            upper=None,
            inverse="compatible_units",
            aggregation="none",
        )
    )
    property_unit: One[PropertyUnit] = One(
        EndMeta(
            name="property_unit",
            cim_role="PropertyUnit",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.property_unit:PropertyUnit",
            many=False,
            lower=0,
            upper=1,
            inverse="compatible_units",
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
            inverse="compatible_units",
            aggregation="none",
        )
    )
    cu_allowable_action: One[CUAllowableAction] = One(
        EndMeta(
            name="cu_allowable_action",
            cim_role="CUAllowableAction",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_allowable_action:CUAllowableAction",
            many=False,
            lower=0,
            upper=1,
            inverse="compatible_units",
            aggregation="none",
        )
    )
    cu_group: One[CUGroup] = One(
        EndMeta(
            name="cu_group",
            cim_role="CUGroup",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_group:CUGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="compatible_units",
            aggregation="none",
        )
    )
    procedures: Many[Procedure] = Many(
        EndMeta(
            name="procedures",
            cim_role="Procedures",
            target="cim_python_sdk.model.iec61968.assets.procedure:Procedure",
            many=True,
            lower=0,
            upper=None,
            inverse="compatible_units",
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
            inverse="compatible_units",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CompatibleUnit",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{0BA3A428-B0EC-43cd-8B48-D299F19C52C0}",
        attributes=(
            AttrMeta("quantity", "quantity", "str", 0, 1, "primitive"),
            AttrMeta("est_cost", "estCost", "Money", 0, 1, "cimdatatype"),
        ),
        ends=(
            cost_type.meta,
            cu_work_equipment_items.meta,
            cu_labor_items.meta,
            generic_asset_model.meta,
            cu_contractor_items.meta,
            property_unit.meta,
            cu_material_items.meta,
            cu_allowable_action.meta,
            cu_group.meta,
            procedures.meta,
            design_location_cus.meta,
        ),
    )

    def __init__(
        self,
        *,
        quantity: str | None = None,
        est_cost: _decimal.Decimal | None = None,
        cost_type: CostType | None = None,
        cu_work_equipment_items: Iterable[CUWorkEquipmentItem] | None = None,
        cu_labor_items: Iterable[CULaborItem] | None = None,
        generic_asset_model: CatalogAssetType | None = None,
        cu_contractor_items: Iterable[CUContractorItem] | None = None,
        property_unit: PropertyUnit | None = None,
        cu_material_items: Iterable[CUMaterialItem] | None = None,
        cu_allowable_action: CUAllowableAction | None = None,
        cu_group: CUGroup | None = None,
        procedures: Iterable[Procedure] | None = None,
        design_location_cus: Iterable[DesignLocationCU] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.quantity = quantity
        self.est_cost = est_cost
        if cost_type is not None:
            self.cost_type = cost_type
        if cu_work_equipment_items is not None:
            CompatibleUnit.cu_work_equipment_items.extend(self, cu_work_equipment_items)
        if cu_labor_items is not None:
            CompatibleUnit.cu_labor_items.extend(self, cu_labor_items)
        if generic_asset_model is not None:
            self.generic_asset_model = generic_asset_model
        if cu_contractor_items is not None:
            CompatibleUnit.cu_contractor_items.extend(self, cu_contractor_items)
        if property_unit is not None:
            self.property_unit = property_unit
        if cu_material_items is not None:
            CompatibleUnit.cu_material_items.extend(self, cu_material_items)
        if cu_allowable_action is not None:
            self.cu_allowable_action = cu_allowable_action
        if cu_group is not None:
            self.cu_group = cu_group
        if procedures is not None:
            CompatibleUnit.procedures.extend(self, procedures)
        if design_location_cus is not None:
            CompatibleUnit.design_location_cus.extend(self, design_location_cus)

    def add_cu_work_equipment_item(self, cu_work_equipment_item: CUWorkEquipmentItem) -> Self:
        return CompatibleUnit.cu_work_equipment_items.add(self, cu_work_equipment_item)

    def remove_cu_work_equipment_item(self, cu_work_equipment_item: CUWorkEquipmentItem) -> Self:
        return CompatibleUnit.cu_work_equipment_items.remove(self, cu_work_equipment_item)

    def clear_cu_work_equipment_items(self) -> Self:
        return CompatibleUnit.cu_work_equipment_items.clear(self)

    def num_cu_work_equipment_item(self) -> int:
        return CompatibleUnit.cu_work_equipment_items.count(self)

    def get_cu_work_equipment_item_by_mrid(self, mrid: str) -> CUWorkEquipmentItem | None:
        return CompatibleUnit.cu_work_equipment_items.get_by_mrid(self, mrid)

    def add_cu_labor_item(self, cu_labor_item: CULaborItem) -> Self:
        return CompatibleUnit.cu_labor_items.add(self, cu_labor_item)

    def remove_cu_labor_item(self, cu_labor_item: CULaborItem) -> Self:
        return CompatibleUnit.cu_labor_items.remove(self, cu_labor_item)

    def clear_cu_labor_items(self) -> Self:
        return CompatibleUnit.cu_labor_items.clear(self)

    def num_cu_labor_item(self) -> int:
        return CompatibleUnit.cu_labor_items.count(self)

    def get_cu_labor_item_by_mrid(self, mrid: str) -> CULaborItem | None:
        return CompatibleUnit.cu_labor_items.get_by_mrid(self, mrid)

    def add_cu_contractor_item(self, cu_contractor_item: CUContractorItem) -> Self:
        return CompatibleUnit.cu_contractor_items.add(self, cu_contractor_item)

    def remove_cu_contractor_item(self, cu_contractor_item: CUContractorItem) -> Self:
        return CompatibleUnit.cu_contractor_items.remove(self, cu_contractor_item)

    def clear_cu_contractor_items(self) -> Self:
        return CompatibleUnit.cu_contractor_items.clear(self)

    def num_cu_contractor_item(self) -> int:
        return CompatibleUnit.cu_contractor_items.count(self)

    def get_cu_contractor_item_by_mrid(self, mrid: str) -> CUContractorItem | None:
        return CompatibleUnit.cu_contractor_items.get_by_mrid(self, mrid)

    def add_cu_material_item(self, cu_material_item: CUMaterialItem) -> Self:
        return CompatibleUnit.cu_material_items.add(self, cu_material_item)

    def remove_cu_material_item(self, cu_material_item: CUMaterialItem) -> Self:
        return CompatibleUnit.cu_material_items.remove(self, cu_material_item)

    def clear_cu_material_items(self) -> Self:
        return CompatibleUnit.cu_material_items.clear(self)

    def num_cu_material_item(self) -> int:
        return CompatibleUnit.cu_material_items.count(self)

    def get_cu_material_item_by_mrid(self, mrid: str) -> CUMaterialItem | None:
        return CompatibleUnit.cu_material_items.get_by_mrid(self, mrid)

    def add_procedure(self, procedure: Procedure) -> Self:
        return CompatibleUnit.procedures.add(self, procedure)

    def remove_procedure(self, procedure: Procedure) -> Self:
        return CompatibleUnit.procedures.remove(self, procedure)

    def clear_procedures(self) -> Self:
        return CompatibleUnit.procedures.clear(self)

    def num_procedure(self) -> int:
        return CompatibleUnit.procedures.count(self)

    def get_procedure_by_mrid(self, mrid: str) -> Procedure | None:
        return CompatibleUnit.procedures.get_by_mrid(self, mrid)

    def add_design_location_cu(self, design_location_cu: DesignLocationCU) -> Self:
        return CompatibleUnit.design_location_cus.add(self, design_location_cu)

    def remove_design_location_cu(self, design_location_cu: DesignLocationCU) -> Self:
        return CompatibleUnit.design_location_cus.remove(self, design_location_cu)

    def clear_design_location_cus(self) -> Self:
        return CompatibleUnit.design_location_cus.clear(self)

    def num_design_location_cu(self) -> int:
        return CompatibleUnit.design_location_cus.count(self)

    def get_design_location_cu_by_mrid(self, mrid: str) -> DesignLocationCU | None:
        return CompatibleUnit.design_location_cus.get_by_mrid(self, mrid)
