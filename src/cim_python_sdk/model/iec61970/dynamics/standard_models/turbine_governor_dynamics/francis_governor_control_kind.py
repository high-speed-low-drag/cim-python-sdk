"""CIM enumeration FrancisGovernorControlKind (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FrancisGovernorControlKind(CimEnum):
    """Governor control flag for Francis hydro model."""

    mechanicHydrolicTachoAccelerator = "mechanicHydrolicTachoAccelerator"
    mechanicHydraulicTransientFeedback = "mechanicHydraulicTransientFeedback"
    electromechanicalElectrohydraulic = "electromechanicalElectrohydraulic"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FrancisGovernorControlKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
            guid="{AD4A17B1-6646-47dc-84A9-14243D94BDAF}",
            kind="enumeration",
        )
    )
