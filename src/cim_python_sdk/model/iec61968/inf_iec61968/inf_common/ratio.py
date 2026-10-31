"""CIM compound Ratio (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class Ratio(CimCompound):
    """Fraction specified explicitly with a numerator and denominator, which can be used to
    calculate the quotient."""

    __slots__ = ("denominator", "numerator")

    numerator: float | None
    denominator: float | None

    _cim_meta = ClassMeta(
        cim_name="Ratio",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{F5D18BFC-D800-46b9-9A8B-CFCA6387C4C8}",
        kind="compound",
        attributes=(
            AttrMeta("numerator", "numerator", "float", 0, 1, "primitive"),
            AttrMeta("denominator", "denominator", "float", 0, 1, "primitive"),
        ),
    )
