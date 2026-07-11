# Phase 7H — Centered Finite-Rank Quartet Testbed

## Purpose

Phase 7G created a toy finite-rank matrix experiment, but the crude sign model did not vanish at \(x=0\).

That is not ideal for a horizontal-defect laboratory.

This phase repairs the testbed by centering the synthetic off-critical quartet against its critical-line collapse.

The goal is not to prove RH.

The goal is to create a clean finite-rank diagnostic model whose signal vanishes exactly at the critical-line configuration.

---

# 1. Synthetic quartet

For horizontal displacement \(x\) and height \(\gamma\), define the synthetic quartet

\[
\rho_{\epsilon,\eta}(x)
=
\frac12+\epsilon x+i\eta\gamma,
\]

where

\[
\epsilon\in\{-1,+1\},
\qquad
\eta\in\{-1,+1\}.
\]

The critical-line collapse is

\[
\rho_{0,\eta}
=
\frac12+i\eta\gamma.
\]

---

# 2. Feature vector

Let

\[
w(\rho)=1-\frac1\rho.
\]

For degree \(m\), define the finite feature vector

\[
v_m(\rho)
=
(w(\rho),w(\rho)^2,\ldots,w(\rho)^m)^T.
\]

---

# 3. Centered quartet matrix

Define the centered finite-rank matrix

\[
C_m(x,\gamma)
=
\sum_{\epsilon=\pm1}
\sum_{\eta=\pm1}
v_m(\rho_{\epsilon,\eta}(x))v_m(\rho_{\epsilon,\eta}(x))^*
-
2\sum_{\eta=\pm1}
v_m(\rho_{0,\eta})v_m(\rho_{0,\eta})^*.
\]

The factor \(2\) appears because the off-critical quartet has two zeros at each sign of \(\eta\), while the collapsed critical-line pair has one zero at each sign.

---

# 4. Basic properties

## Proposition 1

The matrix \(C_m(x,\gamma)\) is Hermitian.

## Proof

Each term

\[
v v^*
\]

is Hermitian. A real linear combination of Hermitian matrices is Hermitian.

---

## Proposition 2

\[
C_m(0,\gamma)=0.
\]

## Proof

When \(x=0\),

\[
\rho_{+,\eta}(0)=\rho_{-,\eta}(0)=\rho_{0,\eta}.
\]

Therefore

\[
\sum_{\epsilon=\pm1}
\sum_{\eta=\pm1}
v_m(\rho_{\epsilon,\eta}(0))v_m(\rho_{\epsilon,\eta}(0))^*
=
2\sum_{\eta=\pm1}
v_m(\rho_{0,\eta})v_m(\rho_{0,\eta})^*.
\]

Subtracting the same quantity gives zero.

---

# 5. Why this is better than Phase 7G

The Phase 7G toy model used a crude sign rule.

The Phase 7H model instead measures the finite-rank matrix displacement from the critical-line collapse.

Thus the diagnostic signal is genuinely tied to horizontal displacement.

---

# 6. What the eigenvalues mean

If \(C_m(x,\gamma)\) has both positive and negative Rayleigh directions, then the finite feature space sees the off-critical quartet as an indefinite perturbation.

This resembles, at a toy level, the way off-critical zeros can create negative directions in positivity frameworks.

However:

\[
\boxed{
C_m(x,\gamma)\text{ is not a classical Weil quadratic form.}
}
\]

It is only a diagnostic finite-rank laboratory.

---

# 7. Phase conclusion

This phase repairs the finite-rank testbed by enforcing

\[
C_m(0,\gamma)=0.
\]

The next step is to study the scaling of positive and negative Rayleigh directions as \(x\to0\).

