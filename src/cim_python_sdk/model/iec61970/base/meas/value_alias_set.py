"""CIM class ValueAliasSet (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.meas.command import Command
    from cim_python_sdk.model.iec61970.base.meas.discrete import Discrete
    from cim_python_sdk.model.iec61970.base.meas.raise_lower_command import RaiseLowerCommand
    from cim_python_sdk.model.iec61970.base.meas.value_to_alias import ValueToAlias


class ValueAliasSet(IdentifiedObject):
    """Describes the translation of a set of values into a name and is intendend to facilitate
    custom translations. Each ValueAliasSet has a name, description etc. A specific
    Measurement may represent a discrete state like Open, Closed, Intermediate etc. This
    requires a translation from the MeasurementValue.value number to a string, e.g.
    0->"Invalid", 1->"Open", 2->"Closed", 3->"Intermediate". Each ValueToAlias member in
    ValueAliasSet.Value describe a mapping for one particular value to a name."""

    __slots__ = ("_commands", "_discretes", "_raise_lower_commands", "_values")

    values: Many[ValueToAlias] = Many(
        EndMeta(
            name="values",
            cim_role="Values",
            target="cim_python_sdk.model.iec61970.base.meas.value_to_alias:ValueToAlias",
            many=True,
            lower=1,
            upper=None,
            inverse="value_alias_set",
            aggregation="shared",
        )
    )
    discretes: Many[Discrete] = Many(
        EndMeta(
            name="discretes",
            cim_role="Discretes",
            target="cim_python_sdk.model.iec61970.base.meas.discrete:Discrete",
            many=True,
            lower=0,
            upper=None,
            inverse="value_alias_set",
            aggregation="none",
        )
    )
    raise_lower_commands: Many[RaiseLowerCommand] = Many(
        EndMeta(
            name="raise_lower_commands",
            cim_role="RaiseLowerCommands",
            target="cim_python_sdk.model.iec61970.base.meas.raise_lower_command:RaiseLowerCommand",
            many=True,
            lower=0,
            upper=None,
            inverse="value_alias_set",
            aggregation="none",
        )
    )
    commands: Many[Command] = Many(
        EndMeta(
            name="commands",
            cim_role="Commands",
            target="cim_python_sdk.model.iec61970.base.meas.command:Command",
            many=True,
            lower=0,
            upper=None,
            inverse="value_alias_set",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ValueAliasSet",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{BBCB7356-E07A-417a-8B1B-0DF35589245D}",
        ends=(
            values.meta,
            discretes.meta,
            raise_lower_commands.meta,
            commands.meta,
        ),
    )

    def __init__(
        self,
        *,
        values: Iterable[ValueToAlias] | None = None,
        discretes: Iterable[Discrete] | None = None,
        raise_lower_commands: Iterable[RaiseLowerCommand] | None = None,
        commands: Iterable[Command] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if values is not None:
            ValueAliasSet.values.extend(self, values)
        if discretes is not None:
            ValueAliasSet.discretes.extend(self, discretes)
        if raise_lower_commands is not None:
            ValueAliasSet.raise_lower_commands.extend(self, raise_lower_commands)
        if commands is not None:
            ValueAliasSet.commands.extend(self, commands)

    def add_value(self, value: ValueToAlias) -> Self:
        return ValueAliasSet.values.add(self, value)

    def remove_value(self, value: ValueToAlias) -> Self:
        return ValueAliasSet.values.remove(self, value)

    def clear_values(self) -> Self:
        return ValueAliasSet.values.clear(self)

    def num_value(self) -> int:
        return ValueAliasSet.values.count(self)

    def get_value_by_mrid(self, mrid: str) -> ValueToAlias | None:
        return ValueAliasSet.values.get_by_mrid(self, mrid)

    def add_discrete(self, discrete: Discrete) -> Self:
        return ValueAliasSet.discretes.add(self, discrete)

    def remove_discrete(self, discrete: Discrete) -> Self:
        return ValueAliasSet.discretes.remove(self, discrete)

    def clear_discretes(self) -> Self:
        return ValueAliasSet.discretes.clear(self)

    def num_discrete(self) -> int:
        return ValueAliasSet.discretes.count(self)

    def get_discrete_by_mrid(self, mrid: str) -> Discrete | None:
        return ValueAliasSet.discretes.get_by_mrid(self, mrid)

    def add_raise_lower_command(self, raise_lower_command: RaiseLowerCommand) -> Self:
        return ValueAliasSet.raise_lower_commands.add(self, raise_lower_command)

    def remove_raise_lower_command(self, raise_lower_command: RaiseLowerCommand) -> Self:
        return ValueAliasSet.raise_lower_commands.remove(self, raise_lower_command)

    def clear_raise_lower_commands(self) -> Self:
        return ValueAliasSet.raise_lower_commands.clear(self)

    def num_raise_lower_command(self) -> int:
        return ValueAliasSet.raise_lower_commands.count(self)

    def get_raise_lower_command_by_mrid(self, mrid: str) -> RaiseLowerCommand | None:
        return ValueAliasSet.raise_lower_commands.get_by_mrid(self, mrid)

    def add_command(self, command: Command) -> Self:
        return ValueAliasSet.commands.add(self, command)

    def remove_command(self, command: Command) -> Self:
        return ValueAliasSet.commands.remove(self, command)

    def clear_commands(self) -> Self:
        return ValueAliasSet.commands.clear(self)

    def num_command(self) -> int:
        return ValueAliasSet.commands.count(self)

    def get_command_by_mrid(self, mrid: str) -> Command | None:
        return ValueAliasSet.commands.get_by_mrid(self, mrid)
