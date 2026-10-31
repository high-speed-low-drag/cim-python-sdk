"""CIM class LoadMotor (TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_aggregate import (
        LoadAggregate,
    )


class LoadMotor(IdentifiedObject):
    """Aggregate induction motor load. This model is used to represent a fraction of an
    ordinary load as "induction motor load". It allows a load that is treated as an ordinary
    constant power in power flow analysis to be represented by an induction motor in dynamic
    simulation. This model is intended for representation of aggregations of many motors
    dispersed through a load represented at a high voltage bus but where there is no
    information on the characteristics of individual motors.

    Either a "one-cage" or "two-cage" model of the induction machine can be modelled.
    Magnetic saturation is not modelled.

    This model treats a fraction of the constant power part of a load as a motor. During
    initialisation, the initial power drawn by the motor is set equal to Pfrac times the
    constant P part of the static load. The remainder of the load is left as a static load.

    The reactive power demand of the motor is calculated during initialisation as a function
    of voltage at the load bus. This reactive power demand can be less than or greater than
    the constant Q component of the load. If the motor's reactive demand is greater than the
    constant Q component of the load, the model inserts a shunt capacitor at the terminal of
    the motor to bring its reactive demand down to equal the constant Q reactive load.

    If an induction motor load model and a static load model are both present for a load,
    the motor Pfrac is assumed to be subtracted from the power flow constant P load before
    the static load model is applied. The remainder of the load, if any, is then represented
    by the static load model."""

    __slots__ = (
        "_load_aggregate",
        "d",
        "h",
        "lfac",
        "lp",
        "lpp",
        "ls",
        "pfrac",
        "ra",
        "tbkr",
        "tpo",
        "tppo",
        "tv",
        "vt",
    )

    pfrac: float | None
    lfac: float | None
    ls: float | None  # PU
    lp: float | None  # PU
    lpp: float | None  # PU
    ra: float | None  # PU
    tpo: float | None  # Seconds
    tppo: float | None  # Seconds
    h: float | None  # Seconds
    d: float | None
    vt: float | None  # PU
    tv: float | None  # Seconds
    tbkr: float | None  # Seconds

    load_aggregate: One[LoadAggregate] = One(
        EndMeta(
            name="load_aggregate",
            cim_role="LoadAggregate",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_aggregate:LoadAggregate",
            many=False,
            lower=1,
            upper=1,
            inverse="load_motor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadMotor",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics",
        guid="{26A10608-6EE9-42d6-8969-6212CD99C9E0}",
        attributes=(
            AttrMeta("pfrac", "pfrac", "float", 0, 1, "primitive"),
            AttrMeta("lfac", "lfac", "float", 0, 1, "primitive"),
            AttrMeta("ls", "ls", "PU", 0, 1, "cimdatatype"),
            AttrMeta("lp", "lp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("lpp", "lpp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ra", "ra", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tpo", "tpo", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tppo", "tppo", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("h", "h", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("d", "d", "float", 0, 1, "primitive"),
            AttrMeta("vt", "vt", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tv", "tv", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tbkr", "tbkr", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(load_aggregate.meta,),
    )

    def __init__(
        self,
        *,
        pfrac: float | None = None,
        lfac: float | None = None,
        ls: float | None = None,
        lp: float | None = None,
        lpp: float | None = None,
        ra: float | None = None,
        tpo: float | None = None,
        tppo: float | None = None,
        h: float | None = None,
        d: float | None = None,
        vt: float | None = None,
        tv: float | None = None,
        tbkr: float | None = None,
        load_aggregate: LoadAggregate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.pfrac = pfrac
        self.lfac = lfac
        self.ls = ls
        self.lp = lp
        self.lpp = lpp
        self.ra = ra
        self.tpo = tpo
        self.tppo = tppo
        self.h = h
        self.d = d
        self.vt = vt
        self.tv = tv
        self.tbkr = tbkr
        if load_aggregate is not None:
            self.load_aggregate = load_aggregate
