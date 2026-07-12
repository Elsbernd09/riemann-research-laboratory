# Phase B10 — Prototype Floating-Point Arithmetic Entry

## Purpose

Phase B9 created the metadata-only arithmetic entry:

\[
M_{00}^{arith}.
\]

Phase B10 upgrades this entry to:

\[
\texttt{PROTOTYPE\_FLOATING\_POINT}.
\]

This phase computes a floating-point prototype value under Bombieri–Lagarias normalization.

It is not certified.

---

# 1. Entry target

The target is:

\[
M_{00}^{arith}
=
T[\phi_0 \vee \overline{\phi_0}]
\]

under Bombieri–Lagarias convention.

The diagonal entry corresponds to the first basis function paired with itself.

---

# 2. Corrected normalization

Bombieri–Lagarias normalization uses the constant term:

\[
-(\log\pi+\gamma)f(1).
\]

This phase therefore uses:

\[
\boxed{
-(\log\pi+\gamma)f(1)
}
\]

not the earlier project form involving:

\[
\log4\pi+\gamma.
\]

---

# 3. Prototype status

The computed value has status:

\[
\texttt{PROTOTYPE\_FLOATING\_POINT}.
\]

This means:

1. the value is approximate;
2. quadrature is not interval-certified;
3. convolution is not interval-certified;
4. rounding error is not certified;
5. the value cannot be used in a certified matrix;
6. the result is only a pipeline test.

---

# 4. Theorem B10.1 — prototype floating entries are not certified entries

An entry with status

\[
\texttt{PROTOTYPE\_FLOATING\_POINT}
\]

cannot be used as a certified interval entry.

## Proof

By Phase B8, a certified interval entry must have status:

\[
\texttt{CERTIFIED\_INTERVAL\_ENTRY}.
\]

The prototype floating-point status is distinct from this.

Therefore a prototype floating-point entry is not certified.

\[
\square
\]

---

# 5. What this phase achieves

This phase gives the first source-normalized numerical prototype entry.

It demonstrates that the metadata schema can carry:

1. source conventions;
2. corrected normalization;
3. numerical value;
4. decomposition components;
5. non-certification boundary.

---

# 6. Next target

Phase B11 should convert this prototype into an interval-candidate object.

That requires crude interval radii for:

1. numerical quadrature;
2. convolution approximation;
3. prime truncation;
4. rounding;
5. normalization.

It still will not be fully certified unless all error terms are justified.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a breakthrough.

This phase does not prove novelty.

This phase does not compute a certified arithmetic entry.

Exact audit strings:

PHASE_B10_PROTOTYPE_FLOATING_ENTRY_COMPLETE

M_00_ARITH_PROTOTYPE_FLOATING_ENTRY_CREATED

BOMBIERI_LAGARIAS_CONSTANT_USED

LOG_PI_GAMMA_NORMALIZATION_USED

EARLIER_LOG_4PI_GAMMA_NOT_USED

PROTOTYPE_FLOATING_POINT_ENTRY_NOT_CERTIFIED

NUMERICAL_VALUE_COMPUTED_BUT_NOT_CERTIFIED

BREAKTHROUGH_NOT_ACHIEVED

READY_FOR_PHASE_B11_INTERVAL_CANDIDATE_ENTRY

