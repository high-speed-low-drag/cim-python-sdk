"""CIM class PowerElectronicsConnectionPhase (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.power_electronics_connection import (
        PowerElectronicsConnection,
    )
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class PowerElectronicsConnectionPhase(PowerSystemResource):
    """A single phase of a power electronics connection."""

    __slots__ = ("_power_electronics_connection", "p", "phase", "q")

    phase: SinglePhaseKind | None
    p: float | None  # ActivePower
    q: float | None  # ReactivePower

    power_electronics_connection: One[PowerElectronicsConnection] = One(
        EndMeta(
            name="power_electronics_connection",
            cim_role="PowerElectronicsConnection",
            target="cim_python_sdk.model.iec61970.base.wires.power_electronics_connection:PowerElectronicsConnection",
            many=False,
            lower=1,
            upper=1,
            inverse="power_electronics_connection_phase",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerElectronicsConnectionPhase",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{E1CB8A17-1A54-4eff-B918-817872DEA162}",
        attributes=(
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("q", "q", "ReactivePower", 0, 1, "cimdatatype"),
        ),
        ends=(power_electronics_connection.meta,),
    )

    def __init__(
        self,
        *,
        phase: SinglePhaseKind | None = None,
        p: float | None = None,
        q: float | None = None,
        power_electronics_connection: PowerElectronicsConnection | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.phase = phase
        self.p = p
        self.q = q
        if power_electronics_connection is not None:
            self.power_electronics_connection = power_electronics_connection
