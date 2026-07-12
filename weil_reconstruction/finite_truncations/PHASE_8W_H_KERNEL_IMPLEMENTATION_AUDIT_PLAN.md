# Phase 8W — H-Kernel Implementation Audit Plan

## Purpose

Phase 8V source-extracted Bombieri Theorem 8 at statement level.

Phase 8W creates the implementation audit plan required before any source-derived H-kernel testbed is coded.

This phase does not implement the matrix.

This phase does not compute eigenvalues.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. Current source-locked objects

The project has source-extracted:

1. finite multiset \(Z\);
2. finite \(\Gamma\)-multiset;
3. Section 8 finite space \(V\);
4. boundary subspace \(V^\circ\);
5. kernel \(K(x)=\sin(x)/x\);
6. scaled kernel \(K_t(x)=K(tx)\);
7. corrected kernel \(K^*(x,y;t)\);
8. matrix kernel

\[
H(x,y;t)=\frac{2tK^*(x,y;t)}{1/4+y^2};
\]

9. coefficient equation

\[
w_\gamma=\Lambda\sum_{\gamma'\in\Gamma}H(\gamma,\gamma';t)w_{\gamma'};
\]

10. Bombieri Theorem 8 at statement level;
11. repeated-\(\gamma\) zero-eigenvalue warning.

---

# 2. Why an implementation audit is necessary

Even though the source formula is extracted, direct code can still be wrong because of:

1. complex arithmetic branch errors;
2. unstable evaluation of \(K(z)=\sin z/z\) near \(z=0\);
3. confusion between full multiset and distinct weighted matrix;
4. non-Hermitian normalization;
5. wrong treatment of conjugate pairs;
6. incorrect treatment of repeated \(\gamma\)-values;
7. accidental interpretation of toy output as a zeta result.

Therefore, implementation requires a separate audit plan.

---

# 3. Required implementation stages

## Stage A — Pure symbolic implementation only

Create functions for:

\[
K(z)=\sin z/z,
\]

\[
K_t(z)=K(tz),
\]

\[
K^*(x,y;t),
\]

and

\[
H(x,y;t).
\]

No eigenvalues.

No zeta zeros.

No theorem claims.

---

## Stage B — Algebraic sanity checks

Before any eigenvalue computation, verify:

1. \(K(0)=1\) by stable limiting branch;
2. \(K(-z)=K(z)\);
3. \(K_t(-z)=K_t(z)\);
4. no NaN or infinity appears for sample complex inputs;
5. conjugate symmetry behavior is inspected numerically;
6. diagonal entries are finite.

---

## Stage C — Multiplicity handling

Implement two separate representations:

## Full multiset representation

Rows and columns repeat repeated \(\gamma\)-values.

## Distinct weighted representation

Rows and columns use distinct \(\gamma_j\), with column weights

\[
m(\gamma_k)
\]

as recorded from Lemma 10.

The two representations must be documented separately.

---

## Stage D — Hermitian conversion audit

Before computing eigenvalues, determine whether the raw matrix

\[
H(\gamma_j,\gamma_k;t)
\]

is already Hermitian under the chosen representation, or whether a similarity transform is required.

A likely weighted similarity form is:

\[
\widetilde H_{jk}
=
\sqrt{m(\gamma_j)}H(\gamma_j,\gamma_k;t)\sqrt{m(\gamma_k)}.
\]

This is only a proposed audit target, not yet a locked implementation.

---

## Stage E — Synthetic Theorem 8 validation

Only after Stages A-D pass, run synthetic finite tests where \(\Gamma\) is constructed with known numbers of real and non-real conjugate pairs.

Validation target:

\[
\#\{\lambda<0\}
=
\#\{\text{distinct complex conjugate pairs }(\gamma,\overline{\gamma})\}.
\]

This must be done on synthetic finite multisets before any zeta-related data.

---

# 4. Explicit non-zeta rule

The first implementation must not use zeta zeros.

Reason:

Section 8 is a finite approximation theorem for finite multisets with prescribed symmetries.

The zeta limiting transition belongs to Sections 10 and 11 and is not yet extracted.

Therefore:

\[
\text{Synthetic finite multisets first.}
\]

---

# 5. Permission status after Phase 8W

## Allowed

1. write source-derived symbolic \(H\)-kernel code in a future phase;
2. evaluate \(K,K_t,K^*,H\) on sample complex inputs;
3. test algebraic sanity properties;
4. document full vs distinct weighted representations.

## Still denied

1. eigenvalue computation;
2. zeta zero experiments;
3. claims of Bombieri-Weil numerical verification;
4. claims of RH progress;
5. Section 10/11 limiting claims.

---

# 6. Boundary

No matrix implementation in this phase.

No eigenvalue computation in this phase.

No RH proof.

No novelty claim.

