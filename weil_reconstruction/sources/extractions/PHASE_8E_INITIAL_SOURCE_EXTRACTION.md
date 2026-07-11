# Phase 8E — Initial Source Extraction Notes

## Purpose

Phase 8D created the source-grounded extraction protocol.

Phase 8E performs the first controlled extraction from the available source material.

This is not a proof of RH.

This is not a new Weil criterion.

This is a source-notes phase.

---

# 1. Sources used in this extraction

## Source A

Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, Rend. Mat. Acc. Lincei, Serie 9, Vol. 11, 183-233, 2000.

## Source B

Masatoshi Suzuki, **Weil's Quadratic Form via the Screw Function**, uploaded source excerpt.

---

# 2. Bombieri extraction

## Bibliographic identity

Author: Enrico Bombieri.

Title: Remarks on Weil's quadratic functional in the theory of prime numbers, I.

Venue: Rendiconti Lincei, Matematica e Applicazioni.

Year: 2000.

Pages: 183-233.

## Extracted classical claims

Bombieri studies Weil's explicit formula and the associated quadratic functional.

The source states that the associated quadratic functional is positive semidefinite if and only if RH is true.

The source studies finite truncations and eigenvalues of an infinite quadratic form obtained from the Fourier transform of the functional.

The source states that if RH is false but has only finitely many off-critical nontrivial zeros, then, for sufficiently large truncation, the number of negative eigenvalues is one-half the number of zeros failing RH.

## Extraction status

This source is the main anchor for the selected Bombieri-style reconstruction.

However, the exact test-function class, transform convention, quadratic functional formula, matrix entries, and finite truncation construction remain unlocked.

---

# 3. Suzuki extraction

## Bibliographic identity

Author: Masatoshi Suzuki.

Title: Weil's Quadratic Form via the Screw Function.

## Extracted classical/contemporary formulation

The source defines or recalls a Weil functional

\[
W(f)
\]

and a Hermitian/symmetric quadratic form

\[
Q_W(v_1,v_2)=W(v_1*\tilde v_2),
\qquad
Q_W(v)=Q_W(v,v).
\]

The source records a version of Weil's positivity criterion:

\[
Q_W(v)\ge0
\]

for all

\[
v\in C_c^\infty(\mathbb R),
\]

as an RH-equivalent positivity statement.

The source also discusses localized spaces such as

\[
C_c^\infty(-a,a)
\]

and operator-theoretic localized forms.

## Extraction status

This source is useful for notation and modern framing.

However, because it is a later framework and includes operator-theoretic refinements, it should not replace the primary Bombieri reconstruction path.

---

# 4. Current locked facts

The following are now source-grounded enough to record as locked high-level facts:

## Locked fact 1

Weil positivity is a classical RH-equivalent positivity framework.

## Locked fact 2

Bombieri studies Weil's quadratic functional, finite truncations, and eigenvalues.

## Locked fact 3

Under the hypothesis that RH fails with only finitely many off-critical nontrivial zeros, Bombieri's framework relates sufficiently large finite truncations to negative eigenvalues.

## Locked fact 4

The notation

\[
Q_W(v_1,v_2)=W(v_1*\tilde v_2)
\]

is a useful modern notation for the Weil quadratic form.

---

# 5. Still unlocked

The following are not yet locked:

1. exact admissible test-function class for the chosen Bombieri reconstruction;
2. exact Fourier transform convention;
3. exact zero-side formula;
4. exact prime-side formula;
5. exact archimedean term;
6. exact quadratic functional formula;
7. exact infinite matrix entries;
8. exact finite truncation definition;
9. exact theorem number dependencies;
10. exact relationship between negative eigenvalue count and off-critical zeros in the full paper.

---

# 6. Immediate next task

The next task is to build a convention-lock file with statuses:

- LOCKED;
- PARTIAL;
- UNLOCKED.

Only high-level structural facts should be marked LOCKED now.

Exact formulas remain UNLOCKED until extracted from the relevant sections.

