"""CIM enumeration InterruptingMediumKind (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class InterruptingMediumKind(CimEnum):
    """Kinds of interrupting mediums."""

    airBlast = "airBlast"
    airMagnetic = "airMagnetic"
    gasTwoPressure = "gasTwoPressure"
    gasSinglePressure = "gasSinglePressure"
    bulkOil = "bulkOil"
    minimumOil = "minimumOil"
    vacuum = "vacuum"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="InterruptingMediumKind",
            package="TC57CIM/IEC61968/AssetInfo",
            guid="{42A70513-C116-4708-B2D1-300745E7E624}",
            kind="enumeration",
        )
    )
