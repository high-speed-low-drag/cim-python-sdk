"""CIM class NetworkModelProjectComponent2 (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.current_state import (
        CurrentState,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project2 import (
        NetworkModelProject2,
    )


class NetworkModelProjectComponent2(IdentifiedObject):
    """CIM class NetworkModelProjectComponent2."""

    __slots__ = ("_current_state", "_parent", "closed", "created", "updated", "version")

    version: int | None
    created: _dt.datetime | None
    closed: _dt.datetime | None
    updated: _dt.datetime | None

    parent: One[NetworkModelProject2] = One(
        EndMeta(
            name="parent",
            cim_role="Parent",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project2:NetworkModelProject2",
            many=False,
            lower=0,
            upper=1,
            inverse="child",
            aggregation="none",
        )
    )
    current_state: One[CurrentState] = One(
        EndMeta(
            name="current_state",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.current_state:CurrentState",
            many=False,
            lower=1,
            upper=1,
            inverse="network_model_project_component2s",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelProjectComponent2",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{B71281F5-4070-444e-9D7A-42C7D9DE600A}",
        attributes=(
            AttrMeta("version", "version", "int", 0, 1, "primitive"),
            AttrMeta("created", "created", "datetime", 0, 1, "primitive"),
            AttrMeta("closed", "closed", "datetime", 0, 1, "primitive"),
            AttrMeta("updated", "updated", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            parent.meta,
            current_state.meta,
        ),
    )

    def __init__(
        self,
        *,
        version: int | None = None,
        created: _dt.datetime | None = None,
        closed: _dt.datetime | None = None,
        updated: _dt.datetime | None = None,
        parent: NetworkModelProject2 | None = None,
        current_state: CurrentState | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.version = version
        self.created = created
        self.closed = closed
        self.updated = updated
        if parent is not None:
            self.parent = parent
        if current_state is not None:
            self.current_state = current_state
