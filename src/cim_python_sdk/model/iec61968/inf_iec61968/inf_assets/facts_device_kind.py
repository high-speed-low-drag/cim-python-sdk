"""CIM enumeration FACTSDeviceKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FACTSDeviceKind(CimEnum):
    """Kind of FACTS device."""

    svc = "svc"
    statcom = "statcom"
    tcpar = "tcpar"
    tcsc = "tcsc"
    tcvl = "tcvl"
    tsbr = "tsbr"
    tssc = "tssc"
    upfc = "upfc"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FACTSDeviceKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{DF08C5B7-466B-42d9-950D-59B1EBE5305B}",
            kind="enumeration",
        )
    )
