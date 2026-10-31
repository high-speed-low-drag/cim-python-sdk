# Progress

| Milestone | Scope | Status |
|---|---|---|
| S3 | Excel to CIM builder for the four MV networks (`mvlv_cim`) | done |
| S4 | Export to CIMXML / JSON-LD and round-trip (`mvlv-cim`) | done |

## S3 (branch `feat/builder`)

- `excel.py` loads the workbooks with types. `builder.py` (`build_network`) returns
  `BuiltNetwork(objects, feeder, zone_substation, source, elements, nodes, issues, islands)`.
  The other modules are `phases.py` and `ids.py`.
- Tests: 42 pass (`uv run pytest -q`, about 43 s). They check:
  - per-type counts against the sheets
  - one EquivalentInjection per distribution transformer
  - terminals and nodes
  - BFS connectivity from the source
  - BaseVoltage consistency per node
  - upstream phase subsets
  - deterministic mRIDs and issues
  - `validate()` (0 messages besides `instance_set`)
  - build time and memory
  - a synthetic quirky workbook
- Build time and tracemalloc peak: N1 2.2 s / 35 MiB, N2 2.3 s / 35 MiB, N3 0.75 s / 7 MiB,
  N4 0.63 s / 7 MiB.
- The SDK was not changed and no SDK bugs were found. A smoke test of serializing N1 with the S2
  writers worked: CIMXML 21 MB in 3.3 s, JSON-LD 23 MB in 2.4 s, no warnings.

### Decisions beyond the brief
- **Delete rows:** the 539 `lines` rows named `Delete` in network 1 are skipped, as backend.py does.
  The line count test uses sheet rows minus these.
- **mvtx classification:** by the `connections` Type (`-ISO`, `-REG`, plain `InLineTransformer`).
  KLO14's `PLENTY_VLY_RISE` (22/22 kV, 1 tap) is an in-line transformer with no tap changer.
- **Single-phase transformers** have 2 ends and `connection_kind = I`.
  - Isolating transformers: secondary `A`, the SWER conductor (node 1).
  - 2-colour lvtx: secondary `s12N`, rated per the sheet (433 V), not backend's 0.25+0.25 kV centre tap.  Issue `backend_centre_tap_differs`, once per network.
- **Regulators:** Yn/Yn (backend.py uses grounded-wye autotransformers) rather than the sheet's
  delta/wye. The tap range comes from the sheet's 17 taps, 0.7478–1.0582.
- **Off-load taps:** lvtx gives only a tap value and no range, so none is invented: one
  `RatioTapChanger` with low 0 / neutral 0 / high 1 / step 1 and increment (tap−1)×100 %.
  Regulators without a range get no tap changer (`regulator_no_tap_range`). Review notes are in
  README.md.
- **Vector group:** D/Yn uses `phase_angle_clock = 1` (OpenDSS ANSI lag).
- **BaseVoltage snapping:** a rating within 5 % snaps to a standard BaseVoltage, so the zone
  secondaries of 22.9 and 22.7 kV map to 22 kV.
- **Feeder head:** `normal_head_terminal` is the zone transformer's terminal 2. The mv_net_txs Bus2
  node sits in the zone 22 kV VoltageLevel; all other MV nodes are in the Feeder.
- **Shared mRIDs:** BaseVoltage and the AusNet GeographicalRegion mRIDs use the network key
  `shared`, so the networks can be merged.
- **Current limits:** one `CurrentLimit` per line, `min(Ampacity1, Ampacity2)` (OpenDSS normamp),
  with one shared `PATL` OperationalLimitType.
- **Source impedance:** backend.py's vsource impedance goes onto the ExternalNetworkInjection
  short-circuit attributes.
- **Shared Location:** a distribution Substation, its transformer and its injection share one
  one-point Location.
- **Source IDs:** `Element_ID` is kept as a `Name` of NameType `source_element_id`.
- **Grouped issues:** issues that repeat per row (`PVs = 'Null'`, `shared_mv_bus`,
  `single_phase_to_earth_rating`) are reported once per network, with the affected rows listed.

### Notes for S4
- `Name`, `NameType` and `PositionPoint` have no mRID, so they are written as `_gen<N>` / blank
  nodes. Compare them by content, not id.
- `PositionPoint` x/y are strings, as in the model.
- When merging networks into one document, deduplicate the shared BaseVoltage and
  GeographicalRegion objects by mRID.
- `Terminal.connected = True` is set everywhere.
- `RatioTapChanger.step` is a float.

## S4 (branch `feat/builder`)

- `export.py` (workbook discovery, header, writers), `verify.py` (round trip), `cli.py` (`mvlv-cim export|verify|summary`).
- All four networks round-trip in CIMXML and JSON-LD, the two read graphs are equal, exports are byte-identical, 0 warnings, 0 dangling. See `docs/EXPORT_REPORT.md`.
- One builder fix found by the round trip: `RatioTapChanger.step` of fixed taps is now a float (was int, read back as float).
- Tests: `tests/test_export.py`; N1 and N2 need `MVLV_FULL=1`. `MVLV_FULL=1 uv run pytest -q`: 53 pass. SDK not changed.

## C6 (Phase 3, branch `claude/cgmes-profile-support-1be5ef`)

- `cgmes.py` (`prepare`, `export_cgmes`, `cgmes_view`), `mvlv-cim export --format cgmes|all [--zip] [--gl]`, `verify --cgmes`, `scripts/pypowsybl_smoke.py`, `tests/test_cgmes.py`.
- `validate_profile` against EQ, SSH, TP: 0 errors for all four networks (and with GL); `read_cgmes` equals the CGMES view; byte-identical re-export. Placeholders (p = q = 0 etc.) and everything CGMES cannot carry are in `docs/EXPORT_REPORT.md`.
