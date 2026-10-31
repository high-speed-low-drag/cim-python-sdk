"""CIM class NetworkModelProjectRelationship (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component import (
        NetworkModelProjectComponent,
    )


class NetworkModelProjectRelationship(IdentifiedObject):
    """A relationship that assists humans and software building cases by assembling project
    changes in the correct sequence. This class may be specialized to create specific types
    of relationships."""

    __slots__ = ("_project_a", "_project_b")

    project_a: One[NetworkModelProjectComponent] = One(
        EndMeta(
            name="project_a",
            cim_role="ProjectA",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component:NetworkModelProjectComponent",
            many=False,
            lower=1,
            upper=1,
            inverse="project_a_relationships",
            aggregation="none",
        )
    )
    project_b: One[NetworkModelProjectComponent] = One(
        EndMeta(
            name="project_b",
            cim_role="ProjectB",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component:NetworkModelProjectComponent",
            many=False,
            lower=1,
            upper=1,
            inverse="project_b_relationships",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelProjectRelationship",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{6437D5D0-8803-45ba-8075-BE458D7F09E0}",
        ends=(
            project_a.meta,
            project_b.meta,
        ),
    )

    def __init__(
        self,
        *,
        project_a: NetworkModelProjectComponent | None = None,
        project_b: NetworkModelProjectComponent | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if project_a is not None:
            self.project_a = project_a
        if project_b is not None:
            self.project_b = project_b
