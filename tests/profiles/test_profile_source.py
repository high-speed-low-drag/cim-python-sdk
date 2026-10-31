import hashlib

import pytest

from codegen import profile_source as ps

DATA = b'<?xml version="1.0"?><rdf:RDF/>'


def _cfg(data=DATA, files=("A.owl", "B.owl")):
    return {
        "repo": "r",
        "commit": "c0ffee",
        "url": "https://example.invalid/{commit}/{file}",
        "profiles": [
            {
                "keyword": f.split(".")[0],
                "file": f,
                "sha256": hashlib.sha256(data).hexdigest(),
                "size": len(data),
            }
            for f in files
        ],
    }


def _fake(payloads, calls=None):
    def dl(url, out_path):
        if calls is not None:
            calls.append(url)
        out_path.write_bytes(payloads[url.rsplit("/", 1)[1]])  # KeyError = failing download

    return dl


def test_load_source_config():
    cfg = ps.load_source_config()
    kws = [p["keyword"] for p in cfg["profiles"]]
    assert sorted(kws) == ["DL", "DY", "EQ", "EQBD", "GL", "OP", "SC", "SSH", "SV", "TP"]
    assert cfg["repo"] == "entsoe/CGMES-AP"
    assert cfg["commit"] == "e96dd4e323b1e2236e141dd03bf9adea81672e00"
    assert all(len(p["sha256"]) == 64 and p["size"] > 0 for p in cfg["profiles"])
    eq = next(p for p in cfg["profiles"] if p["keyword"] == "EQ")
    assert ps.profile_url(cfg, eq) == (
        "https://raw.githubusercontent.com/entsoe/CGMES-AP/"
        "e96dd4e323b1e2236e141dd03bf9adea81672e00/CGMES/RDFS/"
        "61970-600-2_Equipment-AP-Voc-RDFS2020.rdf"
    )
    assert cfg["schema"]["commit"] == "1c7708f5d3bde53e154201707f31961573868cf2"
    assert ps.schema_url(cfg).startswith(
        "https://raw.githubusercontent.com/cimug-org/CGMES-CIM17/1c7708f5d3bde53e154201707f31961573868cf2/"
    )
    assert [c["class"] for c in cfg["corrections"]] == ["Equipment"]


def test_download_and_cache(tmp_path, monkeypatch):
    calls = []
    monkeypatch.setattr(ps, "download", _fake({"A.owl": DATA, "B.owl": DATA}, calls))
    cfg = _cfg()
    paths = ps.ensure_profiles(tmp_path, config=cfg)
    assert paths == {"A": tmp_path / "A.owl", "B": tmp_path / "B.owl"}
    assert calls == ["https://example.invalid/c0ffee/A.owl", "https://example.invalid/c0ffee/B.owl"]
    assert ps.cached_profiles(tmp_path, config=cfg) == paths
    ps.ensure_profiles(tmp_path, config=cfg)
    assert len(calls) == 2  # cache hit
    ps.ensure_profiles(tmp_path, force=True, config=cfg)
    assert len(calls) == 4


def test_hash_mismatch_rejected(tmp_path, monkeypatch):
    bad = DATA.replace(b"RDF", b"XYZ")  # same size, other bytes
    monkeypatch.setattr(ps, "download", _fake({"A.owl": bad}))
    with pytest.raises(ps.ProfileFetchError, match="sha256 mismatch"):
        ps.ensure_profiles(tmp_path, config=_cfg(files=("A.owl",)))
    assert list(tmp_path.iterdir()) == []


def test_size_and_header_rejected(tmp_path, monkeypatch):
    monkeypatch.setattr(ps, "download", _fake({"A.owl": DATA + b" "}))
    with pytest.raises(ps.ProfileFetchError, match="size"):
        ps.ensure_profiles(tmp_path, config=_cfg(files=("A.owl",)))
    html = b"<html>" + DATA[6:]
    monkeypatch.setattr(ps, "download", _fake({"A.owl": html}))
    with pytest.raises(ps.ProfileFetchError, match="bad header"):
        ps.ensure_profiles(tmp_path, config=_cfg(html, files=("A.owl",)))


def test_download_failure_wrapped(tmp_path, monkeypatch):
    monkeypatch.setattr(ps, "download", _fake({}))
    with pytest.raises(ps.ProfileFetchError, match="A.owl"):
        ps.ensure_profiles(tmp_path, config=_cfg(files=("A.owl",)))
    assert ps.cached_profiles(tmp_path, config=_cfg(files=("A.owl",))) is None
