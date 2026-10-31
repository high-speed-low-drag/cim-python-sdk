"""CIM class MktGeneratingUnit (TC57CIM/IEC62325/MarketCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.generation.production.generating_unit import GeneratingUnit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.generating_unit_dynamic_values import (
        GeneratingUnitDynamicValues,
    )


class MktGeneratingUnit(GeneratingUnit):
    """Subclass of IEC61970:Production:GeneratingUnit."""

    __slots__ = ("_generating_unit_dynamic_values",)

    generating_unit_dynamic_values: Many[GeneratingUnitDynamicValues] = Many(
        EndMeta(
            name="generating_unit_dynamic_values",
            cim_role="GeneratingUnitDynamicValues",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.generating_unit_dynamic_values:GeneratingUnitDynamicValues",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_generating_unit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktGeneratingUnit",
        package="TC57CIM/IEC62325/MarketCommon",
        guid="{C783CC9F-4FDF-4911-BA30-0FBA52A031D2}",
        ends=(generating_unit_dynamic_values.meta,),
    )

    def __init__(
        self,
        *,
        generating_unit_dynamic_values: Iterable[GeneratingUnitDynamicValues] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if generating_unit_dynamic_values is not None:
            MktGeneratingUnit.generating_unit_dynamic_values.extend(
                self, generating_unit_dynamic_values
            )

    def add_generating_unit_dynamic_value(
        self, generating_unit_dynamic_value: GeneratingUnitDynamicValues
    ) -> Self:
        return MktGeneratingUnit.generating_unit_dynamic_values.add(
            self, generating_unit_dynamic_value
        )

    def remove_generating_unit_dynamic_value(
        self, generating_unit_dynamic_value: GeneratingUnitDynamicValues
    ) -> Self:
        return MktGeneratingUnit.generating_unit_dynamic_values.remove(
            self, generating_unit_dynamic_value
        )

    def clear_generating_unit_dynamic_values(self) -> Self:
        return MktGeneratingUnit.generating_unit_dynamic_values.clear(self)

    def num_generating_unit_dynamic_value(self) -> int:
        return MktGeneratingUnit.generating_unit_dynamic_values.count(self)
