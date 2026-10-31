"""CIM class SubscribePowerCurve (TC57CIM/IEC61968/InfIEC61968/InfCustomers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.core.curve import Curve


class SubscribePowerCurve(Curve):
    """Price curve for specifying the cost of energy (X) at points in time (y1) according to a
    prcing structure, which is based on a tariff."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="SubscribePowerCurve",
        package="TC57CIM/IEC61968/InfIEC61968/InfCustomers",
        guid="{52014668-2514-4a2f-9238-F992C8BDF1EC}",
    )
