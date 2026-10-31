"""CIM class IOPoint (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.iccp_configuration.io_point_source import IOPointSource
    from cim_python_sdk.model.iec61970.base.iccp_configuration.provided_bilateral_point import (
        ProvidedBilateralPoint,
    )


class IOPoint(IdentifiedObject):
    """The class describe a measurement or control value. The purpose is to enable having
    attributes and associations common for measurement and control."""

    __slots__ = ("_bilateral_to_io_point", "_io_point_source")

    bilateral_to_io_point: Many[ProvidedBilateralPoint] = Many(
        EndMeta(
            name="bilateral_to_io_point",
            cim_role="BilateralToIOPoint",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.provided_bilateral_point:ProvidedBilateralPoint",
            many=True,
            lower=0,
            upper=None,
            inverse="io_point",
            aggregation="none",
        )
    )
    io_point_source: One[IOPointSource] = One(
        EndMeta(
            name="io_point_source",
            cim_role="IOPointSource",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.io_point_source:IOPointSource",
            many=False,
            lower=0,
            upper=1,
            inverse="io_point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IOPoint",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{538879CD-D8B6-4eff-B980-FE6510E2699A}",
        ends=(
            bilateral_to_io_point.meta,
            io_point_source.meta,
        ),
    )

    def __init__(
        self,
        *,
        bilateral_to_io_point: Iterable[ProvidedBilateralPoint] | None = None,
        io_point_source: IOPointSource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if bilateral_to_io_point is not None:
            IOPoint.bilateral_to_io_point.extend(self, bilateral_to_io_point)
        if io_point_source is not None:
            self.io_point_source = io_point_source

    def add_bilateral_to_io_point(self, bilateral_to_io_point: ProvidedBilateralPoint) -> Self:
        return IOPoint.bilateral_to_io_point.add(self, bilateral_to_io_point)

    def remove_bilateral_to_io_point(self, bilateral_to_io_point: ProvidedBilateralPoint) -> Self:
        return IOPoint.bilateral_to_io_point.remove(self, bilateral_to_io_point)

    def clear_bilateral_to_io_point(self) -> Self:
        return IOPoint.bilateral_to_io_point.clear(self)

    def num_bilateral_to_io_point(self) -> int:
        return IOPoint.bilateral_to_io_point.count(self)

    def get_bilateral_to_io_point_by_mrid(self, mrid: str) -> ProvidedBilateralPoint | None:
        return IOPoint.bilateral_to_io_point.get_by_mrid(self, mrid)
