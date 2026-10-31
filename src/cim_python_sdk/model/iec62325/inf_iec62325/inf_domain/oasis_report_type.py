"""CIM enumeration OASISReportType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OASISReportType(CimEnum):
    """CIM enumeration OASISReportType."""

    AS_DA_RESULT = "AS_DA_RESULT"
    AS_OP_RSRV = "AS_OP_RSRV"
    AS_REQ = "AS_REQ"
    AS_RTM_RESULT = "AS_RTM_RESULT"
    BIDS_PUBLIC = "BIDS_PUBLIC"
    CMMT_RA_MLC = "CMMT_RA_MLC"
    CMMT_RMR = "CMMT_RMR"
    CRR_CLEARING = "CRR_CLEARING"
    CRR_INVENTORY = "CRR_INVENTORY"
    ENE_EA = "ENE_EA"
    ENE_HASP = "ENE_HASP"
    ENE_IFM = "ENE_IFM"
    ENE_MPM = "ENE_MPM"
    ENE_RTM = "ENE_RTM"
    ENE_RUC = "ENE_RUC"
    LOSS_DA_HASP = "LOSS_DA_HASP"
    LOSS_RTM = "LOSS_RTM"
    PRC_AS = "PRC_AS"
    PRC_FUEL = "PRC_FUEL"
    PRC_HRLY_LMP = "PRC_HRLY_LMP"
    PRC_INTVL_LMP = "PRC_INTVL_LMP"
    PRC_CNSTR = "PRC_CNSTR"
    SLD_FCST = "SLD_FCST"
    SLD_FCST_PEAK = "SLD_FCST_PEAK"
    SLD_MKTS = "SLD_MKTS"
    TRNS_ATC = "TRNS_ATC"
    TRNS_OUTAGE = "TRNS_OUTAGE"
    TRNS_USAGE = "TRNS_USAGE"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OASISReportType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{4454664E-4E23-4773-B5CB-216BDB61BD47}",
            kind="enumeration",
        )
    )
