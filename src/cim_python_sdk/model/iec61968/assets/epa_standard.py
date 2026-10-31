"""CIM compound EPAStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.epa_standard_edition_kind import (
        EPAStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.epa_standard_kind import EPAStandardKind


class EPAStandard(CimCompound):
    """Standard published by EPA (United States Environmental Protection Agency)."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: EPAStandardKind | None
    standard_edition: EPAStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="EPAStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{45B27DCE-A4DC-430b-9501-4A23D7993BEE}",
        kind="compound",
        attributes=(
            AttrMeta("standard_number", "standardNumber", "EPAStandardKind", 0, 1, "enumeration"),
            AttrMeta(
                "standard_edition", "standardEdition", "EPAStandardEditionKind", 0, 1, "enumeration"
            ),
        ),
    )
