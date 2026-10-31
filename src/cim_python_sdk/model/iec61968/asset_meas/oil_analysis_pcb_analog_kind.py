"""CIM enumeration OilAnalysisPCBAnalogKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilAnalysisPCBAnalogKind(CimEnum):
    """Analogs representing oil PCB analysis result."""

    aroclor1221 = "aroclor1221"
    aroclor1242 = "aroclor1242"
    aroclor1254 = "aroclor1254"
    aroclor1260 = "aroclor1260"
    aroclor1016 = "aroclor1016"
    totalPCB = "totalPCB"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilAnalysisPCBAnalogKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{241D48C5-4BAC-4fd9-85CC-EB7A3B227F36}",
            kind="enumeration",
        )
    )
