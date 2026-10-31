"""CIM class ExpectedEnergyValues (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.expected_energy import (
        ExpectedEnergy,
    )


class ExpectedEnergyValues(CimObject):
    """Model Expected Energy from Market Clearing."""

    __slots__ = ("_expected_energy", "_registered_resource", "energy_type_code", "expected_mwh")

    energy_type_code: str | None
    expected_mwh: float | None

    expected_energy: One[ExpectedEnergy] = One(
        EndMeta(
            name="expected_energy",
            cim_role="ExpectedEnergy",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.expected_energy:ExpectedEnergy",
            many=False,
            lower=1,
            upper=1,
            inverse="expected_energy_values",
            aggregation="none",
        )
    )
    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="expected_energy_values",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExpectedEnergyValues",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{A07D68F4-9F27-40b6-9738-BDDEC26020F7}",
        attributes=(
            AttrMeta("energy_type_code", "energyTypeCode", "str", 0, 1, "primitive"),
            AttrMeta("expected_mwh", "expectedMwh", "float", 0, 1, "primitive"),
        ),
        ends=(
            expected_energy.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        energy_type_code: str | None = None,
        expected_mwh: float | None = None,
        expected_energy: ExpectedEnergy | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.energy_type_code = energy_type_code
        self.expected_mwh = expected_mwh
        if expected_energy is not None:
            self.expected_energy = expected_energy
        if registered_resource is not None:
            self.registered_resource = registered_resource
