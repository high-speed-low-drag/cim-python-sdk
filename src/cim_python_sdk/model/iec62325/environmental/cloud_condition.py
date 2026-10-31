"""CIM class CloudCondition (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.atmospheric_phenomenon import AtmosphericPhenomenon

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.env_domain.cloud_kind import CloudKind


class CloudCondition(AtmosphericPhenomenon):
    """A classified cloud phenomenon with a type."""

    __slots__ = ("kind",)

    kind: CloudKind | None

    _cim_meta = ClassMeta(
        cim_name="CloudCondition",
        package="TC57CIM/IEC62325/Environmental",
        guid="{55D2D9CB-2F09-49c1-8D86-6D6E64F16913}",
        attributes=(AttrMeta("kind", "kind", "CloudKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: CloudKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
