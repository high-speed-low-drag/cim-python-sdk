"""CIM class AssemblyManifest (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.complete_model_to_be_deleted import (
        CompleteModelToBeDeleted,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_version import (
        ModelPartVersion,
    )


class AssemblyManifest(IdentifiedObject):
    """A collection of model parts when combined form a case or part of a case."""

    __slots__ = ("_complete_model_to_be_deleted", "_model_part_versions")

    model_part_versions: Many[ModelPartVersion] = Many(
        EndMeta(
            name="model_part_versions",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_version:ModelPartVersion",
            many=True,
            lower=0,
            upper=None,
            inverse="assembly_manifests",
            aggregation="none",
        )
    )
    complete_model_to_be_deleted: One[CompleteModelToBeDeleted] = One(
        EndMeta(
            name="complete_model_to_be_deleted",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.complete_model_to_be_deleted:CompleteModelToBeDeleted",
            many=False,
            lower=0,
            upper=1,
            inverse="assembly_manifests",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssemblyManifest",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{FC8FF3BB-E525-4d7c-A1E4-6B1C3320C6D9}",
        ends=(
            model_part_versions.meta,
            complete_model_to_be_deleted.meta,
        ),
    )

    def __init__(
        self,
        *,
        model_part_versions: Iterable[ModelPartVersion] | None = None,
        complete_model_to_be_deleted: CompleteModelToBeDeleted | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if model_part_versions is not None:
            AssemblyManifest.model_part_versions.extend(self, model_part_versions)
        if complete_model_to_be_deleted is not None:
            self.complete_model_to_be_deleted = complete_model_to_be_deleted

    def add_model_part_version(self, model_part_version: ModelPartVersion) -> Self:
        return AssemblyManifest.model_part_versions.add(self, model_part_version)

    def remove_model_part_version(self, model_part_version: ModelPartVersion) -> Self:
        return AssemblyManifest.model_part_versions.remove(self, model_part_version)

    def clear_model_part_versions(self) -> Self:
        return AssemblyManifest.model_part_versions.clear(self)

    def num_model_part_version(self) -> int:
        return AssemblyManifest.model_part_versions.count(self)

    def get_model_part_version_by_mrid(self, mrid: str) -> ModelPartVersion | None:
        return AssemblyManifest.model_part_versions.get_by_mrid(self, mrid)
