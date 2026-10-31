"""CIM enumeration AnalyticKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AnalyticKind(CimEnum):
    """Possible kinds of analytics."""

    riskAnalytic = "riskAnalytic"
    faultAnalytic = "faultAnalytic"
    agingAnalytic = "agingAnalytic"
    healthAnalytic = "healthAnalytic"
    replacementAnalytic = "replacementAnalytic"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AnalyticKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{A8C5490A-2C86-4fa6-BD75-391A9145E814}",
            kind="enumeration",
        )
    )
