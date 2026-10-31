"""CIM compound DobleStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.doble_standard_edition_kind import (
        DobleStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.doble_standard_kind import DobleStandardKind


class DobleStandard(CimCompound):
    """Standard published by Doble."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: DobleStandardKind | None
    standard_edition: DobleStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="DobleStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{4D299512-B9E0-4eda-A22D-8DC696AE063A}",
        kind="compound",
        attributes=(
            AttrMeta("standard_number", "standardNumber", "DobleStandardKind", 0, 1, "enumeration"),
            AttrMeta(
                "standard_edition",
                "standardEdition",
                "DobleStandardEditionKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )
