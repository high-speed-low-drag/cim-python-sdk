"""CIM compound CIGREStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.cigre_standard_edition_kind import (
        CIGREStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.cigre_standard_kind import CIGREStandardKind


class CIGREStandard(CimCompound):
    """Standard published by CIGRE (Council on Large Electric Systems)."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: CIGREStandardKind | None
    standard_edition: CIGREStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="CIGREStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{10424179-9770-4002-9BBB-439A8D33EAF6}",
        kind="compound",
        attributes=(
            AttrMeta("standard_number", "standardNumber", "CIGREStandardKind", 0, 1, "enumeration"),
            AttrMeta(
                "standard_edition",
                "standardEdition",
                "CIGREStandardEditionKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )
