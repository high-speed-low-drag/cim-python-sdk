"""CIM class HVDCDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/HVDCDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)


class HVDCDynamics(DynamicsFunctionBlock):
    """HVDC whose behaviour is described by reference to a standard model or by definition of a
    user-defined model."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="HVDCDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/HVDCDynamics",
        guid="{45E165D9-4A7C-4c6f-8256-550E4E86DF94}",
    )
