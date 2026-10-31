"""CIM enumeration OASISMasterType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OASISMasterType(CimEnum):
    """CIM enumeration OASISMasterType."""

    ATL_PNODE = "ATL_PNODE"
    ATL_APNODE = "ATL_APNODE"
    ATL_LDF = "ATL_LDF"
    ATL_LAP = "ATL_LAP"
    ATL_RESOURCE = "ATL_RESOURCE"
    ATL_HUB = "ATL_HUB"
    ATL_PNODE_MAP = "ATL_PNODE_MAP"
    ATL_AS_REGION = "ATL_AS_REGION"
    ATL_AS_REGION_MAP = "ATL_AS_REGION_MAP"
    ATL_RUC_ZONE = "ATL_RUC_ZONE"
    ATL_RUC_ZONE_MAP = "ATL_RUC_ZONE_MAP"
    ATL_TAC_AREA = "ATL_TAC_AREA"
    ATL_TAC_AREA_MAP = "ATL_TAC_AREA_MAP"
    ATL_TIEPOINT = "ATL_TIEPOINT"
    ATL_TI = "ATL_TI"
    ATL_PUB = "ATL_PUB"
    ATL_STAT = "ATL_STAT"
    ATL_PUB_SCHED = "ATL_PUB_SCHED"
    ATL_XREF = "ATL_XREF"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OASISMasterType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{6FF8B250-E97A-4948-878F-9BAE9ADF2F0E}",
            kind="enumeration",
        )
    )
