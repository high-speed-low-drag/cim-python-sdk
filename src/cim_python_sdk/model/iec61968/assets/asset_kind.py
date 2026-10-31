"""CIM enumeration AssetKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetKind(CimEnum):
    """Kinds of assets or asset components."""

    breakerAirBlastBreaker = "breakerAirBlastBreaker"
    breakerBulkOilBreaker = "breakerBulkOilBreaker"
    breakerMinimumOilBreaker = "breakerMinimumOilBreaker"
    breakerSF6DeadTankBreaker = "breakerSF6DeadTankBreaker"
    breakerSF6LiveTankBreaker = "breakerSF6LiveTankBreaker"
    breakerTankAssembly = "breakerTankAssembly"
    breakerInsulatingStackAssembly = "breakerInsulatingStackAssembly"
    transformer = "transformer"
    transformerTank = "transformerTank"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{F59B7C24-2676-4627-9CFF-4EA9AC02D336}",
            kind="enumeration",
        )
    )
