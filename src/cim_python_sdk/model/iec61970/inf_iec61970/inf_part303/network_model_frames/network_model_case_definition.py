"""CIM class NetworkModelCaseDefinition (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.operation import (
        Operation,
    )


class NetworkModelCaseDefinition(CimObject):
    """Instructions to build a network model case, including when appropriate the results."""

    __slots__ = ("_operations",)

    operations: Many[Operation] = Many(
        EndMeta(
            name="operations",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.operation:Operation",
            many=True,
            lower=0,
            upper=None,
            inverse="network_model_case_definition",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelCaseDefinition",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{42B17612-9428-4011-901E-A0360E01C5C1}",
        ends=(operations.meta,),
    )

    def __init__(
        self,
        *,
        operations: Iterable[Operation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if operations is not None:
            NetworkModelCaseDefinition.operations.extend(self, operations)

    def add_operation(self, operation: Operation) -> Self:
        return NetworkModelCaseDefinition.operations.add(self, operation)

    def remove_operation(self, operation: Operation) -> Self:
        return NetworkModelCaseDefinition.operations.remove(self, operation)

    def clear_operations(self) -> Self:
        return NetworkModelCaseDefinition.operations.clear(self)

    def num_operation(self) -> int:
        return NetworkModelCaseDefinition.operations.count(self)
