"""CIM class ACDCTerminal (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement
    from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_set import (
        OperationalLimitSet,
    )
    from cim_python_sdk.model.iec61970.base.topology.bus_name_marker import BusNameMarker


class ACDCTerminal(IdentifiedObject):
    """An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals
    are connected at physical connection points called connectivity nodes."""

    __slots__ = (
        "_bus_name_marker",
        "_measurements",
        "_operational_limit_set",
        "connected",
        "sequence_number",
    )

    connected: bool | None
    sequence_number: int | None

    measurements: Many[Measurement] = Many(
        EndMeta(
            name="measurements",
            cim_role="Measurements",
            target="cim_python_sdk.model.iec61970.base.meas.measurement:Measurement",
            many=True,
            lower=0,
            upper=None,
            inverse="terminal",
            aggregation="none",
        )
    )
    operational_limit_set: Many[OperationalLimitSet] = Many(
        EndMeta(
            name="operational_limit_set",
            cim_role="OperationalLimitSet",
            target="cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_set:OperationalLimitSet",
            many=True,
            lower=0,
            upper=None,
            inverse="terminal",
            aggregation="none",
        )
    )
    bus_name_marker: One[BusNameMarker] = One(
        EndMeta(
            name="bus_name_marker",
            cim_role="BusNameMarker",
            target="cim_python_sdk.model.iec61970.base.topology.bus_name_marker:BusNameMarker",
            many=False,
            lower=0,
            upper=1,
            inverse="terminal",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ACDCTerminal",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{D37077B9-3B0C-4c16-8F5F-9A6F2C83A7F2}",
        attributes=(
            AttrMeta("connected", "connected", "bool", 0, 1, "primitive"),
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
        ),
        ends=(
            measurements.meta,
            operational_limit_set.meta,
            bus_name_marker.meta,
        ),
    )

    def __init__(
        self,
        *,
        connected: bool | None = None,
        sequence_number: int | None = None,
        measurements: Iterable[Measurement] | None = None,
        operational_limit_set: Iterable[OperationalLimitSet] | None = None,
        bus_name_marker: BusNameMarker | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.connected = connected
        self.sequence_number = sequence_number
        if measurements is not None:
            ACDCTerminal.measurements.extend(self, measurements)
        if operational_limit_set is not None:
            ACDCTerminal.operational_limit_set.extend(self, operational_limit_set)
        if bus_name_marker is not None:
            self.bus_name_marker = bus_name_marker

    def add_measurement(self, measurement: Measurement) -> Self:
        return ACDCTerminal.measurements.add(self, measurement)

    def remove_measurement(self, measurement: Measurement) -> Self:
        return ACDCTerminal.measurements.remove(self, measurement)

    def clear_measurements(self) -> Self:
        return ACDCTerminal.measurements.clear(self)

    def num_measurement(self) -> int:
        return ACDCTerminal.measurements.count(self)

    def get_measurement_by_mrid(self, mrid: str) -> Measurement | None:
        return ACDCTerminal.measurements.get_by_mrid(self, mrid)

    def add_operational_limit_set(self, operational_limit_set: OperationalLimitSet) -> Self:
        return ACDCTerminal.operational_limit_set.add(self, operational_limit_set)

    def remove_operational_limit_set(self, operational_limit_set: OperationalLimitSet) -> Self:
        return ACDCTerminal.operational_limit_set.remove(self, operational_limit_set)

    def clear_operational_limit_set(self) -> Self:
        return ACDCTerminal.operational_limit_set.clear(self)

    def num_operational_limit_set(self) -> int:
        return ACDCTerminal.operational_limit_set.count(self)

    def get_operational_limit_set_by_mrid(self, mrid: str) -> OperationalLimitSet | None:
        return ACDCTerminal.operational_limit_set.get_by_mrid(self, mrid)
