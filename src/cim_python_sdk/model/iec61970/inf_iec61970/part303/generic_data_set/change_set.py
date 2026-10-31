"""CIM class ChangeSet (TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.data_set import DataSet

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.incremental_dataset_arg import (
        IncrementalDatasetArg,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_change_version import (
        NetworkModelProjectChangeVersion,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_stage import (
        NetworkModelProjectStage,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set_member import (
        ChangeSetMember,
    )


class ChangeSet(DataSet):
    """Describes a set of changes that can be applied in different situations. A given
    registered target object MRID may only be referenced once by the contained change set
    members."""

    __slots__ = (
        "_change_set_member",
        "_incremental_dataset_arg",
        "_network_model_project_change_version",
        "_nm_project_stage",
    )

    incremental_dataset_arg: Many[IncrementalDatasetArg] = Many(
        EndMeta(
            name="incremental_dataset_arg",
            cim_role="IncrementalDatasetArg",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.incremental_dataset_arg:IncrementalDatasetArg",
            many=True,
            lower=0,
            upper=None,
            inverse="incremental_dataset",
            aggregation="none",
        )
    )
    nm_project_stage: One[NetworkModelProjectStage] = One(
        EndMeta(
            name="nm_project_stage",
            cim_role="NMProjectStage",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_stage:NetworkModelProjectStage",
            many=False,
            lower=0,
            upper=1,
            inverse="change_sets",
            aggregation="none",
        )
    )
    network_model_project_change_version: Many[NetworkModelProjectChangeVersion] = Many(
        EndMeta(
            name="network_model_project_change_version",
            cim_role="NetworkModelProjectChangeVersion",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_change_version:NetworkModelProjectChangeVersion",
            many=True,
            lower=0,
            upper=None,
            inverse="change_set",
            aggregation="none",
        )
    )
    change_set_member: Many[ChangeSetMember] = Many(
        EndMeta(
            name="change_set_member",
            cim_role="ChangeSetMember",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set_member:ChangeSetMember",
            many=True,
            lower=0,
            upper=None,
            inverse="changeset",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ChangeSet",
        package="TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet",
        guid="{EDB0ACC9-0CE3-439f-ADC6-2D753A220486}",
        ends=(
            incremental_dataset_arg.meta,
            nm_project_stage.meta,
            network_model_project_change_version.meta,
            change_set_member.meta,
        ),
    )

    def __init__(
        self,
        *,
        incremental_dataset_arg: Iterable[IncrementalDatasetArg] | None = None,
        nm_project_stage: NetworkModelProjectStage | None = None,
        network_model_project_change_version: Iterable[NetworkModelProjectChangeVersion]
        | None = None,
        change_set_member: Iterable[ChangeSetMember] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if incremental_dataset_arg is not None:
            ChangeSet.incremental_dataset_arg.extend(self, incremental_dataset_arg)
        if nm_project_stage is not None:
            self.nm_project_stage = nm_project_stage
        if network_model_project_change_version is not None:
            ChangeSet.network_model_project_change_version.extend(
                self, network_model_project_change_version
            )
        if change_set_member is not None:
            ChangeSet.change_set_member.extend(self, change_set_member)

    def add_incremental_dataset_arg(self, incremental_dataset_arg: IncrementalDatasetArg) -> Self:
        return ChangeSet.incremental_dataset_arg.add(self, incremental_dataset_arg)

    def remove_incremental_dataset_arg(
        self, incremental_dataset_arg: IncrementalDatasetArg
    ) -> Self:
        return ChangeSet.incremental_dataset_arg.remove(self, incremental_dataset_arg)

    def clear_incremental_dataset_arg(self) -> Self:
        return ChangeSet.incremental_dataset_arg.clear(self)

    def num_incremental_dataset_arg(self) -> int:
        return ChangeSet.incremental_dataset_arg.count(self)

    def get_incremental_dataset_arg_by_mrid(self, mrid: str) -> IncrementalDatasetArg | None:
        return ChangeSet.incremental_dataset_arg.get_by_mrid(self, mrid)

    def add_network_model_project_change_version(
        self, network_model_project_change_version: NetworkModelProjectChangeVersion
    ) -> Self:
        return ChangeSet.network_model_project_change_version.add(
            self, network_model_project_change_version
        )

    def remove_network_model_project_change_version(
        self, network_model_project_change_version: NetworkModelProjectChangeVersion
    ) -> Self:
        return ChangeSet.network_model_project_change_version.remove(
            self, network_model_project_change_version
        )

    def clear_network_model_project_change_version(self) -> Self:
        return ChangeSet.network_model_project_change_version.clear(self)

    def num_network_model_project_change_version(self) -> int:
        return ChangeSet.network_model_project_change_version.count(self)

    def get_network_model_project_change_version_by_mrid(
        self, mrid: str
    ) -> NetworkModelProjectChangeVersion | None:
        return ChangeSet.network_model_project_change_version.get_by_mrid(self, mrid)

    def add_change_set_member(self, change_set_member: ChangeSetMember) -> Self:
        return ChangeSet.change_set_member.add(self, change_set_member)

    def remove_change_set_member(self, change_set_member: ChangeSetMember) -> Self:
        return ChangeSet.change_set_member.remove(self, change_set_member)

    def clear_change_set_member(self) -> Self:
        return ChangeSet.change_set_member.clear(self)

    def num_change_set_member(self) -> int:
        return ChangeSet.change_set_member.count(self)
