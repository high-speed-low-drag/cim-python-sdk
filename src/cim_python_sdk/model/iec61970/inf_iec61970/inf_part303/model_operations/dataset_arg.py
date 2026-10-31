"""CIM class DatasetArg (TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_arg import (
    ModelOperationArg,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.dataset_arg_description import (
        DatasetArgDescription,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.instance_set import (
        InstanceSet,
    )


class DatasetArg(ModelOperationArg):
    """A model operation argument referencing a dataset instance."""

    __slots__ = ("_dataset", "_operation_dataset_arg_description")

    operation_dataset_arg_description: One[DatasetArgDescription] = One(
        EndMeta(
            name="operation_dataset_arg_description",
            cim_role="OperationDatasetArgDescription",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.dataset_arg_description:DatasetArgDescription",
            many=False,
            lower=1,
            upper=1,
            inverse="operation_dataset_arg",
            aggregation="none",
        )
    )
    dataset: One[InstanceSet] = One(
        EndMeta(
            name="dataset",
            cim_role="Dataset",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.instance_set:InstanceSet",
            many=False,
            lower=1,
            upper=1,
            inverse="dataset_arg",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DatasetArg",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations",
        guid="{30320F4F-DE3F-4314-A4D8-B59B81D75099}",
        ends=(
            operation_dataset_arg_description.meta,
            dataset.meta,
        ),
    )

    def __init__(
        self,
        *,
        operation_dataset_arg_description: DatasetArgDescription | None = None,
        dataset: InstanceSet | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if operation_dataset_arg_description is not None:
            self.operation_dataset_arg_description = operation_dataset_arg_description
        if dataset is not None:
            self.dataset = dataset
