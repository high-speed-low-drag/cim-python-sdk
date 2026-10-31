"""CIM class GeneratingUnitDynamicValues (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.mkt_generating_unit import MktGeneratingUnit
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class GeneratingUnitDynamicValues(CimObject):
    """Optimal Power Flow or State Estimator Unit Data for Operator Training Simulator. This is
    used for RealTime, Study and Maintenance Users."""

    __slots__ = (
        "_flowgate",
        "_mkt_generating_unit",
        "loss_factor",
        "m_var",
        "maximum_mw",
        "minimum_mw",
        "mw",
        "sensitivity",
    )

    loss_factor: float | None
    maximum_mw: float | None
    minimum_mw: float | None
    m_var: float | None
    mw: float | None
    sensitivity: float | None

    mkt_generating_unit: One[MktGeneratingUnit] = One(
        EndMeta(
            name="mkt_generating_unit",
            cim_role="MktGeneratingUnit",
            target="cim_python_sdk.model.iec62325.market_common.mkt_generating_unit:MktGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="generating_unit_dynamic_values",
            aggregation="none",
        )
    )
    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=0,
            upper=1,
            inverse="generating_unit_dynamic_values",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GeneratingUnitDynamicValues",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{ED80EA56-BB67-4e02-A964-B4E6AE879FE4}",
        attributes=(
            AttrMeta("loss_factor", "lossFactor", "float", 0, 1, "primitive"),
            AttrMeta("maximum_mw", "maximumMW", "float", 0, 1, "primitive"),
            AttrMeta("minimum_mw", "minimumMW", "float", 0, 1, "primitive"),
            AttrMeta("m_var", "mVAR", "float", 0, 1, "primitive"),
            AttrMeta("mw", "mw", "float", 0, 1, "primitive"),
            AttrMeta("sensitivity", "sensitivity", "float", 0, 1, "primitive"),
        ),
        ends=(
            mkt_generating_unit.meta,
            flowgate.meta,
        ),
    )

    def __init__(
        self,
        *,
        loss_factor: float | None = None,
        maximum_mw: float | None = None,
        minimum_mw: float | None = None,
        m_var: float | None = None,
        mw: float | None = None,
        sensitivity: float | None = None,
        mkt_generating_unit: MktGeneratingUnit | None = None,
        flowgate: Flowgate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.loss_factor = loss_factor
        self.maximum_mw = maximum_mw
        self.minimum_mw = minimum_mw
        self.m_var = m_var
        self.mw = mw
        self.sensitivity = sensitivity
        if mkt_generating_unit is not None:
            self.mkt_generating_unit = mkt_generating_unit
        if flowgate is not None:
            self.flowgate = flowgate
