"""CIM enumeration OASISErrDescription (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OASISErrDescription(CimEnum):
    """CIM enumeration OASISErrDescription."""

    No_data_returned_for_the_specified_selection = "No data returned for the specified selection"
    Invalid_date_format_please_use_valid_date_format = (
        "Invalid date format, please use valid date format"
    )
    Timed_out_waiting_for_query_response = "Timed out waiting for query response"
    Data_can_be_requested_for_period_of_31_days_only = (
        "Data can be requested for period of 31 days only"
    )
    Report_name_does_not_exit_please_use_valid_report_name = (
        "Report name does not exit, please use valid report name"
    )
    Validation_exception_during_transformation_of_XML = (
        "Validation exception during transformation of XML"
    )
    Required_file_does_not_exist = "Required file does not exist"
    Out_of_memory_exception = "Out of memory exception"
    Exceptions_in_reading_and_writing_of_XML_files = (
        "Exceptions in reading and writing of XML files"
    )
    System_Error = "System Error"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OASISErrDescription",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{A72CFA46-17ED-4e68-B3E5-C932438487D5}",
            kind="enumeration",
        )
    )
