"""Pinned model source: load config, download with checksum verification, cache."""

from __future__ import annotations

import hashlib
import os
import tempfile
import tomllib
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "model-source.toml"
DEFAULT_DEST = ROOT / "build" / "model"
SQLITE_MAGIC = b"SQLite format 3\x00"


class ModelFetchError(RuntimeError):
    pass


def load_source_config(path: Path | None = None) -> dict:
    with open(path or CONFIG_PATH, "rb") as f:
        return tomllib.load(f)


def model_path(dest: Path | None = None, config: dict | None = None) -> Path:
    config = config or load_source_config()
    return Path(dest or DEFAULT_DEST) / config["filename"]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, out_path: Path) -> None:
    """Stream url into out_path. Tests monkeypatch this."""
    with urllib.request.urlopen(url, timeout=60) as resp, open(out_path, "wb") as out:
        while chunk := resp.read(1 << 20):
            out.write(chunk)


def verify_file(path: Path, expected_sha256: str) -> None:
    """Raise ModelFetchError if the header or sha256 is wrong."""
    with open(path, "rb") as f:
        header = f.read(len(SQLITE_MAGIC))
    if header != SQLITE_MAGIC:
        raise ModelFetchError(f"bad header {header!r}, not a SQLite database")
    actual = sha256_file(path)
    if actual != expected_sha256:
        raise ModelFetchError(f"sha256 mismatch: expected {expected_sha256}, got {actual}")


def _cache_valid(target: Path, config: dict) -> bool:
    if not target.is_file():
        return False
    actual = sha256_file(target)
    return any(actual == s["sha256"] for s in config["sources"])


def ensure_model(
    dest: Path | None = None, force: bool = False, config: dict | None = None
) -> Path:
    config = config or load_source_config()
    target = model_path(dest, config)
    if not force and _cache_valid(target, config):
        return target
    target.parent.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []
    for source in config["sources"]:
        name = source.get("name", source["url"])
        fd, tmp_name = tempfile.mkstemp(dir=target.parent, suffix=".part")
        os.close(fd)
        tmp = Path(tmp_name)
        try:
            download(source["url"], tmp)
            verify_file(tmp, source["sha256"])
            os.chmod(tmp, 0o644)
            os.replace(tmp, target)
            return target
        except Exception as exc:  # noqa: BLE001 - any failure falls through to next source
            errors.append(f"{name}: {exc}")
        finally:
            tmp.unlink(missing_ok=True)
    raise ModelFetchError("all sources failed:\n  " + "\n  ".join(errors))
