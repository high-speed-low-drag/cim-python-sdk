# cim-python-sdk

Python SDK covering all CIM100 classes (1,426 classes, 405 enums, datatypes and compounds), generated
from the CIM UG Enterprise Architect model. Objects live in memory; CIMXML (IEC 61970-552) and CIM JSON-LD
serialization is in `cim_python_sdk.serialization`. CGMES 3.0 profiles (EQ, SSH, TP, SV, ...) and CGMES file
sets are in `cim_python_sdk.profiles` and `cim_python_sdk.serialization.cgmes`.

Example: [`examples/mvlv-networks`](examples/mvlv-networks) builds four real Australian MV distribution
networks (Team-Nando/MV-LV-Networks) as CIM and exports them to CIMXML, JSON-LD and CGMES 3.0 file sets.

## Install

```
uv sync
uv run pytest -q
uv run ruff check .
```

## Usage

```python
from cim_python_sdk import ACLineSegment, Terminal, Substation, VoltageLevel, UnitSymbol, PhaseCode

# Attributes and enums (keyword-only constructors; everything is optional)
line = ACLineSegment(name="L1", length=12.5)
term = Terminal(phases=PhaseCode.ABC, sequence_number=1)
line.name = "Line 1"
assert UnitSymbol.m.value == "m"

# Automatic mRIDs: a random UUID4 string unless you pass mrid=...
assert len(line.mrid) == 36

# Links update both ends
term.conducting_equipment = line
assert line.terminals == (term,)          # many-ends read as a tuple snapshot
term.conducting_equipment = None
assert line.terminals == ()

# Many-end methods: add_, remove_, clear_, num_, get_*_by_mrid
line.add_terminal(term)
assert term.conducting_equipment is line
assert line.num_terminal() == 1
assert line.get_terminal_by_mrid(term.mrid) is term
line.remove_terminal(term)                 # ValueError if absent
line.add_terminal(term).clear_terminals()  # add/remove/clear return self

sub = Substation(name="S1")
vl = VoltageLevel(name="132kV", substation=sub)
assert sub.voltage_levels == (vl,)
```

### validate()

`obj.validate()` returns a list of messages (empty when fine). Only lower bounds are reported;
upper bounds are not checked, and association targets are type-checked on assignment (`TypeError`). Attribute values are not type-checked.

```python
from cim_python_sdk import Substation

print(Substation(name="S").validate())
# ["Substation(mrid='...'): required association 'instance_set' is not set"]
```

### Copying

`copy.deepcopy` and `pickle` give a separate, consistent graph (cycles are fine).
`copy.copy` raises `TypeError`, because a shallow copy would share half-links with the original.

## Serialization (CIMXML and JSON-LD)

`cim_python_sdk.serialization` writes and reads IEC 61970-552 RDF/XML (CIMXML) and CIM JSON-LD (stdlib
only), generically for every class, driven by `_cim_meta`.

```python
from cim_python_sdk import ACLineSegment, Terminal, Substation, PhaseCode
from cim_python_sdk.serialization import read_cimxml, to_cimxml_string, write_cimxml

sub = Substation(name="Zone Sub", mrid="sub-1")
line = ACLineSegment(name="L1", length=12.5, mrid="line-1", equipment_container=sub)
Terminal(mrid="t-1", sequence_number=1, phases=PhaseCode.ABC, conducting_equipment=line)

print(to_cimxml_string([sub]))             # the roots plus everything reachable (include_reachable=True)
write_cimxml([sub], "network.xml", header={"description": "demo", "version": "1"})

doc = read_cimxml("network.xml")           # CimDocument: .objects .by_id .header .warnings .dangling
line2 = doc.by_id["line-1"]                # keyed by mRID
assert line2.length == 12.5 and line2.terminals[0].phases is PhaseCode.ABC
assert line2.equipment_container is doc.by_id["sub-1"]
```

- Elements are `<cim:ACLineSegment rdf:ID="_<mrid>">`, properties `<cim:Declaring.cimName>` (the CIM
  name of the class that declares them), references `rdf:resource="#_<mrid>"`, enums
  `rdf:resource="<ns>EnumName.literal"`, compounds nested with `rdf:parseType="Resource"`.
- Each association is written once, from its single-valued end (`Terminal.ConductingEquipment`); for
  1:1 and N:M from the end whose `<Owner>.<Role>` sorts first. `write_both_ends=True` writes both.
- Objects without an mRID (for example `PositionPoint`) get `rdf:ID="_gen<N>"`; they are read back
  without an mRID.
- The reader accepts `rdf:ID`, `rdf:about="#_x"` and `urn:uuid:x`, associations on either or both
  ends, and collects unknown classes/properties, bad literals and dangling references in
  `doc.warnings` / `doc.dangling` (`strict=True` raises `CimXmlError` instead).
- Output is deterministic (sorted by CIM class name, then id) and pretty-printed UTF-8.
- The full rules (ids, naming, value encoding, duplicate CIM class names) are in the docstring of
  `cim_python_sdk/serialization/_common.py`.

### CIM JSON-LD

`write_jsonld`, `to_jsonld_string`, `to_jsonld_dict` and `read_jsonld` take the same arguments
(plus `indent=`) and return the same `CimDocument`; the format follows the DIGIN10 "CIMJSON-LD"
convention. Reading CIMXML and JSON-LD of the same objects gives equal graphs.

```python
from cim_python_sdk.serialization import read_jsonld, to_jsonld_string, write_jsonld

print(to_jsonld_string([sub]))
# {
#   "@context": {"cim": "http://iec.ch/TC57/CIM100#", "rdf": "...", "md": "...", "xsd": "..."},
#   "@graph": [
#     {"@id": "#_line-1", "@type": "cim:ACLineSegment",
#      "cim:Conductor.length": 12.5,
#      "cim:IdentifiedObject.mRID": "line-1", "cim:IdentifiedObject.name": "L1",
#      "cim:Equipment.EquipmentContainer": {"@id": "#_sub-1"}},
#     {"@id": "#_t-1", "@type": "cim:Terminal", "cim:Terminal.phases": {"@id": "cim:PhaseCode.ABC"},
#      "cim:Terminal.ConductingEquipment": {"@id": "#_line-1"}, ...},
#     ...
#   ]
# }
write_jsonld([sub], "network.jsonld", header={"description": "demo", "version": "1"})
doc = read_jsonld("network.jsonld")
assert doc.by_id["line-1"].terminals[0].phases is PhaseCode.ABC
```

- `@id` is `urn:uuid:<mrid>` for UUID mRIDs, `#_<percent-encoded mrid>` for any other mRID and the
  blank node `_:gen<N>` for objects without one. Enums are `{"@id": "cim:Enum.literal"}`,
  compounds nested objects without `@id`, many-ends arrays of `{"@id": ...}`, `Decimal` a string,
  datetimes typed `xsd` literals, and NaN/INF `{"@value": "NaN", "@type": "xsd:double"}`.
- A header becomes the DIGIN dataset description (`dcat:Dataset`, `prov:generatedAtTime`,
  `dcterms:description`, ...) next to `@graph`.
- The reader takes `@graph` or a top-level array, `urn:uuid:x`, `_x`, `#_x` and compact IRIs as ids,
  and properties without `cim:` when the context has an `@vocab`.
- The module docstring of `cim_python_sdk/serialization/jsonld.py` lists which conventions are from the
  spec and which are inferred.
- In CIMXML, strings with XML-invalid control characters raise `ValueError` when written (JSON-LD
  can carry them); an mRID that is not a valid XML name (for example `a#b`) is written
  `rdf:about="#_a%23b"`.
- A writer emits one `warnings.warn` per association end that has no CIM role in the model (it is
  then written under its generated Python name, which is not standard CIM).

## CGMES 3.0 profiles

