"""CIM class NetworkModelProjectComponent (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project import (
        NetworkModelProject,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_document import (
        NetworkModelProjectDocument,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_relationship import (
        NetworkModelProjectRelationship,
    )


class NetworkModelProjectComponent(IdentifiedObject):
    """Abstract class for both a network model project and network model change."""

    __slots__ = (
        "_containing_project",
        "_network_model_project_documents",
        "_project_a_relationships",
        "_project_b_relationships",
    )

    network_model_project_documents: Many[NetworkModelProjectDocument] = Many(
        EndMeta(
            name="network_model_project_documents",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_document:NetworkModelProjectDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="network_model_project_components",
            aggregation="none",
        )
    )
    containing_project: One[NetworkModelProject] = One(
        EndMeta(
            name="containing_project",
            cim_role="ContainingProject",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project:NetworkModelProject",
            many=False,
            lower=1,
            upper=1,
            inverse="contained_project",
            aggregation="none",
        )
    )
    project_a_relationships: Many[NetworkModelProjectRelationship] = Many(
        EndMeta(
            name="project_a_relationships",
            cim_role="ProjectARelationships",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_relationship:NetworkModelProjectRelationship",
            many=True,
            lower=0,
            upper=None,
            inverse="project_a",
            aggregation="none",
        )
    )
    project_b_relationships: Many[NetworkModelProjectRelationship] = Many(
        EndMeta(
            name="project_b_relationships",
            cim_role="ProjectBRelationships",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_relationship:NetworkModelProjectRelationship",
            many=True,
            lower=0,
            upper=None,
            inverse="project_b",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelProjectComponent",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{B2433B1C-C4C4-4f2d-B57E-ECB3BB008AAD}",
        ends=(
            network_model_project_documents.meta,
            containing_project.meta,
            project_a_relationships.meta,
            project_b_relationships.meta,
        ),
    )

    def __init__(
        self,
        *,
        network_model_project_documents: Iterable[NetworkModelProjectDocument] | None = None,
        containing_project: NetworkModelProject | None = None,
        project_a_relationships: Iterable[NetworkModelProjectRelationship] | None = None,
        project_b_relationships: Iterable[NetworkModelProjectRelationship] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if network_model_project_documents is not None:
            NetworkModelProjectComponent.network_model_project_documents.extend(
                self, network_model_project_documents
            )
        if containing_project is not None:
            self.containing_project = containing_project
        if project_a_relationships is not None:
            NetworkModelProjectComponent.project_a_relationships.extend(
                self, project_a_relationships
            )
        if project_b_relationships is not None:
            NetworkModelProjectComponent.project_b_relationships.extend(
                self, project_b_relationships
            )

    def add_network_model_project_document(
        self, network_model_project_document: NetworkModelProjectDocument
    ) -> Self:
        return NetworkModelProjectComponent.network_model_project_documents.add(
            self, network_model_project_document
        )

    def remove_network_model_project_document(
        self, network_model_project_document: NetworkModelProjectDocument
    ) -> Self:
        return NetworkModelProjectComponent.network_model_project_documents.remove(
            self, network_model_project_document
        )

    def clear_network_model_project_documents(self) -> Self:
        return NetworkModelProjectComponent.network_model_project_documents.clear(self)

    def num_network_model_project_document(self) -> int:
        return NetworkModelProjectComponent.network_model_project_documents.count(self)

    def add_project_a_relationship(
        self, project_a_relationship: NetworkModelProjectRelationship
    ) -> Self:
        return NetworkModelProjectComponent.project_a_relationships.add(
            self, project_a_relationship
        )

    def remove_project_a_relationship(
        self, project_a_relationship: NetworkModelProjectRelationship
    ) -> Self:
        return NetworkModelProjectComponent.project_a_relationships.remove(
            self, project_a_relationship
        )

    def clear_project_a_relationships(self) -> Self:
        return NetworkModelProjectComponent.project_a_relationships.clear(self)

    def num_project_a_relationship(self) -> int:
        return NetworkModelProjectComponent.project_a_relationships.count(self)

    def get_project_a_relationship_by_mrid(
        self, mrid: str
    ) -> NetworkModelProjectRelationship | None:
        return NetworkModelProjectComponent.project_a_relationships.get_by_mrid(self, mrid)

    def add_project_b_relationship(
        self, project_b_relationship: NetworkModelProjectRelationship
    ) -> Self:
        return NetworkModelProjectComponent.project_b_relationships.add(
            self, project_b_relationship
        )

    def remove_project_b_relationship(
        self, project_b_relationship: NetworkModelProjectRelationship
    ) -> Self:
        return NetworkModelProjectComponent.project_b_relationships.remove(
            self, project_b_relationship
        )

    def clear_project_b_relationships(self) -> Self:
        return NetworkModelProjectComponent.project_b_relationships.clear(self)

    def num_project_b_relationship(self) -> int:
        return NetworkModelProjectComponent.project_b_relationships.count(self)

    def get_project_b_relationship_by_mrid(
        self, mrid: str
    ) -> NetworkModelProjectRelationship | None:
        return NetworkModelProjectComponent.project_b_relationships.get_by_mrid(self, mrid)
