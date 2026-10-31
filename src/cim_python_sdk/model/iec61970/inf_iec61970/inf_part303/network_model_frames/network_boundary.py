"""CIM class NetworkBoundary (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.framework_part import (
    FrameworkPart,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.network_frame import (
        NetworkFrame,
    )


class NetworkBoundary(FrameworkPart):
    """A framework part that is a boundary between 2 frames."""

    __slots__ = ("_network_frame", "_network_frame_network_boundaries")

    network_frame: One[NetworkFrame] = One(
        EndMeta(
            name="network_frame",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.network_frame:NetworkFrame",
            many=False,
            lower=1,
            upper=1,
            inverse="network_boundaries",
            aggregation="none",
        )
    )
    network_frame_network_boundaries: One[NetworkFrame] = One(
        EndMeta(
            name="network_frame_network_boundaries",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.network_frame:NetworkFrame",
            many=False,
            lower=0,
            upper=1,
            inverse="network_boundaries_network_frame",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkBoundary",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{4803F850-0F9E-4f4b-9928-60C03BEA2BF7}",
        ends=(
            network_frame.meta,
            network_frame_network_boundaries.meta,
        ),
    )

    def __init__(
        self,
        *,
        network_frame: NetworkFrame | None = None,
        network_frame_network_boundaries: NetworkFrame | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if network_frame is not None:
            self.network_frame = network_frame
        if network_frame_network_boundaries is not None:
            self.network_frame_network_boundaries = network_frame_network_boundaries
