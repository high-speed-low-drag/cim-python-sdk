"""CIM class SeriesCompensator (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class SeriesCompensator(ConductingEquipment):
    """A Series Compensator is a series capacitor or reactor or an AC transmission line without
    charging susceptance. It is a two terminal device."""

    __slots__ = (
        "r",
        "r0",
        "varistor_present",
        "varistor_rated_current",
        "varistor_voltage_threshold",
        "x",
        "x0",
    )

    r: float | None  # Resistance
    r0: float | None  # Resistance
    x: float | None  # Reactance
    x0: float | None  # Reactance
    varistor_present: bool | None
    varistor_rated_current: float | None  # CurrentFlow
    varistor_voltage_threshold: float | None  # Voltage

    _cim_meta = ClassMeta(
        cim_name="SeriesCompensator",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{5B656059-8C65-455e-9E02-5A14C2631D6A}",
        attributes=(
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r0", "r0", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("x", "x", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x0", "x0", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("varistor_present", "varistorPresent", "bool", 0, 1, "primitive"),
            AttrMeta(
                "varistor_rated_current", "varistorRatedCurrent", "CurrentFlow", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "varistor_voltage_threshold",
                "varistorVoltageThreshold",
                "Voltage",
                0,
                1,
                "cimdatatype",
            ),
        ),
    )

    def __init__(
        self,
        *,
        r: float | None = None,
        r0: float | None = None,
        x: float | None = None,
        x0: float | None = None,
        varistor_present: bool | None = None,
        varistor_rated_current: float | None = None,
        varistor_voltage_threshold: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.r = r
        self.r0 = r0
        self.x = x
        self.x0 = x0
        self.varistor_present = varistor_present
        self.varistor_rated_current = varistor_rated_current
        self.varistor_voltage_threshold = varistor_voltage_threshold
