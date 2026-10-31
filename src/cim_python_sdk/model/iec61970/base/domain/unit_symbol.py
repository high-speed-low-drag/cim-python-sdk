"""CIM enumeration UnitSymbol (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UnitSymbol(CimEnum):
    """The derived units defined for usage in the CIM. In some cases, the derived unit is equal
    to an SI unit. Whenever possible, the standard derived symbol is used instead of the
    formula for the derived unit. For example, the unit symbol Farad is defined as "F"
    instead of "CPerV". In cases where a standard symbol does not exist for a derived unit,
    the formula for the unit is used as the unit symbol. For example, density does not have
    a standard symbol and so it is represented as "kgPerm3". With the exception of the "kg",
    which is an SI unit, the unit symbols do not contain multipliers and therefore represent
    the base derived unit to which a multiplier can be applied as a whole.

    Every unit symbol is treated as an unparseable text as if it were a single-letter
    symbol. The meaning of each unit symbol is defined by the accompanying descriptive text
    and not by the text contents of the unit symbol.

    To allow the widest possible range of serializations without requiring special character
    handling, several substitutions are made which deviate from the format described in IEC
    80000-1. The division symbol "/" is replaced by the letters "Per". Exponents are written
    in plain text after the unit as "m3" instead of being formatted as "m" with a
    superscript of 3 or introducing a symbol as in "m^3". The degree symbol "°" is replaced
    with the letters "deg". Any clarification of the meaning for a substitution is included
    in the description for the unit symbol.

    Non-SI units are included in list of unit symbols to allow sources of data to be
    correctly labelled with their non-SI units (for example, a GPS sensor that is reporting
    numbers that represent feet instead of meters). This allows software to use the unit
    symbol information correctly convert and scale the raw data of those sources into
    SI-based units.

    The integer values are used for harmonization with IEC 61850."""

    none = "none"
    m = "m"
    kg = "kg"
    s = "s"
    A = "A"
    K = "K"
    mol = "mol"
    cd = "cd"
    deg = "deg"
    rad = "rad"
    sr = "sr"
    Gy = "Gy"
    Bq = "Bq"
    degC = "degC"
    Sv = "Sv"
    F = "F"
    C = "C"
    S = "S"
    H = "H"
    V = "V"
    ohm = "ohm"
    J = "J"
    N = "N"
    Hz = "Hz"
    lx = "lx"
    lm = "lm"
    Wb = "Wb"
    T = "T"
    W = "W"
    Pa = "Pa"
    m2 = "m2"
    m3 = "m3"
    mPers = "mPers"
    mPers2 = "mPers2"
    m3Pers = "m3Pers"
    mPerm3 = "mPerm3"
    kgm = "kgm"
    kgPerm3 = "kgPerm3"
    m2Pers = "m2Pers"
    WPermK = "WPermK"
    JPerK = "JPerK"
    ppm = "ppm"
    rotPers = "rotPers"
    radPers = "radPers"
    WPerm2 = "WPerm2"
    JPerm2 = "JPerm2"
    SPerm = "SPerm"
    KPers = "KPers"
    PaPers = "PaPers"
    JPerkgK = "JPerkgK"
    VA = "VA"
    VAr = "VAr"
    cosPhi = "cosPhi"
    Vs = "Vs"
    V2 = "V2"
    As = "As"
    A2 = "A2"
    A2s = "A2s"
    VAh = "VAh"
    Wh = "Wh"
    VArh = "VArh"
    VPerHz = "VPerHz"
    HzPers = "HzPers"
    character = "character"
    charPers = "charPers"
    kgm2 = "kgm2"
    dB = "dB"
    WPers = "WPers"
    lPers = "lPers"
    dBm = "dBm"
    h = "h"
    min = "min"
    Q = "Q"
    Qh = "Qh"
    ohmm = "ohmm"
    APerm = "APerm"
    V2h = "V2h"
    A2h = "A2h"
    Ah = "Ah"
    count = "count"
    ft3 = "ft3"
    m3Perh = "m3Perh"
    gal = "gal"
    Btu = "Btu"
    l = "l"
    lPerh = "lPerh"
    lPerl = "lPerl"
    gPerg = "gPerg"
    molPerm3 = "molPerm3"
    molPermol = "molPermol"
    molPerkg = "molPerkg"
    sPers = "sPers"
    HzPerHz = "HzPerHz"
    VPerV = "VPerV"
    APerA = "APerA"
    VPerVA = "VPerVA"
    rev = "rev"
    kat = "kat"
    JPerkg = "JPerkg"
    m3Uncompensated = "m3Uncompensated"
    m3Compensated = "m3Compensated"
    WPerW = "WPerW"
    therm = "therm"
    onePerm = "onePerm"
    m3Perkg = "m3Perkg"
    Pas = "Pas"
    Nm = "Nm"
    NPerm = "NPerm"
    radPers2 = "radPers2"
    JPerm3 = "JPerm3"
    VPerm = "VPerm"
    CPerm3 = "CPerm3"
    CPerm2 = "CPerm2"
    FPerm = "FPerm"
    HPerm = "HPerm"
    JPermol = "JPermol"
    JPermolK = "JPermolK"
    CPerkg = "CPerkg"
    GyPers = "GyPers"
    WPersr = "WPersr"
    WPerm2sr = "WPerm2sr"
    katPerm3 = "katPerm3"
    d = "d"
    anglemin = "anglemin"
    anglesec = "anglesec"
    ha = "ha"
    tonne = "tonne"
    bar = "bar"
    mmHg = "mmHg"
    M = "M"
    kn = "kn"
    Mx = "Mx"
    G = "G"
    Oe = "Oe"
    Vh = "Vh"
    WPerA = "WPerA"
    onePerHz = "onePerHz"
    VPerVAr = "VPerVAr"
    ohmPerm = "ohmPerm"
    kgPerJ = "kgPerJ"
    JPers = "JPers"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UnitSymbol",
            package="TC57CIM/IEC61970/Base/Domain",
            guid="{80012160-A038-43b5-BA6F-9862E525518C}",
            kind="enumeration",
        )
    )
