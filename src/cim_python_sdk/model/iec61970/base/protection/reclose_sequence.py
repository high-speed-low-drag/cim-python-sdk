"""CIM class RecloseSequence (TC57CIM/IEC61970/Base/Protection). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.protected_switch import ProtectedSwitch


class RecloseSequence(IdentifiedObject):
    """A reclose sequence (open and close) is defined for each possible reclosure of a breaker."""

    __slots__ = ("_protected_switch", "reclose_delay", "reclose_step")

    reclose_delay: float | None  # Seconds
    reclose_step: int | None

    protected_switch: One[ProtectedSwitch] = One(
        EndMeta(
            name="protected_switch",
            cim_role="ProtectedSwitch",
            target="cim_python_sdk.model.iec61970.base.wires.protected_switch:ProtectedSwitch",
            many=False,
            lower=1,
            upper=1,
            inverse="reclose_sequences",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RecloseSequence",
        package="TC57CIM/IEC61970/Base/Protection",
        guid="{2BB9ABD3-5CB7-43ba-88A8-04D971642DA2}",
        attributes=(
            AttrMeta("reclose_delay", "recloseDelay", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("reclose_step", "recloseStep", "int", 0, 1, "primitive"),
        ),
        ends=(protected_switch.meta,),
    )

    def __init__(
        self,
        *,
        reclose_delay: float | None = None,
        reclose_step: int | None = None,
        protected_switch: ProtectedSwitch | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.reclose_delay = reclose_delay
        self.reclose_step = reclose_step
        if protected_switch is not None:
            self.protected_switch = protected_switch
