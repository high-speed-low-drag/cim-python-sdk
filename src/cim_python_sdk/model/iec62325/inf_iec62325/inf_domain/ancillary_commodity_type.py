"""CIM enumeration AncillaryCommodityType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AncillaryCommodityType(CimEnum):
    """ancillary serivce types"""

    REGUP = "REGUP"
    REGDN = "REGDN"
    SPIN = "SPIN"
    NONSPIN = "NONSPIN"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AncillaryCommodityType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{87DD7832-25B0-456b-808D-8819FF7A4133}",
            kind="enumeration",
        )
    )
