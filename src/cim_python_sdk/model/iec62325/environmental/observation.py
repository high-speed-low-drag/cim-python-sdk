"""CIM class Observation (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec62325.environmental.environmental_information import (
    EnvironmentalInformation,
)


class Observation(EnvironmentalInformation):
    """Observed (actual non-forecast) values sets and/or phenomena characteristics."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="Observation",
        package="TC57CIM/IEC62325/Environmental",
        guid="{78A1E5B0-C614-47f1-A3DD-DF1AFD5A39B3}",
    )
