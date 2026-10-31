import hashlib
import sqlite3
from pathlib import Path

import pytest

from codegen import model_source as ms

MAGIC = ms.SQLITE_MAGIC


def _cfg(sources, filename="m.qea"):
    return {"filename": filename, "size": 0, "sources": sources}


def _src(name, url, data):
    return {"name": name, "url": url, "sha256": hashlib.sha256(data).hexdigest()}


def _fake_download(files):
    def dl(url, out_path):
        out_path.write_bytes(files[url])  # KeyError simulates a failing source
    return dl


GOOD = MAGIC + b"payload"


def test_load_source_config():
    cfg = ms.load_source_config()
    assert [s["name"] for s in cfg["sources"]] == ["primary", "mirror"]
    assert all(len(s["sha256"]) == 64 for s in cfg["sources"])
    assert ms.model_path().name == cfg["filename"]


def test_hash_mismatch_rejected(tmp_path, monkeypatch):
    cfg = _cfg([_src("p", "u1", GOOD)])
    monkeypatch.setattr(ms, "download", _fake_download({"u1": MAGIC + b"tampered"}))
    with pytest.raises(ms.ModelFetchError, match="sha256 mismatch"):
        ms.ensure_model(tmp_path, config=cfg)
    assert not (tmp_path / "m.qea").exists()
    assert list(tmp_path.glob("*.part")) == []


def test_bad_header_rejected(tmp_path, monkeypatch):
    bad = b"NOT SQLITE" + b"x" * 20
    cfg = _cfg([_src("p", "u1", bad)])  # hash matches, header does not
    monkeypatch.setattr(ms, "download", _fake_download({"u1": bad}))
    with pytest.raises(ms.ModelFetchError, match="bad header"):
        ms.ensure_model(tmp_path, config=cfg)
    assert not (tmp_path / "m.qea").exists()


def test_mirror_used_when_primary_fails(tmp_path, monkeypatch):
    mirror = MAGIC + b"mirror-bytes"
    cfg = _cfg([_src("p", "u1", GOOD), _src("m", "u2", mirror)])
    monkeypatch.setattr(ms, "download", _fake_download({"u2": mirror}))
    path = ms.ensure_model(tmp_path, config=cfg)
    assert path.read_bytes() == mirror


def test_cache_hit_skips_download(tmp_path, monkeypatch):
    cfg = _cfg([_src("p", "u1", GOOD)])
    (tmp_path / "m.qea").write_bytes(GOOD)

    def boom(url, out):
        raise AssertionError("should not download")

    monkeypatch.setattr(ms, "download", boom)
    assert ms.ensure_model(tmp_path, config=cfg) == tmp_path / "m.qea"


def test_force_redownloads(tmp_path, monkeypatch):
    cfg = _cfg([_src("p", "u1", GOOD)])
    (tmp_path / "m.qea").write_bytes(GOOD)
    calls = []

    def dl(url, out):
        calls.append(url)
        out.write_bytes(GOOD)

    monkeypatch.setattr(ms, "download", dl)
    ms.ensure_model(tmp_path, force=True, config=cfg)
    assert calls == ["u1"]


def test_all_sources_fail(tmp_path, monkeypatch):
    cfg = _cfg([_src("p", "u1", GOOD), _src("m", "u2", GOOD)])
    monkeypatch.setattr(ms, "download", _fake_download({}))
    with pytest.raises(ms.ModelFetchError, match="all sources failed"):
        ms.ensure_model(tmp_path, config=cfg)


def test_cached_model_version():
    path: Path = ms.model_path()
    if not path.is_file():
        pytest.skip("model not cached; run tools/fetch_model.py")
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        rows = con.execute(
            'SELECT DISTINCT a."Default" FROM t_object o JOIN t_attribute a '
            "ON a.Object_ID = o.Object_ID "
            "WHERE o.Name = 'IEC61970CIMVersion' AND a.Name = 'version'"
        ).fetchall()
    finally:
        con.close()
    assert rows == [("IEC61970CIM17v40",)]
