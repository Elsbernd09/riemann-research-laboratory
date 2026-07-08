# Li Quadratic-Response Blind Scales

## Phase 4A

This document derives consequences of the limiting Li zero-kernel quadratic-response profile

\[
\Psi_{\mathrm{Li}}(c)
=
-2c(c\cos c+2\sin c).
\]

The results concern the individual fixed Li zero-kernel susceptibility defined in the project.

They do not assert blind scales for the complete global Li coefficient sequence.

---

# 1. Exact susceptibility

For

\[
f_n(z)
=
1-
\left(
1-\frac1z
\right)^n,
\]

the project proved

\[
\chi_n^{\mathrm{Li}}(\gamma)
=
2\Re
f_n''
\left(
\frac12+i\gamma
\right).
\]

The exact formula is

\[
\chi_n^{\mathrm{Li}}(\gamma)
=
-
\frac{
2n
}{
(\gamma^2+\frac14)^2
}
\left[
n\cos(n\theta_\gamma)
+
2\gamma\sin(n\theta_\gamma)
\right],
\]

where

\[
\theta_\gamma
=
2\arctan
\left(
\frac1{2\gamma}
\right).
\]

---

# 2. Leading coupled response profile

If

\[
\gamma\to\infty
\]

and

\[
\frac n\gamma\to c>0,
\]

then

\[
\gamma^2
\chi_n^{\mathrm{Li}}(\gamma)
\to
\Psi_{\mathrm{Li}}(c),
\]

where

\[
\boxed{
\Psi_{\mathrm{Li}}(c)
=
-2c(c\cos c+2\sin c).
}
\]

---

# 3. No unconstrained global optimum

The profile contains the term

\[
-2c^2\cos c.
\]

Along sequences for which

\[
|\cos c|
\]

is bounded away from zero and \(c\to\infty\),

\[
|\Psi_{\mathrm{Li}}(c)|
\]

is unbounded.

Therefore

\[
\boxed{
\sup_{c>0}
|\Psi_{\mathrm{Li}}(c)|
=
\infty.
}
\]

Thus there is no unconstrained globally optimal similarity coordinate maximizing the magnitude of the leading Li quadratic response.

Any optimization question requires an external parameter-budget, cost, or admissible-coordinate constraint.

---

# 4. Positive profile zeros

For

\[
c>0,
\]

a nonzero root of

\[
\Psi_{\mathrm{Li}}(c)
\]

satisfies

\[
c\cos c+2\sin c=0.
\]

Since such a root cannot satisfy

\[
\cos c=0,
\]

the root equation is equivalent to

\[
\boxed{
\tan c=-\frac c2.
}
\]

For each integer

\[
k\ge0,
\]

define

\[
I_k
=
\left(
\left(k+\frac12\right)\pi,
(k+1)\pi
\right).
\]

On \(I_k\),

\[
h(c)
=
\tan c+\frac c2
\]

is strictly increasing because

\[
h'(c)
=
\sec^2 c+\frac12>0.
\]

Moreover,

\[
h(c)\to-\infty
\]

at the left endpoint and

\[
h(c)\to\frac{(k+1)\pi}{2}>0
\]

at the right endpoint.

Therefore there exists exactly one positive root

\[
c_k
\]

in each \(I_k\).

On

\[
(k\pi,(k+\frac12)\pi),
\]

the tangent is positive and cannot equal \(-c/2\).

Hence the positive nonzero roots of the Li response profile consist of exactly one root

\[
\boxed{
c_k\in
\left(
\left(k+\frac12\right)\pi,
(k+1)\pi
\right)
}
\]

for every

\[
k\ge0.
\]

The project calls these

QUADRATIC-RESPONSE BLIND SCALES

for the individual Li zero-kernel response.

The terminology is project-specific and remains under novelty review.

---

# 5. Large-index root asymptotics

Let

\[
a_k
=
\left(k+\frac12\right)\pi.
\]

Write

\[
c_k
=
a_k+\varepsilon_k.
\]

The equation

\[
\tan c_k=-\frac{c_k}{2}
\]

becomes

\[
\cot\varepsilon_k
=
\frac{
a_k+\varepsilon_k
}{
2
}.
\]

Using

\[
\cot\varepsilon
=
\frac1\varepsilon
-
\frac{\varepsilon}{3}
-
\frac{\varepsilon^3}{45}
+
O(\varepsilon^5),
\]

asymptotic inversion gives

\[
\boxed{
c_k
=
a_k
+
\frac2{a_k}
-
\frac{20}{3a_k^3}
+
O(a_k^{-5}).
}
\]

In particular,

\[
c_k
=
\left(k+\frac12\right)\pi
+
O(k^{-1}).
\]

---

# 6. Two-term coupled susceptibility expansion

Define

\[
q
=
\frac n\gamma.
\]

For \(q\) restricted to a fixed compact subset of \((0,\infty)\),

\[
\theta_\gamma
=
\frac1\gamma
-
\frac1{12\gamma^3}
+
O(\gamma^{-5}),
\]

so

\[
n\theta_\gamma
=
q
-
\frac q{12\gamma^2}
+
O_q(\gamma^{-4}).
\]

Also,

