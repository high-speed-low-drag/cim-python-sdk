"""CIM class Fire (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec62325.environmental.geospheric_phenomenon import GeosphericPhenomenon


class Fire(GeosphericPhenomenon):
    """A fire, often uncontrolled, covering an area of land which typically contains
    combustible vegetation. Associated location information is assumed to describe the total
    area burned as of a specified time."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="Fire",
        package="TC57CIM/IEC62325/Environmental",
        guid="{5D83ADBF-889F-472b-AD60-D126B2168DC5}",
    )
