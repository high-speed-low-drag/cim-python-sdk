"""CIM enumeration MktSubClassType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MktSubClassType(CimEnum):
    """CIM enumeration MktSubClassType."""

    Forecasted_UDC_Direct_Access_Load = "Forecasted_UDC_Direct_Access_Load"
    Day_Ahead_RMR = "Day_Ahead_RMR"
    Ten_Min_Expost_Market_Info = "Ten_Min_Expost_Market_Info"
    Day_Ahead_Interim_Market_Info = "Day_Ahead_Interim_Market_Info"
    Day_Ahead_Final_Market_Info = "Day_Ahead_Final_Market_Info"
    TTC_ATC_Forecast_Information = "TTC/ATC_Forecast_Information"
    TTC_ATC_Hourly_Forecast = "TTC/ATC_Hourly_Forecast"
    Branch_Group_Derates = "Branch_Group_Derates"
    Hour_Ahead_Market_Info = "Hour_Ahead_Market_Info"
    Hourly_Expost_Market_Info = "Hourly_Expost_Market_Info"
    Public_Bid_Data = "Public_Bid_Data"
    Day_Ahead_Forecast_Information = "Day_Ahead_Forecast_Information"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MktSubClassType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{DFD03D77-33FE-41d0-A327-0EECD0FEC905}",
            kind="enumeration",
        )
    )
