"""CGMES European extension enumeration LimitKind (EuropeanCIMExtensions/ExtIEC61970/ExtEuBase/ExtEuOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class LimitKind(CimEnum):
    """Limit kinds."""

    patl = "patl"
    patlt = "patlt"
    tatl = "tatl"
    tc = "tc"
    tct = "tct"
    highVoltage = "highVoltage"
    lowVoltage = "lowVoltage"
    operationalVoltageLimit = "operationalVoltageLimit"
    alarmVoltage = "alarmVoltage"
    warningVoltage = "warningVoltage"
    stability = "stability"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="LimitKind",
            package="EuropeanCIMExtensions/ExtIEC61970/ExtEuBase/ExtEuOperationalLimits",
            guid="{C6901289-57C7-41a3-AF87-9AA5E788E1CF}",
            kind="enumeration",
            namespace="eu",
        )
    )
