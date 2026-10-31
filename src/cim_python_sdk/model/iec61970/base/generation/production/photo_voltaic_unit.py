"""CIM class PhotoVoltaicUnit (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.generation.production.power_electronics_unit import (
    PowerElectronicsUnit,
)


class PhotoVoltaicUnit(PowerElectronicsUnit):
    """A photovoltaic device or an aggregation of such devices."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="PhotoVoltaicUnit",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{4C57184E-FF79-4e7b-97FC-E2252FCA82A7}",
    )
