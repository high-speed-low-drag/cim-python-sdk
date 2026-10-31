"""CIM class NetworkModelProjectStage (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component2 import (
    NetworkModelProjectComponent2,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.annotated_project_dependency import (
        AnnotatedProjectDependency,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set import (
        ChangeSet,
    )


class NetworkModelProjectStage(NetworkModelProjectComponent2):
    """CIM class NetworkModelProjectStage."""

    __slots__ = (
        "_change_sets",
        "_denpendecy_depending_stage",
        "_dependency_dependent_on_stage",
        "changeset_version",
        "commissioned_date",
        "planned_commissioned_date",
    )

    changeset_version: int | None
    planned_commissioned_date: _dt.datetime | None
    commissioned_date: _dt.datetime | None

    change_sets: Many[ChangeSet] = Many(
        EndMeta(
            name="change_sets",
            cim_role="ChangeSets",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set:ChangeSet",
            many=True,
            lower=1,
            upper=None,
            inverse="nm_project_stage",
            aggregation="none",
        )
    )
    denpendecy_depending_stage: Many[AnnotatedProjectDependency] = Many(
        EndMeta(
            name="denpendecy_depending_stage",
            cim_role="DenpendecyDependingStage",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.annotated_project_dependency:AnnotatedProjectDependency",
            many=True,
            lower=0,
            upper=None,
            inverse="depending_stage",
            aggregation="none",
        )
    )
    dependency_dependent_on_stage: One[AnnotatedProjectDependency] = One(
        EndMeta(
            name="dependency_dependent_on_stage",
            cim_role="DependencyDependentOnStage",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.annotated_project_dependency:AnnotatedProjectDependency",
            many=False,
            lower=0,
            upper=1,
            inverse="dependent_on_stage",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelProjectStage",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{43AABFB5-F2C5-475d-9648-EC752AF6C0BB}",
        attributes=(
            AttrMeta("changeset_version", "changesetVersion", "int", 0, 1, "primitive"),
            AttrMeta(
                "planned_commissioned_date",
                "plannedCommissionedDate",
                "datetime",
                0,
                1,
                "primitive",
            ),
            AttrMeta("commissioned_date", "commissionedDate", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            change_sets.meta,
            denpendecy_depending_stage.meta,
            dependency_dependent_on_stage.meta,
        ),
    )

    def __init__(
        self,
        *,
        changeset_version: int | None = None,
        planned_commissioned_date: _dt.datetime | None = None,
        commissioned_date: _dt.datetime | None = None,
        change_sets: Iterable[ChangeSet] | None = None,
        denpendecy_depending_stage: Iterable[AnnotatedProjectDependency] | None = None,
        dependency_dependent_on_stage: AnnotatedProjectDependency | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.changeset_version = changeset_version
        self.planned_commissioned_date = planned_commissioned_date
        self.commissioned_date = commissioned_date
        if change_sets is not None:
            NetworkModelProjectStage.change_sets.extend(self, change_sets)
        if denpendecy_depending_stage is not None:
            NetworkModelProjectStage.denpendecy_depending_stage.extend(
                self, denpendecy_depending_stage
            )
        if dependency_dependent_on_stage is not None:
            self.dependency_dependent_on_stage = dependency_dependent_on_stage

    def add_change_set(self, change_set: ChangeSet) -> Self:
        return NetworkModelProjectStage.change_sets.add(self, change_set)

    def remove_change_set(self, change_set: ChangeSet) -> Self:
        return NetworkModelProjectStage.change_sets.remove(self, change_set)

    def clear_change_sets(self) -> Self:
        return NetworkModelProjectStage.change_sets.clear(self)

    def num_change_set(self) -> int:
        return NetworkModelProjectStage.change_sets.count(self)

    def get_change_set_by_mrid(self, mrid: str) -> ChangeSet | None:
        return NetworkModelProjectStage.change_sets.get_by_mrid(self, mrid)

    def add_denpendecy_depending_stage(
        self, denpendecy_depending_stage: AnnotatedProjectDependency
    ) -> Self:
        return NetworkModelProjectStage.denpendecy_depending_stage.add(
            self, denpendecy_depending_stage
        )

    def remove_denpendecy_depending_stage(
        self, denpendecy_depending_stage: AnnotatedProjectDependency
    ) -> Self:
        return NetworkModelProjectStage.denpendecy_depending_stage.remove(
            self, denpendecy_depending_stage
        )

    def clear_denpendecy_depending_stage(self) -> Self:
        return NetworkModelProjectStage.denpendecy_depending_stage.clear(self)

    def num_denpendecy_depending_stage(self) -> int:
        return NetworkModelProjectStage.denpendecy_depending_stage.count(self)

    def get_denpendecy_depending_stage_by_mrid(
        self, mrid: str
    ) -> AnnotatedProjectDependency | None:
        return NetworkModelProjectStage.denpendecy_depending_stage.get_by_mrid(self, mrid)
