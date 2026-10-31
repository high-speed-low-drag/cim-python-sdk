"""CIM enumeration AmiBillingReadyKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AmiBillingReadyKind(CimEnum):
    """Lifecycle states of the metering installation at a usage point with respect to readiness
    for billing via advanced metering infrastructure reads."""

    enabled = "enabled"
    operable = "operable"
    billingApproved = "billingApproved"
    nonAmi = "nonAmi"
    amiDisabled = "amiDisabled"
    amiCapable = "amiCapable"
    nonMetered = "nonMetered"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AmiBillingReadyKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{E31A9764-F65A-4a70-B936-6128A32C0353}",
            kind="enumeration",
        )
    )
