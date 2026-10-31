"""CIM enumeration ServiceKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ServiceKind(CimEnum):
    """Kind of service."""

    electricity = "electricity"
    gas = "gas"
    water = "water"
    time = "time"
    heat = "heat"
    refuse = "refuse"
    sewerage = "sewerage"
    rates = "rates"
    tvLicence = "tvLicence"
    internet = "internet"
    other = "other"
    air = "air"
    naturalGas = "naturalGas"
    propane = "propane"
    steam = "steam"
    heatingFluid = "heatingFluid"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ServiceKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{1E950BD8-0A33-40a4-924B-F1A272126E3C}",
            kind="enumeration",
        )
    )
