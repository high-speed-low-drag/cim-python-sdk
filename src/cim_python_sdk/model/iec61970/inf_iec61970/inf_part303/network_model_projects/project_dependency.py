"""CIM class ProjectDependency (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_relationship import (
    NetworkModelProjectRelationship,
)


class ProjectDependency(NetworkModelProjectRelationship):
    """Project A change sets should be applied before Project B during case creation."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="ProjectDependency",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{6233873A-EEF6-4d78-8033-AFD194028490}",
    )
