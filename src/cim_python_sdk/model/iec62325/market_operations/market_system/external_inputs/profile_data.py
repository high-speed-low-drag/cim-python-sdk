"""CIM class ProfileData (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.profile import (
        Profile,
    )


class ProfileData(CimObject):
    """Data for profile."""

    __slots__ = (
        "_profile",
        "bid_price",
        "capacity_level",
        "energy_level",
        "minimum_level",
        "sequence_number",
        "start_date_time",
        "stop_date_time",
    )

    bid_price: float | None
    capacity_level: float | None  # ActivePower
    energy_level: float | None  # RealEnergy
    minimum_level: float | None
    sequence_number: int | None
    start_date_time: _dt.datetime | None
    stop_date_time: _dt.datetime | None

    profile: Many[Profile] = Many(
        EndMeta(
            name="profile",
            cim_role="Profile",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.profile:Profile",
            many=True,
            lower=0,
            upper=None,
            inverse="profile_datas",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProfileData",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{75BA1129-9F82-4511-B04F-E21D80832053}",
        attributes=(
            AttrMeta("bid_price", "bidPrice", "float", 0, 1, "primitive"),
            AttrMeta("capacity_level", "capacityLevel", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("energy_level", "energyLevel", "RealEnergy", 0, 1, "cimdatatype"),
            AttrMeta("minimum_level", "minimumLevel", "float", 0, 1, "primitive"),
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("start_date_time", "startDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("stop_date_time", "stopDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(profile.meta,),
    )

    def __init__(
        self,
        *,
        bid_price: float | None = None,
        capacity_level: float | None = None,
        energy_level: float | None = None,
        minimum_level: float | None = None,
        sequence_number: int | None = None,
        start_date_time: _dt.datetime | None = None,
        stop_date_time: _dt.datetime | None = None,
        profile: Iterable[Profile] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bid_price = bid_price
        self.capacity_level = capacity_level
        self.energy_level = energy_level
        self.minimum_level = minimum_level
        self.sequence_number = sequence_number
        self.start_date_time = start_date_time
        self.stop_date_time = stop_date_time
        if profile is not None:
            ProfileData.profile.extend(self, profile)

    def add_profile(self, profile: Profile) -> Self:
        return ProfileData.profile.add(self, profile)

    def remove_profile(self, profile: Profile) -> Self:
        return ProfileData.profile.remove(self, profile)

    def clear_profile(self) -> Self:
        return ProfileData.profile.clear(self)

    def num_profile(self) -> int:
        return ProfileData.profile.count(self)

    def get_profile_by_mrid(self, mrid: str) -> Profile | None:
        return ProfileData.profile.get_by_mrid(self, mrid)
