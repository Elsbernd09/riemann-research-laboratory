# Phase 10A — Original Result Target Selection

## Purpose

This launches the original-result branch.

The target is not to claim a proof of RH.

The target is to build a rigorous, professor-readable research note around a narrow original theorem connected to finite Bombieri/Weil-style matrix stability.

---

# 1. Target level

## Level 2 target

A professor-readable research note containing:

1. precise definitions;
2. one original theorem;
3. a complete proof;
4. computational examples;
5. honest limitations;
6. reproducible code;
7. clear relation to Bombieri/Weil positivity.

## Level 3 aspiration

A result that could interest experts if the theorem is genuinely new, technically clean, and useful for understanding finite approximations or numerical stability in Weil/Bombieri-style positivity frameworks.

Level 3 requires outside expert review.

---

# 2. Proposed original theorem target

## Working title

Finite Bombieri-Matrix Perturbation Stability

## Informal theorem

Let \(\Gamma\) be a finite symmetric multiset and let \(M(\Gamma,t)\) be a normalized Hermitian finite Bombieri-style matrix.

If the entries of \(M(\Gamma,t)\) are perturbed by at most \(\varepsilon\), and the smallest relevant eigenvalue gap is larger than a computable threshold depending on \(\varepsilon\) and matrix size, then the number of negative eigenvalues is unchanged.

In plain language:

Small implementation errors, zero-location perturbations, or kernel-normalization perturbations cannot change the negative eigenvalue count when there is a sufficient spectral gap.

---

# 3. Why this could be original

This theorem would not prove RH.

But it may provide a rigorous stability layer for finite Bombieri/Weil-style computations.

The possible original contribution is:

1. isolating the exact finite stability problem;
2. defining a clean synthetic matrix class;
3. proving a negative-eigenvalue-count stability theorem;
4. connecting it to why finite RH-adjacent computations require spectral-gap certification;
5. building reproducible examples and failure cases.

---

# 4. Candidate theorem skeleton

Let \(M\in\mathbb C^{n\times n}\) be Hermitian.

Let \(E\in\mathbb C^{n\times n}\) be Hermitian with

\[
\|E\|_2 \leq \delta.
\]

Let

\[
\lambda_1(M)\leq \cdots \leq \lambda_n(M)
\]

be the eigenvalues of \(M\).

If no eigenvalue of \(M\) lies in

\[
[-\delta,\delta],
\]

then \(M\) and \(M+E\) have the same number of negative eigenvalues.

This follows from Weyl-type eigenvalue perturbation bounds.

The original branch will specialize this general fact to the finite Bombieri-style matrix pipeline and produce explicit computable perturbation bounds from kernel-entry errors.

---

# 5. Research question

Can we prove a clean finite stability theorem of the form:

\[
\#\{\lambda_j(M(\Gamma,t))<0\}
=
\#\{\lambda_j(\widetilde M(\Gamma,t))<0\}
\]

whenever the implementation or input perturbation is smaller than an explicit spectral-gap threshold?

---

# 6. What must be proven

To make this a real result, the branch must prove:

1. the chosen matrix representation is Hermitian;
2. perturbations in kernel entries imply an operator-norm bound;
3. an operator-norm bound implies eigenvalue stability;
4. eigenvalue stability implies negative-count stability;
5. the final theorem has clear assumptions and no hidden RH claim.

---

# 7. What this does not claim

This does not prove RH.

This does not falsify RH.

This does not verify zeta zeros.

This does not claim a breakthrough yet.

This does not claim novelty until prior-art review and expert review are completed.

---

# 8. Next phases

Phase 10B: define the exact finite matrix object.

Phase 10C: define finite symmetry classes for \(\Gamma\).

Phase 10D: prove Hermitian/self-adjoint structure.

Phase 10E: prove entrywise perturbation to operator-norm bound.

Phase 10F: prove spectral-gap stability.

Phase 10G: state the first complete theorem.

Phase 10H: generate synthetic examples and failure cases.

Phase 10I: write professor-readable proof draft.

Phase 10J: adversarial novelty and correctness audit.

