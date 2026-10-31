"""CIM class Discrete (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.meas.discrete_value import DiscreteValue
    from cim_python_sdk.model.iec61970.base.meas.value_alias_set import ValueAliasSet


class Discrete(Measurement):
    """Discrete represents a discrete Measurement, i.e. a Measurement representing discrete
    values, e.g. a Breaker position."""

    __slots__ = ("_discrete_values", "_value_alias_set", "max_value", "min_value", "normal_value")

    max_value: int | None
    min_value: int | None
    normal_value: int | None

    value_alias_set: One[ValueAliasSet] = One(
        EndMeta(
            name="value_alias_set",
            cim_role="ValueAliasSet",
            target="cim_python_sdk.model.iec61970.base.meas.value_alias_set:ValueAliasSet",
            many=False,
            lower=0,
            upper=1,
            inverse="discretes",
            aggregation="none",
        )
    )
    discrete_values: Many[DiscreteValue] = Many(
        EndMeta(
            name="discrete_values",
            cim_role="DiscreteValues",
            target="cim_python_sdk.model.iec61970.base.meas.discrete_value:DiscreteValue",
            many=True,
            lower=0,
            upper=None,
            inverse="discrete",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Discrete",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{57AFC760-6CA7-42c5-B988-36221A805D38}",
        attributes=(
            AttrMeta("max_value", "maxValue", "int", 0, 1, "primitive"),
            AttrMeta("min_value", "minValue", "int", 0, 1, "primitive"),
            AttrMeta("normal_value", "normalValue", "int", 0, 1, "primitive"),
        ),
        ends=(
            value_alias_set.meta,
            discrete_values.meta,
        ),
    )

    def __init__(
        self,
        *,
        max_value: int | None = None,
        min_value: int | None = None,
        normal_value: int | None = None,
        value_alias_set: ValueAliasSet | None = None,
        discrete_values: Iterable[DiscreteValue] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_value = max_value
        self.min_value = min_value
        self.normal_value = normal_value
        if value_alias_set is not None:
            self.value_alias_set = value_alias_set
        if discrete_values is not None:
            Discrete.discrete_values.extend(self, discrete_values)

    def add_discrete_value(self, discrete_value: DiscreteValue) -> Self:
        return Discrete.discrete_values.add(self, discrete_value)

    def remove_discrete_value(self, discrete_value: DiscreteValue) -> Self:
        return Discrete.discrete_values.remove(self, discrete_value)

    def clear_discrete_values(self) -> Self:
        return Discrete.discrete_values.clear(self)

    def num_discrete_value(self) -> int:
        return Discrete.discrete_values.count(self)

    def get_discrete_value_by_mrid(self, mrid: str) -> DiscreteValue | None:
        return Discrete.discrete_values.get_by_mrid(self, mrid)
