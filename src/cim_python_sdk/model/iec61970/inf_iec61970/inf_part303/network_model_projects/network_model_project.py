"""CIM class NetworkModelProject (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component import (
    NetworkModelProjectComponent,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self


class NetworkModelProject(NetworkModelProjectComponent):
    """A grouping of network model change descriptions. Primarily used to organize the phases
    of an overall project."""

    __slots__ = ("_contained_project",)

    contained_project: Many[NetworkModelProjectComponent] = Many(
        EndMeta(
            name="contained_project",
            cim_role="ContainedProject",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component:NetworkModelProjectComponent",
            many=True,
            lower=0,
            upper=None,
            inverse="containing_project",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelProject",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{39DCFCF6-80FC-4183-820D-4390F0E260FC}",
        ends=(contained_project.meta,),
    )

    def __init__(
        self,
        *,
        contained_project: Iterable[NetworkModelProjectComponent] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if contained_project is not None:
            NetworkModelProject.contained_project.extend(self, contained_project)

    def add_contained_project(self, contained_project: NetworkModelProjectComponent) -> Self:
        return NetworkModelProject.contained_project.add(self, contained_project)

    def remove_contained_project(self, contained_project: NetworkModelProjectComponent) -> Self:
        return NetworkModelProject.contained_project.remove(self, contained_project)

    def clear_contained_project(self) -> Self:
        return NetworkModelProject.contained_project.clear(self)

    def num_contained_project(self) -> int:
        return NetworkModelProject.contained_project.count(self)

    def get_contained_project_by_mrid(self, mrid: str) -> NetworkModelProjectComponent | None:
        return NetworkModelProject.contained_project.get_by_mrid(self, mrid)
