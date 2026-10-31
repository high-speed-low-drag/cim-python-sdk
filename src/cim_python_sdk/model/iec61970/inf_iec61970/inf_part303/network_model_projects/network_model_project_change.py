"""CIM class NetworkModelProjectChange (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component import (
    NetworkModelProjectComponent,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_change_version import (
        NetworkModelProjectChangeVersion,
    )


class NetworkModelProjectChange(NetworkModelProjectComponent):
    """Network model project change described by versions of an associated change set. Has
    persistent identity over multiple versions of the associated change set."""

    __slots__ = ("_network_model_project_change_version",)

    network_model_project_change_version: Many[NetworkModelProjectChangeVersion] = Many(
        EndMeta(
            name="network_model_project_change_version",
            cim_role="NetworkModelProjectChangeVersion",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_change_version:NetworkModelProjectChangeVersion",
            many=True,
            lower=1,
            upper=None,
            inverse="network_model_project_change",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelProjectChange",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{3BE1FB32-2A3E-4d65-8D09-B4F513D28FC6}",
        ends=(network_model_project_change_version.meta,),
    )

    def __init__(
        self,
        *,
        network_model_project_change_version: Iterable[NetworkModelProjectChangeVersion]
        | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if network_model_project_change_version is not None:
            NetworkModelProjectChange.network_model_project_change_version.extend(
                self, network_model_project_change_version
            )

    def add_network_model_project_change_version(
        self, network_model_project_change_version: NetworkModelProjectChangeVersion
    ) -> Self:
        return NetworkModelProjectChange.network_model_project_change_version.add(
            self, network_model_project_change_version
        )

    def remove_network_model_project_change_version(
        self, network_model_project_change_version: NetworkModelProjectChangeVersion
    ) -> Self:
        return NetworkModelProjectChange.network_model_project_change_version.remove(
            self, network_model_project_change_version
        )

    def clear_network_model_project_change_version(self) -> Self:
        return NetworkModelProjectChange.network_model_project_change_version.clear(self)

    def num_network_model_project_change_version(self) -> int:
        return NetworkModelProjectChange.network_model_project_change_version.count(self)

    def get_network_model_project_change_version_by_mrid(
        self, mrid: str
    ) -> NetworkModelProjectChangeVersion | None:
        return NetworkModelProjectChange.network_model_project_change_version.get_by_mrid(
            self, mrid
        )
