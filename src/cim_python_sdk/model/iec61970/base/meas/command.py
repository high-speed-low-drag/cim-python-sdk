"""CIM class Command (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.control import Control

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.discrete_value import DiscreteValue
    from cim_python_sdk.model.iec61970.base.meas.value_alias_set import ValueAliasSet


class Command(Control):
    """A Command is a discrete control used for supervisory control."""

    __slots__ = ("_discrete_value", "_value_alias_set", "normal_value", "value")

    normal_value: int | None
    value: int | None

    discrete_value: One[DiscreteValue] = One(
        EndMeta(
            name="discrete_value",
            cim_role="DiscreteValue",
            target="cim_python_sdk.model.iec61970.base.meas.discrete_value:DiscreteValue",
            many=False,
            lower=1,
            upper=1,
            inverse="command",
            aggregation="none",
        )
    )
    value_alias_set: One[ValueAliasSet] = One(
        EndMeta(
            name="value_alias_set",
            cim_role="ValueAliasSet",
            target="cim_python_sdk.model.iec61970.base.meas.value_alias_set:ValueAliasSet",
            many=False,
            lower=0,
            upper=1,
            inverse="commands",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Command",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{9CE025EC-A020-4c5c-B91F-F8D64E61693F}",
        attributes=(
            AttrMeta("normal_value", "normalValue", "int", 0, 1, "primitive"),
            AttrMeta("value", "value", "int", 0, 1, "primitive"),
        ),
        ends=(
            discrete_value.meta,
            value_alias_set.meta,
        ),
    )

    def __init__(
        self,
        *,
        normal_value: int | None = None,
        value: int | None = None,
        discrete_value: DiscreteValue | None = None,
        value_alias_set: ValueAliasSet | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.normal_value = normal_value
        self.value = value
        if discrete_value is not None:
            self.discrete_value = discrete_value
        if value_alias_set is not None:
            self.value_alias_set = value_alias_set
