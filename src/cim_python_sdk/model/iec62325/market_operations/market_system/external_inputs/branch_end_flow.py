"""CIM class BranchEndFlow (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_power_transformer import (
        MktPowerTransformer,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_ac_line_segment import (
        MktACLineSegment,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_series_compensator import (
        MktSeriesCompensator,
    )


class BranchEndFlow(CimObject):
    """Dynamic flows and ratings associated with a branch end."""

    __slots__ = (
        "_mkt_ac_line_segment_end_a_flow",
        "_mkt_ac_line_segment_end_b_flow",
        "_mkt_power_transformer_end_a_flow",
        "_mkt_power_transformer_end_b_flow",
        "_mkt_series_compensator_end_b_flow",
        "_mkt_serires_compensator_end_a_flow",
        "load_dump_rating",
        "long_term_rating",
        "m_var_flow",
        "mw_flow",
        "normal_rating",
        "short_term_rating",
    )

    mw_flow: float | None
    m_var_flow: float | None
    normal_rating: float | None
    long_term_rating: float | None
    short_term_rating: float | None
    load_dump_rating: float | None

    mkt_serires_compensator_end_a_flow: Many[MktSeriesCompensator] = Many(
        EndMeta(
            name="mkt_serires_compensator_end_a_flow",
            cim_role="MktSeriresCompensatorEndAFlow",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_series_compensator:MktSeriesCompensator",
            many=True,
            lower=0,
            upper=None,
            inverse="end_a_flow",
            aggregation="none",
        )
    )
    mkt_power_transformer_end_a_flow: Many[MktPowerTransformer] = Many(
        EndMeta(
            name="mkt_power_transformer_end_a_flow",
            cim_role="MktPowerTransformerEndAFlow",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_power_transformer:MktPowerTransformer",
            many=True,
            lower=0,
            upper=None,
            inverse="end_a_flow",
            aggregation="none",
        )
    )
    mkt_ac_line_segment_end_b_flow: Many[MktACLineSegment] = Many(
        EndMeta(
            name="mkt_ac_line_segment_end_b_flow",
            cim_role="MktACLineSegmentEndBFlow",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_ac_line_segment:MktACLineSegment",
            many=True,
            lower=0,
            upper=None,
            inverse="end_b_flow",
            aggregation="none",
        )
    )
    mkt_series_compensator_end_b_flow: Many[MktSeriesCompensator] = Many(
        EndMeta(
            name="mkt_series_compensator_end_b_flow",
            cim_role="MktSeriesCompensatorEndBFlow",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_series_compensator:MktSeriesCompensator",
            many=True,
            lower=0,
            upper=None,
            inverse="end_b_flow",
            aggregation="none",
        )
    )
    mkt_ac_line_segment_end_a_flow: Many[MktACLineSegment] = Many(
        EndMeta(
            name="mkt_ac_line_segment_end_a_flow",
            cim_role="MktACLineSegmentEndAFlow",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_ac_line_segment:MktACLineSegment",
            many=True,
            lower=0,
            upper=None,
            inverse="end_a_flow",
            aggregation="none",
        )
    )
    mkt_power_transformer_end_b_flow: Many[MktPowerTransformer] = Many(
        EndMeta(
            name="mkt_power_transformer_end_b_flow",
            cim_role="MktPowerTransformerEndBFlow",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_power_transformer:MktPowerTransformer",
            many=True,
            lower=0,
            upper=None,
            inverse="end_b_flow",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BranchEndFlow",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{34C5B4C6-E2B6-4dc5-AA4F-B1B1AAD61447}",
        attributes=(
            AttrMeta("mw_flow", "mwFlow", "float", 0, 1, "primitive"),
            AttrMeta("m_var_flow", "mVARFlow", "float", 0, 1, "primitive"),
            AttrMeta("normal_rating", "normalRating", "float", 0, 1, "primitive"),
            AttrMeta("long_term_rating", "longTermRating", "float", 0, 1, "primitive"),
            AttrMeta("short_term_rating", "shortTermRating", "float", 0, 1, "primitive"),
            AttrMeta("load_dump_rating", "loadDumpRating", "float", 0, 1, "primitive"),
        ),
        ends=(
            mkt_serires_compensator_end_a_flow.meta,
            mkt_power_transformer_end_a_flow.meta,
            mkt_ac_line_segment_end_b_flow.meta,
            mkt_series_compensator_end_b_flow.meta,
            mkt_ac_line_segment_end_a_flow.meta,
            mkt_power_transformer_end_b_flow.meta,
        ),
    )

    def __init__(
        self,
        *,
        mw_flow: float | None = None,
        m_var_flow: float | None = None,
        normal_rating: float | None = None,
        long_term_rating: float | None = None,
        short_term_rating: float | None = None,
        load_dump_rating: float | None = None,
        mkt_serires_compensator_end_a_flow: Iterable[MktSeriesCompensator] | None = None,
        mkt_power_transformer_end_a_flow: Iterable[MktPowerTransformer] | None = None,
        mkt_ac_line_segment_end_b_flow: Iterable[MktACLineSegment] | None = None,
        mkt_series_compensator_end_b_flow: Iterable[MktSeriesCompensator] | None = None,
        mkt_ac_line_segment_end_a_flow: Iterable[MktACLineSegment] | None = None,
        mkt_power_transformer_end_b_flow: Iterable[MktPowerTransformer] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mw_flow = mw_flow
        self.m_var_flow = m_var_flow
        self.normal_rating = normal_rating
        self.long_term_rating = long_term_rating
        self.short_term_rating = short_term_rating
        self.load_dump_rating = load_dump_rating
        if mkt_serires_compensator_end_a_flow is not None:
            BranchEndFlow.mkt_serires_compensator_end_a_flow.extend(
                self, mkt_serires_compensator_end_a_flow
            )
        if mkt_power_transformer_end_a_flow is not None:
            BranchEndFlow.mkt_power_transformer_end_a_flow.extend(
                self, mkt_power_transformer_end_a_flow
            )
        if mkt_ac_line_segment_end_b_flow is not None:
            BranchEndFlow.mkt_ac_line_segment_end_b_flow.extend(
                self, mkt_ac_line_segment_end_b_flow
            )
        if mkt_series_compensator_end_b_flow is not None:
            BranchEndFlow.mkt_series_compensator_end_b_flow.extend(
                self, mkt_series_compensator_end_b_flow
            )
        if mkt_ac_line_segment_end_a_flow is not None:
            BranchEndFlow.mkt_ac_line_segment_end_a_flow.extend(
                self, mkt_ac_line_segment_end_a_flow
            )
        if mkt_power_transformer_end_b_flow is not None:
            BranchEndFlow.mkt_power_transformer_end_b_flow.extend(
                self, mkt_power_transformer_end_b_flow
            )

    def add_mkt_serires_compensator_end_a_flow(
        self, mkt_serires_compensator_end_a_flow: MktSeriesCompensator
    ) -> Self:
        return BranchEndFlow.mkt_serires_compensator_end_a_flow.add(
            self, mkt_serires_compensator_end_a_flow
        )

    def remove_mkt_serires_compensator_end_a_flow(
        self, mkt_serires_compensator_end_a_flow: MktSeriesCompensator
    ) -> Self:
        return BranchEndFlow.mkt_serires_compensator_end_a_flow.remove(
            self, mkt_serires_compensator_end_a_flow
        )

    def clear_mkt_serires_compensator_end_a_flow(self) -> Self:
        return BranchEndFlow.mkt_serires_compensator_end_a_flow.clear(self)

    def num_mkt_serires_compensator_end_a_flow(self) -> int:
        return BranchEndFlow.mkt_serires_compensator_end_a_flow.count(self)

    def get_mkt_serires_compensator_end_a_flow_by_mrid(
        self, mrid: str
    ) -> MktSeriesCompensator | None:
        return BranchEndFlow.mkt_serires_compensator_end_a_flow.get_by_mrid(self, mrid)

    def add_mkt_power_transformer_end_a_flow(
        self, mkt_power_transformer_end_a_flow: MktPowerTransformer
    ) -> Self:
        return BranchEndFlow.mkt_power_transformer_end_a_flow.add(
            self, mkt_power_transformer_end_a_flow
        )

    def remove_mkt_power_transformer_end_a_flow(
        self, mkt_power_transformer_end_a_flow: MktPowerTransformer
    ) -> Self:
        return BranchEndFlow.mkt_power_transformer_end_a_flow.remove(
            self, mkt_power_transformer_end_a_flow
        )

    def clear_mkt_power_transformer_end_a_flow(self) -> Self:
        return BranchEndFlow.mkt_power_transformer_end_a_flow.clear(self)

    def num_mkt_power_transformer_end_a_flow(self) -> int:
        return BranchEndFlow.mkt_power_transformer_end_a_flow.count(self)

    def get_mkt_power_transformer_end_a_flow_by_mrid(self, mrid: str) -> MktPowerTransformer | None:
        return BranchEndFlow.mkt_power_transformer_end_a_flow.get_by_mrid(self, mrid)

    def add_mkt_ac_line_segment_end_b_flow(
        self, mkt_ac_line_segment_end_b_flow: MktACLineSegment
    ) -> Self:
        return BranchEndFlow.mkt_ac_line_segment_end_b_flow.add(
            self, mkt_ac_line_segment_end_b_flow
        )

    def remove_mkt_ac_line_segment_end_b_flow(
        self, mkt_ac_line_segment_end_b_flow: MktACLineSegment
    ) -> Self:
        return BranchEndFlow.mkt_ac_line_segment_end_b_flow.remove(
            self, mkt_ac_line_segment_end_b_flow
        )

    def clear_mkt_ac_line_segment_end_b_flow(self) -> Self:
        return BranchEndFlow.mkt_ac_line_segment_end_b_flow.clear(self)

    def num_mkt_ac_line_segment_end_b_flow(self) -> int:
        return BranchEndFlow.mkt_ac_line_segment_end_b_flow.count(self)

    def get_mkt_ac_line_segment_end_b_flow_by_mrid(self, mrid: str) -> MktACLineSegment | None:
        return BranchEndFlow.mkt_ac_line_segment_end_b_flow.get_by_mrid(self, mrid)

    def add_mkt_series_compensator_end_b_flow(
        self, mkt_series_compensator_end_b_flow: MktSeriesCompensator
    ) -> Self:
        return BranchEndFlow.mkt_series_compensator_end_b_flow.add(
            self, mkt_series_compensator_end_b_flow
        )

    def remove_mkt_series_compensator_end_b_flow(
        self, mkt_series_compensator_end_b_flow: MktSeriesCompensator
    ) -> Self:
        return BranchEndFlow.mkt_series_compensator_end_b_flow.remove(
            self, mkt_series_compensator_end_b_flow
        )

    def clear_mkt_series_compensator_end_b_flow(self) -> Self:
        return BranchEndFlow.mkt_series_compensator_end_b_flow.clear(self)

    def num_mkt_series_compensator_end_b_flow(self) -> int:
        return BranchEndFlow.mkt_series_compensator_end_b_flow.count(self)

    def get_mkt_series_compensator_end_b_flow_by_mrid(
        self, mrid: str
    ) -> MktSeriesCompensator | None:
        return BranchEndFlow.mkt_series_compensator_end_b_flow.get_by_mrid(self, mrid)

    def add_mkt_ac_line_segment_end_a_flow(
        self, mkt_ac_line_segment_end_a_flow: MktACLineSegment
    ) -> Self:
        return BranchEndFlow.mkt_ac_line_segment_end_a_flow.add(
            self, mkt_ac_line_segment_end_a_flow
        )

    def remove_mkt_ac_line_segment_end_a_flow(
        self, mkt_ac_line_segment_end_a_flow: MktACLineSegment
    ) -> Self:
        return BranchEndFlow.mkt_ac_line_segment_end_a_flow.remove(
            self, mkt_ac_line_segment_end_a_flow
        )

    def clear_mkt_ac_line_segment_end_a_flow(self) -> Self:
        return BranchEndFlow.mkt_ac_line_segment_end_a_flow.clear(self)

    def num_mkt_ac_line_segment_end_a_flow(self) -> int:
        return BranchEndFlow.mkt_ac_line_segment_end_a_flow.count(self)

    def get_mkt_ac_line_segment_end_a_flow_by_mrid(self, mrid: str) -> MktACLineSegment | None:
        return BranchEndFlow.mkt_ac_line_segment_end_a_flow.get_by_mrid(self, mrid)

    def add_mkt_power_transformer_end_b_flow(
        self, mkt_power_transformer_end_b_flow: MktPowerTransformer
    ) -> Self:
        return BranchEndFlow.mkt_power_transformer_end_b_flow.add(
            self, mkt_power_transformer_end_b_flow
        )

    def remove_mkt_power_transformer_end_b_flow(
        self, mkt_power_transformer_end_b_flow: MktPowerTransformer
    ) -> Self:
        return BranchEndFlow.mkt_power_transformer_end_b_flow.remove(
            self, mkt_power_transformer_end_b_flow
        )

    def clear_mkt_power_transformer_end_b_flow(self) -> Self:
        return BranchEndFlow.mkt_power_transformer_end_b_flow.clear(self)

    def num_mkt_power_transformer_end_b_flow(self) -> int:
        return BranchEndFlow.mkt_power_transformer_end_b_flow.count(self)

    def get_mkt_power_transformer_end_b_flow_by_mrid(self, mrid: str) -> MktPowerTransformer | None:
        return BranchEndFlow.mkt_power_transformer_end_b_flow.get_by_mrid(self, mrid)
