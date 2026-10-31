"""CIM class PowerElectronicsConnection (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.wires.regulating_cond_eq import RegulatingCondEq

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.production.power_electronics_unit import (
        PowerElectronicsUnit,
    )
    from cim_python_sdk.model.iec61970.base.wires.power_electronics_connection_phase import (
        PowerElectronicsConnectionPhase,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_dynamics import (
        WindTurbineType3or4Dynamics,
    )


class PowerElectronicsConnection(RegulatingCondEq):
    """A connection to the AC network for energy production or consumption that uses power
    electronics rather than rotating machines."""

    __slots__ = (
        "_power_electronics_connection_phase",
        "_power_electronics_unit",
        "_wind_turbine_type3or4_dynamics",
        "max_i_fault",
        "max_q",
        "min_q",
        "p",
        "q",
        "r",
        "r0",
        "rated_s",
        "rated_u",
        "rn",
        "x",
        "x0",
        "xn",
    )

    max_q: float | None  # ReactivePower
    min_q: float | None  # ReactivePower
    rated_s: float | None  # ApparentPower
    rated_u: float | None  # Voltage
    p: float | None  # ActivePower
    q: float | None  # ReactivePower
    r: float | None  # Resistance
    r0: float | None  # Resistance
    rn: float | None  # Resistance
    x: float | None  # Reactance
    x0: float | None  # Reactance
    xn: float | None  # Reactance
    max_i_fault: float | None  # PU

    wind_turbine_type3or4_dynamics: One[WindTurbineType3or4Dynamics] = One(
        EndMeta(
            name="wind_turbine_type3or4_dynamics",
            cim_role="WindTurbineType3or4Dynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_dynamics:WindTurbineType3or4Dynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="power_electronics_connection",
            aggregation="none",
        )
    )
    power_electronics_unit: Many[PowerElectronicsUnit] = Many(
        EndMeta(
            name="power_electronics_unit",
            cim_role="PowerElectronicsUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.power_electronics_unit:PowerElectronicsUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="power_electronics_connection",
            aggregation="none",
        )
    )
    power_electronics_connection_phase: Many[PowerElectronicsConnectionPhase] = Many(
        EndMeta(
            name="power_electronics_connection_phase",
            cim_role="PowerElectronicsConnectionPhase",
            target="cim_python_sdk.model.iec61970.base.wires.power_electronics_connection_phase:PowerElectronicsConnectionPhase",
            many=True,
            lower=0,
            upper=None,
            inverse="power_electronics_connection",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerElectronicsConnection",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{AEF4A2AB-D126-4311-B299-CAB7D826A16E}",
        attributes=(
            AttrMeta("max_q", "maxQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_q", "minQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("rated_s", "ratedS", "ApparentPower", 0, 1, "cimdatatype"),
            AttrMeta("rated_u", "ratedU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("q", "q", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype", deprecated=True),
            AttrMeta("r0", "r0", "Resistance", 0, 1, "cimdatatype", deprecated=True),
            AttrMeta("rn", "rn", "Resistance", 0, 1, "cimdatatype", deprecated=True),
            AttrMeta("x", "x", "Reactance", 0, 1, "cimdatatype", deprecated=True),
            AttrMeta("x0", "x0", "Reactance", 0, 1, "cimdatatype", deprecated=True),
            AttrMeta("xn", "xn", "Reactance", 0, 1, "cimdatatype", deprecated=True),
            AttrMeta("max_i_fault", "maxIFault", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(
            wind_turbine_type3or4_dynamics.meta,
            power_electronics_unit.meta,
            power_electronics_connection_phase.meta,
        ),
    )

    def __init__(
        self,
        *,
        max_q: float | None = None,
        min_q: float | None = None,
        rated_s: float | None = None,
        rated_u: float | None = None,
        p: float | None = None,
        q: float | None = None,
        r: float | None = None,
        r0: float | None = None,
        rn: float | None = None,
        x: float | None = None,
        x0: float | None = None,
        xn: float | None = None,
        max_i_fault: float | None = None,
        wind_turbine_type3or4_dynamics: WindTurbineType3or4Dynamics | None = None,
        power_electronics_unit: Iterable[PowerElectronicsUnit] | None = None,
        power_electronics_connection_phase: Iterable[PowerElectronicsConnectionPhase] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_q = max_q
        self.min_q = min_q
        self.rated_s = rated_s
        self.rated_u = rated_u
        self.p = p
        self.q = q
        self.r = r
        self.r0 = r0
        self.rn = rn
        self.x = x
        self.x0 = x0
        self.xn = xn
        self.max_i_fault = max_i_fault
        if wind_turbine_type3or4_dynamics is not None:
            self.wind_turbine_type3or4_dynamics = wind_turbine_type3or4_dynamics
        if power_electronics_unit is not None:
            PowerElectronicsConnection.power_electronics_unit.extend(self, power_electronics_unit)
        if power_electronics_connection_phase is not None:
            PowerElectronicsConnection.power_electronics_connection_phase.extend(
                self, power_electronics_connection_phase
            )

    def add_power_electronics_unit(self, power_electronics_unit: PowerElectronicsUnit) -> Self:
        return PowerElectronicsConnection.power_electronics_unit.add(self, power_electronics_unit)

    def remove_power_electronics_unit(self, power_electronics_unit: PowerElectronicsUnit) -> Self:
        return PowerElectronicsConnection.power_electronics_unit.remove(
            self, power_electronics_unit
        )

    def clear_power_electronics_unit(self) -> Self:
        return PowerElectronicsConnection.power_electronics_unit.clear(self)

    def num_power_electronics_unit(self) -> int:
        return PowerElectronicsConnection.power_electronics_unit.count(self)

    def get_power_electronics_unit_by_mrid(self, mrid: str) -> PowerElectronicsUnit | None:
        return PowerElectronicsConnection.power_electronics_unit.get_by_mrid(self, mrid)

    def add_power_electronics_connection_phase(
        self, power_electronics_connection_phase: PowerElectronicsConnectionPhase
    ) -> Self:
        return PowerElectronicsConnection.power_electronics_connection_phase.add(
            self, power_electronics_connection_phase
        )

    def remove_power_electronics_connection_phase(
        self, power_electronics_connection_phase: PowerElectronicsConnectionPhase
    ) -> Self:
        return PowerElectronicsConnection.power_electronics_connection_phase.remove(
            self, power_electronics_connection_phase
        )

    def clear_power_electronics_connection_phase(self) -> Self:
        return PowerElectronicsConnection.power_electronics_connection_phase.clear(self)

    def num_power_electronics_connection_phase(self) -> int:
        return PowerElectronicsConnection.power_electronics_connection_phase.count(self)

    def get_power_electronics_connection_phase_by_mrid(
        self, mrid: str
    ) -> PowerElectronicsConnectionPhase | None:
        return PowerElectronicsConnection.power_electronics_connection_phase.get_by_mrid(self, mrid)
