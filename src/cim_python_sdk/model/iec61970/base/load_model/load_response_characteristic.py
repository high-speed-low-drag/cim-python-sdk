"""CIM class LoadResponseCharacteristic (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.energy_consumer import EnergyConsumer


class LoadResponseCharacteristic(IdentifiedObject):
    """Models the characteristic response of the load demand due to changes in system
    conditions such as voltage and frequency. It is not related to demand response.

    If LoadResponseCharacteristic.exponentModel is True, the exponential voltage or
    frequency dependent models are specified and used as to calculate active and reactive
    power components of the load model.

    The equations to calculate active and reactive power components of the load model are
    internal to the power flow calculation, hence they use different quantities depending on
    the use case of the data exchange.

    The equations for exponential voltage dependent load model injected power are:

    pInjection= Pnominal* (Voltage/cim:BaseVoltage.nominalVoltage) **
    cim:LoadResponseCharacteristic.pVoltageExponent

    qInjection= Qnominal* (Voltage/cim:BaseVoltage.nominalVoltage) **
    cim:LoadResponseCharacteristic.qVoltageExponent

    Where:

    1) * means "multiply" and ** is "raised to power of";

    2) Pnominal and Qnominal represent the active power and reactive power at nominal
    voltage as any load described by the voltage exponential model shall be given at nominal
    voltage. This means that EnergyConsumer.p and EnergyConsumer.q are at nominal voltage.

    3) After power flow is solved:

    -pInjection and qInjection correspond to SvPowerflow.p and SvPowerflow.q respectively.

    - Voltage corresponds to SvVoltage.v at the TopologicalNode where the load is connected."""

    __slots__ = (
        "_energy_consumer",
        "exponent_model",
        "p_constant_current",
        "p_constant_impedance",
        "p_constant_power",
        "p_frequency_exponent",
        "p_voltage_exponent",
        "q_constant_current",
        "q_constant_impedance",
        "q_constant_power",
        "q_frequency_exponent",
        "q_voltage_exponent",
    )

    exponent_model: bool | None
    p_constant_current: float | None
    p_constant_impedance: float | None
    p_constant_power: float | None
    p_frequency_exponent: float | None
    p_voltage_exponent: float | None
    q_constant_current: float | None
    q_constant_impedance: float | None
    q_constant_power: float | None
    q_frequency_exponent: float | None
    q_voltage_exponent: float | None

    energy_consumer: Many[EnergyConsumer] = Many(
        EndMeta(
            name="energy_consumer",
            cim_role="EnergyConsumer",
            target="cim_python_sdk.model.iec61970.base.wires.energy_consumer:EnergyConsumer",
            many=True,
            lower=0,
            upper=None,
            inverse="load_response",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadResponseCharacteristic",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{F80EE4DD-B985-47e3-9832-B5005C24C87E}",
        attributes=(
            AttrMeta("exponent_model", "exponentModel", "bool", 0, 1, "primitive"),
            AttrMeta("p_constant_current", "pConstantCurrent", "float", 0, 1, "primitive"),
            AttrMeta("p_constant_impedance", "pConstantImpedance", "float", 0, 1, "primitive"),
            AttrMeta("p_constant_power", "pConstantPower", "float", 0, 1, "primitive"),
            AttrMeta("p_frequency_exponent", "pFrequencyExponent", "float", 0, 1, "primitive"),
            AttrMeta("p_voltage_exponent", "pVoltageExponent", "float", 0, 1, "primitive"),
            AttrMeta("q_constant_current", "qConstantCurrent", "float", 0, 1, "primitive"),
            AttrMeta("q_constant_impedance", "qConstantImpedance", "float", 0, 1, "primitive"),
            AttrMeta("q_constant_power", "qConstantPower", "float", 0, 1, "primitive"),
            AttrMeta("q_frequency_exponent", "qFrequencyExponent", "float", 0, 1, "primitive"),
            AttrMeta("q_voltage_exponent", "qVoltageExponent", "float", 0, 1, "primitive"),
        ),
        ends=(energy_consumer.meta,),
    )

    def __init__(
        self,
        *,
        exponent_model: bool | None = None,
        p_constant_current: float | None = None,
        p_constant_impedance: float | None = None,
        p_constant_power: float | None = None,
        p_frequency_exponent: float | None = None,
        p_voltage_exponent: float | None = None,
        q_constant_current: float | None = None,
        q_constant_impedance: float | None = None,
        q_constant_power: float | None = None,
        q_frequency_exponent: float | None = None,
        q_voltage_exponent: float | None = None,
        energy_consumer: Iterable[EnergyConsumer] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.exponent_model = exponent_model
        self.p_constant_current = p_constant_current
        self.p_constant_impedance = p_constant_impedance
        self.p_constant_power = p_constant_power
        self.p_frequency_exponent = p_frequency_exponent
        self.p_voltage_exponent = p_voltage_exponent
        self.q_constant_current = q_constant_current
        self.q_constant_impedance = q_constant_impedance
        self.q_constant_power = q_constant_power
        self.q_frequency_exponent = q_frequency_exponent
        self.q_voltage_exponent = q_voltage_exponent
        if energy_consumer is not None:
            LoadResponseCharacteristic.energy_consumer.extend(self, energy_consumer)

    def add_energy_consumer(self, energy_consumer: EnergyConsumer) -> Self:
        return LoadResponseCharacteristic.energy_consumer.add(self, energy_consumer)

    def remove_energy_consumer(self, energy_consumer: EnergyConsumer) -> Self:
        return LoadResponseCharacteristic.energy_consumer.remove(self, energy_consumer)

    def clear_energy_consumer(self) -> Self:
        return LoadResponseCharacteristic.energy_consumer.clear(self)

    def num_energy_consumer(self) -> int:
        return LoadResponseCharacteristic.energy_consumer.count(self)

    def get_energy_consumer_by_mrid(self, mrid: str) -> EnergyConsumer | None:
        return LoadResponseCharacteristic.energy_consumer.get_by_mrid(self, mrid)
