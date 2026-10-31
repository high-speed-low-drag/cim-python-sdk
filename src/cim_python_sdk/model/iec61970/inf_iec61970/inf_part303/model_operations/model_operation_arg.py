"""CIM class ModelOperationArg (TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation import (
        ModelOperation,
    )


class ModelOperationArg(IdentifiedObject):
    """Describes the role a dataset plays in a model operation. The role is applicable only in
    the context of a single operation."""

    __slots__ = ("_model_operation", "sequence_number")

    sequence_number: int | None

    model_operation: One[ModelOperation] = One(
        EndMeta(
            name="model_operation",
            cim_role="ModelOperation",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation:ModelOperation",
            many=False,
            lower=1,
            upper=1,
            inverse="model_operation_arg",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ModelOperationArg",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations",
        guid="{B29AFAE4-9F24-4482-85E2-C1C8CB65F146}",
        attributes=(AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),),
        ends=(model_operation.meta,),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        model_operation: ModelOperation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        if model_operation is not None:
            self.model_operation = model_operation
