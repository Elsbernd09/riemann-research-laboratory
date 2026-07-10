from __future__ import annotations

from pathlib import Path


PROOF_PATH = Path(
    "proofs/PHASE_5O_CLASSICAL_S1_CONDITIONAL_LI_RESPONSE_TRANSFER.md"
)

VALIDATOR_PATH = Path(
    "scripts/validate_phase5o_second_derivative_profile.py"
)

CLAIM_LEDGER_PATH = Path(
    "research_ledger/CLAIM_LEDGER.md"
)

PHASE_LEDGER_PATH = Path(
    "research_ledger/PHASE_LEDGER.md"
)


def replace_required(
    text: str,
    old: str,
    new: str,
    label: str,
) -> str:
    count = text.count(old)

    if count == 0:
        raise RuntimeError(
            f"Expected text not found for {label}."
        )

    return text.replace(old, new)


proof_text = PROOF_PATH.read_text(
    encoding="utf-8"
)

proof_text = replace_required(
    proof_text,
    """J_{Li}'(q)
=
2q^3\\cos q
-
6q^2\\sin q
-
36q\\cos q
-
12\\sin q.""",
    """J_{Li}'(q)
=
2q^3\\cos q
+
18q^2\\sin q
-
36q\\cos q
-
12\\sin q.""",
    "proof J derivative",
)

proof_text = replace_required(
    proof_text,
    """K_{Li}^{(2)}(q)
=
2q^4\\cos q
-
48q^2\\cos q
-
48q\\sin q.""",
    """K_{Li}^{(2)}(q)
=
2q^4\\cos q
+
24q^3\\sin q
-
72q^2\\cos q
-
48q\\sin q.""",
    "proof K2 profile",
)

proof_text = replace_required(
    proof_text,
    """The \\(q^3\\sin q\\) terms cancel exactly.""",
    """The \\(q^3\\sin q\\) terms do not cancel.

Indeed,

\\[
3J_{Li}(q)
\\]

contributes

\\[
6q^3\\sin q,
\\]

while

\\[
qJ_{Li}'(q)
\\]

contributes

\\[
18q^3\\sin q.
\\]

The total contribution is therefore

\\[
24q^3\\sin q.
\\]""",
    "false cancellation sentence",
)

proof_text = proof_text.replace(
    "CONDITIONAL THEOREM UNDER THE RIEMANN HYPOTHESIS.",
    (
        "CONDITIONAL THEOREM UNDER THE RIEMANN HYPOTHESIS "
        "— ALGEBRA REPAIRED AFTER FAILED VALIDATOR."
    ),
    1,
)

proof_text += r"""

---

# Phase 5O-A adversarial correction

The initial Phase 5O second-derivative validator failed before the
second-derivative theorem was accepted.

The failure exposed an algebra error in the displayed derivative of

\[
J_{Li}(q).
\]

The originally committed derivative was false.

The correct derivative is

\[
\boxed{
J_{Li}'(q)
=
2q^3\cos q
+
18q^2\sin q
-
36q\cos q
-
12\sin q.
}
\]

Therefore

\[
K_{Li}^{(2)}(q)
=
3J_{Li}(q)
+
qJ_{Li}'(q)
\]

equals

\[
\boxed{
K_{Li}^{(2)}(q)
=
2q^4\cos q
+
24q^3\sin q
-
72q^2\cos q
-
48q\sin q.
}
\]

The initial claim that the \(q^3\sin q\) terms cancel was false.

The original shell workflow also continued after the validator exception
and committed the unvalidated Phase 5O files.

Therefore the original Phase 5O completion banner was procedurally void.

The conditional theorem may be restored only after the corrected
second-derivative profile passes the unchanged numerical consistency
validator.

No numerical acceptance threshold is changed.
"""

PROOF_PATH.write_text(
    proof_text,
    encoding="utf-8",
)


validator_text = VALIDATOR_PATH.read_text(
    encoding="utf-8"
)

validator_text = replace_required(
    validator_text,
    """    return (
        2 * q**3 * mp.cos(q)
        -
        6 * q**2 * mp.sin(q)
        -
        36 * q * mp.cos(q)
        -
        12 * mp.sin(q)
    )""",
    """    return (
        2 * q**3 * mp.cos(q)
        +
        18 * q**2 * mp.sin(q)
        -
        36 * q * mp.cos(q)
        -
        12 * mp.sin(q)
    )""",
    "validator J derivative",
)

