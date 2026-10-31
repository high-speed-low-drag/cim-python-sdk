"""CIM class AsynchronousMachine (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.rotating_machine import RotatingMachine

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.asynchronous_machine_kind import (
        AsynchronousMachineKind,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.asynchronous_machine_dynamics.asynchronous_machine_dynamics import (
        AsynchronousMachineDynamics,
    )


class AsynchronousMachine(RotatingMachine):
    """A rotating machine whose shaft rotates asynchronously with the electrical field. Also
    known as an induction machine with no external connection to the rotor windings, e.g.
    squirrel-cage induction machine."""

    __slots__ = (
        "_asynchronous_machine_dynamics",
        "asynchronous_machine_type",
        "converter_fed_drive",
        "efficiency",
        "ia_ir_ratio",
        "nominal_frequency",
        "nominal_speed",
        "pole_pair_number",
        "rated_mechanical_power",
        "reversible",
        "rr1",
        "rr2",
        "rx_locked_rotor_ratio",
        "tpo",
        "tppo",
        "xlr1",
        "xlr2",
        "xm",
        "xp",
        "xpp",
        "xs",
    )

    asynchronous_machine_type: AsynchronousMachineKind | None
    converter_fed_drive: bool | None
    efficiency: float | None  # PerCent
    ia_ir_ratio: float | None
    nominal_frequency: float | None  # Frequency
    nominal_speed: float | None  # RotationSpeed
    pole_pair_number: int | None
    rated_mechanical_power: float | None  # ActivePower
    reversible: bool | None
    rr1: float | None  # Resistance
    rr2: float | None  # Resistance
    rx_locked_rotor_ratio: float | None
    tpo: float | None  # Seconds
    tppo: float | None  # Seconds
    xlr1: float | None  # Reactance
    xlr2: float | None  # Reactance
    xm: float | None  # Reactance
    xp: float | None  # Reactance
    xpp: float | None  # Reactance
    xs: float | None  # Reactance

    asynchronous_machine_dynamics: One[AsynchronousMachineDynamics] = One(
        EndMeta(
            name="asynchronous_machine_dynamics",
            cim_role="AsynchronousMachineDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.asynchronous_machine_dynamics.asynchronous_machine_dynamics:AsynchronousMachineDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="asynchronous_machine",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AsynchronousMachine",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{EC5FCEFF-1274-4771-9D92-C0FF7A100AB8}",
        attributes=(
            AttrMeta(
                "asynchronous_machine_type",
                "asynchronousMachineType",
                "AsynchronousMachineKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("converter_fed_drive", "converterFedDrive", "bool", 0, 1, "primitive"),
            AttrMeta("efficiency", "efficiency", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("ia_ir_ratio", "iaIrRatio", "float", 0, 1, "primitive"),
            AttrMeta("nominal_frequency", "nominalFrequency", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("nominal_speed", "nominalSpeed", "RotationSpeed", 0, 1, "cimdatatype"),
            AttrMeta("pole_pair_number", "polePairNumber", "int", 0, 1, "primitive"),
            AttrMeta(
                "rated_mechanical_power", "ratedMechanicalPower", "ActivePower", 0, 1, "cimdatatype"
            ),
            AttrMeta("reversible", "reversible", "bool", 0, 1, "primitive"),
            AttrMeta("rr1", "rr1", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("rr2", "rr2", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("rx_locked_rotor_ratio", "rxLockedRotorRatio", "float", 0, 1, "primitive"),
            AttrMeta("tpo", "tpo", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tppo", "tppo", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("xlr1", "xlr1", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("xlr2", "xlr2", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("xm", "xm", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("xp", "xp", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("xpp", "xpp", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("xs", "xs", "Reactance", 0, 1, "cimdatatype"),
        ),
        ends=(asynchronous_machine_dynamics.meta,),
    )

    def __init__(
        self,
        *,
        asynchronous_machine_type: AsynchronousMachineKind | None = None,
        converter_fed_drive: bool | None = None,
        efficiency: float | None = None,
        ia_ir_ratio: float | None = None,
        nominal_frequency: float | None = None,
        nominal_speed: float | None = None,
        pole_pair_number: int | None = None,
        rated_mechanical_power: float | None = None,
        reversible: bool | None = None,
        rr1: float | None = None,
        rr2: float | None = None,
        rx_locked_rotor_ratio: float | None = None,
        tpo: float | None = None,
        tppo: float | None = None,
        xlr1: float | None = None,
        xlr2: float | None = None,
        xm: float | None = None,
        xp: float | None = None,
        xpp: float | None = None,
        xs: float | None = None,
        asynchronous_machine_dynamics: AsynchronousMachineDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.asynchronous_machine_type = asynchronous_machine_type
        self.converter_fed_drive = converter_fed_drive
        self.efficiency = efficiency
        self.ia_ir_ratio = ia_ir_ratio
        self.nominal_frequency = nominal_frequency
        self.nominal_speed = nominal_speed
        self.pole_pair_number = pole_pair_number
        self.rated_mechanical_power = rated_mechanical_power
        self.reversible = reversible
        self.rr1 = rr1
        self.rr2 = rr2
        self.rx_locked_rotor_ratio = rx_locked_rotor_ratio
        self.tpo = tpo
        self.tppo = tppo
        self.xlr1 = xlr1
        self.xlr2 = xlr2
        self.xm = xm
        self.xp = xp
        self.xpp = xpp
        self.xs = xs
        if asynchronous_machine_dynamics is not None:
            self.asynchronous_machine_dynamics = asynchronous_machine_dynamics
