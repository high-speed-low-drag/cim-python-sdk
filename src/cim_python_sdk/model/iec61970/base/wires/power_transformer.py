"""CIM class PowerTransformer (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.power_transformer_end import PowerTransformerEnd
    from cim_python_sdk.model.iec61970.base.wires.transformer_tank import TransformerTank


class PowerTransformer(ConductingEquipment):
    """An electrical device consisting of two or more coupled windings, with or without a
    magnetic core, for introducing mutual coupling between electric circuits. Transformers
    can be used to control voltage and phase shift (active power flow).

    A power transformer may be composed of separate transformer tanks that need not be
    identical.

    A power transformer can be modelled with or without tanks and is intended for use in
    both balanced and unbalanced representations. A power transformer typically has two
    terminals, but may have one (grounding), three or more terminals.

    The inherited association ConductingEquipment.BaseVoltage should not be used. The
    association from TransformerEnd to BaseVoltage should be used instead."""

    __slots__ = (
        "_power_transformer_end",
        "_transformer_tanks",
        "before_sh_circuit_highest_operating_current",
        "before_sh_circuit_highest_operating_voltage",
        "before_short_circuit_angle_pf",
        "high_side_min_operating_u",
        "is_part_of_generator_unit",
        "operational_values_considered",
        "vector_group",
    )

    before_sh_circuit_highest_operating_current: float | None  # CurrentFlow
    before_sh_circuit_highest_operating_voltage: float | None  # Voltage
    before_short_circuit_angle_pf: float | None  # AngleDegrees
    high_side_min_operating_u: float | None  # Voltage
    is_part_of_generator_unit: bool | None
    operational_values_considered: bool | None
    vector_group: str | None

    transformer_tanks: Many[TransformerTank] = Many(
        EndMeta(
            name="transformer_tanks",
            cim_role="TransformerTanks",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_tank:TransformerTank",
            many=True,
            lower=0,
            upper=None,
            inverse="power_transformer",
            aggregation="none",
        )
    )
    power_transformer_end: Many[PowerTransformerEnd] = Many(
        EndMeta(
            name="power_transformer_end",
            cim_role="PowerTransformerEnd",
            target="cim_python_sdk.model.iec61970.base.wires.power_transformer_end:PowerTransformerEnd",
            many=True,
            lower=0,
            upper=None,
            inverse="power_transformer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerTransformer",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{3D50627C-324C-4e9d-AB5C-592E0A1E0AFE}",
        attributes=(
            AttrMeta(
                "before_sh_circuit_highest_operating_current",
                "beforeShCircuitHighestOperatingCurrent",
                "CurrentFlow",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "before_sh_circuit_highest_operating_voltage",
                "beforeShCircuitHighestOperatingVoltage",
                "Voltage",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "before_short_circuit_angle_pf",
                "beforeShortCircuitAnglePf",
                "AngleDegrees",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "high_side_min_operating_u", "highSideMinOperatingU", "Voltage", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "is_part_of_generator_unit", "isPartOfGeneratorUnit", "bool", 0, 1, "primitive"
            ),
            AttrMeta(
                "operational_values_considered",
                "operationalValuesConsidered",
                "bool",
                0,
                1,
                "primitive",
            ),
            AttrMeta("vector_group", "vectorGroup", "str", 0, 1, "primitive"),
        ),
        ends=(
            transformer_tanks.meta,
            power_transformer_end.meta,
        ),
    )

    def __init__(
        self,
        *,
        before_sh_circuit_highest_operating_current: float | None = None,
        before_sh_circuit_highest_operating_voltage: float | None = None,
        before_short_circuit_angle_pf: float | None = None,
        high_side_min_operating_u: float | None = None,
        is_part_of_generator_unit: bool | None = None,
        operational_values_considered: bool | None = None,
        vector_group: str | None = None,
        transformer_tanks: Iterable[TransformerTank] | None = None,
        power_transformer_end: Iterable[PowerTransformerEnd] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.before_sh_circuit_highest_operating_current = (
            before_sh_circuit_highest_operating_current
        )
        self.before_sh_circuit_highest_operating_voltage = (
            before_sh_circuit_highest_operating_voltage
        )
        self.before_short_circuit_angle_pf = before_short_circuit_angle_pf
        self.high_side_min_operating_u = high_side_min_operating_u
        self.is_part_of_generator_unit = is_part_of_generator_unit
        self.operational_values_considered = operational_values_considered
        self.vector_group = vector_group
        if transformer_tanks is not None:
            PowerTransformer.transformer_tanks.extend(self, transformer_tanks)
        if power_transformer_end is not None:
            PowerTransformer.power_transformer_end.extend(self, power_transformer_end)

    def add_transformer_tank(self, transformer_tank: TransformerTank) -> Self:
        return PowerTransformer.transformer_tanks.add(self, transformer_tank)

    def remove_transformer_tank(self, transformer_tank: TransformerTank) -> Self:
        return PowerTransformer.transformer_tanks.remove(self, transformer_tank)

    def clear_transformer_tanks(self) -> Self:
        return PowerTransformer.transformer_tanks.clear(self)

    def num_transformer_tank(self) -> int:
        return PowerTransformer.transformer_tanks.count(self)

    def get_transformer_tank_by_mrid(self, mrid: str) -> TransformerTank | None:
        return PowerTransformer.transformer_tanks.get_by_mrid(self, mrid)

    def add_power_transformer_end(self, power_transformer_end: PowerTransformerEnd) -> Self:
        return PowerTransformer.power_transformer_end.add(self, power_transformer_end)

    def remove_power_transformer_end(self, power_transformer_end: PowerTransformerEnd) -> Self:
        return PowerTransformer.power_transformer_end.remove(self, power_transformer_end)

    def clear_power_transformer_end(self) -> Self:
        return PowerTransformer.power_transformer_end.clear(self)

    def num_power_transformer_end(self) -> int:
        return PowerTransformer.power_transformer_end.count(self)

    def get_power_transformer_end_by_mrid(self, mrid: str) -> PowerTransformerEnd | None:
        return PowerTransformer.power_transformer_end.get_by_mrid(self, mrid)
