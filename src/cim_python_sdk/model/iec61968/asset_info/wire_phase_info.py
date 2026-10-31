"""CIM class WirePhaseInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_info.wire_assembly_info import WireAssemblyInfo
    from cim_python_sdk.model.iec61968.asset_info.wire_info import WireInfo
    from cim_python_sdk.model.iec61968.asset_info.wire_position import WirePosition
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class WirePhaseInfo(CimObject):
    """Information on a wire carrying a single phase."""

    __slots__ = ("_wire_assembly_info", "_wire_info", "_wire_position", "phase_info")

    phase_info: SinglePhaseKind | None

    wire_position: One[WirePosition] = One(
        EndMeta(
            name="wire_position",
            cim_role="WirePosition",
            target="cim_python_sdk.model.iec61968.asset_info.wire_position:WirePosition",
            many=False,
            lower=0,
            upper=1,
            inverse="wire_phase_info",
            aggregation="none",
        )
    )
    wire_info: One[WireInfo] = One(
        EndMeta(
            name="wire_info",
            cim_role="WireInfo",
            target="cim_python_sdk.model.iec61968.asset_info.wire_info:WireInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="wire_phase_info",
            aggregation="none",
        )
    )
    wire_assembly_info: One[WireAssemblyInfo] = One(
        EndMeta(
            name="wire_assembly_info",
            cim_role="WireAssemblyInfo",
            target="cim_python_sdk.model.iec61968.asset_info.wire_assembly_info:WireAssemblyInfo",
            many=False,
            lower=1,
            upper=1,
            inverse="wire_phase_info",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WirePhaseInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{D8FFDAE8-943B-4f6f-B04F-07AB06B7E75E}",
        attributes=(AttrMeta("phase_info", "phaseInfo", "SinglePhaseKind", 0, 1, "enumeration"),),
        ends=(
            wire_position.meta,
            wire_info.meta,
            wire_assembly_info.meta,
        ),
    )

    def __init__(
        self,
        *,
        phase_info: SinglePhaseKind | None = None,
        wire_position: WirePosition | None = None,
        wire_info: WireInfo | None = None,
        wire_assembly_info: WireAssemblyInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.phase_info = phase_info
        if wire_position is not None:
            self.wire_position = wire_position
        if wire_info is not None:
            self.wire_info = wire_info
        if wire_assembly_info is not None:
            self.wire_assembly_info = wire_assembly_info
