"""CIM enumeration TestMethod (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TestMethod(CimEnum):
    """Possible test methods."""

    D1275A = "D1275A"
    D1275B = "D1275B"
    D3612A = "D3612A"
    D3612B = "D3612B"
    D3612C = "D3612C"
    v60567ByDisplacement = "60567ByDisplacement"
    v60567ByPartition = "60567ByPartition"
    v60567ByVacuum = "60567ByVacuum"
    v60970Automatic = "60970Automatic"
    v60970Manual1 = "60970Manual1"
    v60970Manual2 = "60970Manual2"
    v62535Main = "62535Main"
    v62535AnnexA = "62535AnnexA"
    v61125A = "61125A"
    v61125B = "61125B"
    v61125C = "61125C"
    v62270AnnexA = "62270AnnexA"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TestMethod",
            package="TC57CIM/IEC61968/Assets",
            guid="{E2503A9B-2045-45b6-9945-9F7F40349894}",
            kind="enumeration",
        )
    )
