"""CIM class ValueToAlias (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.value_alias_set import ValueAliasSet


class ValueToAlias(IdentifiedObject):
    """Describes the translation of one particular value into a name, e.g. 1 as "Open"."""

    __slots__ = ("_value_alias_set", "value")

    value: int | None

    value_alias_set: One[ValueAliasSet] = One(
        EndMeta(
            name="value_alias_set",
            cim_role="ValueAliasSet",
            target="cim_python_sdk.model.iec61970.base.meas.value_alias_set:ValueAliasSet",
            many=False,
            lower=1,
            upper=1,
            inverse="values",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ValueToAlias",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{75778847-1FA9-4c53-9075-68C88D3D2369}",
        attributes=(AttrMeta("value", "value", "int", 0, 1, "primitive"),),
        ends=(value_alias_set.meta,),
    )

    def __init__(
        self,
        *,
        value: int | None = None,
        value_alias_set: ValueAliasSet | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
        if value_alias_set is not None:
            self.value_alias_set = value_alias_set
