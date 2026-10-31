"""CIM class EnergyComponent (TC57CIM/IEC61970/InfIEC61970/EnergyArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.energy_connection import EnergyConnection
    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_group import EnergyGroup


class EnergyComponent(IdentifiedObject):
    """CIM class EnergyComponent."""

    __slots__ = ("_energy_connection", "_energy_group")

    energy_group: One[EnergyGroup] = One(
        EndMeta(
            name="energy_group",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_group:EnergyGroup",
            many=False,
            lower=1,
            upper=1,
            inverse="energy_components",
            aggregation="none",
        )
    )
    energy_connection: One[EnergyConnection] = One(
        EndMeta(
            name="energy_connection",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.base.wires.energy_connection:EnergyConnection",
            many=False,
            lower=1,
            upper=1,
            inverse="energy_components",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyComponent",
        package="TC57CIM/IEC61970/InfIEC61970/EnergyArea",
        guid="{31D86E1E-863D-4d07-BBD5-5D1373BBEBC0}",
        ends=(
            energy_group.meta,
            energy_connection.meta,
        ),
    )

    def __init__(
        self,
        *,
        energy_group: EnergyGroup | None = None,
        energy_connection: EnergyConnection | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if energy_group is not None:
            self.energy_group = energy_group
        if energy_connection is not None:
            self.energy_connection = energy_connection
