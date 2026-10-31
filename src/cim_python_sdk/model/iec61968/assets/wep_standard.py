"""CIM compound WEPStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.wep_standard_edition_kind import (
        WEPStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.wep_standard_kind import WEPStandardKind


class WEPStandard(CimCompound):
    """Standard published by Westinghouse - a WEP (Westinghouse Engineering Procedure)."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: WEPStandardKind | None
    standard_edition: WEPStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="WEPStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{4271B466-ED80-4d6a-BAA8-2C21B2562651}",
        kind="compound",
        attributes=(
            AttrMeta("standard_number", "standardNumber", "WEPStandardKind", 0, 1, "enumeration"),
            AttrMeta(
                "standard_edition", "standardEdition", "WEPStandardEditionKind", 0, 1, "enumeration"
            ),
        ),
    )
