"""CIM class EnergyTransaction (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.curtailment_profile import (
        CurtailmentProfile,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.energy_product import (
        EnergyProduct,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.loss_profile import (
        LossProfile,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.tie_line import TieLine
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_profile import (
        EnergyProfile,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_reservation import (
        TransmissionReservation,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.energy_transaction_type import (
        EnergyTransactionType,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.energy_price_curve import (
        EnergyPriceCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class EnergyTransaction(Document):
    """Specifies the schedule for energy transfers between interchange areas that are necessary
    to satisfy the associated interchange transaction."""

    __slots__ = (
        "_curtailment_profiles",
        "_energy_price_curves",
        "_energy_product",
        "_energy_profiles",
        "_export_sub_control_area",
        "_import_sub_control_area",
        "_loss_profiles",
        "_tie_lines",
        "_transmission_reservation",
        "capacity_backed",
        "congest_charge_max",
        "delivery_point_p",
        "energy_min",
        "firm_interchange_flag",
        "pay_congestion",
        "reason",
        "receipt_point_p",
        "state",
    )

    capacity_backed: bool | None
    congest_charge_max: _decimal.Decimal | None  # Money
    delivery_point_p: float | None  # ActivePower
    energy_min: float | None  # ActivePower
    firm_interchange_flag: bool | None
    pay_congestion: bool | None
    reason: str | None
    receipt_point_p: float | None  # ActivePower
    state: EnergyTransactionType | None

    loss_profiles: Many[LossProfile] = Many(
        EndMeta(
            name="loss_profiles",
            cim_role="LossProfiles",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.loss_profile:LossProfile",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_transaction",
            aggregation="shared",
        )
    )
    import_sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="import_sub_control_area",
            cim_role="Import_SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="import_energy_transactions",
            aggregation="none",
        )
    )
    curtailment_profiles: Many[CurtailmentProfile] = Many(
        EndMeta(
            name="curtailment_profiles",
            cim_role="CurtailmentProfiles",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.curtailment_profile:CurtailmentProfile",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_transaction",
            aggregation="shared",
        )
    )
    energy_product: One[EnergyProduct] = One(
        EndMeta(
            name="energy_product",
            cim_role="EnergyProduct",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.energy_product:EnergyProduct",
            many=False,
            lower=1,
            upper=1,
            inverse="energy_transactions",
            aggregation="none",
        )
    )
    energy_price_curves: Many[EnergyPriceCurve] = Many(
        EndMeta(
            name="energy_price_curves",
            cim_role="EnergyPriceCurves",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.energy_price_curve:EnergyPriceCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_transactions",
            aggregation="none",
        )
    )
    transmission_reservation: One[TransmissionReservation] = One(
        EndMeta(
            name="transmission_reservation",
            cim_role="TransmissionReservation",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_reservation:TransmissionReservation",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_transaction",
            aggregation="none",
        )
    )
    energy_profiles: Many[EnergyProfile] = Many(
        EndMeta(
            name="energy_profiles",
            cim_role="EnergyProfiles",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_profile:EnergyProfile",
            many=True,
            lower=1,
            upper=None,
            inverse="energy_transaction",
            aggregation="shared",
        )
    )
    tie_lines: Many[TieLine] = Many(
        EndMeta(
            name="tie_lines",
            cim_role="TieLines",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.tie_line:TieLine",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_transaction",
            aggregation="none",
        )
    )
    export_sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="export_sub_control_area",
            cim_role="Export_SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="export_energy_transactions",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyTransaction",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{3AA037B3-088F-48cd-A4D1-F72BE3E8BE83}",
        attributes=(
            AttrMeta("capacity_backed", "capacityBacked", "bool", 0, 1, "primitive"),
            AttrMeta("congest_charge_max", "congestChargeMax", "Money", 0, 1, "cimdatatype"),
            AttrMeta("delivery_point_p", "deliveryPointP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("energy_min", "energyMin", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("firm_interchange_flag", "firmInterchangeFlag", "bool", 0, 1, "primitive"),
            AttrMeta("pay_congestion", "payCongestion", "bool", 0, 1, "primitive"),
            AttrMeta("reason", "reason", "str", 0, 1, "primitive"),
            AttrMeta("receipt_point_p", "receiptPointP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("state", "state", "EnergyTransactionType", 0, 1, "enumeration"),
        ),
        ends=(
            loss_profiles.meta,
            import_sub_control_area.meta,
            curtailment_profiles.meta,
            energy_product.meta,
            energy_price_curves.meta,
            transmission_reservation.meta,
            energy_profiles.meta,
            tie_lines.meta,
            export_sub_control_area.meta,
        ),
    )

    def __init__(
        self,
        *,
        capacity_backed: bool | None = None,
        congest_charge_max: _decimal.Decimal | None = None,
        delivery_point_p: float | None = None,
        energy_min: float | None = None,
        firm_interchange_flag: bool | None = None,
        pay_congestion: bool | None = None,
        reason: str | None = None,
        receipt_point_p: float | None = None,
        state: EnergyTransactionType | None = None,
        loss_profiles: Iterable[LossProfile] | None = None,
        import_sub_control_area: SubControlArea | None = None,
        curtailment_profiles: Iterable[CurtailmentProfile] | None = None,
        energy_product: EnergyProduct | None = None,
        energy_price_curves: Iterable[EnergyPriceCurve] | None = None,
        transmission_reservation: TransmissionReservation | None = None,
        energy_profiles: Iterable[EnergyProfile] | None = None,
        tie_lines: Iterable[TieLine] | None = None,
        export_sub_control_area: SubControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.capacity_backed = capacity_backed
        self.congest_charge_max = congest_charge_max
        self.delivery_point_p = delivery_point_p
        self.energy_min = energy_min
        self.firm_interchange_flag = firm_interchange_flag
        self.pay_congestion = pay_congestion
        self.reason = reason
        self.receipt_point_p = receipt_point_p
        self.state = state
        if loss_profiles is not None:
            EnergyTransaction.loss_profiles.extend(self, loss_profiles)
        if import_sub_control_area is not None:
            self.import_sub_control_area = import_sub_control_area
        if curtailment_profiles is not None:
            EnergyTransaction.curtailment_profiles.extend(self, curtailment_profiles)
        if energy_product is not None:
            self.energy_product = energy_product
        if energy_price_curves is not None:
            EnergyTransaction.energy_price_curves.extend(self, energy_price_curves)
        if transmission_reservation is not None:
            self.transmission_reservation = transmission_reservation
        if energy_profiles is not None:
            EnergyTransaction.energy_profiles.extend(self, energy_profiles)
        if tie_lines is not None:
            EnergyTransaction.tie_lines.extend(self, tie_lines)
        if export_sub_control_area is not None:
            self.export_sub_control_area = export_sub_control_area

    def add_loss_profile(self, loss_profile: LossProfile) -> Self:
        return EnergyTransaction.loss_profiles.add(self, loss_profile)

    def remove_loss_profile(self, loss_profile: LossProfile) -> Self:
        return EnergyTransaction.loss_profiles.remove(self, loss_profile)

    def clear_loss_profiles(self) -> Self:
        return EnergyTransaction.loss_profiles.clear(self)

    def num_loss_profile(self) -> int:
        return EnergyTransaction.loss_profiles.count(self)

    def get_loss_profile_by_mrid(self, mrid: str) -> LossProfile | None:
        return EnergyTransaction.loss_profiles.get_by_mrid(self, mrid)

    def add_curtailment_profile(self, curtailment_profile: CurtailmentProfile) -> Self:
        return EnergyTransaction.curtailment_profiles.add(self, curtailment_profile)

    def remove_curtailment_profile(self, curtailment_profile: CurtailmentProfile) -> Self:
        return EnergyTransaction.curtailment_profiles.remove(self, curtailment_profile)

    def clear_curtailment_profiles(self) -> Self:
        return EnergyTransaction.curtailment_profiles.clear(self)

    def num_curtailment_profile(self) -> int:
        return EnergyTransaction.curtailment_profiles.count(self)

    def get_curtailment_profile_by_mrid(self, mrid: str) -> CurtailmentProfile | None:
        return EnergyTransaction.curtailment_profiles.get_by_mrid(self, mrid)

    def add_energy_price_curve(self, energy_price_curve: EnergyPriceCurve) -> Self:
        return EnergyTransaction.energy_price_curves.add(self, energy_price_curve)

    def remove_energy_price_curve(self, energy_price_curve: EnergyPriceCurve) -> Self:
        return EnergyTransaction.energy_price_curves.remove(self, energy_price_curve)

    def clear_energy_price_curves(self) -> Self:
        return EnergyTransaction.energy_price_curves.clear(self)

    def num_energy_price_curve(self) -> int:
        return EnergyTransaction.energy_price_curves.count(self)

    def add_energy_profile(self, energy_profile: EnergyProfile) -> Self:
        return EnergyTransaction.energy_profiles.add(self, energy_profile)

    def remove_energy_profile(self, energy_profile: EnergyProfile) -> Self:
        return EnergyTransaction.energy_profiles.remove(self, energy_profile)

    def clear_energy_profiles(self) -> Self:
        return EnergyTransaction.energy_profiles.clear(self)

    def num_energy_profile(self) -> int:
        return EnergyTransaction.energy_profiles.count(self)

    def get_energy_profile_by_mrid(self, mrid: str) -> EnergyProfile | None:
        return EnergyTransaction.energy_profiles.get_by_mrid(self, mrid)

    def add_tie_line(self, tie_line: TieLine) -> Self:
        return EnergyTransaction.tie_lines.add(self, tie_line)

    def remove_tie_line(self, tie_line: TieLine) -> Self:
        return EnergyTransaction.tie_lines.remove(self, tie_line)

    def clear_tie_lines(self) -> Self:
        return EnergyTransaction.tie_lines.clear(self)

    def num_tie_line(self) -> int:
        return EnergyTransaction.tie_lines.count(self)

    def get_tie_line_by_mrid(self, mrid: str) -> TieLine | None:
        return EnergyTransaction.tie_lines.get_by_mrid(self, mrid)
