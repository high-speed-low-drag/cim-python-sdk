"""CIM class StructureSupport (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.assets.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.structure import Structure
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.anchor_kind import AnchorKind
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.structure_support_kind import (
        StructureSupportKind,
    )


class StructureSupport(Asset):
    """Support for structure assets."""

    __slots__ = (
        "_secured_structure",
        "anchor_kind",
        "anchor_rod_count",
        "anchor_rod_length",
        "direction",
        "length",
        "size",
    )

    kind: StructureSupportKind | None  # type: ignore[assignment]
    size: str | None
    direction: float | None  # AngleDegrees
    length: float | None  # Length
    anchor_kind: AnchorKind | None
    anchor_rod_count: int | None
    anchor_rod_length: float | None  # Length

    secured_structure: One[Structure] = One(
        EndMeta(
            name="secured_structure",
            cim_role="SecuredStructure",
            target="cim_python_sdk.model.iec61968.assets.structure:Structure",
            many=False,
            lower=0,
            upper=1,
            inverse="structure_supports",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StructureSupport",
        package="TC57CIM/IEC61968/Assets",
        guid="{04CA8222-E0A1-4a67-A5AD-9CE3AFE3D439}",
        attributes=(
            AttrMeta("kind", "kind", "StructureSupportKind", 0, 1, "enumeration"),
            AttrMeta("size", "size", "str", 0, 1, "primitive"),
            AttrMeta("direction", "direction", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("length", "length", "Length", 0, 1, "cimdatatype"),
            AttrMeta("anchor_kind", "anchorKind", "AnchorKind", 0, 1, "enumeration"),
            AttrMeta("anchor_rod_count", "anchorRodCount", "int", 0, 1, "primitive"),
            AttrMeta("anchor_rod_length", "anchorRodLength", "Length", 0, 1, "cimdatatype"),
        ),
        ends=(secured_structure.meta,),
    )

    def __init__(
        self,
        *,
        kind: StructureSupportKind | None = None,
        size: str | None = None,
        direction: float | None = None,
        length: float | None = None,
        anchor_kind: AnchorKind | None = None,
        anchor_rod_count: int | None = None,
        anchor_rod_length: float | None = None,
        secured_structure: Structure | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.size = size
        self.direction = direction
        self.length = length
        self.anchor_kind = anchor_kind
        self.anchor_rod_count = anchor_rod_count
        self.anchor_rod_length = anchor_rod_length
        if secured_structure is not None:
            self.secured_structure = secured_structure
