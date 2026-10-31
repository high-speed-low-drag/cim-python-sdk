"""CIM class DatasetArgDescription (TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_arg_description import (
    ModelOperationArgDescription,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.dataset_arg import (
        DatasetArg,
    )


class DatasetArgDescription(ModelOperationArgDescription):
    """CIM class DatasetArgDescription."""

    __slots__ = ("_operation_dataset_arg",)

    operation_dataset_arg: Many[DatasetArg] = Many(
        EndMeta(
            name="operation_dataset_arg",
            cim_role="OperationDatasetArg",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.dataset_arg:DatasetArg",
            many=True,
            lower=0,
            upper=None,
            inverse="operation_dataset_arg_description",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DatasetArgDescription",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations",
        guid="{01211A0F-1460-4fb8-97C0-2610DCF987AE}",
        ends=(operation_dataset_arg.meta,),
    )

    def __init__(
        self,
        *,
        operation_dataset_arg: Iterable[DatasetArg] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if operation_dataset_arg is not None:
            DatasetArgDescription.operation_dataset_arg.extend(self, operation_dataset_arg)

    def add_operation_dataset_arg(self, operation_dataset_arg: DatasetArg) -> Self:
        return DatasetArgDescription.operation_dataset_arg.add(self, operation_dataset_arg)

    def remove_operation_dataset_arg(self, operation_dataset_arg: DatasetArg) -> Self:
        return DatasetArgDescription.operation_dataset_arg.remove(self, operation_dataset_arg)

    def clear_operation_dataset_arg(self) -> Self:
        return DatasetArgDescription.operation_dataset_arg.clear(self)

    def num_operation_dataset_arg(self) -> int:
        return DatasetArgDescription.operation_dataset_arg.count(self)

    def get_operation_dataset_arg_by_mrid(self, mrid: str) -> DatasetArg | None:
        return DatasetArgDescription.operation_dataset_arg.get_by_mrid(self, mrid)
