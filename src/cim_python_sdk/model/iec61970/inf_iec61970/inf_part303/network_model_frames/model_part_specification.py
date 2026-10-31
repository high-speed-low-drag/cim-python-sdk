"""CIM class ModelPartSpecification (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.assembly_description import (
        AssemblyDescription,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_authority_set import (
        ModelAuthoritySet,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_version import (
        ModelPartVersion,
    )


class ModelPartSpecification(IdentifiedObject):
    """The type of model. For example, state estimator, planning, planning dynamics, short
    circuit, or real-time dynamics etc. The model must conform to a profile."""

    __slots__ = ("_assembly_description", "_framework_part", "_model")

    assembly_description: Many[AssemblyDescription] = Many(
        EndMeta(
            name="assembly_description",
            cim_role="AssemblyDescription",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.assembly_description:AssemblyDescription",
            many=True,
            lower=0,
            upper=None,
            inverse="model_specification",
            aggregation="none",
        )
    )
    model: Many[ModelPartVersion] = Many(
        EndMeta(
            name="model",
            cim_role="Model",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_version:ModelPartVersion",
            many=True,
            lower=0,
            upper=None,
            inverse="model_specification",
            aggregation="none",
        )
    )
    framework_part: One[ModelAuthoritySet] = One(
        EndMeta(
            name="framework_part",
            cim_role="FrameworkPart",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_authority_set:ModelAuthoritySet",
            many=False,
            lower=0,
            upper=1,
            inverse="model_specification",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ModelPartSpecification",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{763139C3-DC02-4af5-9CFC-AB46D2F47180}",
        ends=(
            assembly_description.meta,
            model.meta,
            framework_part.meta,
        ),
    )

    def __init__(
        self,
        *,
        assembly_description: Iterable[AssemblyDescription] | None = None,
        model: Iterable[ModelPartVersion] | None = None,
        framework_part: ModelAuthoritySet | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if assembly_description is not None:
            ModelPartSpecification.assembly_description.extend(self, assembly_description)
        if model is not None:
            ModelPartSpecification.model.extend(self, model)
        if framework_part is not None:
            self.framework_part = framework_part

    def add_assembly_description(self, assembly_description: AssemblyDescription) -> Self:
        return ModelPartSpecification.assembly_description.add(self, assembly_description)

    def remove_assembly_description(self, assembly_description: AssemblyDescription) -> Self:
        return ModelPartSpecification.assembly_description.remove(self, assembly_description)

    def clear_assembly_description(self) -> Self:
        return ModelPartSpecification.assembly_description.clear(self)

    def num_assembly_description(self) -> int:
        return ModelPartSpecification.assembly_description.count(self)

    def get_assembly_description_by_mrid(self, mrid: str) -> AssemblyDescription | None:
        return ModelPartSpecification.assembly_description.get_by_mrid(self, mrid)

    def add_model(self, model: ModelPartVersion) -> Self:
        return ModelPartSpecification.model.add(self, model)

    def remove_model(self, model: ModelPartVersion) -> Self:
        return ModelPartSpecification.model.remove(self, model)

    def clear_model(self) -> Self:
        return ModelPartSpecification.model.clear(self)

    def num_model(self) -> int:
        return ModelPartSpecification.model.count(self)

    def get_model_by_mrid(self, mrid: str) -> ModelPartVersion | None:
        return ModelPartSpecification.model.get_by_mrid(self, mrid)
