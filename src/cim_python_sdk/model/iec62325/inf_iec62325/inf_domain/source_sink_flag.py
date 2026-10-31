"""CIM enumeration SourceSinkFlag (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SourceSinkFlag(CimEnum):
    """CIM enumeration SourceSinkFlag."""

    CSNK = "CSNK"
    CSRC = "CSRC"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SourceSinkFlag",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{8884AFCA-B94E-41ea-86E9-0DE651DB6C87}",
            kind="enumeration",
        )
    )
