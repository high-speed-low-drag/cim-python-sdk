"""CIM class MaterialItem (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.type_material import TypeMaterial
    from cim_python_sdk.model.iec61968.work.work_task import WorkTask
    from cim_python_sdk.model.iec61970.base.domain.integer_quantity import IntegerQuantity


class MaterialItem(IdentifiedObject):
    """The physical consumable supply used for work and other purposes. It includes items such
    as nuts, bolts, brackets, glue, etc."""

    __slots__ = ("_type_material", "_work_task", "quantity")

    quantity: IntegerQuantity | None

    type_material: One[TypeMaterial] = One(
        EndMeta(
            name="type_material",
            cim_role="TypeMaterial",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.type_material:TypeMaterial",
            many=False,
            lower=0,
            upper=1,
            inverse="material_items",
            aggregation="none",
        )
    )
    work_task: One[WorkTask] = One(
        EndMeta(
            name="work_task",
            cim_role="WorkTask",
            target="cim_python_sdk.model.iec61968.work.work_task:WorkTask",
            many=False,
            lower=0,
            upper=1,
            inverse="material_items",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MaterialItem",
        package="TC57CIM/IEC61968/Work",
        guid="{71A96EF3-A030-44b2-9B34-92A72564646C}",
        attributes=(AttrMeta("quantity", "quantity", "IntegerQuantity", 0, 1, "compound"),),
        ends=(
            type_material.meta,
            work_task.meta,
        ),
    )

    def __init__(
        self,
        *,
        quantity: IntegerQuantity | None = None,
        type_material: TypeMaterial | None = None,
        work_task: WorkTask | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.quantity = quantity
        if type_material is not None:
            self.type_material = type_material
        if work_task is not None:
            self.work_task = work_task
