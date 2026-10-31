"""CIM class Procedure (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet
    from cim_python_sdk.model.iec61968.assets.procedure_kind import ProcedureKind
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit import CompatibleUnit
    from cim_python_sdk.model.iec61970.base.meas.limit import Limit
    from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement


class Procedure(Document):
    """Documented procedure for various types of work or work tasks on assets."""

    __slots__ = (
        "_assets",
        "_compatible_units",
        "_limits",
        "_measurements",
        "_procedure_data_sets",
        "instruction",
        "kind",
        "sequence_number",
    )

    kind: ProcedureKind | None
    sequence_number: str | None
    instruction: str | None

    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="procedures",
            aggregation="none",
        )
    )
    compatible_units: Many[CompatibleUnit] = Many(
        EndMeta(
            name="compatible_units",
            cim_role="CompatibleUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit:CompatibleUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="procedures",
            aggregation="none",
        )
    )
    limits: Many[Limit] = Many(
        EndMeta(
            name="limits",
            cim_role="Limits",
            target="cim_python_sdk.model.iec61970.base.meas.limit:Limit",
            many=True,
            lower=0,
            upper=None,
            inverse="procedures",
            aggregation="none",
        )
    )
    procedure_data_sets: Many[ProcedureDataSet] = Many(
        EndMeta(
            name="procedure_data_sets",
            cim_role="ProcedureDataSets",
            target="cim_python_sdk.model.iec61968.assets.procedure_data_set:ProcedureDataSet",
            many=True,
            lower=0,
            upper=None,
            inverse="procedure",
            aggregation="none",
        )
    )
    measurements: Many[Measurement] = Many(
        EndMeta(
            name="measurements",
            cim_role="Measurements",
            target="cim_python_sdk.model.iec61970.base.meas.measurement:Measurement",
            many=True,
            lower=0,
            upper=None,
            inverse="procedures",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Procedure",
        package="TC57CIM/IEC61968/Assets",
        guid="{AFA1E7DF-53AE-4831-A007-89E83E579270}",
        attributes=(
            AttrMeta("kind", "kind", "ProcedureKind", 0, 1, "enumeration"),
            AttrMeta("sequence_number", "sequenceNumber", "str", 0, 1, "primitive"),
            AttrMeta("instruction", "instruction", "str", 0, 1, "primitive"),
        ),
        ends=(
            assets.meta,
            compatible_units.meta,
            limits.meta,
            procedure_data_sets.meta,
            measurements.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: ProcedureKind | None = None,
        sequence_number: str | None = None,
        instruction: str | None = None,
        assets: Iterable[Asset] | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        limits: Iterable[Limit] | None = None,
        procedure_data_sets: Iterable[ProcedureDataSet] | None = None,
        measurements: Iterable[Measurement] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.sequence_number = sequence_number
        self.instruction = instruction
        if assets is not None:
            Procedure.assets.extend(self, assets)
        if compatible_units is not None:
            Procedure.compatible_units.extend(self, compatible_units)
        if limits is not None:
            Procedure.limits.extend(self, limits)
        if procedure_data_sets is not None:
            Procedure.procedure_data_sets.extend(self, procedure_data_sets)
        if measurements is not None:
            Procedure.measurements.extend(self, measurements)

    def add_asset(self, asset: Asset) -> Self:
        return Procedure.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return Procedure.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return Procedure.assets.clear(self)

    def num_asset(self) -> int:
        return Procedure.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return Procedure.assets.get_by_mrid(self, mrid)

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return Procedure.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return Procedure.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return Procedure.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return Procedure.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return Procedure.compatible_units.get_by_mrid(self, mrid)

    def add_limit(self, limit: Limit) -> Self:
        return Procedure.limits.add(self, limit)

    def remove_limit(self, limit: Limit) -> Self:
        return Procedure.limits.remove(self, limit)

    def clear_limits(self) -> Self:
        return Procedure.limits.clear(self)

    def num_limit(self) -> int:
        return Procedure.limits.count(self)

    def get_limit_by_mrid(self, mrid: str) -> Limit | None:
        return Procedure.limits.get_by_mrid(self, mrid)

    def add_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return Procedure.procedure_data_sets.add(self, procedure_data_set)

    def remove_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return Procedure.procedure_data_sets.remove(self, procedure_data_set)

    def clear_procedure_data_sets(self) -> Self:
        return Procedure.procedure_data_sets.clear(self)

    def num_procedure_data_set(self) -> int:
        return Procedure.procedure_data_sets.count(self)

    def get_procedure_data_set_by_mrid(self, mrid: str) -> ProcedureDataSet | None:
        return Procedure.procedure_data_sets.get_by_mrid(self, mrid)

    def add_measurement(self, measurement: Measurement) -> Self:
        return Procedure.measurements.add(self, measurement)

    def remove_measurement(self, measurement: Measurement) -> Self:
        return Procedure.measurements.remove(self, measurement)

    def clear_measurements(self) -> Self:
        return Procedure.measurements.clear(self)

    def num_measurement(self) -> int:
        return Procedure.measurements.count(self)

    def get_measurement_by_mrid(self, mrid: str) -> Measurement | None:
        return Procedure.measurements.get_by_mrid(self, mrid)
