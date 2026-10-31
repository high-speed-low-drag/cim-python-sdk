"""CIM class VoltageLevel (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.equipment_container import EquipmentContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.base_voltage import BaseVoltage
    from cim_python_sdk.model.iec61970.base.core.bay import Bay
    from cim_python_sdk.model.iec61970.base.core.substation import Substation


class VoltageLevel(EquipmentContainer):
    """A collection of equipment at one common system voltage forming a switchgear. The
    equipment typically consists of breakers, busbars, instrumentation, control, regulation
    and protection devices as well as assemblies of all these."""

    __slots__ = ("_base_voltage", "_bays", "_substation", "high_voltage_limit", "low_voltage_limit")

    high_voltage_limit: float | None  # Voltage
    low_voltage_limit: float | None  # Voltage

    substation: One[Substation] = One(
        EndMeta(
            name="substation",
            cim_role="Substation",
            target="cim_python_sdk.model.iec61970.base.core.substation:Substation",
            many=False,
            lower=1,
            upper=1,
            inverse="voltage_levels",
            aggregation="none",
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
            inverse="voltage_level",
            aggregation="shared",
        )
    )
    base_voltage: One[BaseVoltage] = One(
        EndMeta(
            name="base_voltage",
            cim_role="BaseVoltage",
            target="cim_python_sdk.model.iec61970.base.core.base_voltage:BaseVoltage",
            many=False,
            lower=1,
            upper=1,
            inverse="voltage_level",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VoltageLevel",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{B147BAEA-7339-406b-A8C3-47F85EA0E82A}",
        attributes=(
            AttrMeta("high_voltage_limit", "highVoltageLimit", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("low_voltage_limit", "lowVoltageLimit", "Voltage", 0, 1, "cimdatatype"),
        ),
        ends=(
            substation.meta,
            bays.meta,
            base_voltage.meta,
        ),
    )

    def __init__(
        self,
        *,
        high_voltage_limit: float | None = None,
        low_voltage_limit: float | None = None,
        substation: Substation | None = None,
        bays: Iterable[Bay] | None = None,
        base_voltage: BaseVoltage | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.high_voltage_limit = high_voltage_limit
        self.low_voltage_limit = low_voltage_limit
        if substation is not None:
            self.substation = substation
        if bays is not None:
            VoltageLevel.bays.extend(self, bays)
        if base_voltage is not None:
            self.base_voltage = base_voltage

    def add_bay(self, bay: Bay) -> Self:
        return VoltageLevel.bays.add(self, bay)

    def remove_bay(self, bay: Bay) -> Self:
        return VoltageLevel.bays.remove(self, bay)

    def clear_bays(self) -> Self:
        return VoltageLevel.bays.clear(self)

    def num_bay(self) -> int:
        return VoltageLevel.bays.count(self)

    def get_bay_by_mrid(self, mrid: str) -> Bay | None:
        return VoltageLevel.bays.get_by_mrid(self, mrid)
