"""CIM enumeration ChargeKind (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ChargeKind(CimEnum):
    """Kind of charge."""

    consumptionCharge = "consumptionCharge"
    demandCharge = "demandCharge"
    auxiliaryCharge = "auxiliaryCharge"
    taxCharge = "taxCharge"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ChargeKind",
            package="TC57CIM/IEC61968/PaymentMetering",
            guid="{C71AE130-154B-47e8-8E5E-AB72E94007FD}",
            kind="enumeration",
        )
    )
