"""CIM class Structure (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset_container import AssetContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.wire_spacing_info import WireSpacingInfo
    from cim_python_sdk.model.iec61968.assets.structure_support import StructureSupport
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.structure_material_kind import (
        StructureMaterialKind,
    )


class Structure(AssetContainer):
    """Construction holding assets such as conductors, transformers, switchgear, etc. Where
    applicable, number of conductors can be derived from the number of associated wire
    spacing instances."""

    __slots__ = (
        "_structure_supports",
        "_wire_spacing_infos",
        "fumigant_applied_date",
        "fumigant_name",
        "height",
        "material_kind",
        "rated_voltage",
        "remove_weed",
        "weed_removed_date",
    )

    material_kind: StructureMaterialKind | None
    height: float | None  # Length
    rated_voltage: float | None  # Voltage
    remove_weed: bool | None
    weed_removed_date: _dt.date | None
    fumigant_name: str | None
    fumigant_applied_date: _dt.date | None

    structure_supports: Many[StructureSupport] = Many(
        EndMeta(
            name="structure_supports",
            cim_role="StructureSupports",
            target="cim_python_sdk.model.iec61968.assets.structure_support:StructureSupport",
            many=True,
            lower=0,
            upper=None,
            inverse="secured_structure",
            aggregation="none",
        )
    )
    wire_spacing_infos: Many[WireSpacingInfo] = Many(
        EndMeta(
            name="wire_spacing_infos",
            cim_role="WireSpacingInfos",
            target="cim_python_sdk.model.iec61968.asset_info.wire_spacing_info:WireSpacingInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="structures",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Structure",
        package="TC57CIM/IEC61968/Assets",
        guid="{C67E3DDB-366A-4d7f-B83B-8B85A957FF72}",
        attributes=(
            AttrMeta("material_kind", "materialKind", "StructureMaterialKind", 0, 1, "enumeration"),
            AttrMeta("height", "height", "Length", 0, 1, "cimdatatype"),
            AttrMeta("rated_voltage", "ratedVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("remove_weed", "removeWeed", "bool", 0, 1, "primitive"),
            AttrMeta("weed_removed_date", "weedRemovedDate", "date", 0, 1, "primitive"),
            AttrMeta("fumigant_name", "fumigantName", "str", 0, 1, "primitive"),
            AttrMeta("fumigant_applied_date", "fumigantAppliedDate", "date", 0, 1, "primitive"),
        ),
        ends=(
            structure_supports.meta,
            wire_spacing_infos.meta,
        ),
    )

    def __init__(
        self,
        *,
        material_kind: StructureMaterialKind | None = None,
        height: float | None = None,
        rated_voltage: float | None = None,
        remove_weed: bool | None = None,
        weed_removed_date: _dt.date | None = None,
        fumigant_name: str | None = None,
        fumigant_applied_date: _dt.date | None = None,
        structure_supports: Iterable[StructureSupport] | None = None,
        wire_spacing_infos: Iterable[WireSpacingInfo] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.material_kind = material_kind
        self.height = height
        self.rated_voltage = rated_voltage
        self.remove_weed = remove_weed
        self.weed_removed_date = weed_removed_date
        self.fumigant_name = fumigant_name
        self.fumigant_applied_date = fumigant_applied_date
        if structure_supports is not None:
            Structure.structure_supports.extend(self, structure_supports)
        if wire_spacing_infos is not None:
            Structure.wire_spacing_infos.extend(self, wire_spacing_infos)

    def add_structure_support(self, structure_support: StructureSupport) -> Self:
        return Structure.structure_supports.add(self, structure_support)

    def remove_structure_support(self, structure_support: StructureSupport) -> Self:
        return Structure.structure_supports.remove(self, structure_support)

    def clear_structure_supports(self) -> Self:
        return Structure.structure_supports.clear(self)

    def num_structure_support(self) -> int:
        return Structure.structure_supports.count(self)

    def get_structure_support_by_mrid(self, mrid: str) -> StructureSupport | None:
        return Structure.structure_supports.get_by_mrid(self, mrid)

    def add_wire_spacing_info(self, wire_spacing_info: WireSpacingInfo) -> Self:
        return Structure.wire_spacing_infos.add(self, wire_spacing_info)

    def remove_wire_spacing_info(self, wire_spacing_info: WireSpacingInfo) -> Self:
        return Structure.wire_spacing_infos.remove(self, wire_spacing_info)

    def clear_wire_spacing_infos(self) -> Self:
        return Structure.wire_spacing_infos.clear(self)

    def num_wire_spacing_info(self) -> int:
        return Structure.wire_spacing_infos.count(self)

    def get_wire_spacing_info_by_mrid(self, mrid: str) -> WireSpacingInfo | None:
        return Structure.wire_spacing_infos.get_by_mrid(self, mrid)
