"""CIM class ModelFrameType (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames/unused). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.framework_part import (
        FrameworkPart,
    )


class ModelFrameType(IdentifiedObject):
    """Examples would be "Boundary" or "Region" type of frame."""

    __slots__ = ("_model_frame",)

    model_frame: Many[FrameworkPart] = Many(
        EndMeta(
            name="model_frame",
            cim_role="ModelFrame",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.framework_part:FrameworkPart",
            many=True,
            lower=0,
            upper=None,
            inverse="model_frame_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ModelFrameType",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames/unused",
        guid="{441F5D00-3017-42ce-8499-698FD8022177}",
        ends=(model_frame.meta,),
    )

    def __init__(
        self,
        *,
        model_frame: Iterable[FrameworkPart] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if model_frame is not None:
            ModelFrameType.model_frame.extend(self, model_frame)

    def add_model_frame(self, model_frame: FrameworkPart) -> Self:
        return ModelFrameType.model_frame.add(self, model_frame)

    def remove_model_frame(self, model_frame: FrameworkPart) -> Self:
        return ModelFrameType.model_frame.remove(self, model_frame)

    def clear_model_frame(self) -> Self:
        return ModelFrameType.model_frame.clear(self)

    def num_model_frame(self) -> int:
        return ModelFrameType.model_frame.count(self)

    def get_model_frame_by_mrid(self, mrid: str) -> FrameworkPart | None:
        return ModelFrameType.model_frame.get_by_mrid(self, mrid)
