# Export report (S4, C6)

Generated from a real run of `mvlv-cim verify --all` (all four networks, both formats). The
generated files are in `out/` (gitignored, not committed). The CGMES 3.0 export (C6) has its own
section below.

## Result

Every network round-trips in both formats: `canonical_dump` of the built graph equals that of the
graph read back from CIMXML and from JSON-LD, the two read graphs equal each other, exporting twice
gives byte-identical files, and there are 0 warnings and 0 dangling references.

### Objects by main class

| Network | Objects | ACLineSegment | Terminal | ConnectivityNode | PowerTransformer | PowerTransformerEnd | RatioTapChanger | EquivalentInjection | LinearShuntCompensator |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Network_1_Rural_SMR8 | 47074 | 3611 | 9363 | 4329 | 717 | 1434 | 542 | 704 | 2 |
| Network_2_Rural_KLO14 | 48566 | 3824 | 9773 | 4533 | 711 | 1422 | 502 | 700 | 2 |
| Network_3_Urban_HPK11 | 6538 | 593 | 1321 | 639 | 45 | 90 | 0 | 44 | 0 |
| Network_4_Urban_CRE21 | 7548 | 649 | 1538 | 723 | 80 | 160 | 0 | 79 | 0 |

Other classes per network (Location, PositionPoint, Name, CurrentLimit, ...) are counted in the
total and in `mvlv-cim summary`.

### Files, times and checks

Times are wall clock on the 4-CPU server (the writes include nothing but serialization).

| Network | Format | Size (MB) | Write (s) | Read (s) | Round-trip equal | Deterministic | Warnings | Dangling |
|---|---|---:|---:|---:|---|---|---:|---:|
| Network_1_Rural_SMR8 | .xml | 21.1 | 3.2 | 1.7 | yes | yes | 0 | 0 |
| Network_1_Rural_SMR8 | .jsonld | 23.3 | 2.4 | 1.4 | yes | yes | 0 | 0 |
| Network_1_Rural_SMR8 | xml = jsonld | | | | yes | | | |
| Network_2_Rural_KLO14 | .xml | 21.7 | 3.1 | 1.7 | yes | yes | 0 | 0 |
| Network_2_Rural_KLO14 | .jsonld | 24.0 | 2.4 | 1.4 | yes | yes | 0 | 0 |
| Network_2_Rural_KLO14 | xml = jsonld | | | | yes | | | |
| Network_3_Urban_HPK11 | .xml | 2.8 | 0.3 | 0.4 | yes | yes | 0 | 0 |
| Network_3_Urban_HPK11 | .jsonld | 3.1 | 0.3 | 0.1 | yes | yes | 0 | 0 |
| Network_3_Urban_HPK11 | xml = jsonld | | | | yes | | | |
| Network_4_Urban_CRE21 | .xml | 3.3 | 0.4 | 0.2 | yes | yes | 0 | 0 |
| Network_4_Urban_CRE21 | .jsonld | 3.6 | 0.3 | 0.2 | yes | yes | 0 | 0 |
| Network_4_Urban_CRE21 | xml = jsonld | | | | yes | | | |

Each file holds every object of its network, including the 5 shared BaseVoltages and the shared
GeographicalRegion. The only round-trip discrepancy found was in the builder, not the SDK:
`RatioTapChanger.step` of the fixed off-load taps was the int `1` and came back as the float `1.0`.
It is now a float in `builder.py` (as for the regulators).

`canonical_dump` already handles objects without an mRID (`Name`, `PositionPoint`, `Location`
children): their `gen<N>` ids come from a content-based sort, so they compare by content.

## Header

The `created` timestamp is the UTC mtime of the source workbook (or `--created`), so output is
deterministic for a given checkout. Source URL and licence are in the `description` entries.

```xml
<md:FullModel rdf:about="urn:uuid:c43abbdd-d9fd-5b77-98f8-f0831b3a9f45">
    <md:Model.created>2026-10-27T09:27:58Z</md:Model.created>
    <md:Model.version>1</md:Model.version>
    <md:Model.modelingAuthoritySet>urn:x-mvlv-cim:authority:ausnet-mv-lv-networks</md:Model.modelingAuthoritySet>
    <md:Model.description>CIM100 model of Network_3_Urban_HPK11 (feeder HPK11); MV network with LV equivalents (EquivalentInjection per distribution transformer)</md:Model.description>
    <md:Model.description>Source data: https://github.com/Team-Nando/MV-LV-Networks (workbook Network_3_Urban_HPK11.xlsx), licence BSD-3-Clause, (c) 2024 Team Nando</md:Model.description>
  </md:FullModel>
```

```json
{
  "@id": "urn:uuid:c43abbdd-d9fd-5b77-98f8-f0831b3a9f45",
  "@type": "dcat:Dataset",
  "prov:generatedAtTime": {
    "@value": "2026-10-27T09:27:58Z",
    "@type": "xsd:dateTime"
  },
  "dcterms:issued": {
    "@value": "2026-10-27",
    "@type": "xsd:date"
  },
  "dcat:version": "1",
  "dcat:isVersionOf": {
    "@id": "urn:x-mvlv-cim:authority:ausnet-mv-lv-networks"
  },
  "dcterms:description": [
    {
      "@value": "CIM100 model of Network_3_Urban_HPK11 (feeder HPK11); MV network with LV equivalents (EquivalentInjection per distribution transformer)",
      "@language": "en"
    },
    {
      "@value": "Source data: https://github.com/Team-Nando/MV-LV-Networks (workbook Network_3_Urban_HPK11.xlsx), licence BSD-3-Clause, (c) 2024 Team Nando",
      "@language": "en"
    }
  ]
}
```

## Reproduce

```
cd ~/claude_code/cim_python_sdk-networks
uv sync
uv run mvlv-cim export --all --format both --out out/ --source ~/claude_code/MV-LV-Networks
uv run mvlv-cim verify --all          # build, write, read, compare, determinism (about 55 s)
uv run mvlv-cim summary               # counts by class
uv run pytest -q                      # N3 and N4 round trip
MVLV_FULL=1 uv run pytest -q          # also N1 and N2 (about 2 min)
```

## CGMES 3.0 export (C6)

`mvlv-cim export --format cgmes [--zip] [--gl]` writes one CGMES 3.0 file set per network with
`cim_python_sdk.serialization.write_cgmes`: EQ, SSH and TP (and GL with `--gl`), `out/<workbook>_CGMES/` or
`out/<workbook>_CGMES.zip`. No SV file: the data has no state values (voltages, flows, tap
positions solved by a power flow), so there is no principled content for it. Numbers below are from
`mvlv-cim verify --all --cgmes` and `scripts/pypowsybl_smoke.py` (macOS, one run).

### Result

`mvlv_cim.cgmes.prepare(net)` turns the plain graph into a CGMES-valid one (list below), then
`validate_profile` against EQ, SSH and TP gives **0 errors for all four networks** (also with GL).
The files read back (`read_cgmes`) to exactly the CGMES view of the graph (`cgmes_view`: the objects
whose class a selected profile defines, their attributes and ends that a profile lists, and the links
between them), with 0 reader warnings and 0 dangling references, and a second export is byte for byte
identical (model ids are `uuid5`, times come from `--created` or the source file's mtime).

| Network | EQ (MB) | SSH (MB) | TP (MB) | zip (MB) | Objects in the files | validate_profile errors | warnings | Not carried | Write (s) | Read (s) | Round trip | Deterministic |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Network_1_Rural_SMR8 | 21.5 | 3.5 | 5.0 | 3.9 | 41634 | 0 | 17862 | 35592 | 2.4 | 2.5 | yes | yes |
| Network_2_Rural_KLO14 | 22.4 | 3.6 | 5.2 | 4.1 | 43439 | 0 | 17851 | 35890 | 2.4 | 2.7 | yes | yes |
| Network_3_Urban_HPK11 | 2.9 | 0.5 | 0.7 | 0.5 | 5888 | 0 | 2190 | 4710 | 0.4 | 0.3 | yes | yes |
| Network_4_Urban_CRE21 | 3.4 | 0.6 | 0.8 | 0.6 | 6798 | 0 | 2673 | 5524 | 0.4 | 0.3 | yes | yes |

"Objects in the files" are the objects of the prepared graph (59364, 61478, 8408 and 9649 in all)
that EQ, SSH or TP define. "Warnings" are `validate_profile` warnings, one per value the profiles do
not list (next section), and "Not carried" is the writer's `CgmesReport.dropped` (the same facts,
counted per object or value); both are information, not defects. With `--gl` the files grow by
0.8 to 6.3 MB (GL), the not-carried count falls to 2112, 2527, 17580 and 17052, and the errors stay 0.

### What `prepare` adds or changes (all in place, on a fresh build)

The plain build and its tests are unchanged: `prepare` is a separate step that `export --format
cgmes` and `verify --cgmes` run on a second build.

| Need | What is done |
|---|---|
| Containers | CGMES 3.0 has no `Feeder`. One `Line` named after the feeder takes the feeder's `ConnectivityNode`s and equipment (lines, capacitors, in-line transformers). |
| Transformer sites | `PowerTransformer` terminals must sit on nodes in a `VoltageLevel` of the transformer's `Substation` (pypowsybl otherwise: "Transformer must be within a substation"). Each distribution transformer gets a VoltageLevel `<substation> 22 kV` for its MV node, which moves from the Line into it; each in-line (isolating, regulating) transformer gets a new `Substation` `<name> site` with a VoltageLevel per end (N1: 12, N2: 10). Two transformers on one MV node (N1: BUSH_PEA_10, GREY_BOX_2) cannot both own it, so the later one keeps its terminal in the first one's substation (reported in `Prepared.notes`). |
| Line values | `ACLineSegment.r, x, bch, gch` (required by EQ) = the linecode's per-length value times the line length (from the source, nothing assumed). `r0, x0, b0ch, g0ch` are ShortCircuit profile data (see below). |
| Limits | `OperationalLimitSet.Terminal` is required, so the existing set is tied to terminal 1 and a copy (same value, new mRID) to terminal 2: 2 sets and 2 `CurrentLimit`s per line. `OperationalLimitType.kind = patl` (the name of the type). |
| TopologicalNodes | One per `ConnectivityNode`, 1:1 (N1 4329, N2 4533, N3 639, N4 723); `Terminal.TopologicalNode` set; `BaseVoltage` from the equipment at the node, container = the node's container. The data has no `Switch`, so merging TopologicalNodes across closed switches would give the same result. |
| SSH, from the data | `Terminal.connected = true` (already), `Equipment.inService = true` (the data has no out-of-service state), `RatioTapChanger.step`, `LinearShuntCompensator.sections` (source values). |
| SSH, **placeholders** | **The data has no load, injection or dispatch values.** `EquivalentInjection.p = q = 0` (704 / 700 / 44 / 79 of them) and `ExternalNetworkInjection.p = q = 0`, `minP = maxP = minQ = maxQ = 0`, `governorSCD = 0`, `controlEnabled = false` are placeholders required by the profile. They say nothing about the real network (load flows of these files carry no load, and the infeed has no reactive range). `ExternalNetworkInjection.referencePriority = 1` because it is the only infeed. The `md:Model.description` of every file says so. |
| Units | The builder stores SI base units, CGMES fixes kV, MW, MVAr, MVA and km (ohm, siemens, ampere, percent unchanged). `prepare` divides every `Voltage` (V to kV), `ActivePower`, `ReactivePower`, `ApparentPower` (to M) and `Length` (m to km) value. Without it a consumer reads 22000 kV: pypowsybl rejected the voltage setpoint as implausible until this was done. |
| GL only | The GL profile allows one `PowerSystemResource` per `Location`, the builder shares a transformer site's location between substation, transformer and injection. Each extra resource gets a copy of the Location and its PositionPoint (N3 +90, N4 +160, N1 +1410, N2 +1402). |

Not changed: names, descriptions, phases, ratings, tap data, mRIDs.

### Header

Every file: `modelingAuthoritySet` = `urn:x-mvlv-cim:authority:ausnet-mv-lv-networks`; `created` and
`scenarioTime` = `--created`, else the source file's mtime; `version` 1; `md:Model.profile` the
CGMES 3.0 profile URI; `DependentOn` EQ <- SSH <- TP (the ENTSO-E sample chain); a `uuid5` model id per
network and profile; `description` with the source repository, the workbook, BSD-3-Clause and
"(c) 2024 Team Nando", and the note that load and dispatch values are placeholders.

### What CGMES cannot carry

Counts are `CgmesReport.dropped` per network (objects or values). The profiles EQ, SSH and TP have no
place for them; the CIMXML and JSON-LD exports keep all of it.

| Data | CIM100 | N1 | N2 | N3 | N4 | Why / where it could go |
|---|---|---:|---:|---:|---:|---|
| Coordinates | `Location`, `PositionPoint`, `CoordinateSystem` (`PowerSystemResource.Location`) | 4330 / 7941 / 1 / 5740 | 4537 / 8361 / 1 / 5939 | 638 / 1231 / 1 / 728 | 729 / 1378 / 1 / 889 | GL profile (`--gl`): carried, with the copies above. A local `urn:x-local:anonymised-xy` CRS is still a CRS URN, but GIS tools will not place it. |
| Per-phase line data | `ACLineSegmentPhase` (single-phase SWER sections) | 1059 | 565 | 0 | 0 | No class in any CGMES 3.0 profile. The phase survives as `Terminal.phases = A`; the per-phase sequence number is lost. |
| Per-length impedance | `PerLengthSequenceImpedance`, `ACLineSegment.PerLengthImpedance` | 67 / 3611 | 36 / 3824 | 10 / 593 | 13 / 649 | CGMES has totals only (used: `r, x, bch, gch`). The linecode name and description (cable type, material, size, ampacities) are lost. |
| Zero-sequence line data | `r0, x0, b0ch, g0ch` of the linecode | all | all | all | all | ShortCircuit profile (SC); not written because SC requires data the source does not have (`shortCircuitEndTemperature`, `PowerTransformer.isPartOfGeneratorUnit`, ...). Never copied onto the line, so also lost from the EQ view. |
| Source impedance | `ExternalNetworkInjection.maxInitialSymShCCurrent`, `maxR1ToX1Ratio`, `maxR0ToX0Ratio`, `maxZ0ToZ1Ratio`, `voltageFactor` | 1 each | 1 each | 1 each | 1 each | SC profile only. |
| Names | `Name`, `NameType` (`source_element_id`), `IdentifiedObject.Names` | 4330 / 1 | 4537 / 1 | 638 / 1 | 728 / 1 | CGMES has `IdentifiedObject.name` only. The workbook `Element_ID` is lost; rebuild it from the mRID (`uuid5`, see `ids.py`) or the CIMXML export. |
| Feeder | `Feeder`, `Substation.NormalEnergizingFeeder` / `NormalEnergizedFeeder`, `Terminal.NormalHeadFeeder` | 1 + 705 + 1 | 1 + 701 + 1 | 1 + 45 + 1 | 1 + 80 + 1 | Replaced by the `Line` container (name kept); the normal head terminal is lost. |
| Transformer vector data | `PowerTransformer.vectorGroup`, `PowerTransformerEnd.phaseAngleClock`, `TransformerEnd.grounded` | 717 / 1434 / 258 | 711 / 1422 / 144 | 45 / 90 / 45 | 80 / 160 / 81 | SC profile. `connectionKind` is carried (EQ), but not whether a wye is grounded or the clock number. |
| Shunt phase connection | `ShuntCompensator.phaseConnection` | 2 | 2 | 0 | 0 | Not in the EQ/SSH profiles (`grounded` is). |

The writer lists exactly these in `CgmesReport.dropped`, and `verify --cgmes` reports
`n_warnings` (the `validate_profile` warnings) next to them.

### Remaining `validate_profile` warnings

Every warning is "property X is set but no selected profile lists it". They are the list above,
per object: `ACLineSegment.PerLengthImpedance`, `IdentifiedObject.Names` and
`PowerSystemResource.Location` on lines, transformers, substations and injections,
`PowerTransformer.vectorGroup`, `PowerTransformerEnd.phaseAngleClock`, `TransformerEnd.grounded`,
`Substation.NormalEnergizingFeeder`, the five source-impedance attributes, `Terminal.NormalHeadFeeder`,
`ShuntCompensator.phaseConnection` and `ACLineSegment.ACLineSegmentPhases`. Nothing else is
reported. Objects of classes outside the profiles (Feeder, Name, ...) are not validated; they are
not written (`CgmesReport.dropped`).

### pypowsybl

pypowsybl 1.16.1 in a throwaway environment (`uv run --no-project --with pypowsybl python
scripts/pypowsybl_smoke.py <zip>`; not a project dependency) loads all four zip files without
warnings, with these element counts (loads: 0, there are none):

| Network | Substations | Voltage levels | Buses | Lines | 2-winding transformers | Generators | Shunts | Ratio tap changers | Operational limits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Network_1_Rural_SMR8 | 715 | 4329 | 3576 | 3611 | 717 | 705 | 2 | 542 | 7222 |
| Network_2_Rural_KLO14 | 711 | 4533 | 4456 | 3824 | 711 | 701 | 2 | 502 | 7648 |
| Network_3_Urban_HPK11 | 45 | 639 | 631 | 593 | 45 | 45 | 0 | 0 | 1186 |
| Network_4_Urban_CRE21 | 80 | 723 | 699 | 649 | 80 | 80 | 0 | 0 | 1298 |

(Equivalent and external network injections become generators; the line limits appear on both
sides.) With `--gl` the same counts for N3 and N4.

AC load flow, a smoke test only because there is no load: the script gives the infeed a voltage
setpoint (the export does not, and its zero reactive range would make OpenLoadFlow ignore it).
**N3 and N4 converge in one iteration**, voltages 1.000 to 1.001 pu (line charging only).
**N1 and N2 do not converge** (Newton-Raphson, 16 iterations), also with DC initialisation. The
cause was not found. Tested in pypowsybl, each without effect: disconnecting the capacitors, the
isolating and regulating transformers, all distribution transformers (leaving only the zone
transformer and the lines), the equivalent-injection generators, long lines, and raising the lines
with impedance below 1 mOhm. powsybl leaves 751 line ends of N1 (dead ends) unconnected to a bus
although every `Terminal.connected` is true. Do not read the N1/N2 result as a data error; it is
unexplained.

### Reproduce

```
uv run mvlv-cim export --all --format cgmes --out out           # directories
uv run mvlv-cim export -n 3 --format cgmes --zip --gl --out out  # one zip, with GL
uv run mvlv-cim verify --all --cgmes [--gl]                      # validate, round trip, determinism
uv run --no-project --with pypowsybl python scripts/pypowsybl_smoke.py out/Network_3_Urban_HPK11_CGMES.zip
```

Tests: `tests/test_cgmes.py` (N3, N4 by default; N1, N2 with `MVLV_FULL=1`).

## Sample from Network_3_Urban_HPK11

One ACLineSegment, its two Terminals, one distribution PowerTransformer with its two ends, and the
EquivalentInjection of the first listed injection (ids and order as written).

### CIMXML (`out/Network_3_Urban_HPK11.xml`)

```xml
  <cim:ACLineSegment rdf:ID="_01a9bc18-aa54-52ec-87fd-da5f7c8bbb77">
    <cim:Conductor.length>55.313</cim:Conductor.length>
    <cim:IdentifiedObject.description>linecode=2-3ph; line_number=428</cim:IdentifiedObject.description>
    <cim:IdentifiedObject.name>CDR017</cim:IdentifiedObject.name>
    <cim:ACLineSegment.PerLengthImpedance rdf:resource="#_5b83b26e-ebb5-577a-a541-de586d3ed253" />
    <cim:ConductingEquipment.BaseVoltage rdf:resource="#_d73b3142-13eb-5b25-ba19-3b678882f4be" />
    <cim:Equipment.EquipmentContainer rdf:resource="#_38608542-69a8-5329-9092-7adbccda990d" />
    <cim:PowerSystemResource.Location rdf:resource="#_0aac0de7-4b94-5647-b016-6c3f93750d37" />
  </cim:ACLineSegment>
  <cim:Terminal rdf:ID="_68cd08c3-8bab-5a84-80ae-a0489726c870">
    <cim:ACDCTerminal.connected>true</cim:ACDCTerminal.connected>
    <cim:ACDCTerminal.sequenceNumber>1</cim:ACDCTerminal.sequenceNumber>
    <cim:IdentifiedObject.name>CDR017 T1</cim:IdentifiedObject.name>
    <cim:Terminal.phases rdf:resource="http://iec.ch/TC57/CIM100#PhaseCode.ABC" />
    <cim:Terminal.ConductingEquipment rdf:resource="#_01a9bc18-aa54-52ec-87fd-da5f7c8bbb77" />
    <cim:Terminal.ConnectivityNode rdf:resource="#_f06139e9-f4e2-555a-ae06-311675555235" />
  </cim:Terminal>
  <cim:Terminal rdf:ID="_e428767e-c4c6-5771-bc5e-a5c4c0235788">
    <cim:ACDCTerminal.connected>true</cim:ACDCTerminal.connected>
    <cim:ACDCTerminal.sequenceNumber>2</cim:ACDCTerminal.sequenceNumber>
    <cim:IdentifiedObject.name>CDR017 T2</cim:IdentifiedObject.name>
    <cim:Terminal.phases rdf:resource="http://iec.ch/TC57/CIM100#PhaseCode.ABC" />
    <cim:Terminal.ConductingEquipment rdf:resource="#_01a9bc18-aa54-52ec-87fd-da5f7c8bbb77" />
    <cim:Terminal.ConnectivityNode rdf:resource="#_9e6a8e3d-9be0-5319-b8ec-1d6abcb2c7f8" />
  </cim:Terminal>
  <cim:PowerTransformer rdf:ID="_0103d791-2113-5379-9f41-f13a93823b47">
    <cim:IdentifiedObject.description>source=lvtx; conn_type=RWB; wdg1_tap=1</cim:IdentifiedObject.description>
    <cim:IdentifiedObject.name>MICHELLE_SIMON</cim:IdentifiedObject.name>
    <cim:PowerTransformer.vectorGroup>Dyn1</cim:PowerTransformer.vectorGroup>
    <cim:Equipment.EquipmentContainer rdf:resource="#_19a4d483-c096-5b1a-8cea-112048127744" />
    <cim:PowerSystemResource.Location rdf:resource="#_d9f60ee3-595a-5351-84f0-6e51de336207" />
  </cim:PowerTransformer>
  <cim:PowerTransformerEnd rdf:ID="_5876226c-e947-52d8-b994-2ae95e789aad">
    <cim:IdentifiedObject.name>MICHELLE_SIMON end 1</cim:IdentifiedObject.name>
    <cim:PowerTransformerEnd.b>0.0</cim:PowerTransformerEnd.b>
    <cim:PowerTransformerEnd.connectionKind rdf:resource="http://iec.ch/TC57/CIM100#WindingConnection.D" />
    <cim:PowerTransformerEnd.g>7.8099173553719e-07</cim:PowerTransformerEnd.g>
    <cim:PowerTransformerEnd.phaseAngleClock>0</cim:PowerTransformerEnd.phaseAngleClock>
    <cim:PowerTransformerEnd.r>19.97460317460318</cim:PowerTransformerEnd.r>
    <cim:PowerTransformerEnd.ratedS>315000.0</cim:PowerTransformerEnd.ratedS>
    <cim:PowerTransformerEnd.ratedU>22000.0</cim:PowerTransformerEnd.ratedU>
    <cim:PowerTransformerEnd.x>59.15555555555556</cim:PowerTransformerEnd.x>
    <cim:TransformerEnd.endNumber>1</cim:TransformerEnd.endNumber>
    <cim:PowerTransformerEnd.PowerTransformer rdf:resource="#_0103d791-2113-5379-9f41-f13a93823b47" />
    <cim:TransformerEnd.BaseVoltage rdf:resource="#_d73b3142-13eb-5b25-ba19-3b678882f4be" />
    <cim:TransformerEnd.Terminal rdf:resource="#_568d8dd4-8920-553a-b12c-f42b9991935a" />
  </cim:PowerTransformerEnd>
  <cim:PowerTransformerEnd rdf:ID="_995340e0-9ef4-553a-9c40-c7fe57dfcf77">
    <cim:IdentifiedObject.name>MICHELLE_SIMON end 2</cim:IdentifiedObject.name>
    <cim:PowerTransformerEnd.b>0.0</cim:PowerTransformerEnd.b>
    <cim:PowerTransformerEnd.connectionKind rdf:resource="http://iec.ch/TC57/CIM100#WindingConnection.Yn" />
    <cim:PowerTransformerEnd.g>0.0</cim:PowerTransformerEnd.g>
    <cim:PowerTransformerEnd.phaseAngleClock>1</cim:PowerTransformerEnd.phaseAngleClock>
    <cim:PowerTransformerEnd.r>0.0</cim:PowerTransformerEnd.r>
    <cim:PowerTransformerEnd.ratedS>315000.0</cim:PowerTransformerEnd.ratedS>
    <cim:PowerTransformerEnd.ratedU>433.0</cim:PowerTransformerEnd.ratedU>
    <cim:PowerTransformerEnd.x>0.0</cim:PowerTransformerEnd.x>
    <cim:TransformerEnd.endNumber>2</cim:TransformerEnd.endNumber>
    <cim:TransformerEnd.grounded>true</cim:TransformerEnd.grounded>
    <cim:PowerTransformerEnd.PowerTransformer rdf:resource="#_0103d791-2113-5379-9f41-f13a93823b47" />
    <cim:TransformerEnd.BaseVoltage rdf:resource="#_d7f0a76a-e700-5a32-8fab-10abb4d982a8" />
    <cim:TransformerEnd.Terminal rdf:resource="#_7e0388b0-6320-50d9-b003-68950338d29d" />
  </cim:PowerTransformerEnd>
  <cim:EquivalentInjection rdf:ID="_02eee1ac-15d7-56fd-bd21-55045548417f">
    <cim:EquivalentInjection.regulationCapability>false</cim:EquivalentInjection.regulationCapability>
    <cim:IdentifiedObject.description>type=RES; customers=136; pvs=47; lv_feeders=4</cim:IdentifiedObject.description>
    <cim:IdentifiedObject.name>VON_NIDA_DULWICH LV equivalent</cim:IdentifiedObject.name>
    <cim:ConductingEquipment.BaseVoltage rdf:resource="#_d7f0a76a-e700-5a32-8fab-10abb4d982a8" />
    <cim:Equipment.EquipmentContainer rdf:resource="#_325713d7-1b7a-5a7c-94c3-bc86db93f2a9" />
    <cim:PowerSystemResource.Location rdf:resource="#_602779d7-3b1c-5efe-87ee-8916e92321a9" />
  </cim:EquivalentInjection>
```

### JSON-LD (`out/Network_3_Urban_HPK11.jsonld`)

```json
{
  "@id": "urn:uuid:01a9bc18-aa54-52ec-87fd-da5f7c8bbb77",
  "@type": "cim:ACLineSegment",
  "cim:Conductor.length": 55.313,
  "cim:IdentifiedObject.description": "linecode=2-3ph; line_number=428",
  "cim:IdentifiedObject.mRID": "01a9bc18-aa54-52ec-87fd-da5f7c8bbb77",
  "cim:IdentifiedObject.name": "CDR017",
  "cim:ACLineSegment.PerLengthImpedance": {
    "@id": "urn:uuid:5b83b26e-ebb5-577a-a541-de586d3ed253"
  },
  "cim:ConductingEquipment.BaseVoltage": {
    "@id": "urn:uuid:d73b3142-13eb-5b25-ba19-3b678882f4be"
  },
  "cim:Equipment.EquipmentContainer": {
    "@id": "urn:uuid:38608542-69a8-5329-9092-7adbccda990d"
  },
  "cim:PowerSystemResource.Location": {
    "@id": "urn:uuid:0aac0de7-4b94-5647-b016-6c3f93750d37"
  }
},
{
  "@id": "urn:uuid:68cd08c3-8bab-5a84-80ae-a0489726c870",
  "@type": "cim:Terminal",
  "cim:ACDCTerminal.connected": true,
  "cim:ACDCTerminal.sequenceNumber": 1,
  "cim:IdentifiedObject.mRID": "68cd08c3-8bab-5a84-80ae-a0489726c870",
  "cim:IdentifiedObject.name": "CDR017 T1",
  "cim:Terminal.phases": {
    "@id": "cim:PhaseCode.ABC"
  },
  "cim:Terminal.ConductingEquipment": {
    "@id": "urn:uuid:01a9bc18-aa54-52ec-87fd-da5f7c8bbb77"
  },
  "cim:Terminal.ConnectivityNode": {
    "@id": "urn:uuid:f06139e9-f4e2-555a-ae06-311675555235"
  }
},
{
  "@id": "urn:uuid:e428767e-c4c6-5771-bc5e-a5c4c0235788",
  "@type": "cim:Terminal",
  "cim:ACDCTerminal.connected": true,
  "cim:ACDCTerminal.sequenceNumber": 2,
  "cim:IdentifiedObject.mRID": "e428767e-c4c6-5771-bc5e-a5c4c0235788",
  "cim:IdentifiedObject.name": "CDR017 T2",
  "cim:Terminal.phases": {
    "@id": "cim:PhaseCode.ABC"
  },
  "cim:Terminal.ConductingEquipment": {
    "@id": "urn:uuid:01a9bc18-aa54-52ec-87fd-da5f7c8bbb77"
  },
  "cim:Terminal.ConnectivityNode": {
    "@id": "urn:uuid:9e6a8e3d-9be0-5319-b8ec-1d6abcb2c7f8"
  }
},
{
  "@id": "urn:uuid:0103d791-2113-5379-9f41-f13a93823b47",
  "@type": "cim:PowerTransformer",
  "cim:IdentifiedObject.description": "source=lvtx; conn_type=RWB; wdg1_tap=1",
  "cim:IdentifiedObject.mRID": "0103d791-2113-5379-9f41-f13a93823b47",
  "cim:IdentifiedObject.name": "MICHELLE_SIMON",
  "cim:PowerTransformer.vectorGroup": "Dyn1",
  "cim:Equipment.EquipmentContainer": {
    "@id": "urn:uuid:19a4d483-c096-5b1a-8cea-112048127744"
  },
  "cim:PowerSystemResource.Location": {
    "@id": "urn:uuid:d9f60ee3-595a-5351-84f0-6e51de336207"
  }
},
{
  "@id": "urn:uuid:5876226c-e947-52d8-b994-2ae95e789aad",
  "@type": "cim:PowerTransformerEnd",
  "cim:IdentifiedObject.mRID": "5876226c-e947-52d8-b994-2ae95e789aad",
  "cim:IdentifiedObject.name": "MICHELLE_SIMON end 1",
  "cim:PowerTransformerEnd.b": 0.0,
  "cim:PowerTransformerEnd.connectionKind": {
    "@id": "cim:WindingConnection.D"
  },
  "cim:PowerTransformerEnd.g": 7.8099173553719e-07,
  "cim:PowerTransformerEnd.phaseAngleClock": 0,
  "cim:PowerTransformerEnd.r": 19.97460317460318,
  "cim:PowerTransformerEnd.ratedS": 315000.0,
  "cim:PowerTransformerEnd.ratedU": 22000.0,
  "cim:PowerTransformerEnd.x": 59.15555555555556,
  "cim:TransformerEnd.endNumber": 1,
  "cim:PowerTransformerEnd.PowerTransformer": {
    "@id": "urn:uuid:0103d791-2113-5379-9f41-f13a93823b47"
  },
  "cim:TransformerEnd.BaseVoltage": {
    "@id": "urn:uuid:d73b3142-13eb-5b25-ba19-3b678882f4be"
  },
  "cim:TransformerEnd.Terminal": {
    "@id": "urn:uuid:568d8dd4-8920-553a-b12c-f42b9991935a"
  }
},
{
  "@id": "urn:uuid:995340e0-9ef4-553a-9c40-c7fe57dfcf77",
  "@type": "cim:PowerTransformerEnd",
  "cim:IdentifiedObject.mRID": "995340e0-9ef4-553a-9c40-c7fe57dfcf77",
  "cim:IdentifiedObject.name": "MICHELLE_SIMON end 2",
  "cim:PowerTransformerEnd.b": 0.0,
  "cim:PowerTransformerEnd.connectionKind": {
    "@id": "cim:WindingConnection.Yn"
  },
  "cim:PowerTransformerEnd.g": 0.0,
  "cim:PowerTransformerEnd.phaseAngleClock": 1,
  "cim:PowerTransformerEnd.r": 0.0,
  "cim:PowerTransformerEnd.ratedS": 315000.0,
  "cim:PowerTransformerEnd.ratedU": 433.0,
  "cim:PowerTransformerEnd.x": 0.0,
  "cim:TransformerEnd.endNumber": 2,
  "cim:TransformerEnd.grounded": true,
  "cim:PowerTransformerEnd.PowerTransformer": {
    "@id": "urn:uuid:0103d791-2113-5379-9f41-f13a93823b47"
  },
  "cim:TransformerEnd.BaseVoltage": {
    "@id": "urn:uuid:d7f0a76a-e700-5a32-8fab-10abb4d982a8"
  },
  "cim:TransformerEnd.Terminal": {
    "@id": "urn:uuid:7e0388b0-6320-50d9-b003-68950338d29d"
  }
},
{
  "@id": "urn:uuid:02eee1ac-15d7-56fd-bd21-55045548417f",
  "@type": "cim:EquivalentInjection",
  "cim:EquivalentInjection.regulationCapability": false,
  "cim:IdentifiedObject.description": "type=RES; customers=136; pvs=47; lv_feeders=4",
  "cim:IdentifiedObject.mRID": "02eee1ac-15d7-56fd-bd21-55045548417f",
  "cim:IdentifiedObject.name": "VON_NIDA_DULWICH LV equivalent",
  "cim:ConductingEquipment.BaseVoltage": {
    "@id": "urn:uuid:d7f0a76a-e700-5a32-8fab-10abb4d982a8"
  },
  "cim:Equipment.EquipmentContainer": {
    "@id": "urn:uuid:325713d7-1b7a-5a7c-94c3-bc86db93f2a9"
  },
  "cim:PowerSystemResource.Location": {
    "@id": "urn:uuid:602779d7-3b1c-5efe-87ee-8916e92321a9"
  }
}
```
