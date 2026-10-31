"""CIM class PowerTransformerEnd (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.transformer_end import TransformerEnd

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.power_transformer import PowerTransformer
    from cim_python_sdk.model.iec61970.base.wires.winding_connection import WindingConnection


class PowerTransformerEnd(TransformerEnd):
    """A PowerTransformerEnd is associated with each Terminal of a PowerTransformer.

    The impedance values r, r0, x, and x0 of a PowerTransformerEnd represents a star
    equivalent as follows.

    1) for a two Terminal PowerTransformer the high voltage (TransformerEnd.endNumber=1)
    PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage
    (TransformerEnd.endNumber=2) PowerTransformerEnd has zero values for r, r0, x, and x0.
    Parameters are always provided, even if the PowerTransformerEnds have the same rated
    voltage. In this case, the parameters are provided at the PowerTransformerEnd which has
    TransformerEnd.endNumber equal to 1.

    2) for a three Terminal PowerTransformer the three PowerTransformerEnds represent a star
    equivalent with each leg in the star represented by r, r0, x, and x0 values.

    3) For a three Terminal transformer each PowerTransformerEnd shall have g, g0, b and b0
    values corresponding to the no load losses distributed on the three
    PowerTransformerEnds. The total no load loss shunt impedances may also be placed at one
    of the PowerTransformerEnds, preferably the end numbered 1, having the shunt values on
    end 1. This is the preferred way.

    4) for a PowerTransformer with more than three Terminals the PowerTransformerEnd
    impedance values cannot be used. Instead use the TransformerMeshImpedance or split the
    transformer into multiple PowerTransformers.

    Each PowerTransformerEnd must be contained by a PowerTransformer. Because a
    PowerTransformerEnd (or any other object) can not be contained by more than one parent,
    a PowerTransformerEnd can not have an association to an EquipmentContainer (Substation,
    VoltageLevel, etc)."""

    __slots__ = (
        "_power_transformer",
        "b",
        "b0",
        "connection_kind",
        "g",
        "g0",
        "phase_angle_clock",
        "r",
        "r0",
        "rated_s",
        "rated_u",
        "x",
        "x0",
    )

    b: float | None  # Susceptance
    b0: float | None  # Susceptance
    connection_kind: WindingConnection | None
    g: float | None  # Conductance
    g0: float | None  # Conductance
    phase_angle_clock: int | None
    r: float | None  # Resistance
    r0: float | None  # Resistance
    rated_s: float | None  # ApparentPower
    rated_u: float | None  # Voltage
    x: float | None  # Reactance
    x0: float | None  # Reactance

    power_transformer: One[PowerTransformer] = One(
        EndMeta(
            name="power_transformer",
            cim_role="PowerTransformer",
            target="cim_python_sdk.model.iec61970.base.wires.power_transformer:PowerTransformer",
            many=False,
            lower=0,
            upper=1,
            inverse="power_transformer_end",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerTransformerEnd",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{51A671B1-C546-4106-92F9-ED7C0305A2DB}",
        attributes=(
            AttrMeta("b", "b", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("b0", "b0", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("connection_kind", "connectionKind", "WindingConnection", 0, 1, "enumeration"),
            AttrMeta("g", "g", "Conductance", 0, 1, "cimdatatype"),
            AttrMeta("g0", "g0", "Conductance", 0, 1, "cimdatatype"),
            AttrMeta("phase_angle_clock", "phaseAngleClock", "int", 0, 1, "primitive"),
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r0", "r0", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("rated_s", "ratedS", "ApparentPower", 0, 1, "cimdatatype"),
            AttrMeta("rated_u", "ratedU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("x", "x", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x0", "x0", "Reactance", 0, 1, "cimdatatype"),
        ),
        ends=(power_transformer.meta,),
    )

    def __init__(
        self,
        *,
        b: float | None = None,
        b0: float | None = None,
        connection_kind: WindingConnection | None = None,
        g: float | None = None,
        g0: float | None = None,
        phase_angle_clock: int | None = None,
        r: float | None = None,
        r0: float | None = None,
        rated_s: float | None = None,
        rated_u: float | None = None,
        x: float | None = None,
        x0: float | None = None,
        power_transformer: PowerTransformer | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b = b
        self.b0 = b0
        self.connection_kind = connection_kind
        self.g = g
        self.g0 = g0
        self.phase_angle_clock = phase_angle_clock
        self.r = r
        self.r0 = r0
        self.rated_s = rated_s
        self.rated_u = rated_u
        self.x = x
        self.x0 = x0
        if power_transformer is not None:
            self.power_transformer = power_transformer
