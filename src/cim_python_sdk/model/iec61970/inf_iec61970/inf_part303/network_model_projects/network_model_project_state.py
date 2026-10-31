"""CIM class NetworkModelProjectState (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_change_version import (
        NetworkModelProjectChangeVersion,
    )


class NetworkModelProjectState(IdentifiedObject):
    """A network model project version state. States are agreed upon by the exchange community.
    Examples are "approved", "proposed", "withdrawn", "committed" etc."""

    __slots__ = ("_network_model_project_change_version",)

    network_model_project_change_version: Many[NetworkModelProjectChangeVersion] = Many(
        EndMeta(
            name="network_model_project_change_version",
            cim_role="NetworkModelProjectChangeVersion",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_change_version:NetworkModelProjectChangeVersion",
            many=True,
            lower=0,
            upper=None,
            inverse="network_model_project_state",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelProjectState",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{26500825-18B8-4dc5-99AC-56AFF0A87378}",
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
            NetworkModelProjectState.network_model_project_change_version.extend(
                self, network_model_project_change_version
            )

    def add_network_model_project_change_version(
        self, network_model_project_change_version: NetworkModelProjectChangeVersion
    ) -> Self:
        return NetworkModelProjectState.network_model_project_change_version.add(
            self, network_model_project_change_version
        )

    def remove_network_model_project_change_version(
        self, network_model_project_change_version: NetworkModelProjectChangeVersion
    ) -> Self:
        return NetworkModelProjectState.network_model_project_change_version.remove(
            self, network_model_project_change_version
        )

    def clear_network_model_project_change_version(self) -> Self:
        return NetworkModelProjectState.network_model_project_change_version.clear(self)

    def num_network_model_project_change_version(self) -> int:
        return NetworkModelProjectState.network_model_project_change_version.count(self)

    def get_network_model_project_change_version_by_mrid(
        self, mrid: str
    ) -> NetworkModelProjectChangeVersion | None:
        return NetworkModelProjectState.network_model_project_change_version.get_by_mrid(self, mrid)
