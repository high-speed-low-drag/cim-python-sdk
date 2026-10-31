"""CIM enumeration AdderType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AdderType(CimEnum):
    """BASELI NE

    NEGOTIATED"""

    BASELINE = "BASELINE"
    NEGOTIATED = "NEGOTIATED"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AdderType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{60F4885F-4176-42fe-BF55-160ACAF74B6F}",
            kind="enumeration",
        )
    )
