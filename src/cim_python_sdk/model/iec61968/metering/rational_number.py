"""CIM compound RationalNumber (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class RationalNumber(CimCompound):
    """Rational number = 'numerator' / 'denominator'."""

    __slots__ = ("denominator", "numerator")

    numerator: int | None
    denominator: int | None

    _cim_meta = ClassMeta(
        cim_name="RationalNumber",
        package="TC57CIM/IEC61968/Metering",
        guid="{55480F31-7DA3-4c2d-A240-0A31C3271DE6}",
        kind="compound",
        attributes=(
            AttrMeta("numerator", "numerator", "int", 0, 1, "primitive"),
            AttrMeta("denominator", "denominator", "int", 0, 1, "primitive"),
        ),
    )