A CGMES profile is a subset of the CIM: which classes may appear in a file, which properties each
class has there, which are required, and how many items an association may have. The objects stay
ordinary `cim_python_sdk` objects; a profile is a view over them (`cim_python_sdk.profiles`). The profiles are those
of CGMES 3.0 (IEC 61970-600-2, CIM100 namespace `http://iec.ch/TC57/CIM100#`): `EQ` (equipment),
`SSH` (steady state hypothesis), `TP` (topology), `SV` (state variables), `DL`, `GL`, `OP`, `SC`,
`EQBD` and `DY` (dynamics models: exciters, governors, stabilisers, wind turbines, ...). They are
read from the official ENTSO-E vocabularies (RDFS) and every class and property they list is a
member of the SDK.

```python
from cim_python_sdk import ACLineSegment, Terminal
from cim_python_sdk.profiles import cgmes3, validate_profile

EQ = cgmes3.EQ                                  # also cgmes3.SSH, TP, SV, ...; cgmes3.profiles
print(EQ.keyword, EQ.uri)                       # EQ http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0
print([p.name for p in EQ.required(ACLineSegment)])
# ['IdentifiedObject.mRID', 'IdentifiedObject.name', 'ACLineSegment.bch', 'ACLineSegment.r', 'ACLineSegment.x']
info = EQ.property(ACLineSegment, "r")          # by Python name, bare CIM name or Class.prop
print(info.name, info.range, info.min, info.max)  # ACLineSegment.r cim:Resistance 1 1
print(cgmes3.profiles_of(Terminal, "connected"))  # (Profile('SSH'),): the profiles that list it
print(EQ.has_class("Feeder"), EQ.is_concrete(ACLineSegment))  # False True

for issue in validate_profile([ACLineSegment(name="L1", length=12.5)], [cgmes3.EQ])[:2]:
    print(issue)
# error: ACLineSegment(mrid='...') [EQ]: required property ACLineSegment.bch is not set
# error: ACLineSegment(mrid='...') [EQ]: required property ACLineSegment.r is not set
```

- `Profile.properties(cls)` lists the properties of a class in the profile, including those of its
  profile superclasses; `required(cls)` the ones with a minimum of 1; `classes`, `class_names`,
  `has_class`, `is_concrete`, `allowed_literals(enum)` answer the rest. Each `PropertyInfo` has the
  CIM name, the SDK attribute (`python_name`), `kind`, `min`, `max`, `range`, `targets`, `literals`
  and the `owner` (the end an association is written from).
- `cgmes3.profiles_of(cls, prop)` and `cgmes3.defining_profiles(cls)` answer "where is this" across
  the whole set.
- `validate_profile(objects, profiles)` checks objects (and everything reachable) against the
  profiles you pass: a class that is not in them, a class that is not concrete, a missing required
  property, too many items on an association end, an enumeration literal the profile does not allow
  (errors), and a value that no selected profile lists (warning). Properties of an unselected
  profile are not required, so `[cgmes3.EQ]` alone ignores SSH. About 0.4 s for 35 000 objects.
- IDE autocomplete: `cim_python_sdk.profiles.cgmes3` is also a facade of exactly the CGMES 3.0 classes
  (there is a generated `.pyi`). `from cim_python_sdk.profiles.cgmes3 import ACLineSegment, EQ` gives the
  same `ACLineSegment` as `cim_python_sdk.ACLineSegment`; market, asset and work classes are not in it.
- **European extensions.** CGMES 3.0 EQ, TP and EQBD use a few classes and properties of the
  ENTSO-E namespace `http://iec.ch/TC57/CIM100-European#` (`eu:`): `IdentifiedObject.shortName`,
  `energyIdentCodeEic`, `OperationalLimitType.kind` (enum `LimitKind`), `BoundaryPoint`,
  `WindPowerPlant`, `SolarPowerPlant`. They are real members of the model (`short_name`,
  `energy_ident_code_eic`, `OperationalLimitType.kind`, `from cim_python_sdk import BoundaryPoint, LimitKind`),
  carry their namespace in the metadata, and are written with the `eu:` prefix (CIMXML, JSON-LD and
  CGMES).

