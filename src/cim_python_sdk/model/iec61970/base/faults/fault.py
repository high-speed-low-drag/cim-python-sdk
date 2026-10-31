"""CIM class Fault (TC57CIM/IEC61970/Base/Faults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.operations.outage import Outage
    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment
    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode
    from cim_python_sdk.model.iec61970.base.faults.fault_cause_type import FaultCauseType
    from cim_python_sdk.model.iec61970.base.faults.fault_impedance import FaultImpedance
    from cim_python_sdk.model.iec61970.base.faults.phase_connected_fault_kind import (
        PhaseConnectedFaultKind,
    )


class Fault(IdentifiedObject):
    """Abnormal condition causing current flow through conducting equipment, such as caused by
    equipment failure or short circuits from objects not typically modelled (for example, a
    tree falling on a line)."""

    __slots__ = (
        "_fault_cause_types",
        "_faulty_equipment",
        "_location",
        "_outage",
        "impedance",
        "kind",
        "occurred_date_time",
        "phases",
    )

    impedance: FaultImpedance | None
    kind: PhaseConnectedFaultKind | None
    phases: PhaseCode | None
    occurred_date_time: _dt.datetime | None

    faulty_equipment: One[Equipment] = One(
        EndMeta(
            name="faulty_equipment",
            cim_role="FaultyEquipment",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=False,
            lower=0,
            upper=1,
            inverse="faults",
            aggregation="none",
        )
    )
    fault_cause_types: Many[FaultCauseType] = Many(
        EndMeta(
            name="fault_cause_types",
            cim_role="FaultCauseTypes",
            target="cim_python_sdk.model.iec61970.base.faults.fault_cause_type:FaultCauseType",
            many=True,
            lower=0,
            upper=None,
            inverse="faults",
            aggregation="none",
        )
    )
    location: One[Location] = One(
        EndMeta(
            name="location",
            cim_role="Location",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=False,
            lower=0,
            upper=1,
            inverse="fault",
            aggregation="none",
        )
    )
    outage: One[Outage] = One(
        EndMeta(
            name="outage",
            cim_role="Outage",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=False,
            lower=0,
            upper=1,
            inverse="faults",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Fault",
        package="TC57CIM/IEC61970/Base/Faults",
        guid="{73ABECF2-4B28-4c55-8665-0882A2C8BCA4}",
        attributes=(
            AttrMeta("impedance", "impedance", "FaultImpedance", 0, 1, "compound"),
            AttrMeta("kind", "kind", "PhaseConnectedFaultKind", 0, 1, "enumeration"),
            AttrMeta("phases", "phases", "PhaseCode", 0, 1, "enumeration"),
            AttrMeta("occurred_date_time", "occurredDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            faulty_equipment.meta,
            fault_cause_types.meta,
            location.meta,
            outage.meta,
        ),
    )

    def __init__(
        self,
        *,
        impedance: FaultImpedance | None = None,
        kind: PhaseConnectedFaultKind | None = None,
        phases: PhaseCode | None = None,
        occurred_date_time: _dt.datetime | None = None,
        faulty_equipment: Equipment | None = None,
        fault_cause_types: Iterable[FaultCauseType] | None = None,
        location: Location | None = None,
        outage: Outage | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.impedance = impedance
        self.kind = kind
        self.phases = phases
        self.occurred_date_time = occurred_date_time
        if faulty_equipment is not None:
            self.faulty_equipment = faulty_equipment
        if fault_cause_types is not None:
            Fault.fault_cause_types.extend(self, fault_cause_types)
        if location is not None:
            self.location = location
        if outage is not None:
            self.outage = outage

    def add_fault_cause_type(self, fault_cause_type: FaultCauseType) -> Self:
        return Fault.fault_cause_types.add(self, fault_cause_type)

    def remove_fault_cause_type(self, fault_cause_type: FaultCauseType) -> Self:
        return Fault.fault_cause_types.remove(self, fault_cause_type)

    def clear_fault_cause_types(self) -> Self:
        return Fault.fault_cause_types.clear(self)

    def num_fault_cause_type(self) -> int:
        return Fault.fault_cause_types.count(self)

    def get_fault_cause_type_by_mrid(self, mrid: str) -> FaultCauseType | None:
        return Fault.fault_cause_types.get_by_mrid(self, mrid)
