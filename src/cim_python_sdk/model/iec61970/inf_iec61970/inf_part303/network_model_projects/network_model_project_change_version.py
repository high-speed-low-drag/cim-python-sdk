"""CIM class NetworkModelProjectChangeVersion (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_change import (
        NetworkModelProjectChange,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_state import (
        NetworkModelProjectState,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set import (
        ChangeSet,
    )


class NetworkModelProjectChangeVersion(IdentifiedObject):
    """Describes the status and the planned implementation of the associated change set into
    the as-built model. New instances of this class with new identity are instantiated upon
    changes to the content of this class or changes to the associated change set. Instances
    of this class are considered immutable. The case audit trail can reference this
    immutable data to exactly reproduce a case."""

    __slots__ = (
        "_change_set",
        "_network_model_project_change",
        "_network_model_project_state",
        "_superceded_by",
        "_supercedes",
        "comment",
        "effective_date_time",
        "time_stamp",
    )

    comment: str | None
    effective_date_time: _dt.datetime | None
    time_stamp: _dt.datetime | None

    network_model_project_state: One[NetworkModelProjectState] = One(
        EndMeta(
            name="network_model_project_state",
            cim_role="NetworkModelProjectState",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_state:NetworkModelProjectState",
            many=False,
            lower=0,
            upper=1,
            inverse="network_model_project_change_version",
            aggregation="none",
        )
    )
    superceded_by: One[NetworkModelProjectChangeVersion] = One(
        EndMeta(
            name="superceded_by",
            cim_role="SupercededBy",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_change_version:NetworkModelProjectChangeVersion",
            many=False,
            lower=0,
            upper=1,
            inverse="supercedes",
            aggregation="none",
        )
    )
    supercedes: One[NetworkModelProjectChangeVersion] = One(
        EndMeta(
            name="supercedes",
            cim_role="Supercedes",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_change_version:NetworkModelProjectChangeVersion",
            many=False,
            lower=0,
            upper=1,
            inverse="superceded_by",
            aggregation="none",
        )
    )
    change_set: One[ChangeSet] = One(
        EndMeta(
            name="change_set",
            cim_role="ChangeSet",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set:ChangeSet",
            many=False,
            lower=0,
            upper=1,
            inverse="network_model_project_change_version",
            aggregation="none",
        )
    )
    network_model_project_change: One[NetworkModelProjectChange] = One(
        EndMeta(
            name="network_model_project_change",
            cim_role="NetworkModelProjectChange",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_change:NetworkModelProjectChange",
            many=False,
            lower=1,
            upper=1,
            inverse="network_model_project_change_version",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelProjectChangeVersion",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{DC8F905B-85AF-46f5-9233-C494C3942C12}",
        attributes=(
            AttrMeta("comment", "comment", "str", 0, 1, "primitive"),
            AttrMeta("effective_date_time", "effectiveDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("time_stamp", "timeStamp", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            network_model_project_state.meta,
            superceded_by.meta,
            supercedes.meta,
            change_set.meta,
            network_model_project_change.meta,
        ),
    )

    def __init__(
        self,
        *,
        comment: str | None = None,
        effective_date_time: _dt.datetime | None = None,
        time_stamp: _dt.datetime | None = None,
        network_model_project_state: NetworkModelProjectState | None = None,
        superceded_by: NetworkModelProjectChangeVersion | None = None,
        supercedes: NetworkModelProjectChangeVersion | None = None,
        change_set: ChangeSet | None = None,
        network_model_project_change: NetworkModelProjectChange | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.comment = comment
        self.effective_date_time = effective_date_time
        self.time_stamp = time_stamp
        if network_model_project_state is not None:
            self.network_model_project_state = network_model_project_state
        if superceded_by is not None:
            self.superceded_by = superceded_by
        if supercedes is not None:
            self.supercedes = supercedes
        if change_set is not None:
            self.change_set = change_set
        if network_model_project_change is not None:
            self.network_model_project_change = network_model_project_change
