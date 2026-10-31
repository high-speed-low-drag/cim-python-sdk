"""CIM class UndergroundStructure (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.structure import Structure

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.underground_structure_kind import (
        UndergroundStructureKind,
    )


class UndergroundStructure(Structure):
    """Underground structure."""

    __slots__ = ("has_ventilation", "material", "sealing_warranty_expires_date")

    kind: UndergroundStructureKind | None  # type: ignore[assignment]
    has_ventilation: bool | None
    sealing_warranty_expires_date: _dt.date | None
    material: str | None

    _cim_meta = ClassMeta(
        cim_name="UndergroundStructure",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{09077FDE-DEED-46be-AC7E-1C70E6EB9A49}",
        attributes=(
            AttrMeta("kind", "kind", "UndergroundStructureKind", 0, 1, "enumeration"),
            AttrMeta("has_ventilation", "hasVentilation", "bool", 0, 1, "primitive"),
            AttrMeta(
                "sealing_warranty_expires_date",
                "sealingWarrantyExpiresDate",
                "date",
                0,
                1,
                "primitive",
            ),
            AttrMeta("material", "material", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        kind: UndergroundStructureKind | None = None,
        has_ventilation: bool | None = None,
        sealing_warranty_expires_date: _dt.date | None = None,
        material: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.has_ventilation = has_ventilation
        self.sealing_warranty_expires_date = sealing_warranty_expires_date
        self.material = material
