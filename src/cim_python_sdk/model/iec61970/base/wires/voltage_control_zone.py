"""CIM class VoltageControlZone (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.busbar_section import BusbarSection
    from cim_python_sdk.model.iec61970.base.wires.regulation_schedule import RegulationSchedule


class VoltageControlZone(PowerSystemResource):
    """An area of the power system network which is defined for secondary voltage control
    purposes. A voltage control zone consists of a collection of substations with a
    designated bus bar section whose voltage will be controlled."""

    __slots__ = ("_busbar_section", "_regulation_schedule")

    regulation_schedule: One[RegulationSchedule] = One(
        EndMeta(
            name="regulation_schedule",
            cim_role="RegulationSchedule",
            target="cim_python_sdk.model.iec61970.base.wires.regulation_schedule:RegulationSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="voltage_control_zones",
            aggregation="none",
        )
    )
    busbar_section: One[BusbarSection] = One(
        EndMeta(
            name="busbar_section",
            cim_role="BusbarSection",
            target="cim_python_sdk.model.iec61970.base.wires.busbar_section:BusbarSection",
            many=False,
            lower=1,
            upper=1,
            inverse="voltage_control_zone",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VoltageControlZone",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{709A85C2-97B8-431c-A661-FB83BDEBF933}",
        ends=(
            regulation_schedule.meta,
            busbar_section.meta,
        ),
    )

    def __init__(
        self,
        *,
        regulation_schedule: RegulationSchedule | None = None,
        busbar_section: BusbarSection | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if regulation_schedule is not None:
            self.regulation_schedule = regulation_schedule
        if busbar_section is not None:
            self.busbar_section = busbar_section