```python
from cim_python_sdk import LimitKind, OperationalLimitType

line = ACLineSegment(name="L1", short_name="L1", energy_ident_code_eic="10X1001A1001A450")
patl = OperationalLimitType(name="PATL", kind=LimitKind.patl)
print([i.qname for i in EQ.properties(ACLineSegment) if i.namespace == "eu"])
# ['eu:IdentifiedObject.energyIdentCodeEic', 'eu:IdentifiedObject.shortName']
```

## CGMES file sets

`write_cgmes` writes one CIMXML file per profile with an `md:FullModel` header; `read_cgmes` merges
a set back into one object graph. The CIMXML rules of the previous section apply, with the
CGMES conventions below.

```python
import datetime as dt
from cim_python_sdk import (
    ACLineSegment, BaseVoltage, ConnectivityNode, GeographicalRegion, PhaseCode,
    SubGeographicalRegion, Substation, Terminal, TopologicalNode, VoltageLevel,
)
from cim_python_sdk.profiles import cgmes3, validate_profile
from cim_python_sdk.serialization import CgmesHeader, read_cgmes, write_cgmes

kv = BaseVoltage(name="22 kV", nominal_voltage=22e3)           # SI: V, W, VA, m
region = SubGeographicalRegion(name="Sub-region", region=GeographicalRegion(name="Region"))
sub = Substation(name="S1", region=region)
vl = VoltageLevel(name="22 kV", substation=sub, base_voltage=kv)
a, b = (ConnectivityNode(name=n, connectivity_node_container=vl) for n in ("A", "B"))
line = ACLineSegment(name="L1", length=1200.0, r=0.3, x=0.4, bch=1e-5, base_voltage=kv,
                     equipment_container=vl)
for i, node in enumerate((a, b), start=1):
    tn = TopologicalNode(name=node.name, base_voltage=kv, connectivity_node_container=vl)
    node.topological_node = tn
    Terminal(name=f"L1 T{i}", sequence_number=i, phases=PhaseCode.ABC, connected=True,
             conducting_equipment=line, connectivity_node=node, topological_node=tn)

profiles = [cgmes3.EQ, cgmes3.SSH, cgmes3.TP]
assert not [i for i in validate_profile([line], profiles) if i.severity == "error"]

header = CgmesHeader(
    scenario_time=dt.datetime(2026, 1, 1, 12, 30, tzinfo=dt.UTC),
    modeling_authority_set="http://example.org/mas",
    description="demo",
)
report = write_cgmes([line], "demo_set", profiles=("EQ", "SSH", "TP"), header=header, name="demo")
print(report.files)   # {'EQ': 'demo_EQ.xml', 'SSH': 'demo_SSH.xml', 'TP': 'demo_TP.xml'}
print(len(report.errors), len(report.dropped))   # 0 0

doc = read_cgmes("demo_set")                      # a directory, a .zip, paths or (name, bytes) pairs
print(doc.profiles, len(doc.objects), doc.warnings)   # ('EQ', 'SSH', 'TP') 12 []
print(doc.headers["demo_EQ.xml"].modeling_authority_set)  # http://example.org/mas
```

- **Write.** `write_cgmes(objects, out, *, profiles=("EQ","SSH","TP","SV"), header=CgmesHeader(),
  name="model", file_name="{name}_{keyword}.xml", boundary=(), strict=False)`. `out` is a directory
  or a `.zip` (fixed timestamps, deterministic). `to_cgmes_strings` returns `{keyword: xml}`.
  Each file holds only the properties of its profile. An object is defined (`rdf:ID`, with
  `IdentifiedObject.mRID` as an element) in the profile that defines its class and described
  (`rdf:about`) in the others, which is how SSH, TP and SV add values to EQ objects; each value is
  written once. A class that is in no selected profile is not written.
- **`CgmesHeader`** sets `md:Model.created`, `scenarioTime`, `modelingAuthoritySet`, `description`,
  `version`, the model ids (default: a random UUID per file; pass `model_ids` for reproducible
  output) and `DependentOn`/`Supersedes`. Dependencies between the files written together follow
  the ENTSO-E samples (SSH on EQ, TP on SSH, SV on TP, EQ on EQBD); `dependent_on={"EQ": [...]}` adds
  the model ids of files outside the set. `combine={"EQ": ["SC"]}` writes the ShortCircuit
  properties into the EQ file, as the ENTSO-E samples do. The profile URI comes from the profile.
- **`boundary=`** lists the objects of an equipment boundary set (EQBD); with `EQBD` selected they are
  defined in that file and not in EQ. `read_cgmes` returns them as `doc.boundary_objects`.
- **`CgmesReport`**: `files`, `model_ids`, `headers`, `issues` (the `validate_profile` findings)
  and `dropped` (every value, link or object that no written file carries). Without `strict=True`
  one `UserWarning` summarises both; with it a `CgmesWriteError` is raised before anything is
  written. Check `dropped` whenever your graph is richer than the profiles.
- **Read.** `read_cgmes(sources, strict=False)` returns a `CgmesDocument` (a `CimDocument` with
  `headers`, `profiles`, `boundary_objects`, and `header_for_rewrite()` which gives a
  `CgmesHeader` that makes `write_cgmes` reproduce the original headers). Files are merged by id,
  in any order. Tags are classified by the profiles named in each header; properties outside them,
  unknown classes, conflicting values, objects that are only described and dangling references end
  up in `doc.warnings` and `doc.dangling`.
- **Conventions** come from the ENTSO-E CGMES 3.0 conformity MicroGrid BaseCase v3.0.2 files (BE
  and NL, EQ/SSH/TP/SV/DL/GL, as in powsybl-core commit `f6749ad`) and from powsybl-core's CGMES
  export: the `md:FullModel` header, `rdf:ID="_<uuid>"`, `rdf:about="#_<uuid>"`, `xmlns:eu` always
  declared, associations written from the side the profile lists, SSH describing equipment under
  its ancestor (`<cim:Equipment rdf:about=...>` with `inService`). The module docstring of
  `cim_python_sdk/serialization/cgmes.py` lists them. The full BE and NL sample sets read and write back
  to the same graph (opt-in test: `CIM_PYTHON_SDK_CGMES_SAMPLES=<dir>` or `CIM_PYTHON_SDK_CGMES_DOWNLOAD=1`).
- **Units.** Objects hold SI values (V, W, VAr, VA, m). CGMES fixes a multiplier per datatype
  (kV, MW, MVAr, MVA, km; ohm, S, A, Hz unchanged), so `write_cgmes` divides by it and
  `read_cgmes` multiplies: `nominal_voltage=22e3` is written as `22.0` and reads back as
  `22000.0`. The shift works on the decimal text, so a value survives a write and read exactly.
  `units="cgmes"` (on both) writes and reads the numbers as they are. The multipliers come from
  the ENTSO-E RDFS (`profile-source.toml` `[units]`); `cgmes3.profile_set.unit_exponent("Voltage")`
  is 3.
- **Known limitations.** Objects of classes without an mRID (`PositionPoint`, `Sv*`, curve points,
  ...) get `_gen<N>` ids: not UUIDs, and not stable through a read and write. Only equipment-level descriptions
  are written for classes a profile lacks (the nearest ancestor that has properties there); an
  object that is only described in a read gets the most specific class seen. A zip is read fully
  into memory (no size limit). With `EQBD` selected and no `boundary=`, the EQBD file has no
  objects.

## Naming

- Members, methods and modules are snake_case (`sequence_number`, `voltage_levels`).
- The original CIM names are kept in `Class._cim_meta` (`cim_name`, `package`, `guid`, and per
  attribute/end `cim_name` / `cim_role`); use `cim_python_sdk._runtime.cim_attributes(cls)` for the merged view.
- Renames (keyword escapes, collisions, generated role names) are listed in
  `codegen/snapshot/naming_report.md`.

## Regenerating from the model

The generated package (`src/cim_python_sdk/model/`) is committed; regenerate only when the generator changes.

```
uv run python tools/fetch_model.py        # download + sha256-check the pinned .qea into build/model/
uv run python tools/dump_ir.py            # read the .qea, write codegen/snapshot/cim100_ir.json
uv run python tools/regen.py              # regenerate src/cim_python_sdk/model/ and _registry.py
uv run python tools/regen.py --check      # exit 1 if the committed code is out of date
```

Tests run offline from the committed IR snapshot. Never edit generated files; fix `codegen/` instead.

## Known model quirks

- **IdentifiedObject.InstanceSet:** the model has an association `IdentifiedObject.InstanceSet`
  (multiplicity `1`) to `InstanceSet`, where the other end `InstanceSetMember` is `0..*` and neither end
  is navigable in the source. The SDK generates both ends, and since the lower bound is 1, `validate()`
  reports `instance_set` as missing on every IdentifiedObject that is not linked to an `InstanceSet`.
  Filter it out if you do not use `InstanceSet`.
- **`Mass.unit`:** the model gives `Mass.unit` the default `'g'`, but `UnitSymbol` has no `g` literal.
  The default is therefore left as `None`.
- **Duplicate class names:** `Profile` and `ResourceCertification` exist in two packages, and
  `TroubleReportingKind` and `IEC61968CIMVersion` are duplicated within a package. The most referenced
  class is exported at top level (`from cim_python_sdk import Profile`); the others are reachable only by module
  path (see the table in `naming_report.md`).

## Source model and license

This repository is licensed under the [Apache License 2.0](LICENSE); see also [NOTICE](NOTICE).

The model is the CIM100 `.qea` (SQLite) file from `cimug-org/CIMTool`
(`iec61970cim17v40_iec61968cim13v13b_iec62325cim03v17b_CIM100.1.1.1.qea`), pinned by commit SHA and
sha256 in `model-source.toml` (with a mirror in `netbeheernederland/tc57cim`). The file is not committed; it
is fetched at build time. The UML project file states that it is dedicated to the public domain under an
Apache 2.0 license (the CIMTool repository that hosts it is LGPL-2.1 for its own code).

The CGMES 3.0 profiles (`cim_python_sdk.profiles`) are derived from the ENTSO-E RDFS2020 vocabularies of
`entsoe/CGMES-AP` (Apache-2.0), `CGMES/RDFS/61970-600-2_*-AP-Voc-RDFS2020.rdf`
(IEC 61970-600-2:2021), pinned by commit `e96dd4e323b1e2236e141dd03bf9adea81672e00` and per-file
sha256 in `profile-source.toml`. Classes, properties, multiplicities, enumeration literals, profile
URIs and the fixed unit multipliers all come from these files; one known error (SSH lists
`Equipment` without the `Description` stereotype) is corrected by the `[[corrections]]` table there.
The files are not committed (`tools/fetch_profiles.py` downloads them); the derived snapshot
`src/cim_python_sdk/profiles/data/cgmes_3_0.json` is. The European extension classes (`eu:`) of the model
come from the EA model of `cimug-org/CGMES-CIM17` (Apache-2.0, `ExtEuBase` package).

`tests/serialization/data/cgmes3_fixture/` is a hand-written CGMES 3.0 file set (made-up content
in the layout of the CGMES files). No ENTSO-E data is committed: the ENTSO-E CGMES 3.0 Conformity
Assessment MicroGrid BaseCase (v3.0.2, owned by ENTSO-E) is only downloaded, from a pinned copy in
`powsybl/powsybl-core` with sha256 checks, by the opt-in test (`CIM_PYTHON_SDK_CGMES_DOWNLOAD=1`).
