"""CIM class RotatingMachine (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.regulating_cond_eq import RegulatingCondEq

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.generating_unit import (
        GeneratingUnit,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.hydro_pump import HydroPump


class RotatingMachine(RegulatingCondEq):
    """A rotating machine which may be used as a generator or motor."""

    __slots__ = (
        "_generating_unit",
        "_hydro_pump",
        "p",
        "q",
        "rated_power_factor",
        "rated_s",
        "rated_u",
    )

    rated_power_factor: float | None
    p: float | None  # ActivePower
    rated_s: float | None  # ApparentPower
    q: float | None  # ReactivePower
    rated_u: float | None  # Voltage

    generating_unit: One[GeneratingUnit] = One(
        EndMeta(
            name="generating_unit",
            cim_role="GeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.generating_unit:GeneratingUnit",
            many=False,
            lower=0,
            upper=1,
            inverse="rotating_machine",
            aggregation="none",
        )
    )
    hydro_pump: One[HydroPump] = One(
        EndMeta(
            name="hydro_pump",
            cim_role="HydroPump",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_pump:HydroPump",
            many=False,
            lower=0,
            upper=1,
            inverse="rotating_machine",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RotatingMachine",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{8ADF23B6-43B5-436b-91CE-E22D54B323B8}",
        attributes=(
            AttrMeta("rated_power_factor", "ratedPowerFactor", "float", 0, 1, "primitive"),
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("rated_s", "ratedS", "ApparentPower", 0, 1, "cimdatatype"),
            AttrMeta("q", "q", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("rated_u", "ratedU", "Voltage", 0, 1, "cimdatatype"),
        ),
        ends=(
            generating_unit.meta,
            hydro_pump.meta,
        ),
    )

    def __init__(
        self,
        *,
        rated_power_factor: float | None = None,
        p: float | None = None,
        rated_s: float | None = None,
        q: float | None = None,
        rated_u: float | None = None,
        generating_unit: GeneratingUnit | None = None,
        hydro_pump: HydroPump | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rated_power_factor = rated_power_factor
        self.p = p
        self.rated_s = rated_s
        self.q = q
        self.rated_u = rated_u
        if generating_unit is not None:
            self.generating_unit = generating_unit
        if hydro_pump is not None:
            self.hydro_pump = hydro_pump
