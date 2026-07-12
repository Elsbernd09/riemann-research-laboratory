# Phase 8O — Finite Truncation Source Map

## Purpose

Phase 8N created the finite truncation extraction worksheet.

Phase 8O source-locks the roadmap for where Bombieri's finite truncation construction lives.

This phase does not implement a matrix.

This phase does not compute eigenvalues.

This phase does not prove RH.

This phase does not claim a new Weil criterion.

---

# 1. Source

Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, Rend. Mat. Acc. Lincei, Serie 9, Vol. 11, 183-233, 2000.

---

# 2. Source-grounded roadmap

Bombieri's introduction gives the structure of the finite truncation program.

## Sections 5 and 6

Bombieri studies the structure of extremals and reformulates the eigenvalue problems using Fourier transforms.

Status: SOURCE-LOCATED.

## Section 8

Bombieri introduces finite approximations, odd and even eigenfunctions, and proves Theorem 8 about eigenvalues of finite matrices in the approximation of the first eigenvalue problem.

Status: SOURCE-LOCATED.

## Section 9

Bombieri obtains corresponding results for the second eigenvalue problem.

Status: SOURCE-LOCATED.

## Section 10

Bombieri passes from finite approximations to the zeta-function case.

Status: SOURCE-LOCATED.

## Section 11

Bombieri carries the limiting process for the second eigenvalue problem and discusses how linear relations may arise.

Status: SOURCE-LOCATED.

---

# 3. High-level source statement

The source states at abstract/introduction level that:

1. the Fourier transform of Weil's functional gives a quadratic form in infinitely many variables;
2. finite truncations and corresponding eigenvalues are studied;
3. if RH is false but has only finitely many nontrivial zeros off the critical line, the number of negative eigenvalues is one-half of the number of zeros failing RH, provided the truncation is sufficiently large.

This is a source-level roadmap.

It is not yet the exact finite truncation construction.

---

# 4. Extraction priority

The next extraction phases must proceed in this order:

## Step 1

Extract the Fourier-side infinite quadratic form from Sections 5 and 6.

## Step 2

Extract the finite approximation definition from Section 8.

## Step 3

Extract Theorem 8 and its hypotheses.

## Step 4

Extract the Section 9 analogue for the second eigenvalue problem.

## Step 5

Extract the Section 10 limiting argument for zeta.

## Step 6

Extract the Section 11 second-problem limiting argument.

---

# 5. Current lock status

## LOCKED

Source roadmap:

- Sections 5 and 6: Fourier-side reformulation;
- Section 8: finite approximations and Theorem 8;
- Section 9: second eigenvalue problem;
- Section 10: zeta limiting process;
- Section 11: second limiting process.

## PARTIAL

High-level negative-eigenvalue claim.

High-level finite-truncation claim.

## UNLOCKED

Exact infinite quadratic form.

Exact finite matrix entries.

Exact truncation parameter.

Exact Theorem 8 statement.

Exact Section 10 limiting theorem.

Exact Section 11 limiting theorem.

Implementation permission.

---

# 6. Boundary

No matrix code.

No eigenvalue computation.

No exact finite-rank Weil implementation.

No RH proof.

No novelty claim.

