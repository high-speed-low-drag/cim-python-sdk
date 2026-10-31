"""CIM class HydroPump (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.equipment import Equipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.hydro_power_plant import (
        HydroPowerPlant,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.hydro_pump_op_schedule import (
        HydroPumpOpSchedule,
    )
    from cim_python_sdk.model.iec61970.base.wires.rotating_machine import RotatingMachine


class HydroPump(Equipment):
    """A synchronous motor-driven pump, typically associated with a pumped storage plant."""

    __slots__ = (
        "_hydro_power_plant",
        "_hydro_pump_op_schedule",
        "_rotating_machine",
        "pump_disch_at_max_head",
        "pump_disch_at_min_head",
        "pump_power_at_max_head",
        "pump_power_at_min_head",
    )

    pump_disch_at_max_head: float | None  # VolumeFlowRate
    pump_disch_at_min_head: float | None  # VolumeFlowRate
    pump_power_at_max_head: float | None  # ActivePower
    pump_power_at_min_head: float | None  # ActivePower

    hydro_power_plant: One[HydroPowerPlant] = One(
        EndMeta(
            name="hydro_power_plant",
            cim_role="HydroPowerPlant",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_power_plant:HydroPowerPlant",
            many=False,
            lower=0,
            upper=1,
            inverse="hydro_pumps",
            aggregation="none",
        )
    )
    rotating_machine: One[RotatingMachine] = One(
        EndMeta(
            name="rotating_machine",
            cim_role="RotatingMachine",
            target="cim_python_sdk.model.iec61970.base.wires.rotating_machine:RotatingMachine",
            many=False,
            lower=1,
            upper=1,
            inverse="hydro_pump",
            aggregation="none",
        )
    )
    hydro_pump_op_schedule: One[HydroPumpOpSchedule] = One(
        EndMeta(
            name="hydro_pump_op_schedule",
            cim_role="HydroPumpOpSchedule",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_pump_op_schedule:HydroPumpOpSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="hydro_pump",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HydroPump",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{4C4342EA-F3E1-469a-ACB4-CA80A2524FFE}",
        attributes=(
            AttrMeta(
                "pump_disch_at_max_head",
                "pumpDischAtMaxHead",
                "VolumeFlowRate",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "pump_disch_at_min_head",
                "pumpDischAtMinHead",
                "VolumeFlowRate",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "pump_power_at_max_head", "pumpPowerAtMaxHead", "ActivePower", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "pump_power_at_min_head", "pumpPowerAtMinHead", "ActivePower", 0, 1, "cimdatatype"
            ),
        ),
        ends=(
            hydro_power_plant.meta,
            rotating_machine.meta,
            hydro_pump_op_schedule.meta,
        ),
    )

    def __init__(
        self,
        *,
        pump_disch_at_max_head: float | None = None,
        pump_disch_at_min_head: float | None = None,
        pump_power_at_max_head: float | None = None,
        pump_power_at_min_head: float | None = None,
        hydro_power_plant: HydroPowerPlant | None = None,
        rotating_machine: RotatingMachine | None = None,
        hydro_pump_op_schedule: HydroPumpOpSchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.pump_disch_at_max_head = pump_disch_at_max_head
        self.pump_disch_at_min_head = pump_disch_at_min_head
        self.pump_power_at_max_head = pump_power_at_max_head
        self.pump_power_at_min_head = pump_power_at_min_head
        if hydro_power_plant is not None:
            self.hydro_power_plant = hydro_power_plant
        if rotating_machine is not None:
            self.rotating_machine = rotating_machine
        if hydro_pump_op_schedule is not None:
            self.hydro_pump_op_schedule = hydro_pump_op_schedule
