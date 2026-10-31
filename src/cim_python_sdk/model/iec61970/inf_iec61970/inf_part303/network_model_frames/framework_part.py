"""CIM class FrameworkPart (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_authority_set import (
    ModelAuthoritySet,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.network_frame import (
        NetworkFrame,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.unused.model_frame_type import (
        ModelFrameType,
    )


class FrameworkPart(ModelAuthoritySet):
    """The type of alternate model frame. For example, it could be generator group used to
    represent generators in state estimator, planning, planning dynamics, short circuit, or
    real-time dynamics etc., but does not specifically represent any one alternative model.
    This need to know what objects to be removed in the realization of any one alternate
    model."""

    __slots__ = ("_frame", "_model_frame_type")

    model_frame_type: One[ModelFrameType] = One(
        EndMeta(
            name="model_frame_type",
            cim_role="ModelFrameType",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.unused.model_frame_type:ModelFrameType",
            many=False,
            lower=1,
            upper=1,
            inverse="model_frame",
            aggregation="none",
        )
    )
    frame: One[NetworkFrame] = One(
        EndMeta(
            name="frame",
            cim_role="Frame",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.network_frame:NetworkFrame",
            many=False,
            lower=0,
            upper=1,
            inverse="framework_part",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FrameworkPart",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{78B6C3E3-1981-4953-8F7D-E5D66F6495A7}",
        ends=(
            model_frame_type.meta,
            frame.meta,
        ),
    )

    def __init__(
        self,
        *,
        model_frame_type: ModelFrameType | None = None,
        frame: NetworkFrame | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if model_frame_type is not None:
            self.model_frame_type = model_frame_type
        if frame is not None:
            self.frame = frame
