"""The `cim_python_sdk.profiles.cgmes3` facade and its generated stub."""

import subprocess
import sys
from pathlib import Path

import pytest

import cim_python_sdk as c
from cim_python_sdk._registry import BY_NAME
from cim_python_sdk.profiles import cgmes3

ROOT = Path(__file__).resolve().parents[2]
API = set(cgmes3._API)


def class_exports():
    keywords = set(cgmes3.profile_set.keywords)
    return [n for n in cgmes3.__all__ if n not in API and n not in keywords]


def test_exports_are_exactly_the_profile_classes():
    exported = class_exports()
    assert set(exported) == set(cgmes3.class_names) == {k.__name__ for k in cgmes3.classes}
    assert len(exported) == len(set(exported)) == 490
    assert cgmes3.__all__ == sorted(cgmes3.__all__)
    assert set(cgmes3.__all__) >= set(cgmes3.profile_set.keywords) | API


def test_exports_are_the_cim_python_sdk_objects():
    for name in class_exports():
        assert name in BY_NAME
        assert getattr(cgmes3, name) is getattr(c, name), name
    assert cgmes3.ACLineSegment is c.ACLineSegment and cgmes3.BoundaryPoint is c.BoundaryPoint
    assert set(cgmes3.classes) == {getattr(c, n) for n in class_exports()}


def test_non_cgmes_classes_are_excluded():
    for name in ("Bid", "MarketParticipant", "Asset", "Customer"):
        assert hasattr(c, name)
        assert name not in cgmes3.__all__ and name not in dir(cgmes3)
        with pytest.raises(AttributeError):
            getattr(cgmes3, name)
    with pytest.raises(AttributeError):
        cgmes3._private  # noqa: B018


def test_no_class_hides_an_api_name():
    assert not (set(class_exports()) & (API | set(cgmes3.profile_set.keywords)))
    assert not (API | set(cgmes3.profile_set.keywords)) & set(BY_NAME)


def test_dir_and_star_import():
    d = dir(cgmes3)
    assert {"EQ", "SSH", "ACLineSegment", "profiles_of", "by_keyword"} <= set(d)
    code = (
        "from cim_python_sdk.profiles.cgmes3 import *\n"
        "import cim_python_sdk\n"
        "assert ACLineSegment is cim_python_sdk.ACLineSegment and EQ.keyword == 'EQ'\n"
        "assert 'Bid' not in globals() and 'Terminal' in globals()\n"
    )
    r = subprocess.run(
        [sys.executable, "-I", "-c", code], capture_output=True, text=True, check=False
    )
    assert r.returncode == 0, r.stderr


def test_profile_objects_and_helpers():
    keywords = ("EQ", "SSH", "TP", "SV", "DL", "GL", "OP", "SC", "EQBD", "DY")
    assert [getattr(cgmes3, k) for k in keywords] == list(cgmes3.profiles)
    assert cgmes3.profile_set.name == "CGMES 3.0"
    assert cgmes3.EQ.classes == tuple(getattr(c, n) for n in cgmes3.EQ.class_names)


def test_import_is_lazy():
    code = (
        "import sys, cim_python_sdk.profiles.cgmes3 as g\n"
        "assert not [m for m in sys.modules if m.startswith('cim_python_sdk.model.')], 'model imported'\n"
        "assert g._set.cache_info().currsize == 0, 'snapshot read'\n"
        "g.ACLineSegment\n"
        "assert 'cim_python_sdk.model.iec61970.base.wires.ac_line_segment' in sys.modules\n"
    )
    r = subprocess.run(
        [sys.executable, "-I", "-c", code], capture_output=True, text=True, check=False
    )
    assert r.returncode == 0, r.stderr


def test_stub_is_current():
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "gen_profile_stubs.py"), "--check"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_stub_names_match_the_facade():
    text = (ROOT / "src" / "cim_python_sdk" / "profiles" / "cgmes3.pyi").read_text("utf-8")
    for name in class_exports():
        assert f" import {BY_NAME[name].partition(':')[2]} as {name}\n" in text
    for kw in cgmes3.profile_set.keywords:
        assert f"\n{kw}: _model.Profile\n" in text
    assert "Bid" not in text
