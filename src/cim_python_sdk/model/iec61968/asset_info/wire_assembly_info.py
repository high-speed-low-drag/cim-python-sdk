"""CIM class WireAssemblyInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.wire_phase_info import WirePhaseInfo
    from cim_python_sdk.model.iec61970.base.wires.per_length_line_parameter import (
        PerLengthLineParameter,
    )


class WireAssemblyInfo(AssetInfo):
    """Describes the construction of a multi-conductor wire."""

    __slots__ = ("_per_length_line_parameter", "_wire_phase_info")

    per_length_line_parameter: Many[PerLengthLineParameter] = Many(
        EndMeta(
            name="per_length_line_parameter",
            cim_role="PerLengthLineParameter",
            target="cim_python_sdk.model.iec61970.base.wires.per_length_line_parameter:PerLengthLineParameter",
            many=True,
            lower=0,
            upper=None,
            inverse="wire_assembly_info",
            aggregation="none",
        )
    )
    wire_phase_info: Many[WirePhaseInfo] = Many(
        EndMeta(
            name="wire_phase_info",
            cim_role="WirePhaseInfo",
            target="cim_python_sdk.model.iec61968.asset_info.wire_phase_info:WirePhaseInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="wire_assembly_info",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WireAssemblyInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{7806189A-6D8F-4c2c-84A1-2C4EBF0C33A7}",
        ends=(
            per_length_line_parameter.meta,
            wire_phase_info.meta,
        ),
    )

    def __init__(
        self,
        *,
        per_length_line_parameter: Iterable[PerLengthLineParameter] | None = None,
        wire_phase_info: Iterable[WirePhaseInfo] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if per_length_line_parameter is not None:
            WireAssemblyInfo.per_length_line_parameter.extend(self, per_length_line_parameter)
        if wire_phase_info is not None:
            WireAssemblyInfo.wire_phase_info.extend(self, wire_phase_info)

    def add_per_length_line_parameter(
        self, per_length_line_parameter: PerLengthLineParameter
    ) -> Self:
        return WireAssemblyInfo.per_length_line_parameter.add(self, per_length_line_parameter)

    def remove_per_length_line_parameter(
        self, per_length_line_parameter: PerLengthLineParameter
    ) -> Self:
        return WireAssemblyInfo.per_length_line_parameter.remove(self, per_length_line_parameter)

    def clear_per_length_line_parameter(self) -> Self:
        return WireAssemblyInfo.per_length_line_parameter.clear(self)

    def num_per_length_line_parameter(self) -> int:
        return WireAssemblyInfo.per_length_line_parameter.count(self)

    def get_per_length_line_parameter_by_mrid(self, mrid: str) -> PerLengthLineParameter | None:
        return WireAssemblyInfo.per_length_line_parameter.get_by_mrid(self, mrid)

    def add_wire_phase_info(self, wire_phase_info: WirePhaseInfo) -> Self:
        return WireAssemblyInfo.wire_phase_info.add(self, wire_phase_info)

    def remove_wire_phase_info(self, wire_phase_info: WirePhaseInfo) -> Self:
        return WireAssemblyInfo.wire_phase_info.remove(self, wire_phase_info)

    def clear_wire_phase_info(self) -> Self:
        return WireAssemblyInfo.wire_phase_info.clear(self)

    def num_wire_phase_info(self) -> int:
        return WireAssemblyInfo.wire_phase_info.count(self)
