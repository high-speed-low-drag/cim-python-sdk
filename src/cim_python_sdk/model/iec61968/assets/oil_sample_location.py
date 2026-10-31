"""CIM enumeration OilSampleLocation (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilSampleLocation(CimEnum):
    """Locations where oil can be sampled."""

    oilSampleValve = "oilSampleValve"
    oilDrainageDevice = "oilDrainageDevice"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilSampleLocation",
            package="TC57CIM/IEC61968/Assets",
            guid="{A0B10F74-025D-4966-8127-FA1FF8E5BD2C}",
            kind="enumeration",
        )
    )
