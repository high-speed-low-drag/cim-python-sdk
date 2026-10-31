"""CIM enumeration UnitRegulationKind (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UnitRegulationKind(CimEnum):
    """Unit regulation kind."""

    v0 = "0"
    v1 = "1"
    v2 = "2"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UnitRegulationKind",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{8A931678-F5F6-4de3-BCAD-4CA1E454766B}",
            kind="enumeration",
        )
    )
