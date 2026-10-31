"""CIM enumeration FuelType (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FuelType(CimEnum):
    """Type of fuel."""

    coal = "coal"
    oil = "oil"
    gas = "gas"
    lignite = "lignite"
    hardCoal = "hardCoal"
    oilShale = "oilShale"
    brownCoalLignite = "brownCoalLignite"
    coalDerivedGas = "coalDerivedGas"
    peat = "peat"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FuelType",
            package="TC57CIM/IEC61970/Base/Generation/Production",
            guid="{AE75B683-1EF9-4536-B566-3EED1DAA67D6}",
            kind="enumeration",
        )
    )
