"""CIM class Connector (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment


class Connector(ConductingEquipment):
    """A conductor, or group of conductors, with negligible impedance, that serve to connect
    other conducting equipment within a single substation and are modelled with a single
    logical terminal."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="Connector",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{E33769DD-F111-4793-AF11-B4AFE5FDE50F}",
    )
