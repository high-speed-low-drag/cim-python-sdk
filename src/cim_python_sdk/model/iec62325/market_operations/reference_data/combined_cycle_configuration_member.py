"""CIM class CombinedCycleConfigurationMember (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration import (
        CombinedCycleConfiguration,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_thermal_generating_unit import (
        MktThermalGeneratingUnit,
    )


class CombinedCycleConfigurationMember(IdentifiedObject):
    """Configuration Member of CCP Configuration."""

    __slots__ = (
        "_combined_cycle_configuration",
        "_mkt_thermal_generating_unit",
        "primary",
        "steam",
    )

    primary: bool | None
    steam: bool | None

    combined_cycle_configuration: One[CombinedCycleConfiguration] = One(
        EndMeta(
            name="combined_cycle_configuration",
            cim_role="CombinedCycleConfiguration",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration:CombinedCycleConfiguration",
            many=False,
            lower=1,
            upper=1,
            inverse="combined_cycle_configuration_member",
            aggregation="none",
        )
    )
    mkt_thermal_generating_unit: One[MktThermalGeneratingUnit] = One(
        EndMeta(
            name="mkt_thermal_generating_unit",
            cim_role="MktThermalGeneratingUnit",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_thermal_generating_unit:MktThermalGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="combined_cycle_configuration_member",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CombinedCycleConfigurationMember",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{36551068-B3D4-4e8a-81C1-9ABBE0558648}",
        attributes=(
            AttrMeta("primary", "primary", "bool", 0, 1, "primitive"),
            AttrMeta("steam", "steam", "bool", 0, 1, "primitive"),
        ),
        ends=(
            combined_cycle_configuration.meta,
            mkt_thermal_generating_unit.meta,
        ),
    )

    def __init__(
        self,
        *,
        primary: bool | None = None,
        steam: bool | None = None,
        combined_cycle_configuration: CombinedCycleConfiguration | None = None,
        mkt_thermal_generating_unit: MktThermalGeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.primary = primary
        self.steam = steam
        if combined_cycle_configuration is not None:
            self.combined_cycle_configuration = combined_cycle_configuration
        if mkt_thermal_generating_unit is not None:
            self.mkt_thermal_generating_unit = mkt_thermal_generating_unit
