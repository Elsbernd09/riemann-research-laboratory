# Phase 10AN — Classical Import Map

## Purpose

Phase 10AM defined a toy-but-honest Weil-form abstraction:

\[
Q_\infty,\quad Q_N,\quad P_N,\quad E_N(f).
\]

Phase 10AN maps each toy object to the classical Weil/Bombieri object that must eventually replace it.

This phase does not prove RH.

This phase does not prove convergence.

This phase does not claim novelty.

It creates the import map required for a serious contribution attempt.

---

# 1. Toy-to-classical object map

| Toy abstraction | Classical object needed | Current status |
|---|---|---|
| \(\mathcal D\) | admissible Weil/Bombieri test-function space | missing |
| \(Q_\infty\) | true infinite Weil/Bombieri quadratic form | missing |
| \(B_\infty\) | true Hermitian Weil/Bombieri bilinear or sesquilinear form | missing |
| \(V_N\) | finite-dimensional truncation or approximation space | missing |
| \(M_N\) | finite Bombieri/Weil matrix from the classical construction | partially modeled |
| \(P_N\) | projection/sampling/truncation map | missing |
| \(E_N(f)\) | finite-to-infinite approximation error | missing |
| \(\varepsilon_N(f)\) | quantitative convergence rate | missing |

---

# 2. Classical import obligation 1 — Test-function space

The toy model uses an abstract domain:

\[
\mathcal D.
\]

The classical project must replace this with the correct Weil/Bombieri test-function space.

The needed object is:

\[
\mathcal D_W.
\]

Requirements:

1. closed under the operations used in the Weil/Bombieri formula;
2. compatible with Mellin transform or Fourier-transform normalization;
3. compatible with the involution/star operation;
4. supports positivity statements;
5. admits finite approximation maps.

Current status:

\[
\mathcal D_W \text{ is not yet imported.}
\]

---

# 3. Classical import obligation 2 — Infinite Weil/Bombieri form

The toy model uses:

\[
Q_\infty(f).
\]

The classical project needs:

\[
Q_W(f).
\]

This should be the true infinite Weil/Bombieri quadratic form or positivity form.

Requirements:

1. exact formula;
2. exact normalization;
3. exact star/involution convention;
4. exact prime-sum and archimedean terms if using an explicit formula form;
5. exact relation to RH or Weil positivity.

Current status:

\[
Q_W \text{ is not yet fully imported.}
\]

---

# 4. Classical import obligation 3 — RH relation

The toy model has no RH content by itself.

The classical project needs a known statement of the form:

\[
\text{RH}
\quad\Longleftrightarrow\quad
Q_W(f)\geq0
\text{ for all admissible } f,
\]

or a carefully stated one-direction implication.

Requirements:

1. exact theorem statement from classical sources;
2. exact hypotheses;
3. exact admissible function class;
4. exact positivity convention;
5. exact sign convention.

Current status:

\[
\text{RH relation not yet imported.}
\]

---

# 5. Classical import obligation 4 — Finite spaces

The toy model uses:

\[
V_N\cong\mathbb C^{d_N}.
\]

The classical project needs a finite space from the Bombieri/Weil approximation framework.

Possible forms:

1. finite zero-support spaces;
2. finite-dimensional test-function spaces;
3. finite spectral truncation spaces;
4. finite kernel matrix spaces.

Current status:

\[
V_N \text{ is currently abstract.}
\]

---

# 6. Classical import obligation 5 — Finite matrices

The project already modeled finite matrices:

\[
M_N=D_N^{1/2}A_ND_N^{1/2}.
\]

But the classical project must verify that this matrix is exactly the finite matrix appearing in the true Bombieri/Weil framework.

Requirements:

1. exact kernel;
2. exact weights;
3. exact multiplicities;
4. exact support conventions;
5. exact Hermitian convention;
6. exact negative-eigenvalue interpretation.

Current status:

\[
M_N \text{ is partially modeled but not fully classically validated.}
\]

---

# 7. Classical import obligation 6 — Approximation maps

The toy model uses:

\[
P_N:\mathcal D\to V_N.
\]

The classical project must define:

\[
P_N:\mathcal D_W\to V_N.
\]

Possible options:

1. projection onto finite basis;
2. sampling at finite support points;
3. truncation of a transform;
4. coefficient extraction;
5. finite interpolation.

Current status:

\[
P_N \text{ is missing.}
\]

---

# 8. Classical import obligation 7 — Convergence theorem

The central missing theorem is:

\[
Q_N(P_Nf)\to Q_W(f).
\]

The quantitative version is:

\[
|Q_N(P_Nf)-Q_W(f)|
\leq
\varepsilon_N(f),
\qquad
\varepsilon_N(f)\to0.
\]

This is the most important missing bridge.

Current status:

\[
\text{Convergence theorem missing.}
\]

---

# 9. Classical import obligation 8 — Certified computation link

The finite stability project can contribute only if:

1. \(M_N\) is the correct finite classical matrix;
2. \(\widetilde M_N\) is a certified approximation to \(M_N\);
3. the perturbation margin \(\mu_N\) is explicit;
4. finite negative directions can be certified;
5. certified finite negative directions connect to \(Q_W\) through convergence.

Current status:

\[
\text{Certified finite computation link is structurally defined but not classically completed.}
\]

---

# 10. Contribution meaning

This import map is not a breakthrough.

But it is valuable because it identifies the exact mathematical gap between:

\[
\text{finite matrix stability}
\]

and

\[
\text{RH-relevant Weil positivity}.
\]

The next serious phase must choose one classical source path and import the exact definitions.

---

# 11. Next target

Phase 10AO should create the classical-definition extraction plan:

1. identify source definitions;
2. extract \(Q_W\);
3. extract \(\mathcal D_W\);
4. extract finite matrix framework;
5. extract known RH-positivity theorem;
6. record what is theorem, what is assumption, and what is project-defined.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove convergence.

This phase does not claim novelty.

Exact audit strings:

CLASSICAL_IMPORT_MAP

TOY_TO_CLASSICAL_OBJECT_MAP

TEST_FUNCTION_SPACE_IMPORT_MISSING

INFINITE_WEIL_FORM_IMPORT_MISSING

RH_RELATION_IMPORT_MISSING

FINITE_MATRIX_CLASSICAL_VALIDATION_MISSING

APPROXIMATION_MAP_MISSING

CONVERGENCE_THEOREM_MISSING

NOT_RH_CONTRIBUTION_YET

