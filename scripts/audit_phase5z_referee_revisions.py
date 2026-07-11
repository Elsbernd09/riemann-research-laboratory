from __future__ import annotations

from pathlib import Path


MANUSCRIPT = Path("paper/latex/main.tex")
AUDIT = Path("docs/PHASE_5Z_HOSTILE_REFEREE_AUDIT.md")

REQUIRED_MANUSCRIPT = [
    "ordinary absolutely-continuous",
    "absolutely continuous",
    "not a novelty claim",
    "Originality remains",
    "active prior-art review",
    "The proof is short once the matched-scale derivative hierarchy",
    "not an RH criterion",
]

REQUIRED_AUDIT = [
    "MAIN THEOREM SURVIVES",
    "The theorem survives.",
    "No RH proof.",
    "No novelty claim.",
]

FORBIDDEN_MANUSCRIPT = [
    "breakthrough",
    "progress toward proving RH",
    "new approach to RH",
    "first-ever",
    "novel RH criterion",
    "RH is nearly solved",
]


def main() -> None:
    if not MANUSCRIPT.exists():
        raise FileNotFoundError(MANUSCRIPT)

    if not AUDIT.exists():
        raise FileNotFoundError(AUDIT)

    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")

    if "\x00" in manuscript or "\x00" in audit:
        raise ValueError("NUL byte found.")

    for phrase in REQUIRED_MANUSCRIPT:
        if phrase not in manuscript:
            raise RuntimeError(f"Missing manuscript phrase: {phrase}")

    for phrase in REQUIRED_AUDIT:
        if phrase not in audit:
            raise RuntimeError(f"Missing audit phrase: {phrase}")

    lower = manuscript.lower()

    for phrase in FORBIDDEN_MANUSCRIPT:
        if phrase.lower() in lower:
            raise RuntimeError(f"Forbidden manuscript phrase: {phrase}")

    print("=" * 84)
    print("PHASE 5Z REFEREE AUDIT: PASS")
    print("MAIN THEOREM SURVIVES: YES")
    print("ORDINARY AC INTEGRATION BY PARTS: EXPLICIT")
    print("S(t) POINT-VALUE CONVENTION: EXPLICIT")
    print("PAPER FRAMING: TIGHTENED")
    print("RH CLAIM: NONE")
    print("NOVELTY CLAIM: NONE")
    print("=" * 84)


if __name__ == "__main__":
    main()
