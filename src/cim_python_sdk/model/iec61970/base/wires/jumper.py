"""CIM class Jumper (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.switch import Switch

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.jumper_action import JumperAction


class Jumper(Switch):
    """A short section of conductor with negligible impedance which can be manually removed and
    replaced if the circuit is de-energized. Note that zero-impedance branches can
    potentially be modelled by other equipment types."""

    __slots__ = ("_jumper_action",)

    jumper_action: One[JumperAction] = One(
        EndMeta(
            name="jumper_action",
            cim_role="JumperAction",
            target="cim_python_sdk.model.iec61968.operations.jumper_action:JumperAction",
            many=False,
            lower=0,
            upper=1,
            inverse="jumper",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Jumper",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{1D1D3E1A-76FB-4219-90DD-F6AE687989FC}",
        ends=(jumper_action.meta,),
    )

    def __init__(
        self,
        *,
        jumper_action: JumperAction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if jumper_action is not None:
            self.jumper_action = jumper_action
