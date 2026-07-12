# Phase 12I — Approximation Error Decomposition

## Purpose

Phase 12H proved the negative obstruction detection template.

The remaining hard theorem is:

\[
|Q_N(P_Ng)-Q_W(g)|\le \varepsilon_N(g)
\]

with

\[
\varepsilon_N(g)\to0.
\]

Phase 12I decomposes this approximation error into named terms.

---

# 1. Provisional infinite form

From Phase 12E and Phase 12G, define provisionally:

\[
Q_W(g)=T[g*g^*].
\]

The spectral form is:

\[
Q_W(g)
=
\sum_\rho
\widehat g(\rho)
\overline{\widehat g(1-\bar\rho)}.
\]

This is still provisional pending primary-source confirmation and sign-convention review.

---

# 2. Finite form

Let

\[
Q_N(P_Ng)
\]

be the finite approximating quadratic form.

At this stage, \(P_N\) is not yet classically imported.

So the finite form remains:

\[
Q_N(P_Ng)
\]

with \(P_N\) treated as a required object for the next theorem stage.

---

# 3. Total approximation error

Define

\[
E_N(g)
=
Q_N(P_Ng)-Q_W(g).
\]

The Level 4 target requires:

\[
|E_N(g)|\le \varepsilon_N(g)
\]

with

\[
\varepsilon_N(g)\to0.
\]

For a finite test class,

\[
\mathcal F_R^{(m)}
=
\left\{
g=\sum_{j=1}^m a_j\phi_j:\|a\|_2\le R
\right\},
\]

the uniform target is:

\[
\sup_{g\in\mathcal F_R^{(m)}} |E_N(g)|
\le
\varepsilon_N(R,m)\to0.
\]

---

# 4. Error decomposition

We decompose:

\[
E_N(g)
=
T_N(g)+P_N^{err}(g)+S_N(g)+C_N(g).
\]

The terms are:

\[
T_N(g)
\]

truncation error;

\[
P_N^{err}(g)
\]

projection error;

\[
S_N(g)
\]

source-normalization/sign-convention error;

\[
C_N(g)
\]

computational/certification error.

Thus,

\[
|E_N(g)|
\le
|T_N(g)|
+
|P_N^{err}(g)|
+
|S_N(g)|
+
|C_N(g)|.
\]

---

# 5. Truncation error

The truncation error is the difference between the true infinite form and a source-grounded finite truncation before projection error.

Symbolically:

\[
T_N(g)
=
Q_N^{ideal}(g)-Q_W(g).
\]

Needed theorem:

\[
|T_N(g)|\le \tau_N(g)
\]

with

\[
\tau_N(g)\to0.
\]

For finite test classes:

\[
\sup_{g\in\mathcal F_R^{(m)}} |T_N(g)|
\le
\tau_N(R,m)\to0.
\]

---

# 6. Projection error

The projection error measures the loss caused by replacing \(g\) with \(P_Ng\).

Symbolically:

\[
P_N^{err}(g)
=
Q_N(P_Ng)-Q_N^{ideal}(g).
\]

Needed theorem:

\[
|P_N^{err}(g)|\le \pi_N(g)
\]

with

\[
\pi_N(g)\to0.
\]

For finite test classes:

\[
\sup_{g\in\mathcal F_R^{(m)}} |P_N^{err}(g)|
\le
\pi_N(R,m)\to0.
\]

---

# 7. Source-normalization/sign-convention error

Because \(Q_W(g)=T[g*g^*]\) is still provisionally imported, we introduce a source-normalization/sign term:

\[
S_N(g).
\]

This term records uncertainty from:

1. sign convention;
2. Haar measure convention;
3. star-involution normalization;
4. compatibility between the extracted \(T[f]\) and the provisional \(g*g^*\) import.

If primary-source review confirms exact compatibility, then:

\[
S_N(g)=0.
\]

Until then, this term is not allowed to be silently ignored.

Needed theorem or source confirmation:

\[
S_N(g)=0.
\]

---

# 8. Computational error

