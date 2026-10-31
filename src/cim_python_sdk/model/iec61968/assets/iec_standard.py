"""CIM compound IECStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.iec_standard_edition_kind import (
        IECStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.iec_standard_kind import IECStandardKind


class IECStandard(CimCompound):
    """Standard published by IEC (International Electrotechnical Commission)."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: IECStandardKind | None
    standard_edition: IECStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="IECStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{0EED159E-2522-453c-AEE2-CC950BB56A9F}",
        kind="compound",
        attributes=(
            AttrMeta("standard_number", "standardNumber", "IECStandardKind", 0, 1, "enumeration"),
            AttrMeta(
                "standard_edition", "standardEdition", "IECStandardEditionKind", 0, 1, "enumeration"
            ),
        ),
    )
