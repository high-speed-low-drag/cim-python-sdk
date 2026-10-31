"""CIM class NetworkModelProjectDocument (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component import (
        NetworkModelProjectComponent,
    )


class NetworkModelProjectDocument(CimObject):
    """CIM class NetworkModelProjectDocument."""

    __slots__ = ("_network_model_project_components",)

    network_model_project_components: Many[NetworkModelProjectComponent] = Many(
        EndMeta(
            name="network_model_project_components",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component:NetworkModelProjectComponent",
            many=True,
            lower=0,
            upper=None,
            inverse="network_model_project_documents",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelProjectDocument",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{DCA0BAED-45FE-45d1-BBF3-32B22F2798A7}",
        ends=(network_model_project_components.meta,),
    )

    def __init__(
        self,
        *,
        network_model_project_components: Iterable[NetworkModelProjectComponent] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if network_model_project_components is not None:
            NetworkModelProjectDocument.network_model_project_components.extend(
                self, network_model_project_components
            )

    def add_network_model_project_component(
        self, network_model_project_component: NetworkModelProjectComponent
    ) -> Self:
        return NetworkModelProjectDocument.network_model_project_components.add(
            self, network_model_project_component
        )

    def remove_network_model_project_component(
        self, network_model_project_component: NetworkModelProjectComponent
    ) -> Self:
        return NetworkModelProjectDocument.network_model_project_components.remove(
            self, network_model_project_component
        )

    def clear_network_model_project_components(self) -> Self:
        return NetworkModelProjectDocument.network_model_project_components.clear(self)

    def num_network_model_project_component(self) -> int:
        return NetworkModelProjectDocument.network_model_project_components.count(self)

    def get_network_model_project_component_by_mrid(
        self, mrid: str
    ) -> NetworkModelProjectComponent | None:
        return NetworkModelProjectDocument.network_model_project_components.get_by_mrid(self, mrid)
