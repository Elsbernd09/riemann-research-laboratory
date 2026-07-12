# Phase 8M — Off-Critical Negative-Direction Extraction

## Purpose

Phase 8L recorded the symbolic RH-implies-positivity mechanism:

\[
1-\overline{\rho}=\rho
\]

turns the Hermitian zero-side product into

\[
|g(\rho)|^2.
\]

Phase 8M records the opposite mechanism at statement level:

\[
\boxed{
\text{Off-critical zeros can create negative directions in Weil/Bombieri quadratic positivity.}
}
\]

This is not a proof of RH.

This is not a new Weil criterion.

This is a source-grounded reconstruction of known classical logic.

---

# 1. Source-level negative-direction statement

Bombieri's framework studies Weil's quadratic functional and its Fourier-side infinite quadratic form.

The source-level statement recorded in the project is:

If RH is false but there are only finitely many off-critical nontrivial zeros, then sufficiently large finite truncations of the associated quadratic form have negative eigenvalues.

More precisely, the number of negative eigenvalues is tied to the number of zeros failing RH.

This is a classical Bombieri/Weil statement, not a project-original result.

---

# 2. Conceptual mechanism

The positivity mechanism under RH is:

\[
g(\rho)\overline{g(1-\overline{\rho})}
=
|g(\rho)|^2
\]

because

\[
1-\overline{\rho}=\rho.
\]

If a zero is off the critical line, then

\[
1-\overline{\rho}\ne\rho.
\]

Then the Hermitian product couples values of \(g\) at two different reflected points:

\[
g(\rho)
\quad\text{and}\quad
g(1-\overline{\rho}).
\]

This removes the automatic square-norm structure.

A sufficiently flexible admissible test function can exploit this mismatch to produce a negative value of the quadratic functional.

---

# 3. Relation to horizontal displacement

Let

\[
\rho=\beta+i\gamma.
\]

Then

\[
1-\overline{\rho}
=
1-\beta+i\gamma.
\]

The two points coincide exactly when

\[
\beta=\frac12.
\]

Thus the negative-direction mechanism is directly tied to the horizontal displacement

\[
\beta-\frac12.
\]

This is the classical version of the Phase 7 horizontal-defect idea.

---

# 4. Why Phase 7 toy models were insufficient

Phase 7 built finite-rank diagnostic matrices that reacted to horizontal displacement.

However, Phase 7K showed basis-dependence.

Bombieri's negative-direction mechanism is different:

It is not arbitrary basis behavior.

It arises from a classical RH-equivalent quadratic functional and its finite truncations.

Therefore the next serious task is to extract the actual finite truncation model, not invent another toy matrix.

---

# 5. What is locked

The following high-level facts are locked:

1. RH gives square-norm positivity.
2. Off-critical zeros break the square-norm identity.
3. Bombieri's framework connects off-critical zeros to negative eigenvalues in sufficiently large finite truncations under a finite-exception hypothesis.
4. This negative-direction phenomenon is classical.

---

# 6. What remains unlocked

The following are still unlocked:

1. exact theorem number and source location for the finite-truncation negative-eigenvalue statement;
2. exact Fourier-side infinite quadratic form;
3. exact finite truncation definition;
4. exact matrix entries;
5. precise multiplicity convention;
6. precise statement connecting negative eigenvalue count to off-critical zeros;
7. convergence or stabilization assumptions.

---

# 7. Current implementation status

Symbolic explanation is allowed.

Finite-rank Weil matrix implementation remains blocked.

Eigenvalue computations may not yet be called classical Weil truncations.

The next phase must source-extract Bombieri's finite truncation construction.

---

# 8. Boundary

No RH proof.

No new Weil criterion.

No novelty claim.

No exact finite-rank Weil matrix yet.

