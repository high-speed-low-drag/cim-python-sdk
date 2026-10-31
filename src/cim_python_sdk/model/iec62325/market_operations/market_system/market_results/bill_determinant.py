"""CIM class BillDeterminant (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_user_attribute import (
        MktUserAttribute,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile import (
        ChargeProfile,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile_data import (
        ChargeProfileData,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_component import (
        ChargeComponent,
    )


class BillDeterminant(Document):
    """Models various charges to support billing and settlement."""

    __slots__ = (
        "_charge_components",
        "_charge_profile",
        "_charge_profile_data",
        "_mkt_user_attribute",
        "calculation_level",
        "config_version",
        "delete_status",
        "effective_date",
        "exception",
        "factor",
        "frequency",
        "number_interval",
        "offset",
        "precision_level",
        "primary_yn",
        "reference_flag",
        "reportable",
        "round_off",
        "source",
        "termination_date",
        "unit_of_measure",
    )

    calculation_level: str | None
    config_version: str | None
    delete_status: str | None
    effective_date: _dt.datetime | None
    exception: str | None
    factor: str | None
    frequency: str | None
    number_interval: int | None
    offset: str | None
    precision_level: str | None
    primary_yn: str | None
    reference_flag: str | None
    reportable: str | None
    round_off: str | None
    source: str | None
    termination_date: _dt.datetime | None
    unit_of_measure: str | None

    charge_profile: One[ChargeProfile] = One(
        EndMeta(
            name="charge_profile",
            cim_role="ChargeProfile",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile:ChargeProfile",
            many=False,
            lower=0,
            upper=1,
            inverse="bill_determinant",
            aggregation="none",
        )
    )
    mkt_user_attribute: Many[MktUserAttribute] = Many(
        EndMeta(
            name="mkt_user_attribute",
            cim_role="MktUserAttribute",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_user_attribute:MktUserAttribute",
            many=True,
            lower=0,
            upper=None,
            inverse="bill_determinant",
            aggregation="none",
        )
    )
    charge_components: Many[ChargeComponent] = Many(
        EndMeta(
            name="charge_components",
            cim_role="ChargeComponents",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_component:ChargeComponent",
            many=True,
            lower=0,
            upper=None,
            inverse="bill_determinants",
            aggregation="none",
        )
    )
    charge_profile_data: Many[ChargeProfileData] = Many(
        EndMeta(
            name="charge_profile_data",
            cim_role="ChargeProfileData",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile_data:ChargeProfileData",
            many=True,
            lower=0,
            upper=None,
            inverse="bill_determinant",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BillDeterminant",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{A99EBB39-5FB7-40c7-B742-26AC3A6B11F3}",
        attributes=(
            AttrMeta("calculation_level", "calculationLevel", "str", 0, 1, "primitive"),
            AttrMeta("config_version", "configVersion", "str", 0, 1, "primitive"),
            AttrMeta("delete_status", "deleteStatus", "str", 0, 1, "primitive"),
            AttrMeta("effective_date", "effectiveDate", "datetime", 0, 1, "primitive"),
            AttrMeta("exception", "exception", "str", 0, 1, "primitive"),
            AttrMeta("factor", "factor", "str", 0, 1, "primitive"),
            AttrMeta("frequency", "frequency", "str", 0, 1, "primitive"),
            AttrMeta("number_interval", "numberInterval", "int", 0, 1, "primitive"),
            AttrMeta("offset", "offset", "str", 0, 1, "primitive"),
            AttrMeta("precision_level", "precisionLevel", "str", 0, 1, "primitive"),
            AttrMeta("primary_yn", "primaryYN", "str", 0, 1, "primitive"),
            AttrMeta("reference_flag", "referenceFlag", "str", 0, 1, "primitive"),
            AttrMeta("reportable", "reportable", "str", 0, 1, "primitive"),
            AttrMeta("round_off", "roundOff", "str", 0, 1, "primitive"),
            AttrMeta("source", "source", "str", 0, 1, "primitive"),
            AttrMeta("termination_date", "terminationDate", "datetime", 0, 1, "primitive"),
            AttrMeta("unit_of_measure", "unitOfMeasure", "str", 0, 1, "primitive"),
        ),
        ends=(
            charge_profile.meta,
            mkt_user_attribute.meta,
            charge_components.meta,
            charge_profile_data.meta,
        ),
    )

    def __init__(
        self,
        *,
        calculation_level: str | None = None,
        config_version: str | None = None,
        delete_status: str | None = None,
        effective_date: _dt.datetime | None = None,
        exception: str | None = None,
        factor: str | None = None,
        frequency: str | None = None,
        number_interval: int | None = None,
        offset: str | None = None,
        precision_level: str | None = None,
        primary_yn: str | None = None,
        reference_flag: str | None = None,
        reportable: str | None = None,
        round_off: str | None = None,
        source: str | None = None,
        termination_date: _dt.datetime | None = None,
        unit_of_measure: str | None = None,
        charge_profile: ChargeProfile | None = None,
        mkt_user_attribute: Iterable[MktUserAttribute] | None = None,
        charge_components: Iterable[ChargeComponent] | None = None,
        charge_profile_data: Iterable[ChargeProfileData] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.calculation_level = calculation_level
        self.config_version = config_version
        self.delete_status = delete_status
        self.effective_date = effective_date
        self.exception = exception
        self.factor = factor
        self.frequency = frequency
        self.number_interval = number_interval
        self.offset = offset
        self.precision_level = precision_level
        self.primary_yn = primary_yn
        self.reference_flag = reference_flag
        self.reportable = reportable
        self.round_off = round_off
        self.source = source
        self.termination_date = termination_date
        self.unit_of_measure = unit_of_measure
        if charge_profile is not None:
            self.charge_profile = charge_profile
        if mkt_user_attribute is not None:
            BillDeterminant.mkt_user_attribute.extend(self, mkt_user_attribute)
        if charge_components is not None:
            BillDeterminant.charge_components.extend(self, charge_components)
        if charge_profile_data is not None:
            BillDeterminant.charge_profile_data.extend(self, charge_profile_data)

    def add_mkt_user_attribute(self, mkt_user_attribute: MktUserAttribute) -> Self:
        return BillDeterminant.mkt_user_attribute.add(self, mkt_user_attribute)

    def remove_mkt_user_attribute(self, mkt_user_attribute: MktUserAttribute) -> Self:
        return BillDeterminant.mkt_user_attribute.remove(self, mkt_user_attribute)

    def clear_mkt_user_attribute(self) -> Self:
        return BillDeterminant.mkt_user_attribute.clear(self)

    def num_mkt_user_attribute(self) -> int:
        return BillDeterminant.mkt_user_attribute.count(self)

    def add_charge_component(self, charge_component: ChargeComponent) -> Self:
        return BillDeterminant.charge_components.add(self, charge_component)

    def remove_charge_component(self, charge_component: ChargeComponent) -> Self:
        return BillDeterminant.charge_components.remove(self, charge_component)

    def clear_charge_components(self) -> Self:
        return BillDeterminant.charge_components.clear(self)

    def num_charge_component(self) -> int:
        return BillDeterminant.charge_components.count(self)

    def get_charge_component_by_mrid(self, mrid: str) -> ChargeComponent | None:
        return BillDeterminant.charge_components.get_by_mrid(self, mrid)

    def add_charge_profile_data(self, charge_profile_data: ChargeProfileData) -> Self:
        return BillDeterminant.charge_profile_data.add(self, charge_profile_data)

    def remove_charge_profile_data(self, charge_profile_data: ChargeProfileData) -> Self:
        return BillDeterminant.charge_profile_data.remove(self, charge_profile_data)

    def clear_charge_profile_data(self) -> Self:
        return BillDeterminant.charge_profile_data.clear(self)

    def num_charge_profile_data(self) -> int:
        return BillDeterminant.charge_profile_data.count(self)
