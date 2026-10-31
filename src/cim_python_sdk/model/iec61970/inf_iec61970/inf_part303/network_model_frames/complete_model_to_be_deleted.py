"""CIM class CompleteModelToBeDeleted (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
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
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_version import (
        ModelPartVersion,
    )


class CompleteModelToBeDeleted(ModelToBeDeleted):
    """A complete model can be used in applications to perform meaningful calculations, e.g. a
    study case in offline tools or a real time model in a SCADA/EMS."""

    __slots__ = ("_assembly_manifests", "_model_part_versions")

    assembly_manifests: Many[AssemblyManifest] = Many(
        EndMeta(
            name="assembly_manifests",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.assembly_manifest:AssemblyManifest",
            many=True,
            lower=0,
            upper=None,
            inverse="complete_model_to_be_deleted",
            aggregation="none",
        )
    )
    model_part_versions: Many[ModelPartVersion] = Many(
        EndMeta(
            name="model_part_versions",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_version:ModelPartVersion",
            many=True,
            lower=0,
            upper=None,
            inverse="complete_model_to_be_deleteds",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CompleteModelToBeDeleted",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{FE21071F-E121-4ec9-9733-6214F296C60E}",
        ends=(
            assembly_manifests.meta,
            model_part_versions.meta,
        ),
    )

    def __init__(
        self,
        *,
        assembly_manifests: Iterable[AssemblyManifest] | None = None,
        model_part_versions: Iterable[ModelPartVersion] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if assembly_manifests is not None:
            CompleteModelToBeDeleted.assembly_manifests.extend(self, assembly_manifests)
        if model_part_versions is not None:
            CompleteModelToBeDeleted.model_part_versions.extend(self, model_part_versions)

    def add_assembly_manifest(self, assembly_manifest: AssemblyManifest) -> Self:
        return CompleteModelToBeDeleted.assembly_manifests.add(self, assembly_manifest)

    def remove_assembly_manifest(self, assembly_manifest: AssemblyManifest) -> Self:
        return CompleteModelToBeDeleted.assembly_manifests.remove(self, assembly_manifest)

    def clear_assembly_manifests(self) -> Self:
        return CompleteModelToBeDeleted.assembly_manifests.clear(self)

    def num_assembly_manifest(self) -> int:
        return CompleteModelToBeDeleted.assembly_manifests.count(self)

    def get_assembly_manifest_by_mrid(self, mrid: str) -> AssemblyManifest | None:
        return CompleteModelToBeDeleted.assembly_manifests.get_by_mrid(self, mrid)

    def add_model_part_version(self, model_part_version: ModelPartVersion) -> Self:
        return CompleteModelToBeDeleted.model_part_versions.add(self, model_part_version)

    def remove_model_part_version(self, model_part_version: ModelPartVersion) -> Self:
        return CompleteModelToBeDeleted.model_part_versions.remove(self, model_part_version)

    def clear_model_part_versions(self) -> Self:
        return CompleteModelToBeDeleted.model_part_versions.clear(self)

    def num_model_part_version(self) -> int:
        return CompleteModelToBeDeleted.model_part_versions.count(self)

    def get_model_part_version_by_mrid(self, mrid: str) -> ModelPartVersion | None:
        return CompleteModelToBeDeleted.model_part_versions.get_by_mrid(self, mrid)