validator_text = replace_required(
    validator_text,
    """    return (
        2 * q**4 * mp.cos(q)
        -
        48 * q**2 * mp.cos(q)
        -
        48 * q * mp.sin(q)
    )""",
    """    return (
        2 * q**4 * mp.cos(q)
        +
        24 * q**3 * mp.sin(q)
        -
        72 * q**2 * mp.cos(q)
        -
        48 * q * mp.sin(q)
    )""",
    "validator K2 profile",
)

VALIDATOR_PATH.write_text(
    validator_text,
    encoding="utf-8",
)


claim_text = CLAIM_LEDGER_PATH.read_text(
    encoding="utf-8"
)

claim_text += r"""

---

## CL-0382

**Status:** FAILED CLAIM — ALGEBRA ERROR

**Statement:** The initial Phase 5O expression

\[
J_{Li}'(q)
=
2q^3\cos q
-
6q^2\sin q
-
36q\cos q
-
12\sin q
\]

was false.

The initial derived expression

\[
K_{Li}^{(2)}(q)
=
2q^4\cos q
-
48q^2\cos q
-
48q\sin q
\]

was therefore also false.

**Failure evidence:** The second-derivative profile validator reported a
nonzero profile identity error, including approximately

\[
3917.59
\]

at \(q=20\), and raised an ArithmeticError.

**Disposition:** Initial Phase 5O second-derivative profile rejected.

---

## CL-0383

**Status:** PROVED IN PROJECT — ALGEBRAIC CORRECTION

**Statement:** The correct derivative is

\[
\boxed{
J_{Li}'(q)
=
2q^3\cos q
+
18q^2\sin q
-
36q\cos q
-
12\sin q.
}
\]

Consequently,

\[
\boxed{
K_{Li}^{(2)}(q)
=
3J_{Li}(q)
+
qJ_{Li}'(q)
}
\]

equals

\[
\boxed{
K_{Li}^{(2)}(q)
=
2q^4\cos q
+
24q^3\sin q
-
72q^2\cos q
-
48q\sin q.
}
\]

The previously claimed \(q^3\sin q\) cancellation does not occur.

---

## CL-0384

**Status:** PROCEDURAL FAILURE-PREVENTION

**Statement:** The original Phase 5O shell workflow continued after the
validator failed and committed unvalidated theorem files.

A printed completion banner is not evidence of research-phase completion.

Future theorem-freeze shell workflows must stop immediately on validator
failure by using `set -euo pipefail` or an equivalent explicit success guard.

---

## CL-0385

**Status:** CLAIM STATUS QUARANTINE

**Statement:** CL-0377 through CL-0379 are not accepted through the
original Phase 5O commit.

CL-0377 requires the corrected profile in CL-0383.

CL-0378 and CL-0379 may be restored only after the corrected
second-derivative validator passes without changing its acceptance rule.

"""

CLAIM_LEDGER_PATH.write_text(
    claim_text,
    encoding="utf-8",
)


phase_text = PHASE_LEDGER_PATH.read_text(
    encoding="utf-8"
)

phase_text += r"""

---

## Phase 5O-A — Failed Validator and Second-Derivative Algebra Repair

Status: REPAIR IN PROGRESS

### Trigger

The Phase 5O second-derivative validator failed.

At \(q=20\), the explicit profile identity error was approximately

\[
3917.59.
\]

The validator raised:

`ArithmeticError: K2 explicit-profile identity validation failed.`

### Algebra error

The derivative of

\[
-12q^2\cos q
\]

was combined incorrectly in the initial Phase 5O calculation.

Correctly,

\[
\frac{d}{dq}
\left(
-12q^2\cos q
\right)
=
-24q\cos q
+
12q^2\sin q.
\]

Thus

\[
J_{Li}'(q)
=
2q^3\cos q
+
18q^2\sin q
-
36q\cos q
-
12\sin q.
\]

### Correct second-derivative profile

\[
K_{Li}^{(2)}(q)
=
3J_{Li}(q)
+
qJ_{Li}'(q)
\]

equals

\[
\boxed{
K_{Li}^{(2)}(q)
=
2q^4\cos q
+
24q^3\sin q
-
72q^2\cos q
-
48q\sin q.
}
\]

The initial claimed cancellation of the \(q^3\sin q\) terms was false.

### Procedural failure

The original shell workflow did not stop when the validator raised an
exception.

The invalid theorem files were committed and a Phase 5O completion
banner was printed.

That banner is void.

### Acceptance rule

The corrected validator must pass under the existing profile identity
threshold.

No threshold loosening is permitted.

Only after a pass may the conditional response theorem be restored.

"""

PHASE_LEDGER_PATH.write_text(
    phase_text,
    encoding="utf-8",
)

print("PHASE 5O-A ALGEBRA REPAIR APPLIED")
print("NO VALIDATOR THRESHOLD CHANGED")
