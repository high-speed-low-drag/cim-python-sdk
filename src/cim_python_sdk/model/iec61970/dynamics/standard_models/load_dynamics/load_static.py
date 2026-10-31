"""CIM class LoadStatic (TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_aggregate import (
        LoadAggregate,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.static_load_model_kind import (
        StaticLoadModelKind,
    )


class LoadStatic(IdentifiedObject):
    """General static load. This model represents the sensitivity of the real and reactive
    power consumed by the load to the amplitude and frequency of the bus voltage."""

    __slots__ = (
        "_load_aggregate",
        "ep1",
        "ep2",
        "ep3",
        "eq1",
        "eq2",
        "eq3",
        "kp1",
        "kp2",
        "kp3",
        "kp4",
        "kpf",
        "kq1",
        "kq2",
        "kq3",
        "kq4",
        "kqf",
        "static_load_model_type",
    )

    static_load_model_type: StaticLoadModelKind | None
    kp1: float | None
    kp2: float | None
    kp3: float | None
    kp4: float | None
    ep1: float | None
    ep2: float | None
    ep3: float | None
    kpf: float | None
    kq1: float | None
    kq2: float | None
    kq3: float | None
    kq4: float | None
    eq1: float | None
    eq2: float | None
    eq3: float | None
    kqf: float | None

    load_aggregate: One[LoadAggregate] = One(
        EndMeta(
            name="load_aggregate",
            cim_role="LoadAggregate",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_aggregate:LoadAggregate",
            many=False,
            lower=1,
            upper=1,
            inverse="load_static",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadStatic",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics",
        guid="{2205909C-5373-450d-AE71-9D3F01B279FE}",
        attributes=(
            AttrMeta(
                "static_load_model_type",
                "staticLoadModelType",
                "StaticLoadModelKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("kp1", "kp1", "float", 0, 1, "primitive"),
            AttrMeta("kp2", "kp2", "float", 0, 1, "primitive"),
            AttrMeta("kp3", "kp3", "float", 0, 1, "primitive"),
            AttrMeta("kp4", "kp4", "float", 0, 1, "primitive"),
            AttrMeta("ep1", "ep1", "float", 0, 1, "primitive"),
            AttrMeta("ep2", "ep2", "float", 0, 1, "primitive"),
            AttrMeta("ep3", "ep3", "float", 0, 1, "primitive"),
            AttrMeta("kpf", "kpf", "float", 0, 1, "primitive"),
            AttrMeta("kq1", "kq1", "float", 0, 1, "primitive"),
            AttrMeta("kq2", "kq2", "float", 0, 1, "primitive"),
            AttrMeta("kq3", "kq3", "float", 0, 1, "primitive"),
            AttrMeta("kq4", "kq4", "float", 0, 1, "primitive"),
            AttrMeta("eq1", "eq1", "float", 0, 1, "primitive"),
            AttrMeta("eq2", "eq2", "float", 0, 1, "primitive"),
            AttrMeta("eq3", "eq3", "float", 0, 1, "primitive"),
            AttrMeta("kqf", "kqf", "float", 0, 1, "primitive"),
        ),
        ends=(load_aggregate.meta,),
    )

    def __init__(
        self,
        *,
        static_load_model_type: StaticLoadModelKind | None = None,
        kp1: float | None = None,
        kp2: float | None = None,
        kp3: float | None = None,
        kp4: float | None = None,
        ep1: float | None = None,
        ep2: float | None = None,
        ep3: float | None = None,
        kpf: float | None = None,
        kq1: float | None = None,
        kq2: float | None = None,
        kq3: float | None = None,
        kq4: float | None = None,
        eq1: float | None = None,
        eq2: float | None = None,
        eq3: float | None = None,
        kqf: float | None = None,
        load_aggregate: LoadAggregate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.static_load_model_type = static_load_model_type
        self.kp1 = kp1
        self.kp2 = kp2
        self.kp3 = kp3
        self.kp4 = kp4
        self.ep1 = ep1
        self.ep2 = ep2
        self.ep3 = ep3
        self.kpf = kpf
        self.kq1 = kq1
        self.kq2 = kq2
        self.kq3 = kq3
        self.kq4 = kq4
        self.eq1 = eq1
        self.eq2 = eq2
        self.eq3 = eq3
        self.kqf = kqf
        if load_aggregate is not None:
            self.load_aggregate = load_aggregate
