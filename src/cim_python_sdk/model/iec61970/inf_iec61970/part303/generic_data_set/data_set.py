"""CIM class DataSet (TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.alternate_models.alternate_model import (
        AlternateModel,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_version import (
        ModelPartVersion,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.profile import Profile


class DataSet(CimObject):
    """A generic container of a version of instance data. The MRID can be used in an audit
    trail, not in reusable script intended to work with new versions of data.

    A dataset could be serialized multiple times and in multiple technologies, yet retain
    the same identity."""

    __slots__ = (
        "_alternate_model",
        "_model_part_version",
        "_profile",
        "description",
        "mrid",
        "name",
    )

    mrid: str | None
    name: str | None
    description: str | None

    model_part_version: One[ModelPartVersion] = One(
        EndMeta(
            name="model_part_version",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_version:ModelPartVersion",
            many=False,
            lower=1,
            upper=1,
            inverse="data_sets",
            aggregation="none",
        )
    )
    profile: Many[Profile] = Many(
        EndMeta(
            name="profile",
            cim_role="Profile",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.profile:Profile",
            many=True,
            lower=1,
            upper=None,
            inverse="data_set",
            aggregation="none",
        )
    )
    alternate_model: One[AlternateModel] = One(
        EndMeta(
            name="alternate_model",
            cim_role="AlternateModel",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.alternate_models.alternate_model:AlternateModel",
            many=False,
            lower=0,
            upper=1,
            inverse="dataset",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DataSet",
        package="TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet",
        guid="{28D05F59-6B53-4c1f-A18D-EE6B9CC533F9}",
        attributes=(
            AttrMeta("mrid", "mRID", "str", 0, 1, "primitive"),
            AttrMeta("name", "name", "str", 0, 1, "primitive"),
            AttrMeta("description", "description", "str", 0, 1, "primitive"),
        ),
        ends=(
            model_part_version.meta,
            profile.meta,
            alternate_model.meta,
        ),
    )

    def __init__(
        self,
        *,
        mrid: str | None = None,
        name: str | None = None,
        description: str | None = None,
        model_part_version: ModelPartVersion | None = None,
        profile: Iterable[Profile] | None = None,
        alternate_model: AlternateModel | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mrid = mrid
        self.name = name
        self.description = description
        if model_part_version is not None:
            self.model_part_version = model_part_version
        if profile is not None:
            DataSet.profile.extend(self, profile)
        if alternate_model is not None:
            self.alternate_model = alternate_model

    def add_profile(self, profile: Profile) -> Self:
        return DataSet.profile.add(self, profile)

    def remove_profile(self, profile: Profile) -> Self:
        return DataSet.profile.remove(self, profile)

    def clear_profile(self) -> Self:
        return DataSet.profile.clear(self)

    def num_profile(self) -> int:
        return DataSet.profile.count(self)

    def get_profile_by_mrid(self, mrid: str) -> Profile | None:
        return DataSet.profile.get_by_mrid(self, mrid)
