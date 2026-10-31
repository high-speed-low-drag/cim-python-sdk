"""CIM enumeration FacilityKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FacilityKind(CimEnum):
    """Types of facilities at which an asset can be deployed."""

    substationHydroPlant = "substationHydroPlant"
    substationFossilPlant = "substationFossilPlant"
    substationNuclearPlant = "substationNuclearPlant"
    substationTransmission = "substationTransmission"
    substationSubTransmission = "substationSubTransmission"
    substationDistribution = "substationDistribution"
    distributionPoleTop = "distributionPoleTop"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FacilityKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{70D16D41-D031-4542-ABBE-A477D1CB0872}",
            kind="enumeration",
        )
    )
