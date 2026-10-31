"""CIM enumeration WorkTaskKind (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WorkTaskKind(CimEnum):
    """Kinds of work tasks."""

    install = "install"
    remove = "remove"
    exchange = "exchange"
    investigate = "investigate"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WorkTaskKind",
            package="TC57CIM/IEC61968/Work",
            guid="{0485332B-3E0E-44c5-ADC6-4808216558DD}",
            kind="enumeration",
        )
    )
