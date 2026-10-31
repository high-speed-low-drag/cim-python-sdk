"""CIM class PinGate (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate_input_pin import GateInputPin

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate import Gate


class PinGate(GateInputPin):
    """An output from one gate represent an input to another gate."""

    __slots__ = ("_gate_output",)

    gate_output: One[Gate] = One(
        EndMeta(
            name="gate_output",
            cim_role="GateOutput",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate:Gate",
            many=False,
            lower=1,
            upper=1,
            inverse="pin_gate",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PinGate",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{DB3E650E-6D8F-45ac-96E2-DD5F199DB803}",
        ends=(gate_output.meta,),
    )

    def __init__(
        self,
        *,
        gate_output: Gate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if gate_output is not None:
            self.gate_output = gate_output
