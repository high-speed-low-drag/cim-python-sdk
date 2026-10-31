"""CIM class ParentOrganization (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation import Organisation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self


class ParentOrganization(Organisation):
    """CIM class ParentOrganization."""

    __slots__ = ("_organisation",)

    organisation: Many[Organisation] = Many(
        EndMeta(
            name="organisation",
            cim_role="Organisation",
            target="cim_python_sdk.model.iec61968.common.organisation:Organisation",
            many=True,
            lower=0,
            upper=None,
            inverse="parent_organisation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ParentOrganization",
        package="TC57CIM/IEC61968/Common",
        guid="{F30F7262-89B5-4112-8867-770A060AAD09}",
        ends=(organisation.meta,),
    )

    def __init__(
        self,
        *,
        organisation: Iterable[Organisation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if organisation is not None:
            ParentOrganization.organisation.extend(self, organisation)

    def add_organisation(self, organisation: Organisation) -> Self:
        return ParentOrganization.organisation.add(self, organisation)

    def remove_organisation(self, organisation: Organisation) -> Self:
        return ParentOrganization.organisation.remove(self, organisation)

    def clear_organisation(self) -> Self:
        return ParentOrganization.organisation.clear(self)

    def num_organisation(self) -> int:
        return ParentOrganization.organisation.count(self)

    def get_organisation_by_mrid(self, mrid: str) -> Organisation | None:
        return ParentOrganization.organisation.get_by_mrid(self, mrid)
