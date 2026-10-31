"""CIM class DCLineSegment (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.dc.dc_conducting_equipment import DCConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.dc.per_length_dc_line_parameter import (
        PerLengthDCLineParameter,
    )


class DCLineSegment(DCConductingEquipment):
    """A wire or combination of wires not insulated from one another, with consistent
    electrical characteristics, used to carry direct current between points in the DC region
    of the power system."""

    __slots__ = ("_per_length_parameter", "capacitance", "inductance", "length", "resistance")

    capacitance: float | None  # Capacitance
    inductance: float | None  # Inductance
    resistance: float | None  # Resistance
    length: float | None  # Length

    per_length_parameter: One[PerLengthDCLineParameter] = One(
        EndMeta(
            name="per_length_parameter",
            cim_role="PerLengthParameter",
            target="cim_python_sdk.model.iec61970.base.dc.per_length_dc_line_parameter:PerLengthDCLineParameter",
            many=False,
            lower=0,
            upper=1,
            inverse="dc_line_segments",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCLineSegment",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{6AD33D6A-FCE0-48ab-99A6-522868A70AD2}",
        attributes=(
            AttrMeta("capacitance", "capacitance", "Capacitance", 0, 1, "cimdatatype"),
            AttrMeta("inductance", "inductance", "Inductance", 0, 1, "cimdatatype"),
            AttrMeta("resistance", "resistance", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("length", "length", "Length", 0, 1, "cimdatatype"),
        ),
        ends=(per_length_parameter.meta,),
    )

    def __init__(
        self,
        *,
        capacitance: float | None = None,
        inductance: float | None = None,
        resistance: float | None = None,
        length: float | None = None,
        per_length_parameter: PerLengthDCLineParameter | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.capacitance = capacitance
        self.inductance = inductance
        self.resistance = resistance
        self.length = length
        if per_length_parameter is not None:
            self.per_length_parameter = per_length_parameter
