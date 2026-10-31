"""Pinned CGMES profile vocabularies (ENTSO-E RDFS) and the CGMES EA model (`[schema]`): load config, download with
checksum verification, cache."""

from __future__ import annotations

import os
import tempfile
import tomllib
from pathlib import Path

from codegen.model_source import SQLITE_MAGIC, download, sha256_file

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "profile-source.toml"
DEFAULT_DEST = ROOT / "build" / "profiles"
XML_MAGIC = b"<?xml"


class ProfileFetchError(RuntimeError):
    pass


def load_source_config(path: Path | None = None) -> dict:
    with open(path or CONFIG_PATH, "rb") as f:
        return tomllib.load(f)


def profile_url(config: dict, entry: dict) -> str:
    return config["url"].format(commit=config["commit"], file=entry["file"])


def verify_file(path: Path, entry: dict) -> None:
    """Raise ProfileFetchError if the header, size or sha256 is wrong."""
    with open(path, "rb") as f:
        header = f.read(len(XML_MAGIC))
    if header != XML_MAGIC:
        raise ProfileFetchError(f"{entry['file']}: bad header {header!r}, not an XML file")
    size = path.stat().st_size
    if size != entry["size"]:
        raise ProfileFetchError(f"{entry['file']}: size {size}, expected {entry['size']}")
    actual = sha256_file(path)
    if actual != entry["sha256"]:
        raise ProfileFetchError(
            f"{entry['file']}: sha256 mismatch: expected {entry['sha256']}, got {actual}"
        )


def _cache_valid(target: Path, entry: dict) -> bool:
    return (
        target.is_file()
        and target.stat().st_size == entry["size"]
        and sha256_file(target) == entry["sha256"]
    )


def ensure_profiles(
    dest: Path | None = None, force: bool = False, config: dict | None = None
) -> dict[str, Path]:
    """Download missing or stale vocabulary files into dest; return {keyword: path}."""
    config = config or load_source_config()
    dest = Path(dest or DEFAULT_DEST)
    dest.mkdir(parents=True, exist_ok=True)
    out: dict[str, Path] = {}
    for entry in config["profiles"]:
        target = dest / entry["file"]
        if force or not _cache_valid(target, entry):
            fd, tmp_name = tempfile.mkstemp(dir=dest, suffix=".part")
            os.close(fd)
            tmp = Path(tmp_name)
            try:
                download(profile_url(config, entry), tmp)
                verify_file(tmp, entry)
                os.chmod(tmp, 0o644)
                os.replace(tmp, target)
            except Exception as exc:
                if isinstance(exc, ProfileFetchError):
                    raise
                raise ProfileFetchError(f"{entry['file']}: {exc}") from exc
            finally:
                tmp.unlink(missing_ok=True)
        out[entry["keyword"]] = target
    return out


def cached_profiles(dest: Path | None = None, config: dict | None = None) -> dict[str, Path] | None:
    """{keyword: path} if every pinned file is cached and valid, else None. Never downloads."""
    config = config or load_source_config()
    dest = Path(dest or DEFAULT_DEST)
    out = {e["keyword"]: dest / e["file"] for e in config["profiles"]}
    entries = {e["keyword"]: e for e in config["profiles"]}
    if all(_cache_valid(p, entries[k]) for k, p in out.items()):
        return out
    return None


# --------------------------------------------------------------------------- the EA model


def schema_url(config: dict) -> str:
    schema = config["schema"]
    return schema["url"].format(commit=schema["commit"], file=schema["file"])


def verify_schema(path: Path, entry: dict) -> None:
    """Raise ProfileFetchError if the SQLite header, size or sha256 of the .qea is wrong."""
    with open(path, "rb") as f:
        header = f.read(len(SQLITE_MAGIC))
    if header != SQLITE_MAGIC:
        raise ProfileFetchError(f"{entry['file']}: bad header {header!r}, not a SQLite database")
    if path.stat().st_size != entry["size"] or sha256_file(path) != entry["sha256"]:
        raise ProfileFetchError(f"{entry['file']}: size or sha256 differs from the pin")


def cached_schema(dest: Path | None = None, config: dict | None = None) -> Path | None:
    """Path of the pinned CGMES EA model if it is cached and valid, else None. Never downloads."""
    config = config or load_source_config()
    target = Path(dest or DEFAULT_DEST) / config["schema"]["file"]
    return target if _cache_valid(target, config["schema"]) else None


def ensure_schema(
    dest: Path | None = None, force: bool = False, config: dict | None = None
) -> Path:
    """Download the pinned CGMES EA model into dest unless a valid copy is cached; return it."""
    config = config or load_source_config()
    entry = config["schema"]
    dest = Path(dest or DEFAULT_DEST)
    target = dest / entry["file"]
    if not force and _cache_valid(target, entry):
        return target
    dest.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=dest, suffix=".part")
    os.close(fd)
    tmp = Path(tmp_name)
    try:
        download(schema_url(config), tmp)
        verify_schema(tmp, entry)
        os.chmod(tmp, 0o644)
        os.replace(tmp, target)
    except Exception as exc:
        if isinstance(exc, ProfileFetchError):
            raise
        raise ProfileFetchError(f"{entry['file']}: {exc}") from exc
    finally:
        tmp.unlink(missing_ok=True)
    return target
