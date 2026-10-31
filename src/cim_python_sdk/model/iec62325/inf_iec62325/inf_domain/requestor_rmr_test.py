"""CIM enumeration RequestorRmrTest (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RequestorRmrTest(CimEnum):
    """MP

    ISO"""

    MP = "MP"
    ISO = "ISO"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RequestorRmrTest",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{5529927B-0386-4b8b-98FE-BE33F91D4853}",
            kind="enumeration",
        )
    )
