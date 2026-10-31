"""CIM compound IEEEStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.ieee_standard_edition_kind import (
        IEEEStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.ieee_standard_kind import IEEEStandardKind


class IEEEStandard(CimCompound):
    """Standard published by IEEE (Institute of Electrical and Electronics Engineers)."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: IEEEStandardKind | None
    standard_edition: IEEEStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="IEEEStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{8E61E9C2-2E60-4a07-82F2-05DE8B659579}",
        kind="compound",
        attributes=(
            AttrMeta("standard_number", "standardNumber", "IEEEStandardKind", 0, 1, "enumeration"),
            AttrMeta(
                "standard_edition",
                "standardEdition",
                "IEEEStandardEditionKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )
