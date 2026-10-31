"""Shared, session-scoped fixtures: the IR, the resolved model and every generated class.

`ir` is what the code is generated from: the CIM100 snapshot merged with the CGMES European
extensions (codegen/snapshot/eu_ir.json, namespace ``eu``)."""

from __future__ import annotations

import importlib
from pathlib import Path

import pytest

from cim_python_sdk import _registry
from codegen.ir import Model
from codegen.normalize import load_model, normalize

ROOT = Path(__file__).resolve().parents[2]


def load_ref(ref: str) -> type:
    module, _, name = ref.partition(":")
    return getattr(importlib.import_module(module), name)


@pytest.fixture(scope="session")
def ir() -> Model:
    return load_model()


@pytest.fixture(scope="session")
def resolved(ir):
    return normalize(ir)


@pytest.fixture(scope="session")
def by_guid() -> dict[str, type]:
    """Every generated class and enum, loaded from the registry (keyed by GUID)."""
    return {guid: load_ref(ref) for guid, ref in _registry.BY_GUID.items()}


@pytest.fixture(scope="session")
def ir_classifiers(ir) -> dict:
    return {c.guid: c for c in ir.classifiers}


@pytest.fixture(scope="session")
def owned_ends(by_guid) -> list[tuple[type, object]]:
    """Every (owner class, EndMeta) declared by a generated class."""
    return [(cls, e) for cls in by_guid.values() for e in cls._cim_meta.ends]
