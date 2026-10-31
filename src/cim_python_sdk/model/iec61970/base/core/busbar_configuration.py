"""CIM enumeration BusbarConfiguration (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BusbarConfiguration(CimEnum):
    """Busbar layout for bay."""

    singleBus = "singleBus"
    doubleBus = "doubleBus"
    mainWithTransfer = "mainWithTransfer"
    ringBus = "ringBus"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BusbarConfiguration",
            package="TC57CIM/IEC61970/Base/Core",
            guid="{E0C6B20A-0FEB-4e84-81EE-B34E49A1371F}",
            kind="enumeration",
        )
    )
