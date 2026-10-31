"""CIM class PhaseTapChanger (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.tap_changer import TapChanger

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.transformer_end import TransformerEnd


class PhaseTapChanger(TapChanger):
    """A transformer phase shifting tap model that controls the phase angle difference across
    the power transformer and potentially the active power flow through the power
    transformer. This phase tap model may also impact the voltage magnitude."""

    __slots__ = ("_transformer_end",)

    transformer_end: One[TransformerEnd] = One(
        EndMeta(
            name="transformer_end",
            cim_role="TransformerEnd",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_end:TransformerEnd",
            many=False,
            lower=1,
            upper=1,
            inverse="phase_tap_changer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PhaseTapChanger",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{7CEA69EF-C8A8-4f3d-99B2-9F934CC95BF4}",
        ends=(transformer_end.meta,),
    )

    def __init__(
        self,
        *,
        transformer_end: TransformerEnd | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if transformer_end is not None:
            self.transformer_end = transformer_end
