"""CIM enumeration MeasuringPeriodKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MeasuringPeriodKind(CimEnum):
    """Kind of period for reading / measuring values."""

    none = "none"
    tenMinute = "tenMinute"
    fifteenMinute = "fifteenMinute"
    oneMinute = "oneMinute"
    twentyfourHour = "twentyfourHour"
    thirtyMinute = "thirtyMinute"
    fiveMinute = "fiveMinute"
    sixtyMinute = "sixtyMinute"
    twoMinute = "twoMinute"
    threeMinute = "threeMinute"
    present = "present"
    previous = "previous"
    twentyMinute = "twentyMinute"
    fixedBlock60Min = "fixedBlock60Min"
    fixedBlock30Min = "fixedBlock30Min"
    fixedBlock20Min = "fixedBlock20Min"
    fixedBlock15Min = "fixedBlock15Min"
    fixedBlock10Min = "fixedBlock10Min"
    fixedBlock5Min = "fixedBlock5Min"
    fixedBlock1Min = "fixedBlock1Min"
    rollingBlock60MinIntvl30MinSubIntvl = "rollingBlock60MinIntvl30MinSubIntvl"
    rollingBlock60MinIntvl20MinSubIntvl = "rollingBlock60MinIntvl20MinSubIntvl"
    rollingBlock60MinIntvl15MinSubIntvl = "rollingBlock60MinIntvl15MinSubIntvl"
    rollingBlock60MinIntvl12MinSubIntvl = "rollingBlock60MinIntvl12MinSubIntvl"
    rollingBlock60MinIntvl10MinSubIntvl = "rollingBlock60MinIntvl10MinSubIntvl"
    rollingBlock60MinIntvl6MinSubIntvl = "rollingBlock60MinIntvl6MinSubIntvl"
    rollingBlock60MinIntvl5MinSubIntvl = "rollingBlock60MinIntvl5MinSubIntvl"
    rollingBlock60MinIntvl4MinSubIntvl = "rollingBlock60MinIntvl4MinSubIntvl"
    rollingBlock30MinIntvl15MinSubIntvl = "rollingBlock30MinIntvl15MinSubIntvl"
    rollingBlock30MinIntvl10MinSubIntvl = "rollingBlock30MinIntvl10MinSubIntvl"
    rollingBlock30MinIntvl6MinSubIntvl = "rollingBlock30MinIntvl6MinSubIntvl"
    rollingBlock30MinIntvl5MinSubIntvl = "rollingBlock30MinIntvl5MinSubIntvl"
    rollingBlock30MinIntvl3MinSubIntvl = "rollingBlock30MinIntvl3MinSubIntvl"
    rollingBlock30MinIntvl2MinSubIntvl = "rollingBlock30MinIntvl2MinSubIntvl"
    rollingBlock15MinIntvl5MinSubIntvl = "rollingBlock15MinIntvl5MinSubIntvl"
    rollingBlock15MinIntvl3MinSubIntvl = "rollingBlock15MinIntvl3MinSubIntvl"
    rollingBlock15MinIntvl1MinSubIntvl = "rollingBlock15MinIntvl1MinSubIntvl"
    rollingBlock10MinIntvl5MinSubIntvl = "rollingBlock10MinIntvl5MinSubIntvl"
    rollingBlock10MinIntvl2MinSubIntvl = "rollingBlock10MinIntvl2MinSubIntvl"
    rollingBlock10MinIntvl1MinSubIntvl = "rollingBlock10MinIntvl1MinSubIntvl"
    rollingBlock5MinIntvl1MinSubIntvl = "rollingBlock5MinIntvl1MinSubIntvl"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MeasuringPeriodKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{0DC2C07F-966E-43ab-8DA0-B65F51CB6E2E}",
            kind="enumeration",
        )
    )
