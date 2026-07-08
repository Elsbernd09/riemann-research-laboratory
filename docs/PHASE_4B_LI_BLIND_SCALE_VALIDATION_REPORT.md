# Phase 4B Li Blind-Scale Validation Report

## Objective

Independently validate the profile-zero structure, two-term coupled susceptibility expansion, exact blind-scale response law, and near-blind transition hierarchy derived in Phase 4A.

---

# 1. Blind-scale roots

The positive nonzero zeros of

\[
\Psi_{\mathrm{Li}}(c)
=
-2c(c\cos c+2\sin c)
\]

satisfy

\[
\tan c=-c/2.
\]

High-precision monotone bisection verified exactly one root in each tested interval

\[
\left(
\left(k+\frac12\right)\pi,
(k+1)\pi
\right).
\]

The first blind scale is

\[
c_0
=
2.288929728103404364821414172\ldots
\]

Status:

VALIDATED.

---

# 2. Large-k root asymptotic

The candidate approximation

\[
c_k
=
a_k
+
\frac2{a_k}
-
\frac{20}{3a_k^3}
+
O(a_k^{-5}),
\]

where

\[
a_k=
\left(k+\frac12\right)\pi,
\]

was tested at high precision.

The root error exhibited the predicted fifth-power asymptotic scale.

Status:

VALIDATED.

---

# 3. Two-term susceptibility expansion

Independent symbolic coefficient extraction reproduced

\[
\chi_n^{\mathrm{Li}}(\gamma)
=
\gamma^{-2}
\Psi_{\mathrm{Li}}(q)
+
\gamma^{-4}
K_{\mathrm{Li}}(q)
+
O_q(\gamma^{-6}),
\]

with

\[
q=n/\gamma
\]

and

\[
K_{\mathrm{Li}}(q)
=
\frac43q^2\cos q
+
\left(
2q-\frac{q^3}{6}
\right)\sin q.
\]

The symbolic validator also reproduced the blind-scale simplification

\[
K_{\mathrm{Li}}(c_k)
=
\frac{
c_k^2(c_k^2+4)
}{
12
}
\cos c_k.
\]

Status:

VALIDATED.

---

# 4. Exact matched blind-scale law

For integer \(n\), the validation path

\[
\gamma=n/c_k
\]

enforces

\[
n/\gamma=c_k
\]

exactly.

Across multiple blind-scale indices and increasing \(n\), the scaled susceptibility

\[
\gamma^4
\chi_n^{\mathrm{Li}}(\gamma)
\]

converged toward

\[
\frac{
c_k^2(c_k^2+4)
}{
12
}
\cos c_k.
\]

Thus the generic height exponent \(2\) is replaced by exponent \(4\) at exact matched profile zeros.

Status:

VALIDATED.

---

# 5. Integer-index path control

Near-blind validation did not round a real-valued candidate for \(n\).

For each integer \(n\), the experiment solved

\[
\frac n\gamma-c_k
=
\beta\gamma^{-r}
\]

for \(\gamma\).

This avoids an integer-rounding error of order

\[
\gamma^{-1},
\]

which would dominate the intended path displacement for

\[
r>1.
\]

The solved path residual was checked at arbitrary precision.

---

# 6. Near-blind transition hierarchy

The experiment used

\[
\beta=1
\]

and

\[
r
\in
\left\{
\frac12,
1,
\frac32,
2,
3
\right\}.
\]

The predicted effective exponents were

\[
2.5,
3,
3.5,
4,
4.
\]

For

\[
0<r<2,
\]

the scaled response

\[
\gamma^{2+r}
\chi_n^{\mathrm{Li}}(\gamma)
\]

converged toward

\[
\Psi_{\mathrm{Li}}'(c_0).
\]

For

\[
r=2,
\]

the scaled response

\[
\gamma^4
\chi_n^{\mathrm{Li}}(\gamma)
\]

converged toward

\[
\Psi_{\mathrm{Li}}'(c_0)
+
K_{\mathrm{Li}}(c_0).
\]

For

\[
r>2,
\]

the same fourth-power scaling converged toward

\[
K_{\mathrm{Li}}(c_0).
\]

Status:

VALIDATED.

---

# 7. Mathematical status

The project promotes the following to PROVED IN PROJECT:

1. the positive Li quadratic-response profile has exactly one nonzero root in each interval
   \[
   ((k+1/2)\pi,(k+1)\pi);
   \]

2. the roots satisfy
   \[
   \tan c_k=-c_k/2;
   \]

3. the Li susceptibility admits the compact-range two-term expansion
   \[
   \gamma^{-2}\Psi_{\mathrm{Li}}(q)
   +
   \gamma^{-4}K_{\mathrm{Li}}(q)
   +
   O_q(\gamma^{-6});
   \]

4. exact matched blind-scale paths exhibit
   \[
   \gamma^{-4}
   \]
   response rather than generic
   \[
   \gamma^{-2}
   \]
   response;

5. near a simple blind scale, a path satisfying
   \[
   n/\gamma-c_k
   \sim
   \beta\gamma^{-r}
   \]
   exhibits the transition exponent
   \[
   2+\min(r,2)
   \]
   unless the displayed coefficient cancels at the critical rate.

---

# 8. Interpretation

The individual Li zero-kernel quadratic response possesses profile-degenerate parameter-height scales at which its leading susceptibility vanishes.

The effective response exponent depends on the rate at which the coupled parameter path approaches a simple profile zero.

This is a statement about the individual kernel response.

It is not currently a theorem about global Li coefficient blind spots.

---

# 9. Originality status

Unresolved.

Prior-art review has established substantial ancestry for:

- Li zero-location sensitivity;
- index-versus-zero-height scaling;
- reflection pairing;
- abstract multiset formulations;
- shifted-product horizontal quartet geometry.

No materially equivalent source has yet been identified for the combined quadratic-response profile and near-blind transition hierarchy.

Absence of an identified source is not proof of novelty.

---

# 10. RH implication

None established.

The blind-scale hierarchy does not prove RH, exclude off-critical zeros, or establish global Li positivity.
