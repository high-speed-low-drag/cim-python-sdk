"""Serialization of CIM object graphs (generic, driven by ``_cim_meta``).

``write_cimxml``, ``read_cimxml`` and ``to_cimxml_string`` handle IEC 61970-552 RDF/XML;
``write_jsonld``, ``read_jsonld``, ``to_jsonld_string`` and ``to_jsonld_dict`` handle CIM JSON-LD.
Both readers return a `CimDocument`. ``write_cgmes`` and ``to_cgmes_strings``
(`cim_python_sdk.serialization.cgmes`) write a CGMES 3.0 file set, one CIMXML file per profile;
``read_cgmes`` reads such a set into one merged graph (`CgmesDocument`).
"""

from cim_python_sdk.serialization._common import CimDocument
from cim_python_sdk.serialization.cgmes import (
    CgmesDocument,
    CgmesFileHeader,
    CgmesHeader,
    CgmesReadError,
    CgmesReport,
    CgmesWriteError,
    read_cgmes,
    to_cgmes_strings,
    write_cgmes,
)
from cim_python_sdk.serialization.cimxml import (
    CimXmlError,
    read_cimxml,
    to_cimxml_string,
    write_cimxml,
)
from cim_python_sdk.serialization.jsonld import (
    CimJsonLdError,
    read_jsonld,
    to_jsonld_dict,
    to_jsonld_string,
    write_jsonld,
)

__all__ = [
    "CgmesDocument",
    "CgmesFileHeader",
    "CgmesHeader",
    "CgmesReadError",
    "CgmesReport",
    "CgmesWriteError",
    "CimDocument",
    "CimJsonLdError",
    "CimXmlError",
    "read_cgmes",
    "read_cimxml",
    "read_jsonld",
    "to_cgmes_strings",
    "to_cimxml_string",
    "to_jsonld_dict",
    "to_jsonld_string",
    "write_cgmes",
    "write_cimxml",
    "write_jsonld",
]
