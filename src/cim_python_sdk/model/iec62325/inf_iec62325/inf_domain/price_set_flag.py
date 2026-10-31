"""CIM enumeration PriceSetFlag (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PriceSetFlag(CimEnum):
    """Y - indicates a resource is capable of setting the Markte Clearing Price

    S - indicates the resource must submit bids for energy at $ 0

    N - indicates the resource does not have to submit bids for energy at $ 0"""

    Y = "Y"
    S = "S"
    N = "N"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PriceSetFlag",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{526D0731-D2A7-4851-AA3D-9665E1987A8F}",
            kind="enumeration",
        )
    )
