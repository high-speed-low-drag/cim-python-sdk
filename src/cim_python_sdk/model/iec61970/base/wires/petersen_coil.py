"""CIM class PetersenCoil (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.earth_fault_compensator import EarthFaultCompensator

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.petersen_coil_mode_kind import (
        PetersenCoilModeKind,
    )


class PetersenCoil(EarthFaultCompensator):
    """A variable impedance device normally used to offset line charging during single line
    faults in an ungrounded section of network."""

    __slots__ = (
        "mode",
        "nominal_u",
        "offset_current",
        "position_current",
        "x_ground_max",
        "x_ground_min",
        "x_ground_nominal",
    )

    mode: PetersenCoilModeKind | None
    nominal_u: float | None  # Voltage
    offset_current: float | None  # CurrentFlow
    position_current: float | None  # CurrentFlow
    x_ground_max: float | None  # Reactance
    x_ground_min: float | None  # Reactance
    x_ground_nominal: float | None  # Reactance

    _cim_meta = ClassMeta(
        cim_name="PetersenCoil",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{5538A367-14D4-4160-836F-2D049DB218B6}",
        attributes=(
            AttrMeta("mode", "mode", "PetersenCoilModeKind", 0, 1, "enumeration"),
            AttrMeta("nominal_u", "nominalU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("offset_current", "offsetCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("position_current", "positionCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("x_ground_max", "xGroundMax", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x_ground_min", "xGroundMin", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x_ground_nominal", "xGroundNominal", "Reactance", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mode: PetersenCoilModeKind | None = None,
        nominal_u: float | None = None,
        offset_current: float | None = None,
        position_current: float | None = None,
        x_ground_max: float | None = None,
        x_ground_min: float | None = None,
        x_ground_nominal: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mode = mode
        self.nominal_u = nominal_u
        self.offset_current = offset_current
        self.position_current = position_current
        self.x_ground_max = x_ground_max
        self.x_ground_min = x_ground_min
        self.x_ground_nominal = x_ground_nominal
