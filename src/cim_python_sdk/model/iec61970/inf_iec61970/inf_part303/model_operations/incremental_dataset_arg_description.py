"""CIM class IncrementalDatasetArgDescription (TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_arg_description import (
    ModelOperationArgDescription,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.incremental_dataset_arg import (
        IncrementalDatasetArg,
    )


class IncrementalDatasetArgDescription(ModelOperationArgDescription):
    """CIM class IncrementalDatasetArgDescription."""

    __slots__ = ("_incremental_dataset_arg",)

    incremental_dataset_arg: Many[IncrementalDatasetArg] = Many(
        EndMeta(
            name="incremental_dataset_arg",
            cim_role="IncrementalDatasetArg",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.incremental_dataset_arg:IncrementalDatasetArg",
            many=True,
            lower=0,
            upper=None,
            inverse="incremental_dataset_arg_description",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IncrementalDatasetArgDescription",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations",
        guid="{850587EF-67CD-46a0-8449-9BDC215E8648}",
        ends=(incremental_dataset_arg.meta,),
    )

    def __init__(
        self,
        *,
        incremental_dataset_arg: Iterable[IncrementalDatasetArg] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if incremental_dataset_arg is not None:
            IncrementalDatasetArgDescription.incremental_dataset_arg.extend(
                self, incremental_dataset_arg
            )

    def add_incremental_dataset_arg(self, incremental_dataset_arg: IncrementalDatasetArg) -> Self:
        return IncrementalDatasetArgDescription.incremental_dataset_arg.add(
            self, incremental_dataset_arg
        )

    def remove_incremental_dataset_arg(
        self, incremental_dataset_arg: IncrementalDatasetArg
    ) -> Self:
        return IncrementalDatasetArgDescription.incremental_dataset_arg.remove(
            self, incremental_dataset_arg
        )

    def clear_incremental_dataset_arg(self) -> Self:
        return IncrementalDatasetArgDescription.incremental_dataset_arg.clear(self)

    def num_incremental_dataset_arg(self) -> int:
        return IncrementalDatasetArgDescription.incremental_dataset_arg.count(self)

    def get_incremental_dataset_arg_by_mrid(self, mrid: str) -> IncrementalDatasetArg | None:
        return IncrementalDatasetArgDescription.incremental_dataset_arg.get_by_mrid(self, mrid)
