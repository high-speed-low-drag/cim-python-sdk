"""CIM class AssemblyDescription (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_specification import (
        ModelPartSpecification,
    )


class AssemblyDescription(IdentifiedObject):
    """A description for how to assemble model parts for a specific purpose."""

    __slots__ = ("_model_specification",)

    model_specification: Many[ModelPartSpecification] = Many(
        EndMeta(
            name="model_specification",
            cim_role="ModelSpecification",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_specification:ModelPartSpecification",
            many=True,
            lower=0,
            upper=None,
            inverse="assembly_description",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssemblyDescription",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{446D63EB-80BB-405f-A221-B70FF41142A3}",
        ends=(model_specification.meta,),
    )

    def __init__(
        self,
        *,
        model_specification: Iterable[ModelPartSpecification] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if model_specification is not None:
            AssemblyDescription.model_specification.extend(self, model_specification)

    def add_model_specification(self, model_specification: ModelPartSpecification) -> Self:
        return AssemblyDescription.model_specification.add(self, model_specification)

    def remove_model_specification(self, model_specification: ModelPartSpecification) -> Self:
        return AssemblyDescription.model_specification.remove(self, model_specification)

    def clear_model_specification(self) -> Self:
        return AssemblyDescription.model_specification.clear(self)

    def num_model_specification(self) -> int:
        return AssemblyDescription.model_specification.count(self)

    def get_model_specification_by_mrid(self, mrid: str) -> ModelPartSpecification | None:
        return AssemblyDescription.model_specification.get_by_mrid(self, mrid)
