"""CIM class ModelOperationSequence (TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation import (
        ModelOperation,
    )


class ModelOperationSequence(IdentifiedObject):
    """A concrete sequence of operations. For example, this may be used to describe a specific
    audit trail, a script or other specific set of actions on specific datasets."""

    __slots__ = ("_model_operation",)

    model_operation: Many[ModelOperation] = Many(
        EndMeta(
            name="model_operation",
            cim_role="ModelOperation",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation:ModelOperation",
            many=True,
            lower=0,
            upper=None,
            inverse="operation_sequence",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ModelOperationSequence",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations",
        guid="{9656D19D-8924-42b5-8754-3DCECBCC6B9C}",
        ends=(model_operation.meta,),
    )

    def __init__(
        self,
        *,
        model_operation: Iterable[ModelOperation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if model_operation is not None:
            ModelOperationSequence.model_operation.extend(self, model_operation)

    def add_model_operation(self, model_operation: ModelOperation) -> Self:
        return ModelOperationSequence.model_operation.add(self, model_operation)

    def remove_model_operation(self, model_operation: ModelOperation) -> Self:
        return ModelOperationSequence.model_operation.remove(self, model_operation)

    def clear_model_operation(self) -> Self:
        return ModelOperationSequence.model_operation.clear(self)

    def num_model_operation(self) -> int:
        return ModelOperationSequence.model_operation.count(self)

    def get_model_operation_by_mrid(self, mrid: str) -> ModelOperation | None:
        return ModelOperationSequence.model_operation.get_by_mrid(self, mrid)
