# Phase 7J — Second-Order Coefficient Indefiniteness Audit

## Purpose

Phase 7I proved the centered finite-rank quartet scaling law

\[
C_m(x,\gamma)
=
x^2B_m(\gamma)+O_{m,\gamma}(x^4).
\]

This phase studies the second-order coefficient matrix

\[
B_m(\gamma).
\]

The question is whether the finite-rank horizontal displacement signal has both positive and negative Rayleigh directions.

This is not a proof of RH.

This is not a Weil theorem.

It is a finite-rank diagnostic audit.

---

# 1. Recall the centered matrix

For

\[
\rho_{\epsilon,\eta}(x)
=
\frac12+\epsilon x+i\eta\gamma,
\]

and

\[
v_m(\rho)
=
(w(\rho),w(\rho)^2,\ldots,w(\rho)^m)^T,
\qquad
w(\rho)=1-\frac1\rho,
\]

define

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

By Phase 7I,

\[
C_m(x,\gamma)
=
x^2B_m(\gamma)+O(x^4).
\]

---

# 2. Definition of second-order coefficient

The second-order coefficient is

\[
B_m(\gamma)
=
\lim_{x\to0}
\frac{C_m(x,\gamma)}{x^2}.
\]

Equivalently,

\[
B_m(\gamma)
=
\sum_{\eta=\pm1}
A_\eta''(0),
\]

where

\[
A_\eta(x)
=
v_m\left(\frac12+x+i\eta\gamma\right)
v_m\left(\frac12+x+i\eta\gamma\right)^*.
\]

---

# 3. Hermitian property

Since each

\[
C_m(x,\gamma)
\]

is Hermitian, and since the space of Hermitian matrices is closed under limits,

\[
B_m(\gamma)
\]

is Hermitian.

Therefore its Rayleigh quotients are real.

---

# 4. Why indefiniteness matters

If

\[
B_m(\gamma)
\]

has both positive and negative Rayleigh directions, then the centered finite-rank signal is not merely a positive energy.

It is an indefinite perturbation.

This resembles, at a toy level, the way off-critical zeros can create negative directions in positivity frameworks.

However, this resemblance is only diagnostic.

It does not establish a Weil criterion.

---

# 5. Audit goal

The computational audit estimates

\[
B_m(\gamma)
\approx
\frac{C_m(h,\gamma)}{h^2}
\]

for small \(h\), then scans Rayleigh quotients over a deterministic finite vector family.

The audit records whether both signs appear.

---

# 6. Boundary

This phase does not prove global indefiniteness for all degrees and all heights.

It does not prove a Weil theorem.

It does not prove RH.

It creates a reproducible finite-rank diagnostic for the second-order horizontal displacement signal.

