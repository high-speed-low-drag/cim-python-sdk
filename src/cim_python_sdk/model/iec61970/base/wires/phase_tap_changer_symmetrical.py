"""CIM class PhaseTapChangerSymmetrical (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.wires.phase_tap_changer_non_linear import (
    PhaseTapChangerNonLinear,
)


class PhaseTapChangerSymmetrical(PhaseTapChangerNonLinear):
    """Describes a symmetrical phase shifting transformer tap model in which the voltage
    magnitude of both sides is the same. The difference voltage magnitude is the base in an
    equal-sided triangle where the sides corresponds to the primary and secondary voltages.
    The phase angle difference corresponds to the top angle and can be expressed as twice
    the arctangent of half the total difference voltage."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="PhaseTapChangerSymmetrical",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{4841E53F-1B5B-487b-8F43-2ABA7B1FC93D}",
    )
