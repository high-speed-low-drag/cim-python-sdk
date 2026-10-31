"""CIM class MagneticStorm (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.space_phenomenon import SpacePhenomenon

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class MagneticStorm(SpacePhenomenon):
    """A magnetic storm, a temporary disturbance of the earth's magnetic field, induced by
    radiation and streams of charged particles from the sun."""

    __slots__ = ("change_dst",)

    change_dst: float | None  # MagneticField

    _cim_meta = ClassMeta(
        cim_name="MagneticStorm",
        package="TC57CIM/IEC62325/Environmental",
        guid="{58047739-8B91-44ea-8807-EEDFC6F44AF5}",
        attributes=(AttrMeta("change_dst", "changeDst", "MagneticField", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        change_dst: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.change_dst = change_dst
