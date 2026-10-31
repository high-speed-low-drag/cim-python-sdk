"""CIM class EquivalentInjection (TC57CIM/IEC61970/Base/Equivalents). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.equivalents.equivalent_equipment import EquivalentEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.reactive_capability_curve import (
        ReactiveCapabilityCurve,
    )


class EquivalentInjection(EquivalentEquipment):
    """This class represents equivalent injections (generation or load). Voltage regulation is
    allowed only at the point of connection."""

    __slots__ = (
        "_reactive_capability_curve",
        "max_p",
        "max_q",
        "min_p",
        "min_q",
        "p",
        "q",
        "r",
        "r0",
        "r2",
        "regulation_capability",
        "regulation_status",
        "regulation_target",
        "x",
        "x0",
        "x2",
    )

    max_p: float | None  # ActivePower
    max_q: float | None  # ReactivePower
    min_p: float | None  # ActivePower
    min_q: float | None  # ReactivePower
    r: float | None  # Resistance
    r0: float | None  # Resistance
    r2: float | None  # Resistance
    regulation_capability: bool | None
    regulation_status: bool | None
    regulation_target: float | None  # Voltage
    x: float | None  # Reactance
    x0: float | None  # Reactance
    x2: float | None  # Reactance
    p: float | None  # ActivePower
    q: float | None  # ReactivePower

    reactive_capability_curve: One[ReactiveCapabilityCurve] = One(
        EndMeta(
            name="reactive_capability_curve",
            cim_role="ReactiveCapabilityCurve",
            target="cim_python_sdk.model.iec61970.base.wires.reactive_capability_curve:ReactiveCapabilityCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="equivalent_injection",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EquivalentInjection",
        package="TC57CIM/IEC61970/Base/Equivalents",
        guid="{9749AD93-8F33-48c8-9291-02B9D671C172}",
        attributes=(
            AttrMeta("max_p", "maxP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_q", "maxQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_p", "minP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_q", "minQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r0", "r0", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r2", "r2", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("regulation_capability", "regulationCapability", "bool", 0, 1, "primitive"),
            AttrMeta("regulation_status", "regulationStatus", "bool", 0, 1, "primitive"),
            AttrMeta("regulation_target", "regulationTarget", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("x", "x", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x0", "x0", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x2", "x2", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("q", "q", "ReactivePower", 0, 1, "cimdatatype"),
        ),
        ends=(reactive_capability_curve.meta,),
    )

    def __init__(
        self,
        *,
        max_p: float | None = None,
        max_q: float | None = None,
        min_p: float | None = None,
        min_q: float | None = None,
        r: float | None = None,
        r0: float | None = None,
        r2: float | None = None,
        regulation_capability: bool | None = None,
        regulation_status: bool | None = None,
        regulation_target: float | None = None,
        x: float | None = None,
        x0: float | None = None,
        x2: float | None = None,
        p: float | None = None,
        q: float | None = None,
        reactive_capability_curve: ReactiveCapabilityCurve | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_p = max_p
        self.max_q = max_q
        self.min_p = min_p
        self.min_q = min_q
        self.r = r
        self.r0 = r0
        self.r2 = r2
        self.regulation_capability = regulation_capability
        self.regulation_status = regulation_status
        self.regulation_target = regulation_target
        self.x = x
        self.x0 = x0
        self.x2 = x2
        self.p = p
        self.q = q
        if reactive_capability_curve is not None:
            self.reactive_capability_curve = reactive_capability_curve
