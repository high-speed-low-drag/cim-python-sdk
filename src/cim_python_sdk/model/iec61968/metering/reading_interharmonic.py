"""CIM compound ReadingInterharmonic (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class ReadingInterharmonic(CimCompound):
    """Interharmonics are represented as a rational number 'numerator' / 'denominator', and
    harmonics are represented using the same mechanism and identified by 'denominator'=1."""

    __slots__ = ("denominator", "numerator")

    numerator: int | None
    denominator: int | None

    _cim_meta = ClassMeta(
        cim_name="ReadingInterharmonic",
        package="TC57CIM/IEC61968/Metering",
        guid="{80DBF0DD-0EBD-4e62-89E1-BF2CEF3B59BA}",
        kind="compound",
        attributes=(
            AttrMeta("numerator", "numerator", "int", 0, 1, "primitive"),
            AttrMeta("denominator", "denominator", "int", 0, 1, "primitive"),
        ),
    )
