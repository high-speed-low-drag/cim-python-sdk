"""CIM class DCConverterUnit (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.dc.dc_equipment_container import DCEquipmentContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.substation import Substation
    from cim_python_sdk.model.iec61970.base.dc.dc_converter_operating_mode_kind import (
        DCConverterOperatingModeKind,
    )


class DCConverterUnit(DCEquipmentContainer):
    """Indivisible operative unit comprising all equipment between the point of common coupling
    on the AC side and the point of common coupling – DC side, essentially one or more
    converters, together with one or more converter transformers, converter control
    equipment, essential protective and switching devices and auxiliaries, if any, used for
    conversion."""

    __slots__ = ("_substation", "operation_mode")

    operation_mode: DCConverterOperatingModeKind | None

    substation: One[Substation] = One(
        EndMeta(
            name="substation",
            cim_role="Substation",
            target="cim_python_sdk.model.iec61970.base.core.substation:Substation",
            many=False,
            lower=0,
            upper=1,
            inverse="dc_converter_unit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCConverterUnit",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{C9C13B9F-32C9-48cc-B9A5-1019739572D7}",
        attributes=(
            AttrMeta(
                "operation_mode",
                "operationMode",
                "DCConverterOperatingModeKind",
                0,
                1,
                "enumeration",
            ),
        ),
        ends=(substation.meta,),
    )

    def __init__(
        self,
        *,
        operation_mode: DCConverterOperatingModeKind | None = None,
        substation: Substation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.operation_mode = operation_mode
        if substation is not None:
            self.substation = substation
