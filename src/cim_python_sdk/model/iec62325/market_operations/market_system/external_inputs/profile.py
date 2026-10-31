"""CIM class Profile (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.profile_data import (
        ProfileData,
    )


class Profile(IdentifiedObject):
    """A profile is a simpler curve type."""

    __slots__ = ("_profile_datas",)

    profile_datas: Many[ProfileData] = Many(
        EndMeta(
            name="profile_datas",
            cim_role="ProfileDatas",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.profile_data:ProfileData",
            many=True,
            lower=0,
            upper=None,
            inverse="profile",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Profile",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{DA460209-200E-46b5-A5FB-3C600B650ED2}",
        ends=(profile_datas.meta,),
    )

    def __init__(
        self,
        *,
        profile_datas: Iterable[ProfileData] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if profile_datas is not None:
            Profile.profile_datas.extend(self, profile_datas)

    def add_profile_data(self, profile_data: ProfileData) -> Self:
        return Profile.profile_datas.add(self, profile_data)

    def remove_profile_data(self, profile_data: ProfileData) -> Self:
        return Profile.profile_datas.remove(self, profile_data)

    def clear_profile_datas(self) -> Self:
        return Profile.profile_datas.clear(self)

    def num_profile_data(self) -> int:
        return Profile.profile_datas.count(self)
