"""CIM class TiePoint (TC57CIM/IEC62325/InfIEC62325/InfReservation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_measurement import (
        MktMeasurement,
    )


class TiePoint(IdentifiedObject):
    """Site of an interface between interchange areas. The tie point can be a network branch
    (e.g., transmission line or transformer) or a switching device. For transmission lines,
    the interchange area boundary is usually at a designated point such as the middle of the
    line. Line end metering is then corrected for line losses."""

    __slots__ = ("_by_mkt_measurement", "_for_mkt_measurement", "tie_point_mw_rating")

    tie_point_mw_rating: float | None  # ActivePower

    by_mkt_measurement: Many[MktMeasurement] = Many(
        EndMeta(
            name="by_mkt_measurement",
            cim_role="ByMktMeasurement",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_measurement:MktMeasurement",
            many=True,
            lower=1,
            upper=None,
            inverse="by_tie_point",
            aggregation="none",
        )
    )
    for_mkt_measurement: Many[MktMeasurement] = Many(
        EndMeta(
            name="for_mkt_measurement",
            cim_role="ForMktMeasurement",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_measurement:MktMeasurement",
            many=True,
            lower=1,
            upper=None,
            inverse="for_tie_point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TiePoint",
        package="TC57CIM/IEC62325/InfIEC62325/InfReservation",
        guid="{5646690B-90BB-4493-B579-67E48CDF0860}",
        attributes=(
            AttrMeta("tie_point_mw_rating", "tiePointMWRating", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            by_mkt_measurement.meta,
            for_mkt_measurement.meta,
        ),
    )

    def __init__(
        self,
        *,
        tie_point_mw_rating: float | None = None,
        by_mkt_measurement: Iterable[MktMeasurement] | None = None,
        for_mkt_measurement: Iterable[MktMeasurement] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tie_point_mw_rating = tie_point_mw_rating
        if by_mkt_measurement is not None:
            TiePoint.by_mkt_measurement.extend(self, by_mkt_measurement)
        if for_mkt_measurement is not None:
            TiePoint.for_mkt_measurement.extend(self, for_mkt_measurement)

    def add_by_mkt_measurement(self, by_mkt_measurement: MktMeasurement) -> Self:
        return TiePoint.by_mkt_measurement.add(self, by_mkt_measurement)

    def remove_by_mkt_measurement(self, by_mkt_measurement: MktMeasurement) -> Self:
        return TiePoint.by_mkt_measurement.remove(self, by_mkt_measurement)

    def clear_by_mkt_measurement(self) -> Self:
        return TiePoint.by_mkt_measurement.clear(self)

    def num_by_mkt_measurement(self) -> int:
        return TiePoint.by_mkt_measurement.count(self)

    def get_by_mkt_measurement_by_mrid(self, mrid: str) -> MktMeasurement | None:
        return TiePoint.by_mkt_measurement.get_by_mrid(self, mrid)

    def add_for_mkt_measurement(self, for_mkt_measurement: MktMeasurement) -> Self:
        return TiePoint.for_mkt_measurement.add(self, for_mkt_measurement)

    def remove_for_mkt_measurement(self, for_mkt_measurement: MktMeasurement) -> Self:
        return TiePoint.for_mkt_measurement.remove(self, for_mkt_measurement)

    def clear_for_mkt_measurement(self) -> Self:
        return TiePoint.for_mkt_measurement.clear(self)

    def num_for_mkt_measurement(self) -> int:
        return TiePoint.for_mkt_measurement.count(self)

    def get_for_mkt_measurement_by_mrid(self, mrid: str) -> MktMeasurement | None:
        return TiePoint.for_mkt_measurement.get_by_mrid(self, mrid)