\[
\left(
\gamma^2+\frac14
\right)^{-2}
=
\gamma^{-4}
\left[
1-\frac1{2\gamma^2}
+
O(\gamma^{-4})
\right].
\]

Substitution into the exact susceptibility gives

\[
\boxed{
\chi_n^{\mathrm{Li}}(\gamma)
=
\gamma^{-2}
\Psi_{\mathrm{Li}}(q)
+
\gamma^{-4}
K_{\mathrm{Li}}(q)
+
O_q(\gamma^{-6}),
}
\]

where

\[
\boxed{
K_{\mathrm{Li}}(q)
=
q(q\cos q+2\sin q)
+
\frac{q^2}{6}
(-q\sin q+2\cos q).
}
\]

Equivalently,

\[
\boxed{
K_{\mathrm{Li}}(q)
=
\frac43q^2\cos q
+
\left(
2q-\frac{q^3}{6}
\right)\sin q.
}
\]

The uniformity claim in compact q-ranges must be independently reviewed during Phase 4B.

---

# 7. Exact matched blind-scale response

Let

\[
c_k
\]

be a positive profile zero.

Consider a path satisfying

\[
\frac n\gamma=c_k
\]

exactly.

Then

\[
\Psi_{\mathrm{Li}}(c_k)=0,
\]

and therefore

\[
\chi_n^{\mathrm{Li}}(\gamma)
=
\gamma^{-4}
K_{\mathrm{Li}}(c_k)
+
O(\gamma^{-6}).
\]

At a profile root,

\[
\sin c_k
=
-\frac{c_k}{2}\cos c_k.
\]

Hence

\[
\boxed{
K_{\mathrm{Li}}(c_k)
=
\frac{
c_k^2(c_k^2+4)
}{
12
}
\cos c_k.
}
\]

Since

\[
\cos c_k\ne0,
\]

one has

\[
K_{\mathrm{Li}}(c_k)\ne0.
\]

Thus

\[
\boxed{
\gamma^4
\chi_n^{\mathrm{Li}}(\gamma)
\to
\frac{
c_k^2(c_k^2+4)
}{
12
}
\cos c_k
}
\]

along exact matched paths.

The generic height exponent \(2\) is replaced by exponent \(4\) at an exact quadratic-response blind scale.

---

# 8. Simplicity of blind scales

Define

\[
B(c)
=
c\cos c+2\sin c.
\]

Then

\[
\Psi_{\mathrm{Li}}(c)
=
-2cB(c).
\]

At a positive root \(c_k\),

\[
\Psi_{\mathrm{Li}}'(c_k)
=
-2c_kB'(c_k).
\]

Since

\[
B'(c)
=
3\cos c-c\sin c,
\]

and

\[
\sin c_k
=
-\frac{c_k}{2}\cos c_k,
\]

one obtains

\[
B'(c_k)
=
\left(
3+\frac{c_k^2}{2}
\right)
\cos c_k
\ne0.
\]

Therefore every positive blind scale is a simple profile zero.

---

# 9. Near-blind parameter paths

Suppose

\[
q_\gamma
=
\frac n\gamma
\]

satisfies

\[
q_\gamma-c_k
\sim
\beta\gamma^{-r},
\qquad
\beta\ne0.
\]

Since \(c_k\) is a simple profile zero,

\[
\Psi_{\mathrm{Li}}(q_\gamma)
=
\Psi_{\mathrm{Li}}'(c_k)
(q_\gamma-c_k)
+
O((q_\gamma-c_k)^2).
\]

Combining with the two-term susceptibility expansion gives the following candidate transition laws.

## Case 0 < r < 2

\[
\boxed{
\chi_n^{\mathrm{Li}}(\gamma)
\sim
\beta
\Psi_{\mathrm{Li}}'(c_k)
\gamma^{-(2+r)}.
}
\]

## Case r = 2

\[
\boxed{
\gamma^4
\chi_n^{\mathrm{Li}}(\gamma)
\to
\beta
\Psi_{\mathrm{Li}}'(c_k)
+
K_{\mathrm{Li}}(c_k).
}
\]

## Case r > 2

\[
\boxed{
\gamma^4
\chi_n^{\mathrm{Li}}(\gamma)
\to
K_{\mathrm{Li}}(c_k).
}
\]

Thus, absent a further coefficient cancellation, the effective height exponent follows

\[
\boxed{
\alpha_{\mathrm{eff}}
=
2+\min(r,2).
}
\]

At the critical approach rate \(r=2\), a specially chosen \(\beta\) can cancel the displayed order-four coefficient and require a deeper expansion.

That deeper cancellation is not analyzed in Phase 4A.

---

# 10. Interpretation boundary

The theorem concerns the individual Li zero-kernel quadratic response.

The project has not established that the full Li coefficient sequence exhibits observable global blind scales at the same coordinates.

The complete zero sum may produce collective effects that change practical detectability.

Accordingly, the project must not state that "Li coefficients have blind spots."

The supported project phrase is:

"the individual Li zero-kernel quadratic response has profile-degenerate blind scales."

---

# 11. Claim status

The profile-zero location theorem, two-term expansion, and transition laws have direct analytic derivations.

They remain candidates pending independent symbolic, arbitrary-precision, and path-scaling validation in Phase 4B.

No originality claim is made.
