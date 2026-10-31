"""CIM class DuctBank (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset_container import AssetContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.wire_spacing_info import WireSpacingInfo


class DuctBank(AssetContainer):
    """A duct contains individual wires in the layout as specified with associated wire spacing
    instances; number of them gives the number of conductors in this duct."""

    __slots__ = ("_wire_spacing_infos", "circuit_count")

    circuit_count: int | None

    wire_spacing_infos: Many[WireSpacingInfo] = Many(
        EndMeta(
            name="wire_spacing_infos",
            cim_role="WireSpacingInfos",
            target="cim_python_sdk.model.iec61968.asset_info.wire_spacing_info:WireSpacingInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="duct_bank",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DuctBank",
        package="TC57CIM/IEC61968/Assets",
        guid="{55A6E582-CD40-43be-BFC1-6ED585946784}",
        attributes=(AttrMeta("circuit_count", "circuitCount", "int", 0, 1, "primitive"),),
        ends=(wire_spacing_infos.meta,),
    )

    def __init__(
        self,
        *,
        circuit_count: int | None = None,
        wire_spacing_infos: Iterable[WireSpacingInfo] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.circuit_count = circuit_count
        if wire_spacing_infos is not None:
            DuctBank.wire_spacing_infos.extend(self, wire_spacing_infos)

    def add_wire_spacing_info(self, wire_spacing_info: WireSpacingInfo) -> Self:
        return DuctBank.wire_spacing_infos.add(self, wire_spacing_info)

    def remove_wire_spacing_info(self, wire_spacing_info: WireSpacingInfo) -> Self:
        return DuctBank.wire_spacing_infos.remove(self, wire_spacing_info)

    def clear_wire_spacing_infos(self) -> Self:
        return DuctBank.wire_spacing_infos.clear(self)

    def num_wire_spacing_info(self) -> int:
        return DuctBank.wire_spacing_infos.count(self)

    def get_wire_spacing_info_by_mrid(self, mrid: str) -> WireSpacingInfo | None:
        return DuctBank.wire_spacing_infos.get_by_mrid(self, mrid)
