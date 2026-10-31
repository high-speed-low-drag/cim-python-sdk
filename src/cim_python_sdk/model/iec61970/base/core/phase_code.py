"""CIM enumeration PhaseCode (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PhaseCode(CimEnum):
    """An unordered enumeration of phase identifiers. Allows designation of phases for both
    transmission and distribution equipment, circuits and loads. The enumeration, by itself,
    does not describe how the phases are connected together or connected to ground. Ground
    is not explicitly denoted as a phase.

    Residential and small commercial loads are often served from single-phase, or
    split-phase, secondary circuits. For the example of s12N, phases 1 and 2 refer to hot
    wires that are 180 degrees out of phase, while N refers to the neutral wire. Through
    single-phase transformer connections, these secondary circuits may be served from one or
    two of the primary phases A, B, and C. For three-phase loads, use the A, B, C phase
    codes instead of s12N.

    The integer values are from IEC 61968-9 to support revenue metering applications."""

    ABCN = "ABCN"
    ABC = "ABC"
    ABN = "ABN"
    ACN = "ACN"
    BCN = "BCN"
    AB = "AB"
    AC = "AC"
    BC = "BC"
    AN = "AN"
    BN = "BN"
    CN = "CN"
    A = "A"
    B = "B"
    C = "C"
    N = "N"
    s1N = "s1N"
    s2N = "s2N"
    s12N = "s12N"
    s1 = "s1"
    s2 = "s2"
    s12 = "s12"
    none = "none"
    X = "X"
    XY = "XY"
    XN = "XN"
    XYN = "XYN"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PhaseCode",
            package="TC57CIM/IEC61970/Base/Core",
            guid="{3687AEED-A1B1-4557-899E-5985D184FCE9}",
            kind="enumeration",
        )
    )