The computational/certification error is:

\[
C_N(g).
\]

This includes:

1. interval arithmetic error;
2. matrix-entry approximation error;
3. quadrature error;
4. finite precision error;
5. implementation error.

Earlier phases already created a model for certified computational error.

Needed theorem:

\[
|C_N(g)|\le \chi_N(g)
\]

with controlled or vanishing \(\chi_N(g)\).

For finite test classes:

\[
\sup_{g\in\mathcal F_R^{(m)}} |C_N(g)|
\le
\chi_N(R,m).
\]

---

# Theorem 12I.1 — Approximation error decomposition bound

Assume

\[
E_N(g)=T_N(g)+P_N^{err}(g)+S_N(g)+C_N(g).
\]

Assume bounds:

\[
|T_N(g)|\le\tau_N(g),
\]

\[
|P_N^{err}(g)|\le\pi_N(g),
\]

\[
|S_N(g)|\le\sigma_N(g),
\]

\[
|C_N(g)|\le\chi_N(g).
\]

Then

\[
|Q_N(P_Ng)-Q_W(g)|
\le
\tau_N(g)+\pi_N(g)+\sigma_N(g)+\chi_N(g).
\]

## Proof

By definition,

\[
Q_N(P_Ng)-Q_W(g)
=
T_N(g)+P_N^{err}(g)+S_N(g)+C_N(g).
\]

By the triangle inequality,

\[
|Q_N(P_Ng)-Q_W(g)|
\le
|T_N(g)|
+
|P_N^{err}(g)|
+
|S_N(g)|
+
|C_N(g)|.
\]

Using the assumed bounds gives

\[
|Q_N(P_Ng)-Q_W(g)|
\le
\tau_N(g)+\pi_N(g)+\sigma_N(g)+\chi_N(g).
\]

\[
\square
\]

---

# Corollary 12I.2 — Uniform finite-class approximation bound

Assume for every \(g\in\mathcal F_R^{(m)}\),

\[
|T_N(g)|\le\tau_N(R,m),
\]

\[
|P_N^{err}(g)|\le\pi_N(R,m),
\]

\[
|S_N(g)|\le\sigma_N(R,m),
\]

\[
|C_N(g)|\le\chi_N(R,m).
\]

Then

\[
\sup_{g\in\mathcal F_R^{(m)}}
|Q_N(P_Ng)-Q_W(g)|
\le
\tau_N(R,m)
+
\pi_N(R,m)
+
\sigma_N(R,m)
+
\chi_N(R,m).
\]

---

# 9. Level 4 convergence target

The Level 4 convergence target is now exact:

\[
\tau_N(R,m)
+
\pi_N(R,m)
+
\sigma_N(R,m)
+
\chi_N(R,m)
\to0.
\]

If source review proves

\[
\sigma_N(R,m)=0,
\]

then the target becomes:

\[
\tau_N(R,m)+\pi_N(R,m)+\chi_N(R,m)\to0.
\]

This is the real battle.

---

# 10. Next target

Phase 12J should attack the source-normalization/sign term:

\[
S_N(g).
\]

The goal is either:

1. prove \(S_N(g)=0\) using source confirmation;
2. keep it unresolved and stop;
3. define a primary-source checklist that must be satisfied before \(S_N(g)\) can be set to zero.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove finite approximation convergence.

This phase does not prove Level 4 contribution.

This phase does not establish novelty.

Exact audit strings:

APPROXIMATION_ERROR_DECOMPOSITION_COMPLETE

TOTAL_ERROR_E_N_DEFINED

TRUNCATION_ERROR_TERM_DEFINED

PROJECTION_ERROR_TERM_DEFINED

SOURCE_NORMALIZATION_ERROR_TERM_DEFINED

COMPUTATIONAL_ERROR_TERM_DEFINED

APPROXIMATION_ERROR_BOUND_PROVED

UNIFORM_FINITE_CLASS_BOUND_PROVED

FINITE_APPROXIMATION_CONVERGENCE_STILL_MISSING

LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED

