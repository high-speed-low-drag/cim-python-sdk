"""CIM class NetworkFrame (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.framework_part import (
    FrameworkPart,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.network_boundary import (
        NetworkBoundary,
    )


class NetworkFrame(FrameworkPart):
    """A region isolated by boundaries."""

    __slots__ = ("_framework_part", "_network_boundaries", "_network_boundaries_network_frame")

    network_boundaries: Many[NetworkBoundary] = Many(
        EndMeta(
            name="network_boundaries",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.network_boundary:NetworkBoundary",
            many=True,
            lower=0,
            upper=None,
            inverse="network_frame",
            aggregation="none",
        )
    )
    network_boundaries_network_frame: Many[NetworkBoundary] = Many(
        EndMeta(
            name="network_boundaries_network_frame",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.network_boundary:NetworkBoundary",
            many=True,
            lower=0,
            upper=None,
            inverse="network_frame_network_boundaries",
            aggregation="none",
        )
    )
    framework_part: Many[FrameworkPart] = Many(
        EndMeta(
            name="framework_part",
            cim_role="FrameworkPart",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.framework_part:FrameworkPart",
            many=True,
            lower=0,
            upper=None,
            inverse="frame",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkFrame",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{98774A6E-0A19-461c-BD45-3B81201BF60C}",
        ends=(
            network_boundaries.meta,
            network_boundaries_network_frame.meta,
            framework_part.meta,
        ),
    )

    def __init__(
        self,
        *,
        network_boundaries: Iterable[NetworkBoundary] | None = None,
        network_boundaries_network_frame: Iterable[NetworkBoundary] | None = None,
        framework_part: Iterable[FrameworkPart] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if network_boundaries is not None:
            NetworkFrame.network_boundaries.extend(self, network_boundaries)
        if network_boundaries_network_frame is not None:
            NetworkFrame.network_boundaries_network_frame.extend(
                self, network_boundaries_network_frame
            )
        if framework_part is not None:
            NetworkFrame.framework_part.extend(self, framework_part)

    def add_network_boundary(self, network_boundary: NetworkBoundary) -> Self:
        return NetworkFrame.network_boundaries.add(self, network_boundary)

    def remove_network_boundary(self, network_boundary: NetworkBoundary) -> Self:
        return NetworkFrame.network_boundaries.remove(self, network_boundary)

    def clear_network_boundaries(self) -> Self:
        return NetworkFrame.network_boundaries.clear(self)

    def num_network_boundary(self) -> int:
        return NetworkFrame.network_boundaries.count(self)

    def get_network_boundary_by_mrid(self, mrid: str) -> NetworkBoundary | None:
        return NetworkFrame.network_boundaries.get_by_mrid(self, mrid)

    def add_network_boundaries_network_frame(
        self, network_boundaries_network_frame: NetworkBoundary
    ) -> Self:
        return NetworkFrame.network_boundaries_network_frame.add(
            self, network_boundaries_network_frame
        )

    def remove_network_boundaries_network_frame(
        self, network_boundaries_network_frame: NetworkBoundary
    ) -> Self:
        return NetworkFrame.network_boundaries_network_frame.remove(
            self, network_boundaries_network_frame
        )

    def clear_network_boundaries_network_frame(self) -> Self:
        return NetworkFrame.network_boundaries_network_frame.clear(self)

    def num_network_boundaries_network_frame(self) -> int:
        return NetworkFrame.network_boundaries_network_frame.count(self)

    def get_network_boundaries_network_frame_by_mrid(self, mrid: str) -> NetworkBoundary | None:
        return NetworkFrame.network_boundaries_network_frame.get_by_mrid(self, mrid)

    def add_framework_part(self, framework_part: FrameworkPart) -> Self:
        return NetworkFrame.framework_part.add(self, framework_part)

    def remove_framework_part(self, framework_part: FrameworkPart) -> Self:
        return NetworkFrame.framework_part.remove(self, framework_part)

    def clear_framework_part(self) -> Self:
        return NetworkFrame.framework_part.clear(self)

    def num_framework_part(self) -> int:
        return NetworkFrame.framework_part.count(self)

    def get_framework_part_by_mrid(self, mrid: str) -> FrameworkPart | None:
        return NetworkFrame.framework_part.get_by_mrid(self, mrid)
