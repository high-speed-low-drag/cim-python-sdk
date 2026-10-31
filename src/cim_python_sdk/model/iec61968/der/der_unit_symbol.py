"""CIM enumeration DERUnitSymbol (TC57CIM/IEC61968/DER). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DERUnitSymbol(CimEnum):
    """The units defined for usage in DER related contexts. This class is a subset plus
    possible additions of the UnitSymbol Class in the CIM Domain Package."""

    s = "s"
    A = "A"
    deg = "deg"
    degC = "degC"
    V = "V"
    ohm = "ohm"
    Hz = "Hz"
    W = "W"
    VA = "VA"
    VAr = "VAr"
    Vs = "Vs"
    As = "As"
    VAh = "VAh"
    Wh = "Wh"
    VArh = "VArh"
    WPers = "WPers"
    h = "h"
    min = "min"
    Q = "Q"
    Qh = "Qh"
    ohmm = "ohmm"
    Ah = "Ah"
    Btu = "Btu"
    VPerVA = "VPerVA"
    therm = "therm"
    Vh = "Vh"
    WPerA = "WPerA"
    onePerHz = "onePerHz"
    VPerVAr = "VPerVAr"
    ohmPerm = "ohmPerm"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DERUnitSymbol",
            package="TC57CIM/IEC61968/DER",
            guid="{7102E1CC-0B48-42aa-B738-5DDC382A17FD}",
            kind="enumeration",
        )
    )
