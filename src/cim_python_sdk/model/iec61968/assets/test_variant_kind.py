"""CIM enumeration TestVariantKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TestVariantKind(CimEnum):
    """Test variants."""

    v1mm = "1mm"
    v2mm = "2mm"
    minus40C = "minus40C"
    minus30C = "minus30C"
    v0C = "0C"
    v25C = "25C"
    v30C = "30C"
    v40C = "40C"
    v100C = "100C"
    v72hours = "72hours"
    v164hours = "164hours"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TestVariantKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{F1139730-E3EA-41bf-B39B-8A759C840EA6}",
            kind="enumeration",
        )
    )
