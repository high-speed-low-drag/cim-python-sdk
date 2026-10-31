"""CIM class CurrentState (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component2 import (
        NetworkModelProjectComponent2,
    )


class CurrentState(IdentifiedObject):
    """CIM class CurrentState."""

    __slots__ = ("_network_model_project_component2s",)

    network_model_project_component2s: Many[NetworkModelProjectComponent2] = Many(
        EndMeta(
            name="network_model_project_component2s",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component2:NetworkModelProjectComponent2",
            many=True,
            lower=0,
            upper=None,
            inverse="current_state",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CurrentState",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{68BF5F3C-57C0-4961-B749-E4706391D883}",
        ends=(network_model_project_component2s.meta,),
    )

    def __init__(
        self,
        *,
        network_model_project_component2s: Iterable[NetworkModelProjectComponent2] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if network_model_project_component2s is not None:
            CurrentState.network_model_project_component2s.extend(
                self, network_model_project_component2s
            )

    def add_network_model_project_component2(
        self, network_model_project_component2: NetworkModelProjectComponent2
    ) -> Self:
        return CurrentState.network_model_project_component2s.add(
            self, network_model_project_component2
        )

    def remove_network_model_project_component2(
        self, network_model_project_component2: NetworkModelProjectComponent2
    ) -> Self:
        return CurrentState.network_model_project_component2s.remove(
            self, network_model_project_component2
        )

    def clear_network_model_project_component2s(self) -> Self:
        return CurrentState.network_model_project_component2s.clear(self)

    def num_network_model_project_component2(self) -> int:
        return CurrentState.network_model_project_component2s.count(self)

    def get_network_model_project_component2_by_mrid(
        self, mrid: str
    ) -> NetworkModelProjectComponent2 | None:
        return CurrentState.network_model_project_component2s.get_by_mrid(self, mrid)
