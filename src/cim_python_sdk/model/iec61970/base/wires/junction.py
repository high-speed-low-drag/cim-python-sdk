"""CIM class Junction (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.wires.connector import Connector


class Junction(Connector):
    """A point where one or more conducting equipments are connected with zero resistance."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="Junction",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{BE90EE60-8212-44ec-9F4D-775719E80216}",
    )
