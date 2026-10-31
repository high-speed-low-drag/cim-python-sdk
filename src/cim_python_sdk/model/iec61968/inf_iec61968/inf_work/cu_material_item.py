"""CIM class CUMaterialItem (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.property_unit import PropertyUnit
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.type_material import TypeMaterial
    from cim_python_sdk.model.iec61970.base.domain.integer_quantity import IntegerQuantity


class CUMaterialItem(WorkIdentifiedObject):
    """Compatible unit of a consumable supply item. For example, nuts, bolts, brackets, glue,
    etc."""

    __slots__ = (
        "_compatible_units",
        "_property_units",
        "_type_material",
        "corporate_code",
        "quantity",
        "status",
    )

    corporate_code: str | None
    quantity: IntegerQuantity | None
    status: Status | None

    type_material: One[TypeMaterial] = One(
        EndMeta(
            name="type_material",
            cim_role="TypeMaterial",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.type_material:TypeMaterial",
            many=False,
            lower=0,
            upper=1,
            inverse="cu_material_items",
            aggregation="none",
        )
    )
    compatible_units: Many[CompatibleUnit] = Many(
        EndMeta(
            name="compatible_units",
            cim_role="CompatibleUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit:CompatibleUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="cu_material_items",
            aggregation="none",
        )
    )
    property_units: Many[PropertyUnit] = Many(
        EndMeta(
            name="property_units",
            cim_role="PropertyUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.property_unit:PropertyUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="cu_material_items",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CUMaterialItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{8775417D-D473-4904-9042-5E7AFC57FE87}",
        attributes=(
            AttrMeta("corporate_code", "corporateCode", "str", 0, 1, "primitive"),
            AttrMeta("quantity", "quantity", "IntegerQuantity", 0, 1, "compound"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            type_material.meta,
            compatible_units.meta,
            property_units.meta,
        ),
    )

    def __init__(
        self,
        *,
        corporate_code: str | None = None,
        quantity: IntegerQuantity | None = None,
        status: Status | None = None,
        type_material: TypeMaterial | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        property_units: Iterable[PropertyUnit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.corporate_code = corporate_code
        self.quantity = quantity
        self.status = status
        if type_material is not None:
            self.type_material = type_material
        if compatible_units is not None:
            CUMaterialItem.compatible_units.extend(self, compatible_units)
        if property_units is not None:
            CUMaterialItem.property_units.extend(self, property_units)

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CUMaterialItem.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CUMaterialItem.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return CUMaterialItem.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return CUMaterialItem.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return CUMaterialItem.compatible_units.get_by_mrid(self, mrid)

    def add_property_unit(self, property_unit: PropertyUnit) -> Self:
        return CUMaterialItem.property_units.add(self, property_unit)

    def remove_property_unit(self, property_unit: PropertyUnit) -> Self:
        return CUMaterialItem.property_units.remove(self, property_unit)

    def clear_property_units(self) -> Self:
        return CUMaterialItem.property_units.clear(self)

    def num_property_unit(self) -> int:
        return CUMaterialItem.property_units.count(self)

    def get_property_unit_by_mrid(self, mrid: str) -> PropertyUnit | None:
        return CUMaterialItem.property_units.get_by_mrid(self, mrid)
