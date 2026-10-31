"""Deterministic mRIDs: ``uuid5(NAMESPACE, f"{network}/{kind}/{source_id}")``.

Rebuilding a network from the same workbook therefore gives the same mRIDs. Objects shared by all
networks (the AusNet GeographicalRegion and the BaseVoltages) use the network key ``"shared"`` so
that models of several networks can be merged without duplicating them.
"""

from __future__ import annotations

import uuid

NAMESPACE = uuid.uuid5(uuid.NAMESPACE_URL, "urn:x-local:cim_python_sdk-networks:mvlv-cim")
SHARED = "shared"


def make_mrid(network: str, kind: str, source_id: object) -> str:
    """The mRID of the object of ``kind`` built from ``source_id`` in ``network``."""
    return str(uuid.uuid5(NAMESPACE, f"{network}/{kind}/{source_id}"))
