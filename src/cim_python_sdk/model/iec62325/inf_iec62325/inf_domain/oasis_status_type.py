"""CIM enumeration OASISStatusType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OASISStatusType(CimEnum):
    """CIM enumeration OASISStatusType."""

    Data_Transfer_Procedure_Initiated = "Data_Transfer_Procedure_Initiated"
    Valid = "Valid"
    Obsolete = "Obsolete"
    Data_Transfer_Succesful = "Data_Transfer_Succesful"
    Push_Failed = "Push_Failed"
    Forced_Termination = "Forced_Termination"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OASISStatusType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{3F8A7A13-1C10-4e7c-8363-4893A8779A7E}",
            kind="enumeration",
        )
    )
