"""CIM class SubGeographicalRegion (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.geographical_region import GeographicalRegion
    from cim_python_sdk.model.iec61970.base.core.substation import Substation
    from cim_python_sdk.model.iec61970.base.dc.dc_line import DCLine
    from cim_python_sdk.model.iec61970.base.wires.line import Line


class SubGeographicalRegion(IdentifiedObject):
    """A subset of a geographical region of a power system network model."""

    __slots__ = ("_dc_lines", "_lines", "_region", "_substations")

    region: One[GeographicalRegion] = One(
        EndMeta(
            name="region",
            cim_role="Region",
            target="cim_python_sdk.model.iec61970.base.core.geographical_region:GeographicalRegion",
            many=False,
            lower=0,
            upper=1,
            inverse="regions",
            aggregation="none",
        )
    )
    substations: Many[Substation] = Many(
        EndMeta(
            name="substations",
            cim_role="Substations",
            target="cim_python_sdk.model.iec61970.base.core.substation:Substation",
            many=True,
            lower=0,
            upper=None,
            inverse="region",
            aggregation="shared",
        )
    )
    dc_lines: Many[DCLine] = Many(
        EndMeta(
            name="dc_lines",
            cim_role="DCLines",
            target="cim_python_sdk.model.iec61970.base.dc.dc_line:DCLine",
            many=True,
            lower=0,
            upper=None,
            inverse="region",
            aggregation="none",
        )
    )
    lines: Many[Line] = Many(
        EndMeta(
            name="lines",
            cim_role="Lines",
            target="cim_python_sdk.model.iec61970.base.wires.line:Line",
            many=True,
            lower=0,
            upper=None,
            inverse="region",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SubGeographicalRegion",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{D3CE44CA-5AED-484b-92A3-89F156425204}",
        ends=(
            region.meta,
            substations.meta,
            dc_lines.meta,
            lines.meta,
        ),
    )

    def __init__(
        self,
        *,
        region: GeographicalRegion | None = None,
        substations: Iterable[Substation] | None = None,
        dc_lines: Iterable[DCLine] | None = None,
        lines: Iterable[Line] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if region is not None:
            self.region = region
        if substations is not None:
            SubGeographicalRegion.substations.extend(self, substations)
        if dc_lines is not None:
            SubGeographicalRegion.dc_lines.extend(self, dc_lines)
        if lines is not None:
            SubGeographicalRegion.lines.extend(self, lines)

    def add_substation(self, substation: Substation) -> Self:
        return SubGeographicalRegion.substations.add(self, substation)

    def remove_substation(self, substation: Substation) -> Self:
        return SubGeographicalRegion.substations.remove(self, substation)

    def clear_substations(self) -> Self:
        return SubGeographicalRegion.substations.clear(self)

    def num_substation(self) -> int:
        return SubGeographicalRegion.substations.count(self)

    def get_substation_by_mrid(self, mrid: str) -> Substation | None:
        return SubGeographicalRegion.substations.get_by_mrid(self, mrid)

    def add_dc_line(self, dc_line: DCLine) -> Self:
        return SubGeographicalRegion.dc_lines.add(self, dc_line)

    def remove_dc_line(self, dc_line: DCLine) -> Self:
        return SubGeographicalRegion.dc_lines.remove(self, dc_line)

    def clear_dc_lines(self) -> Self:
        return SubGeographicalRegion.dc_lines.clear(self)

    def num_dc_line(self) -> int:
        return SubGeographicalRegion.dc_lines.count(self)

    def get_dc_line_by_mrid(self, mrid: str) -> DCLine | None:
        return SubGeographicalRegion.dc_lines.get_by_mrid(self, mrid)

    def add_line(self, line: Line) -> Self:
        return SubGeographicalRegion.lines.add(self, line)

    def remove_line(self, line: Line) -> Self:
        return SubGeographicalRegion.lines.remove(self, line)

    def clear_lines(self) -> Self:
        return SubGeographicalRegion.lines.clear(self)

    def num_line(self) -> int:
        return SubGeographicalRegion.lines.count(self)

    def get_line_by_mrid(self, mrid: str) -> Line | None:
        return SubGeographicalRegion.lines.get_by_mrid(self, mrid)
