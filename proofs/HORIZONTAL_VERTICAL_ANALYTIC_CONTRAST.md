# Horizontal–Vertical Analytic Contrast

## Phase 1E

This document replaces the project's rational signed-factor interpretation with a finite degree-preserving comparison between two reflection- and conjugation-invariant zero configurations.

---

# 1. Horizontal configuration

For

\[
\delta>0
\]

and

\[
\gamma>\delta,
\]

define

\[
H_{\delta,\gamma}
=
\left\{
\frac12+\epsilon\delta+i\eta\gamma:
\epsilon,\eta\in\{-1,+1\}
\right\}.
\]

This configuration contains four points counted with multiplicity.

It is invariant under

\[
z\mapsto\overline z
\]

and

\[
z\mapsto1-z.
\]

---

# 2. Vertical configuration

Define

\[
V_{\delta,\gamma}
=
\left\{
\frac12+i\eta(\gamma+\epsilon\delta):
\epsilon,\eta\in\{-1,+1\}
\right\}.
\]

Explicitly,

\[
V_{\delta,\gamma}
=
\left\{
\frac12+i(\gamma+\delta),
\frac12+i(\gamma-\delta),
\frac12-i(\gamma+\delta),
\frac12-i(\gamma-\delta)
\right\}.
\]

This configuration also contains four points counted with multiplicity.

It is invariant under conjugation and reflection.

---

# 3. Horizontal response

Let

\[
\rho_\eta
=
\frac12+i\eta\gamma.
\]

For a function \(f\) analytic near both centers, define

\[
\mathcal H_f(\delta,\gamma)
=
\sum_{\eta=\pm1}
\left[
f(\rho_\eta+\delta)
+
f(\rho_\eta-\delta)
-
2f(\rho_\eta)
\right].
\]

Taylor expansion gives

\[
f(\rho+\delta)+f(\rho-\delta)-2f(\rho)
=
\delta^2f''(\rho)
+
\frac{\delta^4}{12}f^{(4)}(\rho)
+
O(\delta^6).
\]

Therefore

\[
\mathcal H_f(\delta,\gamma)
=
\delta^2
\sum_{\eta=\pm1}
f''(\rho_\eta)
+
O(\delta^4).
\]

---

# 4. Vertical response

Define

\[
\mathcal V_f(\delta,\gamma)
=
\sum_{\eta=\pm1}
\left[
f(\rho_\eta+i\eta\delta)
+
f(\rho_\eta-i\eta\delta)
-
2f(\rho_\eta)
\right].
\]

For either sign of \(\eta\), the symmetric displacement pair is equivalent to displacement by

\[
\pm i\delta.
\]

Thus

\[
f(\rho+i\delta)+f(\rho-i\delta)-2f(\rho)
=
-\delta^2f''(\rho)
+
\frac{\delta^4}{12}f^{(4)}(\rho)
+
O(\delta^6).
\]

Hence

\[
\mathcal V_f(\delta,\gamma)
=
-\delta^2
\sum_{\eta=\pm1}
f''(\rho_\eta)
+
O(\delta^4).
\]

---

# 5. Matched directional contrast

Define

\[
\mathcal A_f(\delta,\gamma)
=
\mathcal H_f(\delta,\gamma)
-
\mathcal V_f(\delta,\gamma).
\]

Then

\[
\mathcal A_f(\delta,\gamma)
=
2\delta^2
\sum_{\eta=\pm1}
f''(\rho_\eta)
+
O(\delta^4).
\]

If

\[
f(\overline z)=\overline{f(z)},
\]

then

\[
f''(\overline z)
=
\overline{f''(z)}.
\]

Therefore

\[
\sum_{\eta=\pm1}
f''(\rho_\eta)
=
2\Re
f''\left(\frac12+i\gamma\right).
\]

Thus

\[
\boxed{
\mathcal A_f(\delta,\gamma)
=
4\delta^2
\Re
f''\left(\frac12+i\gamma\right)
+
O(\delta^4).
}
\]

Using the project susceptibility

\[
\chi_f(\gamma)
=
2\Re
f''\left(\frac12+i\gamma\right),
\]

we obtain

\[
\boxed{
\mathcal A_f(\delta,\gamma)
=
2\delta^2
\chi_f(\gamma)
+
O(\delta^4).
}
\]

Consequently,

\[
\boxed{
\chi_f(\gamma)
=
\lim_{\delta\to0}
\frac{
\mathcal A_f(\delta,\gamma)
}{
2\delta^2
}.
}
\]

---

# 6. Direct zero-configuration form

The doubled central-pair contributions cancel between

\[
\mathcal H_f
\]

and

\[
\mathcal V_f.
\]

Therefore

\[
\mathcal A_f(\delta,\gamma)
=
\sum_{\rho\in H_{\delta,\gamma}}f(\rho)
-
\sum_{\rho\in V_{\delta,\gamma}}f(\rho).
\]

Thus

\[
\boxed{
\chi_f(\gamma)
=
\lim_{\delta\to0}
\frac{
\sum_{\rho\in H_{\delta,\gamma}}f(\rho)
-
\sum_{\rho\in V_{\delta,\gamma}}f(\rho)
}{
2\delta^2
}.
}
\]

Both configurations contain exactly four points counted with multiplicity.

No negative point masses are required in this final contrast representation.

---

# 7. Finite polynomial factors

Define

\[
F_H(s;\delta,\gamma)
=
\prod_{\rho\in H_{\delta,\gamma}}
\left(
1-\frac{s}{\rho}
\right)
\]

and

\[
F_V(s;\delta,\gamma)
=
\prod_{\rho\in V_{\delta,\gamma}}
\left(
1-\frac{s}{\rho}
\right).
\]

Each is a degree-four polynomial in \(s\) up to its nonzero constant normalization.

Each zero multiset is reflection invariant.

Therefore the Phase 1D reflection-mediated Li bridge applies separately to both factors.

For the Li kernel \(f_n\),

\[
\mathscr L_n[F_H]
-
\mathscr L_n[F_V]
=
\sum_{\rho\in H_{\delta,\gamma}}f_n(\rho)
-
\sum_{\rho\in V_{\delta,\gamma}}f_n(\rho).
\]

Hence the Li susceptibility admits a finite entire-factor directional-contrast interpretation.

---

# 8. Harmonic interpretation

For an analytic function

\[
f=u+iv,
\]

the real part \(u\) is harmonic:

\[
u_{xx}+u_{yy}=0.
\]

The opposite signs of the horizontal and vertical quadratic responses are therefore consistent with

\[
u_{yy}=-u_{xx}.
\]

The matched directional contrast isolates twice the horizontal second-order response.

This is standard complex analysis and is not asserted as a project discovery.

---

# 9. What this repairs

The original signed double-orbit response was naturally represented by a rational finite factor because the baseline subtraction had negative multiplicity.

The horizontal–vertical contrast uses two degree-four finite zero factors.

It therefore preserves total zero count and avoids negative multiplicities in the two comparison objects.

---

# 10. What remains unproved

The finite factors are not Riemann xi-functions.

They have no demonstrated Euler product, Dirichlet series, prime interpretation, or global zeta zero set.

The result does not construct an entire deformation of the actual xi-function.

The result supplies an entire finite-factor interpretation of the local susceptibility object.

---

# 11. Candidate proposition status

The horizontal–vertical analytic contrast identity has a direct Taylor proof.

It must undergo symbolic and arbitrary-precision numerical validation before promotion to PROVED IN PROJECT.

No originality claim is made.
