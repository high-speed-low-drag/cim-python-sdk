"""CIM compound LaborelecStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.laborelec_standard_edition_kind import (
        LaborelecStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.laborelec_standard_kind import LaborelecStandardKind


class LaborelecStandard(CimCompound):
    """Standard published by Laborelec."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: LaborelecStandardKind | None
    standard_edition: LaborelecStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="LaborelecStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{893CFA2A-D17F-40ec-9E4B-0859DCF3A569}",
        kind="compound",
        attributes=(
            AttrMeta(
                "standard_number", "standardNumber", "LaborelecStandardKind", 0, 1, "enumeration"
            ),
            AttrMeta(
                "standard_edition",
                "standardEdition",
                "LaborelecStandardEditionKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )
