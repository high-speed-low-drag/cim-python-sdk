"""CIM class Bay (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.equipment_container import EquipmentContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.breaker_configuration import BreakerConfiguration
    from cim_python_sdk.model.iec61970.base.core.busbar_configuration import BusbarConfiguration
    from cim_python_sdk.model.iec61970.base.core.substation import Substation
    from cim_python_sdk.model.iec61970.base.core.voltage_level import VoltageLevel
    from cim_python_sdk.model.iec61970.inf_iec61970.feeder.circuit import Circuit


class Bay(EquipmentContainer):
    """A collection of power system resources (within a given substation) including conducting
    equipment, protection relays, measurements, and telemetry. A bay typically represents a
    physical grouping related to modularization of equipment."""

    __slots__ = (
        "_circuit",
        "_substation",
        "_voltage_level",
        "bay_energy_meas_flag",
        "bay_power_meas_flag",
        "breaker_configuration",
        "bus_bar_configuration",
    )

    bay_energy_meas_flag: bool | None
    bay_power_meas_flag: bool | None
    breaker_configuration: BreakerConfiguration | None
    bus_bar_configuration: BusbarConfiguration | None

    circuit: One[Circuit] = One(
        EndMeta(
            name="circuit",
            cim_role="Circuit",
            target="cim_python_sdk.model.iec61970.inf_iec61970.feeder.circuit:Circuit",
            many=False,
            lower=0,
            upper=1,
            inverse="end_bay",
            aggregation="none",
        )
    )
    substation: One[Substation] = One(
        EndMeta(
            name="substation",
            cim_role="Substation",
            target="cim_python_sdk.model.iec61970.base.core.substation:Substation",
            many=False,
            lower=0,
            upper=1,
            inverse="bays",
            aggregation="none",
        )
    )
    voltage_level: One[VoltageLevel] = One(
        EndMeta(
            name="voltage_level",
            cim_role="VoltageLevel",
            target="cim_python_sdk.model.iec61970.base.core.voltage_level:VoltageLevel",
            many=False,
            lower=0,
            upper=1,
            inverse="bays",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Bay",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{45910062-D4E8-40ee-99EB-FEC14DD9FAB0}",
        attributes=(
            AttrMeta("bay_energy_meas_flag", "bayEnergyMeasFlag", "bool", 0, 1, "primitive"),
            AttrMeta("bay_power_meas_flag", "bayPowerMeasFlag", "bool", 0, 1, "primitive"),
            AttrMeta(
                "breaker_configuration",
                "breakerConfiguration",
                "BreakerConfiguration",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "bus_bar_configuration",
                "busBarConfiguration",
                "BusbarConfiguration",
                0,
                1,
                "enumeration",
            ),
        ),
        ends=(
            circuit.meta,
            substation.meta,
            voltage_level.meta,
        ),
    )

    def __init__(
        self,
        *,
        bay_energy_meas_flag: bool | None = None,
        bay_power_meas_flag: bool | None = None,
        breaker_configuration: BreakerConfiguration | None = None,
        bus_bar_configuration: BusbarConfiguration | None = None,
        circuit: Circuit | None = None,
        substation: Substation | None = None,
        voltage_level: VoltageLevel | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bay_energy_meas_flag = bay_energy_meas_flag
        self.bay_power_meas_flag = bay_power_meas_flag
        self.breaker_configuration = breaker_configuration
        self.bus_bar_configuration = bus_bar_configuration
        if circuit is not None:
            self.circuit = circuit
        if substation is not None:
            self.substation = substation
        if voltage_level is not None:
            self.voltage_level = voltage_level
