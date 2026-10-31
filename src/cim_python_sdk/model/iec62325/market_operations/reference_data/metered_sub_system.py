"""CIM class MeteredSubSystem (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.mss_aggregation import (
        MSSAggregation,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mss_zone import MSSZone


class MeteredSubSystem(IdentifiedObject):
    """A metered subsystem."""

    __slots__ = ("_mss_aggregation", "_mss_zone")

    mss_zone: Many[MSSZone] = Many(
        EndMeta(
            name="mss_zone",
            cim_role="MSSZone",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mss_zone:MSSZone",
            many=True,
            lower=0,
            upper=None,
            inverse="metered_sub_system",
            aggregation="none",
        )
    )
    mss_aggregation: One[MSSAggregation] = One(
        EndMeta(
            name="mss_aggregation",
            cim_role="MSSAggregation",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mss_aggregation:MSSAggregation",
            many=False,
            lower=0,
            upper=1,
            inverse="metered_sub_system",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeteredSubSystem",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{72CD6CEF-766E-4cab-A58D-5E6020F0E358}",
        ends=(
            mss_zone.meta,
            mss_aggregation.meta,
        ),
    )

    def __init__(
        self,
        *,
        mss_zone: Iterable[MSSZone] | None = None,
        mss_aggregation: MSSAggregation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if mss_zone is not None:
            MeteredSubSystem.mss_zone.extend(self, mss_zone)
        if mss_aggregation is not None:
            self.mss_aggregation = mss_aggregation

    def add_mss_zone(self, mss_zone: MSSZone) -> Self:
        return MeteredSubSystem.mss_zone.add(self, mss_zone)

    def remove_mss_zone(self, mss_zone: MSSZone) -> Self:
        return MeteredSubSystem.mss_zone.remove(self, mss_zone)

    def clear_mss_zone(self) -> Self:
        return MeteredSubSystem.mss_zone.clear(self)

    def num_mss_zone(self) -> int:
        return MeteredSubSystem.mss_zone.count(self)

    def get_mss_zone_by_mrid(self, mrid: str) -> MSSZone | None:
        return MeteredSubSystem.mss_zone.get_by_mrid(self, mrid)
