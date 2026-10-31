"""CIM class Profile (TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.data_set import DataSet


class Profile(IdentifiedObject):
    """Describes the existence of a profile. The MRID is usually defined as a static value by
    the document or artifact that defines the contents of the profile and the rules for
    using the profile."""

    __slots__ = ("_data_set",)

    data_set: Many[DataSet] = Many(
        EndMeta(
            name="data_set",
            cim_role="DataSet",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.data_set:DataSet",
            many=True,
            lower=0,
            upper=None,
            inverse="profile",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Profile",
        package="TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet",
        guid="{BC499E60-2398-46aa-A340-8421A864B0C1}",
        ends=(data_set.meta,),
    )

    def __init__(
        self,
        *,
        data_set: Iterable[DataSet] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if data_set is not None:
            Profile.data_set.extend(self, data_set)

    def add_data_set(self, data_set: DataSet) -> Self:
        return Profile.data_set.add(self, data_set)

    def remove_data_set(self, data_set: DataSet) -> Self:
        return Profile.data_set.remove(self, data_set)

    def clear_data_set(self) -> Self:
        return Profile.data_set.clear(self)

    def num_data_set(self) -> int:
        return Profile.data_set.count(self)

    def get_data_set_by_mrid(self, mrid: str) -> DataSet | None:
        return Profile.data_set.get_by_mrid(self, mrid)
