"""CIM class Tower (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.structure import Structure

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.tower_construction_kind import (
        TowerConstructionKind,
    )


class Tower(Structure):
    """Tower asset. Dimensions of the Tower are specified in associated DimensionsInfo class.

    When used for planning purposes, a transmission tower carrying two 3-phase circuits will
    have 2 instances of Connection, each of which will have 3 MountingPoint instances, one
    for each phase all with coordinates relative to a common origin on the tower. (It may
    also have a 3rd Connection with a single MountingPoint for the Neutral line)."""

    __slots__ = ("construction_kind",)

    construction_kind: TowerConstructionKind | None

    _cim_meta = ClassMeta(
        cim_name="Tower",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{B61B782C-51A5-49d4-AB6B-2971702A92D8}",
        attributes=(
            AttrMeta(
                "construction_kind",
                "constructionKind",
                "TowerConstructionKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )

    def __init__(
        self,
        *,
        construction_kind: TowerConstructionKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.construction_kind = construction_kind
