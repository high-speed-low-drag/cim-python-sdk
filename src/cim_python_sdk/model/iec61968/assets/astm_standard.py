"""CIM compound ASTMStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.astm_standard_edition_kind import (
        ASTMStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.astm_standard_kind import ASTMStandardKind


class ASTMStandard(CimCompound):
    """Standard published by ASTM (ASTM International)."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: ASTMStandardKind | None
    standard_edition: ASTMStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="ASTMStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{50546C5D-FFCB-433e-868C-8DC104A32BC3}",
        kind="compound",
        attributes=(
            AttrMeta("standard_number", "standardNumber", "ASTMStandardKind", 0, 1, "enumeration"),
            AttrMeta(
                "standard_edition",
                "standardEdition",
                "ASTMStandardEditionKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )
