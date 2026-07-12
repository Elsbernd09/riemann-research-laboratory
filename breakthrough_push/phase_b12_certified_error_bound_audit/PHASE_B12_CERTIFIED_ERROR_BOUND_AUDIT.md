# Phase B12 — Certified Error-Bound Audit

## Purpose

Phase B11 created the first interval-candidate arithmetic entry:

\[
M_{00}^{arith}.
\]

Phase B12 audits whether that candidate can be upgraded to:

\[
\texttt{CERTIFIED\_INTERVAL\_ENTRY}.
\]

This phase does not certify the entry.

It identifies the remaining mathematical and numerical gates.

---

# 1. Certification target

The target future object is:

\[
M_{00}^{arith}
=
T[\phi_0 \vee \overline{\phi_0}]
\]

under Bombieri–Lagarias normalization.

A certified entry would require:

\[
M_{00}^{arith}\in [L,U]
\]

with a proof that the true value lies in that interval.

---

# 2. Error gates

## Gate 1 — Quadrature error

Status:

\[
\boxed{\text{HARD BUT POSSIBLE}}
\]

The current midpoint rule is floating-point only.

To certify it, we need either:

1. interval arithmetic quadrature;
2. rigorous derivative bounds;
3. adaptive interval integration;
4. exact symbolic integration for the toy basis.

## Gate 2 — Convolution error

Status:

\[
\boxed{\text{NEEDS NEW THEOREM / IMPLEMENTATION}}
\]

The convolution

\[
F(x)=\int \phi(y)\phi^*(x/y)\frac{dy}{y}
\]

is numerically approximated.

Certification needs an interval enclosure of the inner convolution uniformly over the outer integration domain.

This is harder than ordinary one-dimensional quadrature because it is nested.

## Gate 3 — Archimedean singularity handling

Status:

\[
\boxed{\text{BLOCKS CERTIFICATION UNTIL FIXED}}
\]

The integrand near \(x=1\) has a removable singularity structure.

The current prototype avoids it using a small epsilon.

That is not certifiable.

A certified version must prove and implement the limiting value at \(x=1\), or integrate with a validated singularity subtraction.

## Gate 4 — Floating-point rounding error

Status:

\[
\boxed{\text{EASY TO CERTIFY}}
\]

This can be controlled by outward-rounded interval arithmetic or rational arithmetic.

It is not the main blocker.

## Gate 5 — Basis smoothness

Status:

\[
\boxed{\text{BLOCKS TRUE WEIL CERTIFICATION}}
\]

The current triangular toy basis is not \(C_c^\infty\).

A real Weil-test certification should replace it with a smooth compactly supported basis.

The toy basis can support engineering tests, but not a final Weil-form certificate.

## Gate 6 — Pole constraints

Status:

\[
\boxed{\text{REQUIRES EXPERT / SOURCE REVIEW}}
\]

The pole constraints

\[
\widehat g(0)=0,
\qquad
\widehat g(1)=0
\]

are plausible and natural, but the exact admissibility condition must be confirmed in the specific source convention.

## Gate 7 — Source normalization

Status:

\[
\boxed{\text{REQUIRES SOURCE REVIEW}}
\]

Bombieri–Lagarias normalization was extracted, but the relationship between their displayed formula and other Weil/Bombieri normalizations must be kept explicit.

Certified work should use only one named normalization.

---

# 3. Certification verdict

The B11 interval candidate is not close to certification yet.

The main blockers are:

\[
\boxed{\text{archimedean singularity}}
\]

\[
\boxed{\text{non-smooth toy basis}}
\]

\[
\boxed{\text{nested convolution certification}}
\]

\[
\boxed{\text{source/admissibility review}}
\]

Therefore the honest status is:

\[
\boxed{
\text{INTERVAL CANDIDATE ONLY — NOT CERTIFIED}
}
\]

---

# 4. Shortest realistic path to certification

The shortest serious path is not to certify the triangular toy basis.

Instead:

## Step 1

Define a smooth compactly supported bump:

\[
\psi(u)=
\begin{cases}
\exp\left(-\frac1{1-u^2}\right), & |u|<1,\\
0, & |u|\ge1.
\end{cases}
\]

and

\[
\phi(x)=\psi\left(\frac{\log x-c}{w}\right).
\]

## Step 2

Build interval arithmetic for \(\psi\), \(\phi\), \(\phi^*\), and \(F=\phi\vee \bar\phi\).

## Step 3

Derive singularity-subtracted archimedean integrand.

## Step 4

Use interval quadrature with rigorous subdivision.

## Step 5

Only then attempt:

\[
\texttt{CERTIFIED\_INTERVAL\_ENTRY}.
\]

---

# 5. Breakthrough relevance

This audit shows that the project is serious enough to identify the real blockers.

But it also shows that we do not yet have a certified arithmetic entry.

Therefore:

\[
\boxed{\text{BREAKTHROUGH\_NOT\_ACHIEVED}}
\]

---

# Theorem B12.1 — B11 interval candidate is not certifiable without closing all gates

If any required error source is unbounded, then the interval candidate cannot be labeled certified.

## Proof

A certified interval entry requires a proof that the true mathematical value lies in the claimed interval.

If any error source is unbounded, then the distance between the computed approximation and the true value is not bounded.

Therefore the interval cannot be proven to contain the true value.

Thus the entry cannot be certified.

\[
\square
\]

---

# Theorem B12.2 — triangular toy basis blocks true Weil-test certification

If the target test space requires \(C_c^\infty(0,\infty)\), then a triangular log-coordinate basis is insufficient for final Weil-test certification.

## Proof

A triangular bump has corner points where derivatives fail to exist.

Thus it is not \(C^\infty\).

Therefore it is not an element of \(C_c^\infty(0,\infty)\).

If the true admissible test space requires \(C_c^\infty\), the triangular basis cannot be used for final certification in that space.

\[
\square
\]

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a breakthrough.

This phase does not prove novelty.

This phase does not certify the interval candidate.

Exact audit strings:

PHASE_B12_CERTIFIED_ERROR_BOUND_AUDIT_COMPLETE

ERROR_GATES_AUDITED

QUADRATURE_ERROR_HARD_BUT_POSSIBLE

CONVOLUTION_ERROR_NEEDS_NEW_THEOREM_OR_IMPLEMENTATION

ARCHIMEDEAN_SINGULARITY_BLOCKS_CERTIFICATION

ROUNDING_ERROR_EASY_TO_CERTIFY

TOY_BASIS_BLOCKS_TRUE_WEIL_CERTIFICATION

POLE_CONSTRAINTS_REQUIRE_SOURCE_REVIEW

SOURCE_NORMALIZATION_REQUIRES_REVIEW

INTERVAL_CANDIDATE_NOT_CERTIFIED

BREAKTHROUGH_NOT_ACHIEVED

READY_FOR_PHASE_B13_SMOOTH_BASIS_CERTIFICATION_PLAN

