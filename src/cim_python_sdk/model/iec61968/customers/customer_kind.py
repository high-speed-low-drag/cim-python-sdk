"""CIM enumeration CustomerKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CustomerKind(CimEnum):
    """Kind of customer."""

    residential = "residential"
    residentialAndCommercial = "residentialAndCommercial"
    residentialAndStreetlight = "residentialAndStreetlight"
    residentialStreetlightOthers = "residentialStreetlightOthers"
    residentialFarmService = "residentialFarmService"
    commercialIndustrial = "commercialIndustrial"
    pumpingLoad = "pumpingLoad"
    windMachine = "windMachine"
    energyServiceSupplier = "energyServiceSupplier"
    energyServiceScheduler = "energyServiceScheduler"
    internalUse = "internalUse"
    enterprise = "enterprise"
    regionalOperator = "regionalOperator"
    subsidiary = "subsidiary"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CustomerKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{9BCC64AE-9D73-46d4-BFFF-FDBEF38B891A}",
            kind="enumeration",
        )
    )
