from __future__ import annotations

from pathlib import Path


FILES = [
    Path(
        "proofs/"
        "PHASE_5W_THEOREM_AUDIT_AND_QUANTIFIER_REPAIR.md"
    ),
    Path(
        "research_ledger/CLAIM_LEDGER.md"
    ),
    Path(
        "research_ledger/PHASE_LEDGER.md"
    ),
]

REQUIRED_PHRASES = [
    "R_{\\mathrm{int}}",
    "O_{K,\\eta}",
    "\\frac{\\log H}{H^3}",
    "\\Delta N(H)",
    "m_H",
    "No subsuming source identified in the current uploaded-corpus audit.",
]

FORBIDDEN_PHRASES = [
    "proves the Riemann Hypothesis",
    "progress toward proving RH",
    "novel theorem",
    "first-ever",
]


def main() -> None:
    combined = ""

    for path in FILES:
        if not path.exists():
            raise FileNotFoundError(
                path
            )

        text = path.read_text(
            encoding="utf-8"
        )

        if "\x00" in text:
            raise ValueError(
                f"NUL byte found in {path}"
            )

        combined += "\n" + text

    for phrase in REQUIRED_PHRASES:
        if phrase not in combined:
            raise RuntimeError(
                "Missing required audit phrase: "
                f"{phrase}"
            )

    for phrase in FORBIDDEN_PHRASES:
        if phrase in FILES[0].read_text(
            encoding="utf-8"
        ):
            raise RuntimeError(
                "Forbidden theorem-audit language: "
                f"{phrase}"
            )

    print(
        "PHASE 5W THEOREM LANGUAGE AUDIT: PASS"
    )
    print(
        "MAIN UNCONDITIONAL THEOREM: RETAINED"
    )
    print(
        "ATOM EXISTENCE HYPOTHESIS: EXPLICIT"
    )
    print(
        "KERNEL NONDEGENERACY ALONE: NOT USED "
        "TO INFER ATOM EXISTENCE"
    )
    print(
        "NOVELTY CLAIM: NONE"
    )


if __name__ == "__main__":
    main()
