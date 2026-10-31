"""CIM class UnitInitialConditions (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )


class UnitInitialConditions(IdentifiedObject):
    """Resource status at the end of a given clearing period."""

    __slots__ = (
        "_generating_unit",
        "cum_energy",
        "cum_status_changes",
        "number_of_startups",
        "online_status",
        "resource_mw",
        "resource_status",
        "status_date",
        "time_in_status",
        "time_interval",
    )

    cum_energy: float | None  # RealEnergy
    cum_status_changes: int | None
    number_of_startups: int | None
    online_status: bool | None
    resource_mw: float | None  # ActivePower
    resource_status: int | None
    status_date: _dt.datetime | None
    time_in_status: float | None
    time_interval: _dt.datetime | None

    generating_unit: One[RegisteredGenerator] = One(
        EndMeta(
            name="generating_unit",
            cim_role="GeneratingUnit",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=False,
            lower=0,
            upper=1,
            inverse="unit_initial_conditions",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="UnitInitialConditions",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{80C061E1-02EC-485d-B2C1-D45841DB65BD}",
        attributes=(
            AttrMeta("cum_energy", "cumEnergy", "RealEnergy", 0, 1, "cimdatatype"),
            AttrMeta("cum_status_changes", "cumStatusChanges", "int", 0, 1, "primitive"),
            AttrMeta("number_of_startups", "numberOfStartups", "int", 0, 1, "primitive"),
            AttrMeta("online_status", "onlineStatus", "bool", 0, 1, "primitive"),
            AttrMeta("resource_mw", "resourceMW", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("resource_status", "resourceStatus", "int", 0, 1, "primitive"),
            AttrMeta("status_date", "statusDate", "datetime", 0, 1, "primitive"),
            AttrMeta("time_in_status", "timeInStatus", "float", 0, 1, "primitive"),
            AttrMeta("time_interval", "timeInterval", "datetime", 0, 1, "primitive"),
        ),
        ends=(generating_unit.meta,),
    )

    def __init__(
        self,
        *,
        cum_energy: float | None = None,
        cum_status_changes: int | None = None,
        number_of_startups: int | None = None,
        online_status: bool | None = None,
        resource_mw: float | None = None,
        resource_status: int | None = None,
        status_date: _dt.datetime | None = None,
        time_in_status: float | None = None,
        time_interval: _dt.datetime | None = None,
        generating_unit: RegisteredGenerator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cum_energy = cum_energy
        self.cum_status_changes = cum_status_changes
        self.number_of_startups = number_of_startups
        self.online_status = online_status
        self.resource_mw = resource_mw
        self.resource_status = resource_status
        self.status_date = status_date
        self.time_in_status = time_in_status
        self.time_interval = time_interval
        if generating_unit is not None:
            self.generating_unit = generating_unit
