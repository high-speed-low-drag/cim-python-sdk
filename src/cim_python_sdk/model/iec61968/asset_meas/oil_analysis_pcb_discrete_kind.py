"""CIM enumeration OilAnalysisPCBDiscreteKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilAnalysisPCBDiscreteKind(CimEnum):
    """Discretes representing oil PCB test analysis result."""

    testKitPCB = "testKitPCB"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilAnalysisPCBDiscreteKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{EA96531E-665F-4237-822A-1488CF0C1410}",
            kind="enumeration",
        )
    )
