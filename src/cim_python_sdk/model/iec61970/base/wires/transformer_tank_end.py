"""CIM class TransformerTankEnd (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.transformer_end import TransformerEnd

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode
    from cim_python_sdk.model.iec61970.base.wires.transformer_tank import TransformerTank


class TransformerTankEnd(TransformerEnd):
    """Transformer tank end represents an individual winding for unbalanced models or for
    transformer tanks connected into a bank (and bank is modelled with the
    PowerTransformer)."""

    __slots__ = ("_transformer_tank", "phases")

    phases: PhaseCode | None

    transformer_tank: One[TransformerTank] = One(
        EndMeta(
            name="transformer_tank",
            cim_role="TransformerTank",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_tank:TransformerTank",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_tank_ends",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransformerTankEnd",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{7CAE4704-5B8C-4ad5-B3B1-6ECD141F8A09}",
        attributes=(AttrMeta("phases", "phases", "PhaseCode", 0, 1, "enumeration"),),
        ends=(transformer_tank.meta,),
    )

    def __init__(
        self,
        *,
        phases: PhaseCode | None = None,
        transformer_tank: TransformerTank | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.phases = phases
        if transformer_tank is not None:
            self.transformer_tank = transformer_tank
