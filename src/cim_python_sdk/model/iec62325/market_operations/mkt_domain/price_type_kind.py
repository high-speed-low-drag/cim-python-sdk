"""CIM enumeration PriceTypeKind (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PriceTypeKind(CimEnum):
    """Value of this enumeration for different prices include "total" for the
    complete/full/all-in price, "congestion" for the congestion cost associated with the
    total price, the "loss" for the loss price associated with the total price, "capacity"
    for prices related to installed or reserved capacity, "mileage" for use-based
    accounting, "system" for system-wide/copper-plate prices, and "delivery" for
    distribution-based prices."""

    capacity = "capacity"
    congestion = "congestion"
    delivery = "delivery"
    loss = "loss"
    mileage = "mileage"
    system = "system"
    total = "total"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PriceTypeKind",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{013C960C-3541-445f-A0D0-3081FA4BBE6D}",
            kind="enumeration",
        )
    )
