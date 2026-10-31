"""CIM class TroubleSymptoms (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.customers.trouble_symptoms_extent_kind import (
        TroubleSymptomsExtentKind,
    )
    from cim_python_sdk.model.iec61968.customers.trouble_symptoms_light_kind import (
        TroubleSymptomsLightKind,
    )
    from cim_python_sdk.model.iec61968.customers.trouble_symptoms_pole_kind import (
        TroubleSymptomsPoleKind,
    )
    from cim_python_sdk.model.iec61968.customers.trouble_symptoms_transformer_kind import (
        TroubleSymptomsTransformerKind,
    )
    from cim_python_sdk.model.iec61968.customers.trouble_symptoms_tree_kind import (
        TroubleSymptomsTree_Kind,
    )
    from cim_python_sdk.model.iec61968.customers.trouble_symptoms_wire_kind import (
        TroubleSymptomsWireKind,
    )
    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket


class TroubleSymptoms(CimObject):
    """Trouble symptoms reported by person reporting the trouble. The symptoms provide clues to
    utility personnel analyzing the ticket to help identify the root cause of the problem."""

    __slots__ = (
        "_trouble_ticket",
        "trouble_symptoms_extent",
        "trouble_symptoms_extent_other",
        "trouble_symptoms_light",
        "trouble_symptoms_light_other",
        "trouble_symptoms_pole",
        "trouble_symptoms_pole_other",
        "trouble_symptoms_transformer",
        "trouble_symptoms_transformer_other",
        "trouble_symptoms_tree",
        "trouble_symptoms_tree_other",
        "trouble_symptoms_wire",
        "trouble_symptoms_wire_other",
    )

    trouble_symptoms_extent: TroubleSymptomsExtentKind | None
    trouble_symptoms_extent_other: str | None
    trouble_symptoms_light: TroubleSymptomsLightKind | None
    trouble_symptoms_light_other: str | None
    trouble_symptoms_pole: TroubleSymptomsPoleKind | None
    trouble_symptoms_pole_other: str | None
    trouble_symptoms_transformer: TroubleSymptomsTransformerKind | None
    trouble_symptoms_transformer_other: str | None
    trouble_symptoms_tree: TroubleSymptomsTree_Kind | None
    trouble_symptoms_tree_other: str | None
    trouble_symptoms_wire: TroubleSymptomsWireKind | None
    trouble_symptoms_wire_other: str | None

    trouble_ticket: One[TroubleTicket] = One(
        EndMeta(
            name="trouble_ticket",
            cim_role="TroubleTicket",
            target="cim_python_sdk.model.iec61968.customers.trouble_ticket:TroubleTicket",
            many=False,
            lower=0,
            upper=1,
            inverse="trouble_symptoms",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TroubleSymptoms",
        package="TC57CIM/IEC61968/Customers",
        guid="{7F639177-DA42-4bc5-943B-71243289A34A}",
        attributes=(
            AttrMeta(
                "trouble_symptoms_extent",
                "troubleSymptomsExtent",
                "TroubleSymptomsExtentKind",
                1,
                1,
                "enumeration",
            ),
            AttrMeta(
                "trouble_symptoms_extent_other",
                "troubleSymptomsExtentOther",
                "str",
                1,
                1,
                "primitive",
            ),
            AttrMeta(
                "trouble_symptoms_light",
                "troubleSymptomsLight",
                "TroubleSymptomsLightKind",
                1,
                1,
                "enumeration",
            ),
            AttrMeta(
                "trouble_symptoms_light_other",
                "troubleSymptomsLightOther",
                "str",
                1,
                1,
                "primitive",
            ),
            AttrMeta(
                "trouble_symptoms_pole",
                "troubleSymptomsPole",
                "TroubleSymptomsPoleKind",
                1,
                1,
                "enumeration",
            ),
            AttrMeta(
                "trouble_symptoms_pole_other", "troubleSymptomsPoleOther", "str", 1, 1, "primitive"
            ),
            AttrMeta(
                "trouble_symptoms_transformer",
                "troubleSymptomsTransformer",
                "TroubleSymptomsTransformerKind",
                1,
                1,
                "enumeration",
            ),
            AttrMeta(
                "trouble_symptoms_transformer_other",
                "troubleSymptomsTransformerOther",
                "str",
                1,
                1,
                "primitive",
            ),
            AttrMeta(
                "trouble_symptoms_tree",
                "troubleSymptomsTree",
                "TroubleSymptomsTree Kind",
                1,
                1,
                "enumeration",
            ),
            AttrMeta(
                "trouble_symptoms_tree_other", "troubleSymptomsTreeOther", "str", 1, 1, "primitive"
            ),
            AttrMeta(
                "trouble_symptoms_wire",
                "troubleSymptomsWire",
                "TroubleSymptomsWireKind",
                1,
                1,
                "enumeration",
            ),
            AttrMeta(
                "trouble_symptoms_wire_other", "troubleSymptomsWireOther", "str", 1, 1, "primitive"
            ),
        ),
        ends=(trouble_ticket.meta,),
    )

    def __init__(
        self,
        *,
        trouble_symptoms_extent: TroubleSymptomsExtentKind | None = None,
        trouble_symptoms_extent_other: str | None = None,
        trouble_symptoms_light: TroubleSymptomsLightKind | None = None,
        trouble_symptoms_light_other: str | None = None,
        trouble_symptoms_pole: TroubleSymptomsPoleKind | None = None,
        trouble_symptoms_pole_other: str | None = None,
        trouble_symptoms_transformer: TroubleSymptomsTransformerKind | None = None,
        trouble_symptoms_transformer_other: str | None = None,
        trouble_symptoms_tree: TroubleSymptomsTree_Kind | None = None,
        trouble_symptoms_tree_other: str | None = None,
        trouble_symptoms_wire: TroubleSymptomsWireKind | None = None,
        trouble_symptoms_wire_other: str | None = None,
        trouble_ticket: TroubleTicket | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.trouble_symptoms_extent = trouble_symptoms_extent
        self.trouble_symptoms_extent_other = trouble_symptoms_extent_other
        self.trouble_symptoms_light = trouble_symptoms_light
        self.trouble_symptoms_light_other = trouble_symptoms_light_other
        self.trouble_symptoms_pole = trouble_symptoms_pole
        self.trouble_symptoms_pole_other = trouble_symptoms_pole_other
        self.trouble_symptoms_transformer = trouble_symptoms_transformer
        self.trouble_symptoms_transformer_other = trouble_symptoms_transformer_other
        self.trouble_symptoms_tree = trouble_symptoms_tree
        self.trouble_symptoms_tree_other = trouble_symptoms_tree_other
        self.trouble_symptoms_wire = trouble_symptoms_wire
        self.trouble_symptoms_wire_other = trouble_symptoms_wire_other
        if trouble_ticket is not None:
            self.trouble_ticket = trouble_ticket
