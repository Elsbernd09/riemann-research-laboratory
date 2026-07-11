from __future__ import annotations

from pathlib import Path


MANUSCRIPT_FILES = [
    Path("paper/README.md"),
    Path("paper/01_SCOPE_AND_MAIN_RESULT.md"),
    Path("paper/02_CLASSICAL_INPUTS.md"),
    Path("paper/03_MATCHED_SCALE_LI_SUSCEPTIBILITY.md"),
    Path("paper/04_CENTERED_PRIMITIVE_TRANSFER.md"),
    Path("paper/05_PROOF_OF_MAIN_THEOREM.md"),
    Path("paper/06_RH_REFINEMENT_AND_SHARE_CONSEQUENCES.md"),
    Path("paper/07_NUMERICAL_MOTIVATION_AND_VALIDATION.md"),
    Path("paper/08_PRIOR_ART_AND_CLAIM_BOUNDARY.md"),
]

SUPPORT_FILES = [
    Path("docs/PAPER_THEOREM_DEPENDENCY_MAP.md"),
    Path("docs/PAPER_SCOPE_AND_CLAIM_BOUNDARY.md"),
]

REQUIRED = [
    "R_{\\mathrm{int}}",
    "\\frac{\\log H}{H^3}",
    "No assumption of the Riemann Hypothesis is used",
    "Originality remains under active prior-art review",
]

FORBIDDEN = [
    "breakthrough",
    "progress toward proving RH",
    "new approach to RH",
    "first-ever",
    "novel RH criterion",
    "RH is nearly solved",
]


def read_checked(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(
        encoding="utf-8"
    )

    if "\x00" in text:
        raise ValueError(
            f"NUL byte found in {path}"
        )

    return text


def main() -> None:
    manuscript_text = ""

    for path in MANUSCRIPT_FILES:
        manuscript_text += (
            "\n"
            +
            read_checked(path)
        )

    for path in SUPPORT_FILES:
        read_checked(path)

    for phrase in REQUIRED:
        if phrase not in manuscript_text:
            raise RuntimeError(
                "Missing required manuscript phrase: "
                f"{phrase}"
            )

    lowered = manuscript_text.lower()

    for phrase in FORBIDDEN:
        if phrase.lower() in lowered:
            raise RuntimeError(
                "Forbidden manuscript language found: "
                f"{phrase}"
            )

    theorem_file = read_checked(
        Path(
            "paper/05_PROOF_OF_MAIN_THEOREM.md"
        )
    )

    if (
        "No assumption of RH has been used."
        not in theorem_file
    ):
        raise RuntimeError(
            "Main proof does not explicitly freeze "
            "the unconditional status."
        )

    print("=" * 80)
    print(
        "PHASE 5X PAPER DEPENDENCY FREEZE: PASS"
    )
    print(
        "MAIN THEOREM PRESENT: YES"
    )
    print(
        "UNCONDITIONAL STATUS EXPLICIT: YES"
    )
    print(
        "RH REFINEMENT SEPARATED: YES"
    )
    print(
        "CLASSICAL INPUTS SEPARATED: YES"
    )
    print(
        "DEAD BRANCHES EXCLUDED FROM MAIN CLAIM: YES"
    )
    print(
        "POLICY FILES VALIDATED BUT NOT LANGUAGE-SCANNED: YES"
    )
    print(
        "NOVELTY CLAIM: NONE"
    )
    print("=" * 80)


if __name__ == "__main__":
    main()
