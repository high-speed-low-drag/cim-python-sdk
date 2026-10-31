"""CIM class SCADAInformation (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any


class SCADAInformation(CimObject):
    """Contains information about the update from SCADA."""

    __slots__ = ("time_stamp",)

    time_stamp: _dt.datetime | None

    _cim_meta = ClassMeta(
        cim_name="SCADAInformation",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{6AF470D5-833C-4f98-A478-B123D22758FB}",
        attributes=(AttrMeta("time_stamp", "timeStamp", "datetime", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        time_stamp: _dt.datetime | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.time_stamp = time_stamp
