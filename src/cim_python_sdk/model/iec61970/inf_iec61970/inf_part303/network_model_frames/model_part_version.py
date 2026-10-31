"""CIM class ModelPartVersion (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_to_be_deleted import (
    ModelToBeDeleted,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.assembly_manifest import (
        AssemblyManifest,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.complete_model_to_be_deleted import (
        CompleteModelToBeDeleted,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_specification import (
        ModelPartSpecification,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.data_set import DataSet


class ModelPartVersion(ModelToBeDeleted):
    """This is a version of a part of a model. New instances of this class with new identity
    are instantiated upon changes to the content of this class or changes to the associated
    data set. Instances of this class are considered immutable. The case audit trail can
    reference this immutable data to exactly reproduce a case."""

    __slots__ = (
        "_assembly_manifests",
        "_complete_model_to_be_deleteds",
        "_data_sets",
        "_model_specification",
    )

    assembly_manifests: Many[AssemblyManifest] = Many(
        EndMeta(
            name="assembly_manifests",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.assembly_manifest:AssemblyManifest",
            many=True,
            lower=0,
            upper=None,
            inverse="model_part_versions",
            aggregation="none",
        )
    )
    data_sets: Many[DataSet] = Many(
        EndMeta(
            name="data_sets",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.data_set:DataSet",
            many=True,
            lower=0,
            upper=None,
            inverse="model_part_version",
            aggregation="none",
        )
    )
    complete_model_to_be_deleteds: Many[CompleteModelToBeDeleted] = Many(
        EndMeta(
            name="complete_model_to_be_deleteds",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.complete_model_to_be_deleted:CompleteModelToBeDeleted",
            many=True,
            lower=0,
            upper=None,
            inverse="model_part_versions",
            aggregation="none",
        )
    )
    model_specification: One[ModelPartSpecification] = One(
        EndMeta(
            name="model_specification",
            cim_role="ModelSpecification",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_specification:ModelPartSpecification",
            many=False,
            lower=1,
            upper=1,
            inverse="model",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ModelPartVersion",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{7B26D541-A396-4882-8F03-75BE30976A2F}",
        ends=(
            assembly_manifests.meta,
            data_sets.meta,
            complete_model_to_be_deleteds.meta,
            model_specification.meta,
        ),
    )

    def __init__(
        self,
        *,
        assembly_manifests: Iterable[AssemblyManifest] | None = None,
        data_sets: Iterable[DataSet] | None = None,
        complete_model_to_be_deleteds: Iterable[CompleteModelToBeDeleted] | None = None,
        model_specification: ModelPartSpecification | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if assembly_manifests is not None:
            ModelPartVersion.assembly_manifests.extend(self, assembly_manifests)
        if data_sets is not None:
            ModelPartVersion.data_sets.extend(self, data_sets)
        if complete_model_to_be_deleteds is not None:
            ModelPartVersion.complete_model_to_be_deleteds.extend(
                self, complete_model_to_be_deleteds
            )
        if model_specification is not None:
            self.model_specification = model_specification

    def add_assembly_manifest(self, assembly_manifest: AssemblyManifest) -> Self:
        return ModelPartVersion.assembly_manifests.add(self, assembly_manifest)

    def remove_assembly_manifest(self, assembly_manifest: AssemblyManifest) -> Self:
        return ModelPartVersion.assembly_manifests.remove(self, assembly_manifest)

    def clear_assembly_manifests(self) -> Self:
        return ModelPartVersion.assembly_manifests.clear(self)

    def num_assembly_manifest(self) -> int:
        return ModelPartVersion.assembly_manifests.count(self)

    def get_assembly_manifest_by_mrid(self, mrid: str) -> AssemblyManifest | None:
        return ModelPartVersion.assembly_manifests.get_by_mrid(self, mrid)

    def add_data_set(self, data_set: DataSet) -> Self:
        return ModelPartVersion.data_sets.add(self, data_set)

    def remove_data_set(self, data_set: DataSet) -> Self:
        return ModelPartVersion.data_sets.remove(self, data_set)

    def clear_data_sets(self) -> Self:
        return ModelPartVersion.data_sets.clear(self)

    def num_data_set(self) -> int:
        return ModelPartVersion.data_sets.count(self)

    def get_data_set_by_mrid(self, mrid: str) -> DataSet | None:
        return ModelPartVersion.data_sets.get_by_mrid(self, mrid)

    def add_complete_model_to_be_deleted(
        self, complete_model_to_be_deleted: CompleteModelToBeDeleted
    ) -> Self:
        return ModelPartVersion.complete_model_to_be_deleteds.add(
            self, complete_model_to_be_deleted
        )

    def remove_complete_model_to_be_deleted(
        self, complete_model_to_be_deleted: CompleteModelToBeDeleted
    ) -> Self:
        return ModelPartVersion.complete_model_to_be_deleteds.remove(
            self, complete_model_to_be_deleted
        )

    def clear_complete_model_to_be_deleteds(self) -> Self:
        return ModelPartVersion.complete_model_to_be_deleteds.clear(self)

    def num_complete_model_to_be_deleted(self) -> int:
        return ModelPartVersion.complete_model_to_be_deleteds.count(self)

    def get_complete_model_to_be_deleted_by_mrid(
        self, mrid: str
    ) -> CompleteModelToBeDeleted | None:
        return ModelPartVersion.complete_model_to_be_deleteds.get_by_mrid(self, mrid)
