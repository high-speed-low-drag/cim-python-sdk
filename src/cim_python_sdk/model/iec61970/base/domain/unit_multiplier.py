"""CIM enumeration UnitMultiplier (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UnitMultiplier(CimEnum):
    """The unit multipliers defined for the CIM. When applied to unit symbols, the unit symbol
    is treated as a derived unit. Regardless of the contents of the unit symbol text, the
    unit symbol shall be treated as if it were a single-character unit symbol. Unit symbols
    should not contain multipliers, and it should be left to the multiplier to define the
    multiple for an entire data type.

    For example, if a unit symbol is "m2Pers" and the multiplier is "k", then the value is
    k(m**2/s), and the multiplier applies to the entire final value, not to any individual
    part of the value. This can be conceptualized by substituting a derived unit symbol for
    the unit type. If one imagines that the symbol "Þ" represents the derived unit "m2Pers",
    then applying the multiplier "k" can be conceptualized simply as "kÞ".

    For example, the SI unit for mass is "kg" and not "g". If the unit symbol is defined as
    "kg", then the multiplier is applied to "kg" as a whole and does not replace the "k" in
    front of the "g". In this case, the multiplier of "m" would be used with the unit symbol
    of "kg" to represent one gram. As a text string, this violates the instructions in IEC
    80000-1. However, because the unit symbol in CIM is treated as a derived unit instead of
    as an SI unit, it makes more sense to conceptualize the "kg" as if it were replaced by
    one of the proposed replacements for the SI mass symbol. If one imagines that the "kg"
    were replaced by a symbol "Þ", then it is easier to conceptualize the multiplier "m" as
    creating the proper unit "mÞ", and not the forbidden unit "mkg"."""

    y = "y"
    z = "z"
    a = "a"
    f = "f"
    p = "p"
    n = "n"
    micro = "micro"
    m = "m"
    c = "c"
    d = "d"
    none = "none"
    da = "da"
    h = "h"
    k = "k"
    M = "M"
    G = "G"
    T = "T"
    P = "P"
    E = "E"
    Z = "Z"
    Y = "Y"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UnitMultiplier",
            package="TC57CIM/IEC61970/Base/Domain",
            guid="{DC62CC93-2E3F-4b9c-9C81-C84C30A6C67D}",
            kind="enumeration",
        )
    )
