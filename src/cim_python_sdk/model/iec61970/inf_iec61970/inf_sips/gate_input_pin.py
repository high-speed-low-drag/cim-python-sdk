"""CIM class GateInputPin (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.analog_to_digital_logic_kind import (
        AnalogToDigitalLogicKind,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate import Gate


class GateInputPin(IdentifiedObject):
    """Input pin for a logical gate. The condition described in the input pin will give a
    logical true or false. Result from measurement and calculation are converted to a true
    or false."""

    __slots__ = (
        "_gate",
        "a_d_logic_kind",
        "absolute_value",
        "duration",
        "negate",
        "threshold_percentage",
        "threshold_value",
    )

    absolute_value: bool | None
    a_d_logic_kind: AnalogToDigitalLogicKind | None
    duration: float | None  # Seconds
    negate: bool | None
    threshold_percentage: float | None  # PerCent
    threshold_value: float | None

    gate: One[Gate] = One(
        EndMeta(
            name="gate",
            cim_role="Gate",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate:Gate",
            many=False,
            lower=1,
            upper=1,
            inverse="gate_input_pin",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GateInputPin",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{34FB8459-3EC3-424d-8903-D1B106DD0E74}",
        attributes=(
            AttrMeta("absolute_value", "absoluteValue", "bool", 0, 1, "primitive"),
            AttrMeta(
                "a_d_logic_kind", "aDLogicKind", "AnalogToDigitalLogicKind", 0, 1, "enumeration"
            ),
            AttrMeta("duration", "duration", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("negate", "negate", "bool", 0, 1, "primitive"),
            AttrMeta("threshold_percentage", "thresholdPercentage", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("threshold_value", "thresholdValue", "float", 0, 1, "primitive"),
        ),
        ends=(gate.meta,),
    )

    def __init__(
        self,
        *,
        absolute_value: bool | None = None,
        a_d_logic_kind: AnalogToDigitalLogicKind | None = None,
        duration: float | None = None,
        negate: bool | None = None,
        threshold_percentage: float | None = None,
        threshold_value: float | None = None,
        gate: Gate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.absolute_value = absolute_value
        self.a_d_logic_kind = a_d_logic_kind
        self.duration = duration
        self.negate = negate
        self.threshold_percentage = threshold_percentage
        self.threshold_value = threshold_value
        if gate is not None:
            self.gate = gate
