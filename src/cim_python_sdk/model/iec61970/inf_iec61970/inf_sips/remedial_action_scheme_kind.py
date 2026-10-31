"""CIM enumeration RemedialActionSchemeKind (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RemedialActionSchemeKind(CimEnum):
    """Classification of Remedial Action Scheme."""

    rAS = "rAS"
    rAP = "rAP"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RemedialActionSchemeKind",
            package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
            guid="{A024B5FF-8AE9-4f91-A91B-806CA4FF2B6C}",
            kind="enumeration",
        )
    )
