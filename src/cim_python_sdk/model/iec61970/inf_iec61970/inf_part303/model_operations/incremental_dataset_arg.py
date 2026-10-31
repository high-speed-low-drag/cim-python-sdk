"""CIM class IncrementalDatasetArg (TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_arg import (
    ModelOperationArg,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.incremental_dataset_arg_description import (
        IncrementalDatasetArgDescription,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set import (
        ChangeSet,
    )


class IncrementalDatasetArg(ModelOperationArg):
    """A generic model operation argument referencing an incremental change description."""

    __slots__ = ("_incremental_dataset", "_incremental_dataset_arg_description")

    incremental_dataset_arg_description: One[IncrementalDatasetArgDescription] = One(
        EndMeta(
            name="incremental_dataset_arg_description",
            cim_role="IncrementalDatasetArgDescription",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.incremental_dataset_arg_description:IncrementalDatasetArgDescription",
            many=False,
            lower=1,
            upper=1,
            inverse="incremental_dataset_arg",
            aggregation="none",
        )
    )
    incremental_dataset: One[ChangeSet] = One(
        EndMeta(
            name="incremental_dataset",
            cim_role="IncrementalDataset",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set:ChangeSet",
            many=False,
            lower=1,
            upper=1,
            inverse="incremental_dataset_arg",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IncrementalDatasetArg",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations",
        guid="{4AC6A487-907B-4a92-AF68-AB20542CD308}",
        ends=(
            incremental_dataset_arg_description.meta,
            incremental_dataset.meta,
        ),
    )

    def __init__(
        self,
        *,
        incremental_dataset_arg_description: IncrementalDatasetArgDescription | None = None,
        incremental_dataset: ChangeSet | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if incremental_dataset_arg_description is not None:
            self.incremental_dataset_arg_description = incremental_dataset_arg_description
        if incremental_dataset is not None:
            self.incremental_dataset = incremental_dataset
