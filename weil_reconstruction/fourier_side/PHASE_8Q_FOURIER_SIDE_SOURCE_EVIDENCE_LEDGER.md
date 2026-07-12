# Phase 8Q — Fourier-Side Source Evidence Ledger

## Purpose

Phase 8P created the extraction worksheet for Bombieri's Fourier-side infinite quadratic form.

Phase 8Q records exactly what has been source-located so far and what remains formula-unlocked.

This phase does not implement a matrix.

This phase does not compute eigenvalues.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. Source used

Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, Rend. Mat. Acc. Lincei, Serie 9, Vol. 11, 183-233, 2000.

---

# 2. Source-located high-level facts

## Fact 1

Bombieri's abstract states that the Fourier transform of Weil's functional gives a quadratic form in infinitely many variables.

Status: SOURCE-LOCATED.

Formula status: UNLOCKED.

## Fact 2

Bombieri studies finite truncations and corresponding eigenvalues of this Fourier-side quadratic form.

Status: SOURCE-LOCATED.

Formula status: UNLOCKED.

## Fact 3

Bombieri's introduction says Sections 5 and 6 study the structure of extremals and reformulate the eigenvalue problems by taking Fourier transforms.

Status: SOURCE-LOCATED.

Formula status: UNLOCKED.

## Fact 4

Bombieri's introduction says Section 8 introduces finite approximations and proves Theorem 8 about eigenvalues of finite matrices in the approximation of the first eigenvalue problem.

Status: SOURCE-LOCATED.

Formula status: UNLOCKED.

## Fact 5

Bombieri's introduction says Sections 10 and 11 pass from finite approximations to zeta-function limiting cases.

Status: SOURCE-LOCATED.

Formula status: UNLOCKED.

---

# 3. What this phase locks

This phase locks the source evidence chain:

\[
T[f*f^*]
\rightarrow
\text{Fourier-side infinite quadratic form}
\rightarrow
\text{finite approximations}
\rightarrow
\text{finite matrices}
\rightarrow
\text{eigenvalue statements}.
\]

However, it does not lock the exact formulas.

---

# 4. What remains unlocked

The following remain unlocked:

1. exact Fourier transform convention;
2. exact function space;
3. exact infinite quadratic form;
4. exact eigenvalue problem;
5. exact finite approximation definition;
6. exact finite matrix entries;
7. exact Theorem 8 statement;
8. exact limiting theorem statements in Sections 10 and 11.

---

# 5. Consequence

The project is now allowed to say:

Bombieri source-locates a Fourier-side infinite quadratic form and later finite truncations.

The project is not allowed to say:

- we have implemented Bombieri's matrix;
- we know the exact matrix entries;
- our code computes Bombieri-Weil eigenvalues;
- our toy matrices are classical Weil truncations.

---

# 6. Boundary

No matrix code.

No eigenvalue computation.

No exact finite-rank Weil implementation.

No RH proof.

No novelty claim.

