"""CIM class RemotePoint (TC57CIM/IEC61970/Base/SCADA). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.scada.remote_unit import RemoteUnit


class RemotePoint(IdentifiedObject):
    """For an RTU, remote points correspond to telemetered values or control outputs. Other
    units (e.g. control centres) usually also contain calculated values."""

    __slots__ = ("_remote_unit",)

    remote_unit: One[RemoteUnit] = One(
        EndMeta(
            name="remote_unit",
            cim_role="RemoteUnit",
            target="cim_python_sdk.model.iec61970.base.scada.remote_unit:RemoteUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="remote_points",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RemotePoint",
        package="TC57CIM/IEC61970/Base/SCADA",
        guid="{4628091D-2315-459f-9E5F-2CFECA557F1C}",
        ends=(remote_unit.meta,),
    )

    def __init__(
        self,
        *,
        remote_unit: RemoteUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if remote_unit is not None:
            self.remote_unit = remote_unit
