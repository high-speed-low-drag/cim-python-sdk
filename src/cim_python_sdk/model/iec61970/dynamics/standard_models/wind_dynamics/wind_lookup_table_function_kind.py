"""CIM enumeration WindLookupTableFunctionKind (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WindLookupTableFunctionKind(CimEnum):
    """Function of the lookup table."""

    prr = "prr"
    omegap = "omegap"
    ipmax = "ipmax"
    iqmax = "iqmax"
    pwp = "pwp"
    tcwdu = "tcwdu"
    tduwt = "tduwt"
    qmaxp = "qmaxp"
    qminp = "qminp"
    qmaxu = "qmaxu"
    qminu = "qminu"
    tuover = "tuover"
    tuunder = "tuunder"
    tfover = "tfover"
    tfunder = "tfunder"
    qwp = "qwp"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WindLookupTableFunctionKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
            guid="{6735A5DE-574A-4c0a-BAC1-09CE63D5BB30}",
            kind="enumeration",
        )
    )
