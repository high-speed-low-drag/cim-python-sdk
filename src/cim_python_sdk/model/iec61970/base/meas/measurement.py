"""CIM class Measurement (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_meas.calculation_method_hierarchy import (
        CalculationMethodHierarchy,
    )
    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.procedure import Procedure
    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.operations.measurement_action import MeasurementAction
    from cim_python_sdk.model.iec61970.base.core.acdc_terminal import ACDCTerminal
    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode
    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.measurement_calculator_input import (
        MeasurementCalculatorInput,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_measurement import PinMeasurement
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_adjustment import (
        ProtectiveActionAdjustment,
    )


class Measurement(IdentifiedObject):
    """A Measurement represents any measured, calculated or non-measured non-calculated
    quantity. Any piece of equipment may contain Measurements, e.g. a substation may have
    temperature measurements and door open indications, a transformer may have oil
    temperature and tank pressure measurements, a bay may contain a number of power flow
    measurements and a Breaker may contain a switch status measurement.

    The PSR - Measurement association is intended to capture this use of Measurement and is
    included in the naming hierarchy based on EquipmentContainer. The naming hierarchy
    typically has Measurements as leaves, e.g.
    Substation-VoltageLevel-Bay-Switch-Measurement.

    Some Measurements represent quantities related to a particular sensor location in the
    network, e.g. a voltage transformer (VT) or potential transformer (PT) at a busbar or a
    current transformer (CT) at the bar between a breaker and an isolator. The sensing
    position is not captured in the PSR - Measurement association. Instead it is captured by
    the Measurement - Terminal association that is used to define the sensing location in
    the network topology. The location is defined by the connection of the Terminal to
    ConductingEquipment.

    If both a Terminal and PSR are associated, and the PSR is of type ConductingEquipment,
    the associated Terminal should belong to that ConductingEquipment instance.

    When the sensor location is needed both Measurement-PSR and Measurement-Terminal are
    used. The Measurement-Terminal association is never used alone."""

    __slots__ = (
        "_asset",
        "_calculation_method_hierarchy",
        "_locations",
        "_measurement_action",
        "_measurement_calculator_input",
        "_pin_measurement",
        "_power_system_resource",
        "_procedures",
        "_protective_action_adjustment",
        "_terminal",
        "measurement_type",
        "phases",
        "unit_multiplier",
        "unit_symbol",
    )

    measurement_type: str | None
    phases: PhaseCode | None
    unit_multiplier: UnitMultiplier | None
    unit_symbol: UnitSymbol | None

    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="measurements",
            aggregation="none",
        )
    )
    measurement_calculator_input: Many[MeasurementCalculatorInput] = Many(
        EndMeta(
            name="measurement_calculator_input",
            cim_role="MeasurementCalculatorInput",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.measurement_calculator_input:MeasurementCalculatorInput",
            many=True,
            lower=0,
            upper=None,
            inverse="measurement",
            aggregation="none",
        )
    )
    measurement_action: One[MeasurementAction] = One(
        EndMeta(
            name="measurement_action",
            cim_role="MeasurementAction",
            target="cim_python_sdk.model.iec61968.operations.measurement_action:MeasurementAction",
            many=False,
            lower=0,
            upper=1,
            inverse="measurement",
            aggregation="none",
        )
    )
    power_system_resource: One[PowerSystemResource] = One(
        EndMeta(
            name="power_system_resource",
            cim_role="PowerSystemResource",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=False,
            lower=0,
            upper=1,
            inverse="measurements",
            aggregation="none",
        )
    )
    protective_action_adjustment: Many[ProtectiveActionAdjustment] = Many(
        EndMeta(
            name="protective_action_adjustment",
            cim_role="ProtectiveActionAdjustment",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_adjustment:ProtectiveActionAdjustment",
            many=True,
            lower=0,
            upper=None,
            inverse="measurement",
            aggregation="none",
        )
    )
    terminal: One[ACDCTerminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.acdc_terminal:ACDCTerminal",
            many=False,
            lower=0,
            upper=1,
            inverse="measurements",
            aggregation="none",
        )
    )
    pin_measurement: Many[PinMeasurement] = Many(
        EndMeta(
            name="pin_measurement",
            cim_role="PinMeasurement",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_measurement:PinMeasurement",
            many=True,
            lower=0,
            upper=None,
            inverse="measurement",
            aggregation="none",
        )
    )
    locations: Many[Location] = Many(
        EndMeta(
            name="locations",
            cim_role="Locations",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=True,
            lower=0,
            upper=None,
            inverse="measurements",
            aggregation="none",
        )
    )
    calculation_method_hierarchy: One[CalculationMethodHierarchy] = One(
        EndMeta(
            name="calculation_method_hierarchy",
            cim_role="CalculationMethodHierarchy",
            target="cim_python_sdk.model.iec61968.asset_meas.calculation_method_hierarchy:CalculationMethodHierarchy",
            many=False,
            lower=0,
            upper=1,
            inverse="measurement",
            aggregation="none",
        )
    )
    procedures: Many[Procedure] = Many(
        EndMeta(
            name="procedures",
            cim_role="Procedures",
            target="cim_python_sdk.model.iec61968.assets.procedure:Procedure",
            many=True,
            lower=0,
            upper=None,
            inverse="measurements",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Measurement",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{AB1758FA-3A4D-478f-BE4F-ADC8E2F886CC}",
        attributes=(
            AttrMeta("measurement_type", "measurementType", "str", 0, 1, "primitive"),
            AttrMeta("phases", "phases", "PhaseCode", 0, 1, "enumeration"),
            AttrMeta("unit_multiplier", "unitMultiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit_symbol", "unitSymbol", "UnitSymbol", 0, 1, "enumeration"),
        ),
        ends=(
            asset.meta,
            measurement_calculator_input.meta,
            measurement_action.meta,
            power_system_resource.meta,
            protective_action_adjustment.meta,
            terminal.meta,
            pin_measurement.meta,
            locations.meta,
            calculation_method_hierarchy.meta,
            procedures.meta,
        ),
    )

    def __init__(
        self,
        *,
        measurement_type: str | None = None,
        phases: PhaseCode | None = None,
        unit_multiplier: UnitMultiplier | None = None,
        unit_symbol: UnitSymbol | None = None,
        asset: Asset | None = None,
        measurement_calculator_input: Iterable[MeasurementCalculatorInput] | None = None,
        measurement_action: MeasurementAction | None = None,
        power_system_resource: PowerSystemResource | None = None,
        protective_action_adjustment: Iterable[ProtectiveActionAdjustment] | None = None,
        terminal: ACDCTerminal | None = None,
        pin_measurement: Iterable[PinMeasurement] | None = None,
        locations: Iterable[Location] | None = None,
        calculation_method_hierarchy: CalculationMethodHierarchy | None = None,
        procedures: Iterable[Procedure] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.measurement_type = measurement_type
        self.phases = phases
        self.unit_multiplier = unit_multiplier
        self.unit_symbol = unit_symbol
        if asset is not None:
            self.asset = asset
        if measurement_calculator_input is not None:
            Measurement.measurement_calculator_input.extend(self, measurement_calculator_input)
        if measurement_action is not None:
            self.measurement_action = measurement_action
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource
        if protective_action_adjustment is not None:
            Measurement.protective_action_adjustment.extend(self, protective_action_adjustment)
        if terminal is not None:
            self.terminal = terminal
        if pin_measurement is not None:
            Measurement.pin_measurement.extend(self, pin_measurement)
        if locations is not None:
            Measurement.locations.extend(self, locations)
        if calculation_method_hierarchy is not None:
            self.calculation_method_hierarchy = calculation_method_hierarchy
        if procedures is not None:
            Measurement.procedures.extend(self, procedures)

    def add_measurement_calculator_input(
        self, measurement_calculator_input: MeasurementCalculatorInput
    ) -> Self:
        return Measurement.measurement_calculator_input.add(self, measurement_calculator_input)

    def remove_measurement_calculator_input(
        self, measurement_calculator_input: MeasurementCalculatorInput
    ) -> Self:
        return Measurement.measurement_calculator_input.remove(self, measurement_calculator_input)

    def clear_measurement_calculator_input(self) -> Self:
        return Measurement.measurement_calculator_input.clear(self)

    def num_measurement_calculator_input(self) -> int:
        return Measurement.measurement_calculator_input.count(self)

    def get_measurement_calculator_input_by_mrid(
        self, mrid: str
    ) -> MeasurementCalculatorInput | None:
        return Measurement.measurement_calculator_input.get_by_mrid(self, mrid)

    def add_protective_action_adjustment(
        self, protective_action_adjustment: ProtectiveActionAdjustment
    ) -> Self:
        return Measurement.protective_action_adjustment.add(self, protective_action_adjustment)

    def remove_protective_action_adjustment(
        self, protective_action_adjustment: ProtectiveActionAdjustment
    ) -> Self:
        return Measurement.protective_action_adjustment.remove(self, protective_action_adjustment)

    def clear_protective_action_adjustment(self) -> Self:
        return Measurement.protective_action_adjustment.clear(self)

    def num_protective_action_adjustment(self) -> int:
        return Measurement.protective_action_adjustment.count(self)

    def get_protective_action_adjustment_by_mrid(
        self, mrid: str
    ) -> ProtectiveActionAdjustment | None:
        return Measurement.protective_action_adjustment.get_by_mrid(self, mrid)

    def add_pin_measurement(self, pin_measurement: PinMeasurement) -> Self:
        return Measurement.pin_measurement.add(self, pin_measurement)

    def remove_pin_measurement(self, pin_measurement: PinMeasurement) -> Self:
        return Measurement.pin_measurement.remove(self, pin_measurement)

    def clear_pin_measurement(self) -> Self:
        return Measurement.pin_measurement.clear(self)

    def num_pin_measurement(self) -> int:
        return Measurement.pin_measurement.count(self)

    def get_pin_measurement_by_mrid(self, mrid: str) -> PinMeasurement | None:
        return Measurement.pin_measurement.get_by_mrid(self, mrid)

    def add_location(self, location: Location) -> Self:
        return Measurement.locations.add(self, location)

    def remove_location(self, location: Location) -> Self:
        return Measurement.locations.remove(self, location)

    def clear_locations(self) -> Self:
        return Measurement.locations.clear(self)

    def num_location(self) -> int:
        return Measurement.locations.count(self)

    def get_location_by_mrid(self, mrid: str) -> Location | None:
        return Measurement.locations.get_by_mrid(self, mrid)

    def add_procedure(self, procedure: Procedure) -> Self:
        return Measurement.procedures.add(self, procedure)

    def remove_procedure(self, procedure: Procedure) -> Self:
        return Measurement.procedures.remove(self, procedure)

    def clear_procedures(self) -> Self:
        return Measurement.procedures.clear(self)

    def num_procedure(self) -> int:
        return Measurement.procedures.count(self)

    def get_procedure_by_mrid(self, mrid: str) -> Procedure | None:
        return Measurement.procedures.get_by_mrid(self, mrid)
