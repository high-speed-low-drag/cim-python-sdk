"""CIM compound ISOStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.iso_standard_edition_kind import (
        ISOStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.iso_standard_kind import ISOStandardKind


class ISOStandard(CimCompound):
    """Standard published by ISO (International Organization for Standardization)."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: ISOStandardKind | None
    standard_edition: ISOStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="ISOStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{0C619E7D-CF4D-4436-9E26-745DDB0C67BB}",
        kind="compound",
        attributes=(
            AttrMeta("standard_number", "standardNumber", "ISOStandardKind", 0, 1, "enumeration"),
            AttrMeta(
                "standard_edition", "standardEdition", "ISOStandardEditionKind", 0, 1, "enumeration"
            ),
        ),
    )
