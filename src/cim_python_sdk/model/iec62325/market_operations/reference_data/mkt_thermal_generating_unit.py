"""CIM class MktThermalGeneratingUnit (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
    ThermalGeneratingUnit,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration_member import (
        CombinedCycleConfigurationMember,
    )


class MktThermalGeneratingUnit(ThermalGeneratingUnit):
    """Subclass of ThermalGeneratingUnit from Production Package in IEC 61970."""

    __slots__ = ("_combined_cycle_configuration_member",)

    combined_cycle_configuration_member: Many[CombinedCycleConfigurationMember] = Many(
        EndMeta(
            name="combined_cycle_configuration_member",
            cim_role="CombinedCycleConfigurationMember",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration_member:CombinedCycleConfigurationMember",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_thermal_generating_unit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktThermalGeneratingUnit",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{FDE35007-FB33-4d14-B0B4-96A9AA230BD3}",
        ends=(combined_cycle_configuration_member.meta,),
    )

    def __init__(
        self,
        *,
        combined_cycle_configuration_member: Iterable[CombinedCycleConfigurationMember]
        | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if combined_cycle_configuration_member is not None:
            MktThermalGeneratingUnit.combined_cycle_configuration_member.extend(
                self, combined_cycle_configuration_member
            )

    def add_combined_cycle_configuration_member(
        self, combined_cycle_configuration_member: CombinedCycleConfigurationMember
    ) -> Self:
        return MktThermalGeneratingUnit.combined_cycle_configuration_member.add(
            self, combined_cycle_configuration_member
        )

    def remove_combined_cycle_configuration_member(
        self, combined_cycle_configuration_member: CombinedCycleConfigurationMember
    ) -> Self:
        return MktThermalGeneratingUnit.combined_cycle_configuration_member.remove(
            self, combined_cycle_configuration_member
        )

    def clear_combined_cycle_configuration_member(self) -> Self:
        return MktThermalGeneratingUnit.combined_cycle_configuration_member.clear(self)

    def num_combined_cycle_configuration_member(self) -> int:
        return MktThermalGeneratingUnit.combined_cycle_configuration_member.count(self)

    def get_combined_cycle_configuration_member_by_mrid(
        self, mrid: str
    ) -> CombinedCycleConfigurationMember | None:
        return MktThermalGeneratingUnit.combined_cycle_configuration_member.get_by_mrid(self, mrid)
