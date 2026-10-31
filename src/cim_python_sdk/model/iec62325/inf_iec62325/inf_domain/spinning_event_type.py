"""CIM enumeration SpinningEventType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SpinningEventType(CimEnum):
    """CIM enumeration SpinningEventType."""

    RZ = "RZ"
    AA = "AA"
    CA = "CA"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SpinningEventType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{7FC49840-94E6-4808-841E-B8CCE110F3A9}",
            kind="enumeration",
        )
    )
