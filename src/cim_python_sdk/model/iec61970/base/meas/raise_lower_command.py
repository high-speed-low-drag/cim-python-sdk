"""CIM class RaiseLowerCommand (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.analog_control import AnalogControl

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.value_alias_set import ValueAliasSet


class RaiseLowerCommand(AnalogControl):
    """An analog control that increases or decreases a set point value with pulses. Unless
    otherwise specified, one pulse moves the set point by one."""

    __slots__ = ("_value_alias_set",)

    value_alias_set: One[ValueAliasSet] = One(
        EndMeta(
            name="value_alias_set",
            cim_role="ValueAliasSet",
            target="cim_python_sdk.model.iec61970.base.meas.value_alias_set:ValueAliasSet",
            many=False,
            lower=0,
            upper=1,
            inverse="raise_lower_commands",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RaiseLowerCommand",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{E19BB2D1-4556-4afd-994D-3244337C8F3E}",
        ends=(value_alias_set.meta,),
    )

    def __init__(
        self,
        *,
        value_alias_set: ValueAliasSet | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if value_alias_set is not None:
            self.value_alias_set = value_alias_set
