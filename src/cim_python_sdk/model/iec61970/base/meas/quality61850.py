"""CIM class Quality61850 (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.validity import Validity
    from cim_python_sdk.model.iec61970.base.scada.source import Source


class Quality61850(CimObject):
    """Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced,
    which has been included in this class for convenience."""

    __slots__ = (
        "bad_reference",
        "estimator_replaced",
        "failure",
        "old_data",
        "operator_blocked",
        "oscillatory",
        "out_of_range",
        "over_flow",
        "source",
        "suspect",
        "test",
        "validity",
    )

    bad_reference: bool | None
    estimator_replaced: bool | None
    failure: bool | None
    old_data: bool | None
    operator_blocked: bool | None
    oscillatory: bool | None
    out_of_range: bool | None
    over_flow: bool | None
    source: Source | None
    suspect: bool | None
    test: bool | None
    validity: Validity | None

    _cim_meta = ClassMeta(
        cim_name="Quality61850",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{3561961B-F3BD-41f7-B693-9D9F77C613A0}",
        attributes=(
            AttrMeta("bad_reference", "badReference", "bool", 0, 1, "primitive"),
            AttrMeta("estimator_replaced", "estimatorReplaced", "bool", 0, 1, "primitive"),
            AttrMeta("failure", "failure", "bool", 0, 1, "primitive"),
            AttrMeta("old_data", "oldData", "bool", 0, 1, "primitive"),
            AttrMeta("operator_blocked", "operatorBlocked", "bool", 0, 1, "primitive"),
            AttrMeta("oscillatory", "oscillatory", "bool", 0, 1, "primitive"),
            AttrMeta("out_of_range", "outOfRange", "bool", 0, 1, "primitive"),
            AttrMeta("over_flow", "overFlow", "bool", 0, 1, "primitive"),
            AttrMeta("source", "source", "Source", 0, 1, "enumeration"),
            AttrMeta("suspect", "suspect", "bool", 0, 1, "primitive"),
            AttrMeta("test", "test", "bool", 0, 1, "primitive"),
            AttrMeta("validity", "validity", "Validity", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        bad_reference: bool | None = None,
        estimator_replaced: bool | None = None,
        failure: bool | None = None,
        old_data: bool | None = None,
        operator_blocked: bool | None = None,
        oscillatory: bool | None = None,
        out_of_range: bool | None = None,
        over_flow: bool | None = None,
        source: Source | None = None,
        suspect: bool | None = None,
        test: bool | None = None,
        validity: Validity | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bad_reference = bad_reference
        self.estimator_replaced = estimator_replaced
        self.failure = failure
        self.old_data = old_data
        self.operator_blocked = operator_blocked
        self.oscillatory = oscillatory
        self.out_of_range = out_of_range
        self.over_flow = over_flow
        self.source = source
        self.suspect = suspect
        self.test = test
        self.validity = validity
