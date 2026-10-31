"""CIM class ModelOperation (TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_arg import (
        ModelOperationArg,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_description import (
        ModelOperationDescription,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_sequence import (
        ModelOperationSequence,
    )


class ModelOperation(IdentifiedObject):
    """An operation performed on models."""

    __slots__ = (
        "_model_operation_arg",
        "_model_operation_description",
        "_operation_sequence",
        "sequence_number",
    )

    sequence_number: int | None

    operation_sequence: One[ModelOperationSequence] = One(
        EndMeta(
            name="operation_sequence",
            cim_role="OperationSequence",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_sequence:ModelOperationSequence",
            many=False,
            lower=1,
            upper=1,
            inverse="model_operation",
            aggregation="none",
        )
    )
    model_operation_description: One[ModelOperationDescription] = One(
        EndMeta(
            name="model_operation_description",
            cim_role="ModelOperationDescription",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_description:ModelOperationDescription",
            many=False,
            lower=1,
            upper=1,
            inverse="model_operation",
            aggregation="none",
        )
    )
    model_operation_arg: Many[ModelOperationArg] = Many(
        EndMeta(
            name="model_operation_arg",
            cim_role="ModelOperationArg",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_arg:ModelOperationArg",
            many=True,
            lower=0,
            upper=None,
            inverse="model_operation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ModelOperation",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations",
        guid="{DD8B0627-7F67-4d51-9ABC-03D0BF4BA7CD}",
        attributes=(AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),),
        ends=(
            operation_sequence.meta,
            model_operation_description.meta,
            model_operation_arg.meta,
        ),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        operation_sequence: ModelOperationSequence | None = None,
        model_operation_description: ModelOperationDescription | None = None,
        model_operation_arg: Iterable[ModelOperationArg] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        if operation_sequence is not None:
            self.operation_sequence = operation_sequence
        if model_operation_description is not None:
            self.model_operation_description = model_operation_description
        if model_operation_arg is not None:
            ModelOperation.model_operation_arg.extend(self, model_operation_arg)

    def add_model_operation_arg(self, model_operation_arg: ModelOperationArg) -> Self:
        return ModelOperation.model_operation_arg.add(self, model_operation_arg)

    def remove_model_operation_arg(self, model_operation_arg: ModelOperationArg) -> Self:
        return ModelOperation.model_operation_arg.remove(self, model_operation_arg)

    def clear_model_operation_arg(self) -> Self:
        return ModelOperation.model_operation_arg.clear(self)

    def num_model_operation_arg(self) -> int:
        return ModelOperation.model_operation_arg.count(self)

    def get_model_operation_arg_by_mrid(self, mrid: str) -> ModelOperationArg | None:
        return ModelOperation.model_operation_arg.get_by_mrid(self, mrid)
