"""CIM class ModelOperationDescription (TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_arg_description import (
        ModelOperationArgDescription,
    )


class ModelOperationDescription(IdentifiedObject):
    """The type of model operation. This class is referenced by model operations and defines
    the kind of operation."""

    __slots__ = ("_model_operation", "_operation_dataset_arg_description")

    operation_dataset_arg_description: Many[ModelOperationArgDescription] = Many(
        EndMeta(
            name="operation_dataset_arg_description",
            cim_role="OperationDatasetArgDescription",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_arg_description:ModelOperationArgDescription",
            many=True,
            lower=0,
            upper=None,
            inverse="model_operation_definition",
            aggregation="none",
        )
    )
    model_operation: Many[ModelOperation] = Many(
        EndMeta(
            name="model_operation",
            cim_role="ModelOperation",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation:ModelOperation",
            many=True,
            lower=0,
            upper=None,
            inverse="model_operation_description",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ModelOperationDescription",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations",
        guid="{E7A4D5EF-6269-4060-9926-32B91503ED92}",
        ends=(
            operation_dataset_arg_description.meta,
            model_operation.meta,
        ),
    )

    def __init__(
        self,
        *,
        operation_dataset_arg_description: Iterable[ModelOperationArgDescription] | None = None,
        model_operation: Iterable[ModelOperation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if operation_dataset_arg_description is not None:
            ModelOperationDescription.operation_dataset_arg_description.extend(
                self, operation_dataset_arg_description
            )
        if model_operation is not None:
            ModelOperationDescription.model_operation.extend(self, model_operation)

    def add_operation_dataset_arg_description(
        self, operation_dataset_arg_description: ModelOperationArgDescription
    ) -> Self:
        return ModelOperationDescription.operation_dataset_arg_description.add(
            self, operation_dataset_arg_description
        )

    def remove_operation_dataset_arg_description(
        self, operation_dataset_arg_description: ModelOperationArgDescription
    ) -> Self:
        return ModelOperationDescription.operation_dataset_arg_description.remove(
            self, operation_dataset_arg_description
        )

    def clear_operation_dataset_arg_description(self) -> Self:
        return ModelOperationDescription.operation_dataset_arg_description.clear(self)

    def num_operation_dataset_arg_description(self) -> int:
        return ModelOperationDescription.operation_dataset_arg_description.count(self)

    def get_operation_dataset_arg_description_by_mrid(
        self, mrid: str
    ) -> ModelOperationArgDescription | None:
        return ModelOperationDescription.operation_dataset_arg_description.get_by_mrid(self, mrid)

    def add_model_operation(self, model_operation: ModelOperation) -> Self:
        return ModelOperationDescription.model_operation.add(self, model_operation)

    def remove_model_operation(self, model_operation: ModelOperation) -> Self:
        return ModelOperationDescription.model_operation.remove(self, model_operation)

    def clear_model_operation(self) -> Self:
        return ModelOperationDescription.model_operation.clear(self)

    def num_model_operation(self) -> int:
        return ModelOperationDescription.model_operation.count(self)

    def get_model_operation_by_mrid(self, mrid: str) -> ModelOperation | None:
        return ModelOperationDescription.model_operation.get_by_mrid(self, mrid)
