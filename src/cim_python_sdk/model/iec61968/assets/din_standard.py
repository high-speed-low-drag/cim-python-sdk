"""CIM compound DINStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.din_standard_edition_kind import (
        DINStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.din_standard_kind import DINStandardKind


class DINStandard(CimCompound):
    """Standard published by DIN (German Institute of Standards)."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: DINStandardKind | None
    standard_edition: DINStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="DINStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{A4B8945D-7CB4-4afe-85F8-9CFC03E01F75}",
        kind="compound",
        attributes=(
            AttrMeta("standard_number", "standardNumber", "DINStandardKind", 0, 1, "enumeration"),
            AttrMeta(
                "standard_edition", "standardEdition", "DINStandardEditionKind", 0, 1, "enumeration"
            ),
        ),
    )
