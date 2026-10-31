"""CIM class VsCapabilityCurve (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.dc.vs_converter import VsConverter


class VsCapabilityCurve(Curve):
    """The P-Q capability curve for a voltage source converter, with P on X-axis and Qmin and
    Qmax on Y1-axis and Y2-axis."""

    __slots__ = ("_vs_converter_dc_sides",)

    vs_converter_dc_sides: Many[VsConverter] = Many(
        EndMeta(
            name="vs_converter_dc_sides",
            cim_role="VsConverterDCSides",
            target="cim_python_sdk.model.iec61970.base.dc.vs_converter:VsConverter",
            many=True,
            lower=0,
            upper=None,
            inverse="capability_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VsCapabilityCurve",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{64F5C25B-18FF-4bb5-AA4C-F66F8EE815D5}",
        ends=(vs_converter_dc_sides.meta,),
    )

    def __init__(
        self,
        *,
        vs_converter_dc_sides: Iterable[VsConverter] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if vs_converter_dc_sides is not None:
            VsCapabilityCurve.vs_converter_dc_sides.extend(self, vs_converter_dc_sides)

    def add_vs_converter_dc_side(self, vs_converter_dc_side: VsConverter) -> Self:
        return VsCapabilityCurve.vs_converter_dc_sides.add(self, vs_converter_dc_side)

    def remove_vs_converter_dc_side(self, vs_converter_dc_side: VsConverter) -> Self:
        return VsCapabilityCurve.vs_converter_dc_sides.remove(self, vs_converter_dc_side)

    def clear_vs_converter_dc_sides(self) -> Self:
        return VsCapabilityCurve.vs_converter_dc_sides.clear(self)

    def num_vs_converter_dc_side(self) -> int:
        return VsCapabilityCurve.vs_converter_dc_sides.count(self)

    def get_vs_converter_dc_side_by_mrid(self, mrid: str) -> VsConverter | None:
        return VsCapabilityCurve.vs_converter_dc_sides.get_by_mrid(self, mrid)
