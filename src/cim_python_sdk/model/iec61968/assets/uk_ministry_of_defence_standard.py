"""CIM compound UKMinistryOfDefenceStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.assets.uk_ministry_of_defence_standard_edition_kind import (
        UKMinistryOfDefenceStandardEditionKind,
    )
    from cim_python_sdk.model.iec61968.assets.uk_ministryof_defence_standard_kind import (
        UKMinistryofDefenceStandardKind,
    )


class UKMinistryOfDefenceStandard(CimCompound):
    """Standard published by United Kingdom Ministry of Defence."""

    __slots__ = ("standard_edition", "standard_number")

    standard_number: UKMinistryofDefenceStandardKind | None
    standard_edition: UKMinistryOfDefenceStandardEditionKind | None

    _cim_meta = ClassMeta(
        cim_name="UKMinistryOfDefenceStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{AAE5D3FA-5C3A-4740-8495-D6E351A88263}",
        kind="compound",
        attributes=(
            AttrMeta(
                "standard_number",
                "standardNumber",
                "UKMinistryofDefenceStandardKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "standard_edition",
                "standardEdition",
                "UKMinistryOfDefenceStandardEditionKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )
