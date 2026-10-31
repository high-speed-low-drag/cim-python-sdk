"""CIM class BusbarSection (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.connector import Connector

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.voltage_control_zone import VoltageControlZone


class BusbarSection(Connector):
    """A conductor, or group of conductors, with negligible impedance, that serve to connect
    other conducting equipment within a single substation.

    Voltage measurements are typically obtained from voltage transformers that are connected
    to busbar sections. A bus bar section may have many physical terminals but for analysis
    is modelled with exactly one logical terminal."""

    __slots__ = ("_voltage_control_zone", "ip_max")

    ip_max: float | None  # CurrentFlow

    voltage_control_zone: One[VoltageControlZone] = One(
        EndMeta(
            name="voltage_control_zone",
            cim_role="VoltageControlZone",
            target="cim_python_sdk.model.iec61970.base.wires.voltage_control_zone:VoltageControlZone",
            many=False,
            lower=0,
            upper=1,
            inverse="busbar_section",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BusbarSection",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{0A63A81D-5142-4736-BD22-8C28BA32F233}",
        attributes=(AttrMeta("ip_max", "ipMax", "CurrentFlow", 0, 1, "cimdatatype"),),
        ends=(voltage_control_zone.meta,),
    )

    def __init__(
        self,
        *,
        ip_max: float | None = None,
        voltage_control_zone: VoltageControlZone | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ip_max = ip_max
        if voltage_control_zone is not None:
            self.voltage_control_zone = voltage_control_zone
