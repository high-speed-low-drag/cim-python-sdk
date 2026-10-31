"""CIM class InstanceSet (TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.data_set import DataSet

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.dataset_arg import (
        DatasetArg,
    )


class InstanceSet(DataSet):
    """Instance of a version of a model part. This corresponds to a payload of instance data."""

    __slots__ = ("_dataset_arg", "_instance_set_member")

    dataset_arg: Many[DatasetArg] = Many(
        EndMeta(
            name="dataset_arg",
            cim_role="DatasetArg",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.model_operations.dataset_arg:DatasetArg",
            many=True,
            lower=0,
            upper=None,
            inverse="dataset",
            aggregation="none",
        )
    )
    instance_set_member: Many[IdentifiedObject] = Many(
        EndMeta(
            name="instance_set_member",
            cim_role="InstanceSetMember",
            target="cim_python_sdk.model.iec61970.base.core.identified_object:IdentifiedObject",
            many=True,
            lower=0,
            upper=None,
            inverse="instance_set",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InstanceSet",
        package="TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet",
        guid="{FEDB9C0B-593C-4a43-BB13-710F6141C1E3}",
        ends=(
            dataset_arg.meta,
            instance_set_member.meta,
        ),
    )

    def __init__(
        self,
        *,
        dataset_arg: Iterable[DatasetArg] | None = None,
        instance_set_member: Iterable[IdentifiedObject] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dataset_arg is not None:
            InstanceSet.dataset_arg.extend(self, dataset_arg)
        if instance_set_member is not None:
            InstanceSet.instance_set_member.extend(self, instance_set_member)

    def add_dataset_arg(self, dataset_arg: DatasetArg) -> Self:
        return InstanceSet.dataset_arg.add(self, dataset_arg)

    def remove_dataset_arg(self, dataset_arg: DatasetArg) -> Self:
        return InstanceSet.dataset_arg.remove(self, dataset_arg)

    def clear_dataset_arg(self) -> Self:
        return InstanceSet.dataset_arg.clear(self)

    def num_dataset_arg(self) -> int:
        return InstanceSet.dataset_arg.count(self)

    def get_dataset_arg_by_mrid(self, mrid: str) -> DatasetArg | None:
        return InstanceSet.dataset_arg.get_by_mrid(self, mrid)

    def add_instance_set_member(self, instance_set_member: IdentifiedObject) -> Self:
        return InstanceSet.instance_set_member.add(self, instance_set_member)

    def remove_instance_set_member(self, instance_set_member: IdentifiedObject) -> Self:
        return InstanceSet.instance_set_member.remove(self, instance_set_member)

    def clear_instance_set_member(self) -> Self:
        return InstanceSet.instance_set_member.clear(self)

    def num_instance_set_member(self) -> int:
        return InstanceSet.instance_set_member.count(self)

    def get_instance_set_member_by_mrid(self, mrid: str) -> IdentifiedObject | None:
        return InstanceSet.instance_set_member.get_by_mrid(self, mrid)
