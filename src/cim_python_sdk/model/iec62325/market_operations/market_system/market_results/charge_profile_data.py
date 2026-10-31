"""CIM class ChargeProfileData (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.bill_determinant import (
        BillDeterminant,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile import (
        ChargeProfile,
    )


class ChargeProfileData(CimObject):
    """Model of various charges associated with an energy profile to support billing and
    settlement."""

    __slots__ = ("_bill_determinant", "_charge_profile", "sequence", "time_stamp", "value")

    sequence: int | None
    time_stamp: _dt.datetime | None
    value: float | None

    bill_determinant: One[BillDeterminant] = One(
        EndMeta(
            name="bill_determinant",
            cim_role="BillDeterminant",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.bill_determinant:BillDeterminant",
            many=False,
            lower=0,
            upper=1,
            inverse="charge_profile_data",
            aggregation="none",
        )
    )
    charge_profile: One[ChargeProfile] = One(
        EndMeta(
            name="charge_profile",
            cim_role="ChargeProfile",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile:ChargeProfile",
            many=False,
            lower=0,
            upper=1,
            inverse="charge_profile_data",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ChargeProfileData",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{51D83713-9EB5-4dba-A5EF-C2307F99096A}",
        attributes=(
            AttrMeta("sequence", "sequence", "int", 0, 1, "primitive"),
            AttrMeta("time_stamp", "timeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
        ends=(
            bill_determinant.meta,
            charge_profile.meta,
        ),
    )

    def __init__(
        self,
        *,
        sequence: int | None = None,
        time_stamp: _dt.datetime | None = None,
        value: float | None = None,
        bill_determinant: BillDeterminant | None = None,
        charge_profile: ChargeProfile | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence = sequence
        self.time_stamp = time_stamp
        self.value = value
        if bill_determinant is not None:
            self.bill_determinant = bill_determinant
        if charge_profile is not None:
            self.charge_profile = charge_profile
