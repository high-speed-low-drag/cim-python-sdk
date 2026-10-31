"""CIM class GenericConstraints (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_capacity import (
        TransmissionCapacity,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class GenericConstraints(IdentifiedObject):
    """Generic constraints can represent secure areas, voltage profile, transient stability and
    voltage collapse limits.

    The generic constraints can be one of the following forms:

    a) Thermal MW limit constraints type

    b) Group line flow constraint type"""

    __slots__ = (
        "_flowgate",
        "_transmission_capacity",
        "interval_end_time",
        "interval_start_time",
        "max_limit",
        "min_limit",
    )

    interval_end_time: _dt.datetime | None
    interval_start_time: _dt.datetime | None
    max_limit: float | None
    min_limit: float | None

    transmission_capacity: Many[TransmissionCapacity] = Many(
        EndMeta(
            name="transmission_capacity",
            cim_role="TransmissionCapacity",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_capacity:TransmissionCapacity",
            many=True,
            lower=0,
            upper=None,
            inverse="generic_constraints",
            aggregation="none",
        )
    )
    flowgate: Many[Flowgate] = Many(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=True,
            lower=0,
            upper=None,
            inverse="generic_constraints",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GenericConstraints",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{DEE63525-3D7B-41c3-98F6-EFA5FAE3DEF1}",
        attributes=(
            AttrMeta("interval_end_time", "intervalEndTime", "datetime", 0, 1, "primitive"),
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("max_limit", "maxLimit", "float", 0, 1, "primitive"),
            AttrMeta("min_limit", "minLimit", "float", 0, 1, "primitive"),
        ),
        ends=(
            transmission_capacity.meta,
            flowgate.meta,
        ),
    )

    def __init__(
        self,
        *,
        interval_end_time: _dt.datetime | None = None,
        interval_start_time: _dt.datetime | None = None,
        max_limit: float | None = None,
        min_limit: float | None = None,
        transmission_capacity: Iterable[TransmissionCapacity] | None = None,
        flowgate: Iterable[Flowgate] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_end_time = interval_end_time
        self.interval_start_time = interval_start_time
        self.max_limit = max_limit
        self.min_limit = min_limit
        if transmission_capacity is not None:
            GenericConstraints.transmission_capacity.extend(self, transmission_capacity)
        if flowgate is not None:
            GenericConstraints.flowgate.extend(self, flowgate)

    def add_transmission_capacity(self, transmission_capacity: TransmissionCapacity) -> Self:
        return GenericConstraints.transmission_capacity.add(self, transmission_capacity)

    def remove_transmission_capacity(self, transmission_capacity: TransmissionCapacity) -> Self:
        return GenericConstraints.transmission_capacity.remove(self, transmission_capacity)

    def clear_transmission_capacity(self) -> Self:
        return GenericConstraints.transmission_capacity.clear(self)

    def num_transmission_capacity(self) -> int:
        return GenericConstraints.transmission_capacity.count(self)

    def add_flowgate(self, flowgate: Flowgate) -> Self:
        return GenericConstraints.flowgate.add(self, flowgate)

    def remove_flowgate(self, flowgate: Flowgate) -> Self:
        return GenericConstraints.flowgate.remove(self, flowgate)

    def clear_flowgate(self) -> Self:
        return GenericConstraints.flowgate.clear(self)

    def num_flowgate(self) -> int:
        return GenericConstraints.flowgate.count(self)

    def get_flowgate_by_mrid(self, mrid: str) -> Flowgate | None:
        return GenericConstraints.flowgate.get_by_mrid(self, mrid)
