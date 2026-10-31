"""Phase mapping from the workbook / OpenDSS conventions to CIM ``PhaseCode``.

backend.py maps the Australian phase colours with ``{'R': 1, 'W': 2, 'B': 3}`` (``char_to_num``)
and uses OpenDSS node numbers 1, 2, 3 for the conductors; we map node 1/2/3 to CIM phases A/B/C,
so R -> A, W -> B, B -> C.

CIM ``PhaseCode`` has no ``CA`` literal: a two-phase connection is named by its sorted phases (AB,
AC, BC). The order of the colours in ``Conn_Type`` (for example ``BWR`` or ``BR``, which in
OpenDSS sets the winding-to-phase wiring) is not representable in a PhaseCode and is kept in the
equipment description instead.
"""

from __future__ import annotations

from cim_python_sdk import PhaseCode, SinglePhaseKind

COLOUR_TO_PHASE = {"R": "A", "W": "B", "B": "C"}
NODE_TO_PHASE = {"1": "A", "2": "B", "3": "C"}

_CODES = {
    "ABC": PhaseCode.ABC,
    "AB": PhaseCode.AB,
    "AC": PhaseCode.AC,
    "BC": PhaseCode.BC,
    "A": PhaseCode.A,
    "B": PhaseCode.B,
    "C": PhaseCode.C,
}
_SINGLE = {"A": SinglePhaseKind.A, "B": SinglePhaseKind.B, "C": SinglePhaseKind.C}


def conn_type_phases(conn_type: str | None) -> str | None:
    """``Conn_Type`` (e.g. ``"RWB"``, ``"BR"``, ``"R"``) to sorted CIM phase letters, or None."""
    if not conn_type:
        return None
    try:
        letters = {COLOUR_TO_PHASE[c] for c in conn_type.strip().upper()}
    except KeyError:
        return None
    if len(letters) != len(conn_type.strip()):
        return None  # a repeated colour such as "RR"
    return "".join(sorted(letters))


def node_spec_phases(spec: str | None) -> str | None:
    """OpenDSS node spec from ``lines.Start_Node_Phase`` (``"1.2.3"`` or ``"1"``) to letters."""
    if spec is None:
        return None
    parts = [p for p in str(spec).strip().split(".") if p]
    try:
        letters = {NODE_TO_PHASE[p] for p in parts}
    except KeyError:
        return None
    if not letters or len(letters) != len(parts):
        return None
    return "".join(sorted(letters))


def phase_code(letters: str) -> PhaseCode:
    """Sorted phase letters (``"ABC"``, ``"AC"``, ``"A"``) to the PhaseCode literal."""
    return _CODES[letters]


def single_phase_kind(letter: str) -> SinglePhaseKind:
    return _SINGLE[letter]


def lv_secondary_code(conn_type_len: int) -> PhaseCode:
    """Secondary PhaseCode of a distribution transformer, as backend.py wires it.

    - 3 colours: 3-phase, ``buses=[... busbar]`` -> ABC.
    - 2 colours: single phase across two MV phases, 3-winding centre-tapped secondary
      ``busbar.1.0 busbar.0.2`` -> split phase s12N.
    - 1 colour (SWER): 2-winding, secondary ``busbar.1`` -> s1N.
    """
    return {3: PhaseCode.ABC, 2: PhaseCode.s12N, 1: PhaseCode.s1N}[conn_type_len]


def phase_letters(code: PhaseCode | None) -> frozenset[str]:
    """The conductor letters of a PhaseCode, ignoring the neutral (``ABCN`` -> {A, B, C}).

    Secondary (split-phase) codes map to their own letters (``s12N`` -> {s1, s2}).
    """
    if code is None:
        return frozenset()
    name = code.name
    if name.startswith("s"):
        return frozenset(f"s{c}" for c in name[1:] if c in "12")
    return frozenset(c for c in name if c in "ABC")
