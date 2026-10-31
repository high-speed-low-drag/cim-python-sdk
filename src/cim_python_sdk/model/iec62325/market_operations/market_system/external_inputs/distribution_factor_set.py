"""CIM class DistributionFactorSet (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.gen_distribution_factor import (
        GenDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.load_distribution_factor import (
        LoadDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.sys_load_distribution_factor import (
        SysLoadDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType


class DistributionFactorSet(CimObject):
    """A containing class that groups all the distribution factors within a market.

    This is calculated daily for DA factors and hourly for RT factors."""

    __slots__ = (
        "_gen_distribution_factor",
        "_load_distribution_factor",
        "_sys_load_distribu_factor",
        "interval_end_time",
        "interval_start_time",
        "market_type",
    )

    interval_start_time: _dt.datetime | None
    interval_end_time: _dt.datetime | None
    market_type: MarketType | None

    load_distribution_factor: Many[LoadDistributionFactor] = Many(
        EndMeta(
            name="load_distribution_factor",
            cim_role="LoadDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.load_distribution_factor:LoadDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="distribution_factor_set",
            aggregation="none",
        )
    )
    sys_load_distribu_factor: Many[SysLoadDistributionFactor] = Many(
        EndMeta(
            name="sys_load_distribu_factor",
            cim_role="SysLoadDistribuFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.sys_load_distribution_factor:SysLoadDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="distribution_factor_set",
            aggregation="none",
        )
    )
    gen_distribution_factor: Many[GenDistributionFactor] = Many(
        EndMeta(
            name="gen_distribution_factor",
            cim_role="GenDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.gen_distribution_factor:GenDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="distribution_factor_set",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DistributionFactorSet",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{1E74415F-603A-40d9-BBCC-5C768430FD5E}",
        attributes=(
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("interval_end_time", "intervalEndTime", "datetime", 0, 1, "primitive"),
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
        ),
        ends=(
            load_distribution_factor.meta,
            sys_load_distribu_factor.meta,
            gen_distribution_factor.meta,
        ),
    )

    def __init__(
        self,
        *,
        interval_start_time: _dt.datetime | None = None,
        interval_end_time: _dt.datetime | None = None,
        market_type: MarketType | None = None,
        load_distribution_factor: Iterable[LoadDistributionFactor] | None = None,
        sys_load_distribu_factor: Iterable[SysLoadDistributionFactor] | None = None,
        gen_distribution_factor: Iterable[GenDistributionFactor] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_start_time = interval_start_time
        self.interval_end_time = interval_end_time
        self.market_type = market_type
        if load_distribution_factor is not None:
            DistributionFactorSet.load_distribution_factor.extend(self, load_distribution_factor)
        if sys_load_distribu_factor is not None:
            DistributionFactorSet.sys_load_distribu_factor.extend(self, sys_load_distribu_factor)
        if gen_distribution_factor is not None:
            DistributionFactorSet.gen_distribution_factor.extend(self, gen_distribution_factor)

    def add_load_distribution_factor(
        self, load_distribution_factor: LoadDistributionFactor
    ) -> Self:
        return DistributionFactorSet.load_distribution_factor.add(self, load_distribution_factor)

    def remove_load_distribution_factor(
        self, load_distribution_factor: LoadDistributionFactor
    ) -> Self:
        return DistributionFactorSet.load_distribution_factor.remove(self, load_distribution_factor)

    def clear_load_distribution_factor(self) -> Self:
        return DistributionFactorSet.load_distribution_factor.clear(self)

    def num_load_distribution_factor(self) -> int:
        return DistributionFactorSet.load_distribution_factor.count(self)

    def add_sys_load_distribu_factor(
        self, sys_load_distribu_factor: SysLoadDistributionFactor
    ) -> Self:
        return DistributionFactorSet.sys_load_distribu_factor.add(self, sys_load_distribu_factor)

    def remove_sys_load_distribu_factor(
        self, sys_load_distribu_factor: SysLoadDistributionFactor
    ) -> Self:
        return DistributionFactorSet.sys_load_distribu_factor.remove(self, sys_load_distribu_factor)

    def clear_sys_load_distribu_factor(self) -> Self:
        return DistributionFactorSet.sys_load_distribu_factor.clear(self)

    def num_sys_load_distribu_factor(self) -> int:
        return DistributionFactorSet.sys_load_distribu_factor.count(self)

    def add_gen_distribution_factor(self, gen_distribution_factor: GenDistributionFactor) -> Self:
        return DistributionFactorSet.gen_distribution_factor.add(self, gen_distribution_factor)

    def remove_gen_distribution_factor(
        self, gen_distribution_factor: GenDistributionFactor
    ) -> Self:
        return DistributionFactorSet.gen_distribution_factor.remove(self, gen_distribution_factor)

    def clear_gen_distribution_factor(self) -> Self:
        return DistributionFactorSet.gen_distribution_factor.clear(self)

    def num_gen_distribution_factor(self) -> int:
        return DistributionFactorSet.gen_distribution_factor.count(self)
