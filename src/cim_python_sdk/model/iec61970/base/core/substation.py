"""CIM class Substation (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.equipment_container import EquipmentContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.bay import Bay
    from cim_python_sdk.model.iec61970.base.core.feeder import Feeder
    from cim_python_sdk.model.iec61970.base.core.sub_geographical_region import (
        SubGeographicalRegion,
    )
    from cim_python_sdk.model.iec61970.base.core.voltage_level import VoltageLevel
    from cim_python_sdk.model.iec61970.base.dc.dc_converter_unit import DCConverterUnit


class Substation(EquipmentContainer):
    """A collection of equipment for purposes other than generation or utilization, through
    which electric energy in bulk is passed for the purposes of switching or modifying its
    characteristics."""

    __slots__ = (
        "_bays",
        "_dc_converter_unit",
        "_naming_feeder",
        "_normal_energized_feeder",
        "_normal_energizing_feeder",
        "_region",
        "_voltage_levels",
    )

    voltage_levels: Many[VoltageLevel] = Many(
        EndMeta(
            name="voltage_levels",
            cim_role="VoltageLevels",
            target="cim_python_sdk.model.iec61970.base.core.voltage_level:VoltageLevel",
            many=True,
            lower=0,
            upper=None,
            inverse="substation",
            aggregation="shared",
        )
    )
    normal_energizing_feeder: Many[Feeder] = Many(
        EndMeta(
            name="normal_energizing_feeder",
            cim_role="NormalEnergizingFeeder",
            target="cim_python_sdk.model.iec61970.base.core.feeder:Feeder",
            many=True,
            lower=0,
            upper=None,
            inverse="normal_energized_substation",
            aggregation="none",
        )
    )
    dc_converter_unit: Many[DCConverterUnit] = Many(
        EndMeta(
            name="dc_converter_unit",
            cim_role="DCConverterUnit",
            target="cim_python_sdk.model.iec61970.base.dc.dc_converter_unit:DCConverterUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="substation",
            aggregation="shared",
        )
    )
    bays: Many[Bay] = Many(
        EndMeta(
            name="bays",
            cim_role="Bays",
            target="cim_python_sdk.model.iec61970.base.core.bay:Bay",
            many=True,
            lower=0,
            upper=None,
            inverse="substation",
            aggregation="shared",
        )
    )
    region: One[SubGeographicalRegion] = One(
        EndMeta(
            name="region",
            cim_role="Region",
            target="cim_python_sdk.model.iec61970.base.core.sub_geographical_region:SubGeographicalRegion",
            many=False,
            lower=0,
            upper=1,
            inverse="substations",
            aggregation="none",
        )
    )
    naming_feeder: One[Feeder] = One(
        EndMeta(
            name="naming_feeder",
            cim_role="NamingFeeder",
            target="cim_python_sdk.model.iec61970.base.core.feeder:Feeder",
            many=False,
            lower=0,
            upper=1,
            inverse="naming_secondary_substation",
            aggregation="none",
        )
    )
    normal_energized_feeder: Many[Feeder] = Many(
        EndMeta(
            name="normal_energized_feeder",
            cim_role="NormalEnergizedFeeder",
            target="cim_python_sdk.model.iec61970.base.core.feeder:Feeder",
            many=True,
            lower=0,
            upper=None,
            inverse="normal_energizing_substation",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Substation",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{D8A14AC5-D17B-4d42-8F12-1B674E5D12D7}",
        ends=(
            voltage_levels.meta,
            normal_energizing_feeder.meta,
            dc_converter_unit.meta,
            bays.meta,
            region.meta,
            naming_feeder.meta,
            normal_energized_feeder.meta,
        ),
    )

    def __init__(
        self,
        *,
        voltage_levels: Iterable[VoltageLevel] | None = None,
        normal_energizing_feeder: Iterable[Feeder] | None = None,
        dc_converter_unit: Iterable[DCConverterUnit] | None = None,
        bays: Iterable[Bay] | None = None,
        region: SubGeographicalRegion | None = None,
        naming_feeder: Feeder | None = None,
        normal_energized_feeder: Iterable[Feeder] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if voltage_levels is not None:
            Substation.voltage_levels.extend(self, voltage_levels)
        if normal_energizing_feeder is not None:
            Substation.normal_energizing_feeder.extend(self, normal_energizing_feeder)
        if dc_converter_unit is not None:
            Substation.dc_converter_unit.extend(self, dc_converter_unit)
        if bays is not None:
            Substation.bays.extend(self, bays)
        if region is not None:
            self.region = region
        if naming_feeder is not None:
            self.naming_feeder = naming_feeder
        if normal_energized_feeder is not None:
            Substation.normal_energized_feeder.extend(self, normal_energized_feeder)

    def add_voltage_level(self, voltage_level: VoltageLevel) -> Self:
        return Substation.voltage_levels.add(self, voltage_level)

    def remove_voltage_level(self, voltage_level: VoltageLevel) -> Self:
        return Substation.voltage_levels.remove(self, voltage_level)

    def clear_voltage_levels(self) -> Self:
        return Substation.voltage_levels.clear(self)

    def num_voltage_level(self) -> int:
        return Substation.voltage_levels.count(self)

    def get_voltage_level_by_mrid(self, mrid: str) -> VoltageLevel | None:
        return Substation.voltage_levels.get_by_mrid(self, mrid)

    def add_normal_energizing_feeder(self, normal_energizing_feeder: Feeder) -> Self:
        return Substation.normal_energizing_feeder.add(self, normal_energizing_feeder)

    def remove_normal_energizing_feeder(self, normal_energizing_feeder: Feeder) -> Self:
        return Substation.normal_energizing_feeder.remove(self, normal_energizing_feeder)

    def clear_normal_energizing_feeder(self) -> Self:
        return Substation.normal_energizing_feeder.clear(self)

    def num_normal_energizing_feeder(self) -> int:
        return Substation.normal_energizing_feeder.count(self)

    def get_normal_energizing_feeder_by_mrid(self, mrid: str) -> Feeder | None:
        return Substation.normal_energizing_feeder.get_by_mrid(self, mrid)

    def add_dc_converter_unit(self, dc_converter_unit: DCConverterUnit) -> Self:
        return Substation.dc_converter_unit.add(self, dc_converter_unit)

    def remove_dc_converter_unit(self, dc_converter_unit: DCConverterUnit) -> Self:
        return Substation.dc_converter_unit.remove(self, dc_converter_unit)

    def clear_dc_converter_unit(self) -> Self:
        return Substation.dc_converter_unit.clear(self)

    def num_dc_converter_unit(self) -> int:
        return Substation.dc_converter_unit.count(self)

    def get_dc_converter_unit_by_mrid(self, mrid: str) -> DCConverterUnit | None:
        return Substation.dc_converter_unit.get_by_mrid(self, mrid)

    def add_bay(self, bay: Bay) -> Self:
        return Substation.bays.add(self, bay)

    def remove_bay(self, bay: Bay) -> Self:
        return Substation.bays.remove(self, bay)

    def clear_bays(self) -> Self:
        return Substation.bays.clear(self)

    def num_bay(self) -> int:
        return Substation.bays.count(self)

    def get_bay_by_mrid(self, mrid: str) -> Bay | None:
        return Substation.bays.get_by_mrid(self, mrid)

    def add_normal_energized_feeder(self, normal_energized_feeder: Feeder) -> Self:
        return Substation.normal_energized_feeder.add(self, normal_energized_feeder)

    def remove_normal_energized_feeder(self, normal_energized_feeder: Feeder) -> Self:
        return Substation.normal_energized_feeder.remove(self, normal_energized_feeder)

    def clear_normal_energized_feeder(self) -> Self:
        return Substation.normal_energized_feeder.clear(self)

    def num_normal_energized_feeder(self) -> int:
        return Substation.normal_energized_feeder.count(self)

    def get_normal_energized_feeder_by_mrid(self, mrid: str) -> Feeder | None:
        return Substation.normal_energized_feeder.get_by_mrid(self, mrid)
