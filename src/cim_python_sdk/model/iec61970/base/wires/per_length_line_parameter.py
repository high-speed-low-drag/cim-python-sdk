"""CIM class PerLengthLineParameter (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_info.wire_assembly_info import WireAssemblyInfo


class PerLengthLineParameter(IdentifiedObject):
    """Common type for per-length electrical catalogues describing line parameters."""

    __slots__ = ("_wire_assembly_info",)

    wire_assembly_info: One[WireAssemblyInfo] = One(
        EndMeta(
            name="wire_assembly_info",
            cim_role="WireAssemblyInfo",
            target="cim_python_sdk.model.iec61968.asset_info.wire_assembly_info:WireAssemblyInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="per_length_line_parameter",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PerLengthLineParameter",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{5E96862B-1FFF-4fbf-B5D5-919E4DE8A1A9}",
        ends=(wire_assembly_info.meta,),
    )

    def __init__(
        self,
        *,
        wire_assembly_info: WireAssemblyInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wire_assembly_info is not None:
            self.wire_assembly_info = wire_assembly_info
