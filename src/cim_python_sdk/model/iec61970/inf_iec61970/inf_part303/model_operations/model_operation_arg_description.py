"""CIM class ModelOperationArgDescription (TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_description import (
        ModelOperationDescription,
    )


class ModelOperationArgDescription(IdentifiedObject):
    """The type of custom operation dataset role for an operation description."""

    __slots__ = ("_model_operation_definition", "multiplicity_maximum", "multiplicity_minimum")

    multiplicity_maximum: int | None
    multiplicity_minimum: int | None

    model_operation_definition: One[ModelOperationDescription] = One(
        EndMeta(
            name="model_operation_definition",
            cim_role="ModelOperationDefinition",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.model_operation_description:ModelOperationDescription",
            many=False,
            lower=1,
            upper=1,
            inverse="operation_dataset_arg_description",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ModelOperationArgDescription",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/ModelOperations",
        guid="{E557275F-6438-417b-9835-80AA612233C9}",
        attributes=(
            AttrMeta("multiplicity_maximum", "multiplicityMaximum", "int", 0, 1, "primitive"),
            AttrMeta("multiplicity_minimum", "multiplicityMinimum", "int", 0, 1, "primitive"),
        ),
        ends=(model_operation_definition.meta,),
    )

    def __init__(
        self,
        *,
        multiplicity_maximum: int | None = None,
        multiplicity_minimum: int | None = None,
        model_operation_definition: ModelOperationDescription | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.multiplicity_maximum = multiplicity_maximum
        self.multiplicity_minimum = multiplicity_minimum
        if model_operation_definition is not None:
            self.model_operation_definition = model_operation_definition
