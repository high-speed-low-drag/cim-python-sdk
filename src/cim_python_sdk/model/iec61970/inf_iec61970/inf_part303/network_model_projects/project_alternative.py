"""CIM class ProjectAlternative (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_relationship import (
    NetworkModelProjectRelationship,
)


class ProjectAlternative(NetworkModelProjectRelationship):
    """Project B is an alternative to project A. Project A is the primary alternative.

    Multiple project alternatives should not be selected into a single network study case."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="ProjectAlternative",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{CAC3DF1E-520C-4d51-AFBC-7B5D3751B91D}",
    )
