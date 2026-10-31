"""CIM enumeration TestKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TestKind(CimEnum):
    """The test applied to determine if the condition is met."""

    equalTo = "equalTo"
    greaterThan = "greaterThan"
    lessThan = "lessThan"
    greaterThanOrEqualTo = "greaterThanOrEqualTo"
    lessThanOrEqualTo = "lessThanOrEqualTo"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TestKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{558863B0-1947-46d8-BE29-54D352B6F524}",
            kind="enumeration",
        )
    )
