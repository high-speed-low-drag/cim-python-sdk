"""CIM class AlertTypeList (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.environmental.environmental_alert import EnvironmentalAlert
    from cim_python_sdk.model.iec62325.environmental.environmental_data_authority import (
        EnvironmentalDataAuthority,
    )


class AlertTypeList(IdentifiedObject):
    """A named list of alert types.

    Note: the name of the list is reflected in the .name attribute (inherited from
    IdentifiedObject)."""

    __slots__ = ("_environmental_alert", "_environmental_data_authority", "version")

    version: str | None

    environmental_data_authority: One[EnvironmentalDataAuthority] = One(
        EndMeta(
            name="environmental_data_authority",
            cim_role="EnvironmentalDataAuthority",
            target="cim_python_sdk.model.iec62325.environmental.environmental_data_authority:EnvironmentalDataAuthority",
            many=False,
            lower=0,
            upper=1,
            inverse="alert_type_list",
            aggregation="none",
        )
    )
    environmental_alert: Many[EnvironmentalAlert] = Many(
        EndMeta(
            name="environmental_alert",
            cim_role="EnvironmentalAlert",
            target="cim_python_sdk.model.iec62325.environmental.environmental_alert:EnvironmentalAlert",
            many=True,
            lower=0,
            upper=None,
            inverse="alert_type_list",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AlertTypeList",
        package="TC57CIM/IEC62325/Environmental",
        guid="{2A1D60DD-5EE2-4c5d-9C38-3B2A84660EF8}",
        attributes=(AttrMeta("version", "version", "str", 0, 1, "primitive"),),
        ends=(
            environmental_data_authority.meta,
            environmental_alert.meta,
        ),
    )

    def __init__(
        self,
        *,
        version: str | None = None,
        environmental_data_authority: EnvironmentalDataAuthority | None = None,
        environmental_alert: Iterable[EnvironmentalAlert] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.version = version
        if environmental_data_authority is not None:
            self.environmental_data_authority = environmental_data_authority
        if environmental_alert is not None:
            AlertTypeList.environmental_alert.extend(self, environmental_alert)

    def add_environmental_alert(self, environmental_alert: EnvironmentalAlert) -> Self:
        return AlertTypeList.environmental_alert.add(self, environmental_alert)

    def remove_environmental_alert(self, environmental_alert: EnvironmentalAlert) -> Self:
        return AlertTypeList.environmental_alert.remove(self, environmental_alert)

    def clear_environmental_alert(self) -> Self:
        return AlertTypeList.environmental_alert.clear(self)

    def num_environmental_alert(self) -> int:
        return AlertTypeList.environmental_alert.count(self)

    def get_environmental_alert_by_mrid(self, mrid: str) -> EnvironmentalAlert | None:
        return AlertTypeList.environmental_alert.get_by_mrid(self, mrid)
