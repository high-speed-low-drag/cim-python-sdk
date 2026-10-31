"""CIM class AnnotatedProjectDependency (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.dependency_kind import (
        DependencyKind,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_stage import (
        NetworkModelProjectStage,
    )


class AnnotatedProjectDependency(IdentifiedObject):
    """CIM class AnnotatedProjectDependency."""

    __slots__ = ("_dependent_on_stage", "_depending_stage", "dependency_type")

    dependency_type: DependencyKind | None

    depending_stage: One[NetworkModelProjectStage] = One(
        EndMeta(
            name="depending_stage",
            cim_role="DependingStage",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_stage:NetworkModelProjectStage",
            many=False,
            lower=1,
            upper=1,
            inverse="denpendecy_depending_stage",
            aggregation="none",
        )
    )
    dependent_on_stage: One[NetworkModelProjectStage] = One(
        EndMeta(
            name="dependent_on_stage",
            cim_role="DependentOnStage",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_stage:NetworkModelProjectStage",
            many=False,
            lower=1,
            upper=1,
            inverse="dependency_dependent_on_stage",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AnnotatedProjectDependency",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{03CC228C-C9FF-4ffd-9F8E-760435D9D1C4}",
        attributes=(
            AttrMeta("dependency_type", "dependencyType", "DependencyKind", 0, 1, "enumeration"),
        ),
        ends=(
            depending_stage.meta,
            dependent_on_stage.meta,
        ),
    )

    def __init__(
        self,
        *,
        dependency_type: DependencyKind | None = None,
        depending_stage: NetworkModelProjectStage | None = None,
        dependent_on_stage: NetworkModelProjectStage | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dependency_type = dependency_type
        if depending_stage is not None:
            self.depending_stage = depending_stage
        if dependent_on_stage is not None:
            self.dependent_on_stage = dependent_on_stage
