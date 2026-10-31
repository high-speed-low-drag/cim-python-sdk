"""CIM class PowerElectronicsUnit (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.equipment import Equipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.power_electronics_connection import (
        PowerElectronicsConnection,
    )


class PowerElectronicsUnit(Equipment):
    """A generating unit or battery or aggregation that connects to the AC network using power
    electronics rather than rotating machines."""

    __slots__ = ("_power_electronics_connection", "max_p", "min_p")

    max_p: float | None  # ActivePower
    min_p: float | None  # ActivePower

    power_electronics_connection: One[PowerElectronicsConnection] = One(
        EndMeta(
            name="power_electronics_connection",
            cim_role="PowerElectronicsConnection",
            target="cim_python_sdk.model.iec61970.base.wires.power_electronics_connection:PowerElectronicsConnection",
            many=False,
            lower=1,
            upper=1,
            inverse="power_electronics_unit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerElectronicsUnit",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{EC401F21-E818-46dc-88CE-2CFD1E60B76C}",
        attributes=(
            AttrMeta("max_p", "maxP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_p", "minP", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(power_electronics_connection.meta,),
    )

    def __init__(
        self,
        *,
        max_p: float | None = None,
        min_p: float | None = None,
        power_electronics_connection: PowerElectronicsConnection | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_p = max_p
        self.min_p = min_p
        if power_electronics_connection is not None:
            self.power_electronics_connection = power_electronics_connection
