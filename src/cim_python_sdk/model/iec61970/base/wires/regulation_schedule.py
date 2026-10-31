"""CIM class RegulationSchedule (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.load_model.season_day_type_schedule import (
    SeasonDayTypeSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.regulating_control import RegulatingControl
    from cim_python_sdk.model.iec61970.base.wires.voltage_control_zone import VoltageControlZone


class RegulationSchedule(SeasonDayTypeSchedule):
    """A pre-established pattern over time for a controlled variable, e.g., busbar voltage."""

    __slots__ = ("_regulating_control", "_voltage_control_zones")

    voltage_control_zones: Many[VoltageControlZone] = Many(
        EndMeta(
            name="voltage_control_zones",
            cim_role="VoltageControlZones",
            target="cim_python_sdk.model.iec61970.base.wires.voltage_control_zone:VoltageControlZone",
            many=True,
            lower=0,
            upper=None,
            inverse="regulation_schedule",
            aggregation="none",
        )
    )
    regulating_control: One[RegulatingControl] = One(
        EndMeta(
            name="regulating_control",
            cim_role="RegulatingControl",
            target="cim_python_sdk.model.iec61970.base.wires.regulating_control:RegulatingControl",
            many=False,
            lower=1,
            upper=1,
            inverse="regulation_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegulationSchedule",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{48632975-29AC-44f1-AC6C-1C7E7CEDBB0B}",
        ends=(
            voltage_control_zones.meta,
            regulating_control.meta,
        ),
    )

    def __init__(
        self,
        *,
        voltage_control_zones: Iterable[VoltageControlZone] | None = None,
        regulating_control: RegulatingControl | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if voltage_control_zones is not None:
            RegulationSchedule.voltage_control_zones.extend(self, voltage_control_zones)
        if regulating_control is not None:
            self.regulating_control = regulating_control

    def add_voltage_control_zone(self, voltage_control_zone: VoltageControlZone) -> Self:
        return RegulationSchedule.voltage_control_zones.add(self, voltage_control_zone)

    def remove_voltage_control_zone(self, voltage_control_zone: VoltageControlZone) -> Self:
        return RegulationSchedule.voltage_control_zones.remove(self, voltage_control_zone)

    def clear_voltage_control_zones(self) -> Self:
        return RegulationSchedule.voltage_control_zones.clear(self)

    def num_voltage_control_zone(self) -> int:
        return RegulationSchedule.voltage_control_zones.count(self)

    def get_voltage_control_zone_by_mrid(self, mrid: str) -> VoltageControlZone | None:
        return RegulationSchedule.voltage_control_zones.get_by_mrid(self, mrid)
