"""CIM compound TAPPIStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.tappi_standard_edition_kind import (
        TAPPIStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.tappi_standard_kind import TAPPIStandardKind


class TAPPIStandard(CimCompound):
    """Standard published by TAPPI."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: TAPPIStandardKind | None
    standard_edition: TAPPIStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="TAPPIStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{537D52C0-0FD0-45aa-BBCE-D4A34B5F845E}",
        kind="compound",
        attributes=(
            AttrMeta("standard_number", "standardNumber", "TAPPIStandardKind", 0, 1, "enumeration"),
            AttrMeta(
                "standard_edition",
                "standardEdition",
                "TAPPIStandardEditionKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )
