# CGMES 3.0 profile support: report (2026-10-31)

Branch `claude/cgmes-profile-support-1be5ef`, 17 commits from `77b00f0` (plan) to the final report
commit. Everything is local: nothing is pushed and no PR is open. Plan in [PLAN.md](PLAN.md) under
Phase 3. Milestone notes are in [PROGRESS.md](PROGRESS.md).

## Results

- **SDK:** 403 passed, 14 skipped (262 before). `ruff`, `regen.py --check`, `dump_profiles.py --check`
  and `gen_profile_stubs.py --check` are clean.
- **Example (`examples/mvlv-networks`):** 70 passed, 5 skipped. With `MVLV_FULL=1`, all 22 CGMES tests pass.
- **ENTSO-E CGMES 3.0.2 MicroGrid samples** (BE + NL + boundary, 13 files, 957 objects):
  - They read with 0 dangling references and 0 unknown classes or properties.
  - Writing them back gives the same structure. The only differences are formatting and generated
    ids (see Decisions and open issues).
- **pypowsybl 1.16.1** (only in a scratch venv):
  - Our writer's test network imports and its AC load flow converges.
  - All four MV networks import. N3 and N4 converge; N1 and N2 do not (see Decisions and open issues).
- **Performance**, for 50k objects and 14.4k terminals across EQ, SSH, TP and SV: write 1.9 s,
  read 1.2 s, validate 0.3 s.

## What you can do now

```python
from cim_python_sdk.profiles import cgmes3, validate_profile
from cim_python_sdk.profiles.cgmes3 import ACLineSegment, Terminal   # only the 490 CGMES classes (same objects as cim_python_sdk.X)
from cim_python_sdk.serialization import write_cgmes, read_cgmes, CgmesHeader

cgmes3.EQ.required(ACLineSegment)            # PropertyInfo for mRID, name, r, x, bch, ...
cgmes3.profiles_of(Terminal, "connected")    # (SSH,)
issues = validate_profile(objects, [cgmes3.EQ, cgmes3.SSH, cgmes3.TP])
report = write_cgmes(objects, "out/model.zip", header=CgmesHeader(scenario_time=...))
doc = read_cgmes("out/model.zip")            # one merged graph; doc.headers, doc.warnings
```

The README sections "CGMES 3.0 profiles" and "CGMES file sets" cover the details.

## What was built, by milestone

| # | Commit | What |
|---|---|---|
| C1 | 5c866cf | Pinned CGMES-CIM17 OWL (Apache-2.0), OWL reader, committed profile snapshot (10 profiles; URIs from ENTSO-E RDFS) |
| C2 | d5cbb30 | European `eu:` extensions (BoundaryPoint, Wind/SolarPowerPlant, LimitKind, shortName, energyIdentCodeEic, ...) generated from the pinned CGMES .qea; namespace in metadata; CIMXML/JSON-LD write `eu:` |
| R1 | 87f58c4 | Review: PASS WITH NITS; pinned the association-direction differences |
| C3 | 03b8f4e | `cim_python_sdk.profiles`: Profile/ProfileSet API, `cgmes3` facade + `.pyi`, `validate_profile` |
| C4 | 47cf3a5 | `write_cgmes`: one file per profile, `md:FullModel` headers, rdf:ID/rdf:about and mRID per the samples, profile-side association direction |
| C5 | 035ab91 | `read_cgmes`: merges a file set (dir/zip/memory) by id, headers per file, conflict and dangling reporting |
| R2 | f30ffbc | Review: PASS WITH NITS; fixes for EQ/EQBD double definition, cross-file conflicts, combined EQ+SC files, file name collisions |
| C6 | d239b7f | MV-LV example: `mvlv-cim export --format cgmes`, `prepare()` makes the four feeders CGMES-valid (0 errors), round trip, pypowsybl smoke; README/NOTICE |

## Decisions and open issues

These are ordered by how much they matter.

1. **Units: decided and done (option a).** Objects hold SI values (V, W, m); `write_cgmes`
   scales to the CGMES multipliers (kV, MW, MVAr, MVA, km) and `read_cgmes` back to SI.
   `units="cgmes"` turns it off. The multipliers are the `cims:isFixed` values of the ENTSO-E
   RDFS, pinned in `profile-source.toml` `[units]` and in the snapshot. The shift is done on the
   decimal text, so values survive a write and read exactly. The MV-LV example no longer
   converts by itself.
2. **N1 and N2 don't converge in pypowsybl.** These are the rural feeders with SWER and two-phase
   sections. They import, and their DC load flow converges, but the AC load flow does not. Likely
   causes:
   - CGMES EQ is balanced three-phase, so per-phase and SWER data is dropped;
   - all loads are 0, because the source has no load values;
   - two transformer nodes are shared (listed in `Prepared.notes`).

   This needs a closer look before anyone relies on those exports for load flow.
3. **Data CGMES EQ/SSH/TP cannot carry** (counts in
   `examples/mvlv-networks/docs/EXPORT_REPORT.md`):
   - ACLineSegmentPhase (N1 1059, N2 565) and PerLengthSequenceImpedance;
   - Names, and the Feeder (replaced by a Line container);
   - shunt `phaseConnection`;
   - SC-only transformer and source data;
   - Location data unless `--gl` is used.

   `CgmesReport.dropped` lists all of these.
4. **Generated ids.** Classes without an mRID (Sv*, CurveData, PositionPoint, DiagramObjectPoint)
   are written as `_gen<N>`. These are not UUIDs and not stable across a read and re-write.
   Deterministic UUIDv5 ids would fix it.
5. **ENTSO-E excerpt in tests: replaced.** The tests use a hand-written fixture
   (`tests/serialization/data/cgmes3_fixture/`); ENTSO-E files are only downloaded by the opt-in
   test, with sha256 checks.
6. **Profiles now come from the official ENTSO-E vocabularies; no SDK gaps.** The SDK model is
   CIM17 (IEC61970CIM17v40, the same version as the CGMES-CIM17 EA model; "CIM100" is the
   namespace name used from CIM17 on). The CIMTool OWL used before had 4 properties the official
   RDFS does not (`VsConverter.uf`, a stale `cim15:SynchronousMachine.GeneratingUnit`,
   `BasicIntervalSchedule.value1Multiplier`/`value2Multiplier`), the non-standard `Simple_Float`
   datatype, narrowed enumeration lists, looser multiplicities and an empty Dynamics profile. The
   snapshot is now built from `entsoe/CGMES-AP` (`codegen/rdfs_reader.py`): all 10 profiles,
   including **DY with 260 classes and 2,787 properties**, and every one of them maps to an SDK
   member. Differences that matter to users: `Terminal.ConductingEquipment` and
   `PhaseTapChangerLinear/NonLinear.xMin` are required in EQ, `PowerTransformerEnd.g`,
   `connectionKind` and `ratedS` are optional, and no enumeration is narrowed. One error of the
   vocabularies is corrected in `profile-source.toml` (`[[corrections]]`): SSH lists `Equipment`
   without the `Description` stereotype (reported upstream as a follow-up).
7. **Smaller items:**
   - **Header defaults:** the default modelling authority set is a placeholder
     (`http://cim-python-sdk.invalid/...`). DependentOn follows the samples' chain
     (SSH→EQ, TP→SSH, SV→TP), which differs from powsybl's own export.
   - **Reader:**
     - An object described only as `cim:Equipment` is not upgraded by typed references.
     - Zip and file reads have no size limit.
     - Conflicting values across files warn, and the last value wins.
   - **Profile validation:** `validate_profile` skips mRID and values still at their SDK default.
     `Location.PowerSystemResources` is 1..1 in the GL source.

## Suggested next steps

Look into the N1/N2 convergence, switch to stable UUIDv5 ids for
mRID-less classes, and push the branch and open a PR when you're happy.
