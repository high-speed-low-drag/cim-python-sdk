"""CIM enumeration IPAddressKind (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class IPAddressKind(CimEnum):
    """Indicates if the addressing of the IPAccessPoint, gateway, and subnet are per IPv4 or
    IPv6."""

    iPv4 = "iPv4"
    iPv6 = "iPv6"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="IPAddressKind",
            package="TC57CIM/IEC61970/Base/ICCPConfiguration",
            guid="{63D432DD-2F98-4142-8CA2-8490F343B490}",
            kind="enumeration",
        )
    )
