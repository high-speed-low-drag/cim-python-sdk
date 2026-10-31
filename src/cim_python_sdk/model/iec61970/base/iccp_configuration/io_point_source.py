"""CIM class IOPointSource (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.meas.measurement_value_source import MeasurementValueSource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.meas.io_point import IOPoint


class IOPointSource(MeasurementValueSource):
    """Indicates the point source for an IO Point."""

    __slots__ = ("_io_point",)

    io_point: Many[IOPoint] = Many(
        EndMeta(
            name="io_point",
            cim_role="IOPoint",
            target="cim_python_sdk.model.iec61970.base.meas.io_point:IOPoint",
            many=True,
            lower=0,
            upper=None,
            inverse="io_point_source",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IOPointSource",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{E7EF5D7B-47F2-4830-82A4-B867566CBF7E}",
        ends=(io_point.meta,),
    )

    def __init__(
        self,
        *,
        io_point: Iterable[IOPoint] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if io_point is not None:
            IOPointSource.io_point.extend(self, io_point)

    def add_io_point(self, io_point: IOPoint) -> Self:
        return IOPointSource.io_point.add(self, io_point)

    def remove_io_point(self, io_point: IOPoint) -> Self:
        return IOPointSource.io_point.remove(self, io_point)

    def clear_io_point(self) -> Self:
        return IOPointSource.io_point.clear(self)

    def num_io_point(self) -> int:
        return IOPointSource.io_point.count(self)

    def get_io_point_by_mrid(self, mrid: str) -> IOPoint | None:
        return IOPointSource.io_point.get_by_mrid(self, mrid)
