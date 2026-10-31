"""CIM class ACDCConverterDCTerminal (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.dc.dc_base_terminal import DCBaseTerminal

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.dc.acdc_converter import ACDCConverter
    from cim_python_sdk.model.iec61970.base.dc.dc_polarity_kind import DCPolarityKind


class ACDCConverterDCTerminal(DCBaseTerminal):
    """A DC electrical connection point at the AC/DC converter. The AC/DC converter is
    electrically connected also to the AC side. The AC connection is inherited from the AC
    conducting equipment in the same way as any other AC equipment. The AC/DC converter DC
    terminal is separate from generic DC terminal to restrict the connection with the AC
    side to AC/DC converter and so that no other DC conducting equipment can be connected to
    the AC side."""

    __slots__ = ("_dc_conducting_equipment", "polarity")

    polarity: DCPolarityKind | None

    dc_conducting_equipment: One[ACDCConverter] = One(
        EndMeta(
            name="dc_conducting_equipment",
            cim_role="DCConductingEquipment",
            target="cim_python_sdk.model.iec61970.base.dc.acdc_converter:ACDCConverter",
            many=False,
            lower=1,
            upper=1,
            inverse="dc_terminals",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ACDCConverterDCTerminal",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{58B81D5E-10FF-4e21-A564-304AD5297BAE}",
        attributes=(AttrMeta("polarity", "polarity", "DCPolarityKind", 0, 1, "enumeration"),),
        ends=(dc_conducting_equipment.meta,),
    )

    def __init__(
        self,
        *,
        polarity: DCPolarityKind | None = None,
        dc_conducting_equipment: ACDCConverter | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.polarity = polarity
        if dc_conducting_equipment is not None:
            self.dc_conducting_equipment = dc_conducting_equipment
