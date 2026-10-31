"""CIM class BaseFrequency (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class BaseFrequency(IdentifiedObject):
    """The BaseFrequency class describes a base frequency for a power system network. In case
    of multiple power networks with different frequencies, e.g. 50 Hz or 60 Hz each network
    will have its own base frequency class. Hence it is assumed that power system objects
    having different base frequencies appear in separate documents where each document has a
    single base frequency instance."""

    __slots__ = ("frequency",)

    frequency: float | None  # Frequency

    _cim_meta = ClassMeta(
        cim_name="BaseFrequency",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{2FA6A39A-A920-4ab7-92DC-D005DDDBB348}",
        attributes=(AttrMeta("frequency", "frequency", "Frequency", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        frequency: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.frequency = frequency
