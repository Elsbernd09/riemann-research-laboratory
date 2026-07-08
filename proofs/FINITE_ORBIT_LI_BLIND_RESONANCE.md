# Finite-Orbit Li Blind-Scale Resonance

## Phase 4C

This document studies whether the individual Li zero-kernel quadratic-response blind-scale phenomenon survives finite aggregation over multiple critical-line conjugate orbits.

The model remains a finite orbit-response model.

It is not the complete Li coefficient zero sum.

---

# 1. Finite aggregate susceptibility

Let

\[
a_1,\ldots,a_J>0
\]

be fixed relative heights and let

\[
w_1,\ldots,w_J
\]

be fixed real weights.

For a common height parameter

\[
\Gamma>0,
\]

define

\[
\gamma_j
=
a_j\Gamma.
\]

The finite aggregate quadratic response is

\[
\boxed{
\mathcal X_n^{\mathbf a,\mathbf w}(\Gamma)
=
\sum_{j=1}^J
w_j
\chi_n^{\mathrm{Li}}(a_j\Gamma).
}
\]

---

# 2. Aggregate leading profile

Suppose

\[
\Gamma\to\infty
\]

and

\[
n/\Gamma\to c>0.
\]

For each fixed \(j\),

\[
\frac n{a_j\Gamma}
\to
\frac c{a_j}.
\]

Using the individual-kernel Li susceptibility scaling law,

\[
\chi_n^{\mathrm{Li}}(a_j\Gamma)
=
\Gamma^{-2}
a_j^{-2}
\Psi_{\mathrm{Li}}
\left(
\frac c{a_j}
\right)
+
o(\Gamma^{-2}).
\]

Since the orbit family is finite,

\[
\boxed{
\Gamma^2
\mathcal X_n^{\mathbf a,\mathbf w}(\Gamma)
\to
\Psi_{\mathbf a,\mathbf w}^{\mathrm{agg}}(c),
}
\]

where

\[
\boxed{
\Psi_{\mathbf a,\mathbf w}^{\mathrm{agg}}(c)
=
\sum_{j=1}^J
w_j
a_j^{-2}
\Psi_{\mathrm{Li}}
\left(
\frac c{a_j}
\right).
}
\]

---

# 3. Aggregate two-term expansion

For

\[
q_j
=
\frac n{a_j\Gamma}
\]

in fixed compact positive ranges, the individual two-term expansion gives

\[
\chi_n^{\mathrm{Li}}(a_j\Gamma)
=
\Gamma^{-2}
a_j^{-2}
\Psi_{\mathrm{Li}}(q_j)
+
\Gamma^{-4}
a_j^{-4}
K_{\mathrm{Li}}(q_j)
+
O(\Gamma^{-6}).
\]

For a finite orbit family,

\[
\boxed{
\mathcal X_n^{\mathbf a,\mathbf w}(\Gamma)
=
\Gamma^{-2}
\Psi_{\mathbf a,\mathbf w}^{\mathrm{agg}}(c)
+
\Gamma^{-4}
K_{\mathbf a,\mathbf w}^{\mathrm{agg}}(c)
+
O(\Gamma^{-6})
}
\]

along an exact path

\[
n/\Gamma=c,
\]

where

\[
\boxed{
K_{\mathbf a,\mathbf w}^{\mathrm{agg}}(c)
=
\sum_{j=1}^J
w_j
a_j^{-4}
K_{\mathrm{Li}}
\left(
\frac c{a_j}
\right).
}
\]

---

# 4. Two-orbit model

Take

\[
a_1=1,
\qquad
a_2=a>0,
\]

and

\[
w_1=w_2=1.
\]

Then

\[
\boxed{
\Psi_a^{(2)}(c)
=
\Psi_{\mathrm{Li}}(c)
+
a^{-2}
\Psi_{\mathrm{Li}}
\left(
\frac ca
\right).
}
\]

Let

\[
c_k
\]

be a positive individual Li response blind scale.

Since

\[
\Psi_{\mathrm{Li}}(c_k)=0,
\]

one has

\[
\boxed{
\Psi_a^{(2)}(c_k)
=
a^{-2}
\Psi_{\mathrm{Li}}
\left(
\frac{c_k}{a}
\right).
}
\]

Thus a blind scale of the first orbit remains a leading-order blind scale of the two-orbit aggregate if and only if

\[
\Psi_{\mathrm{Li}}
\left(
\frac{c_k}{a}
\right)
=
0.
\]

---

# 5. Two-orbit blind-scale resonance

The positive nonzero roots of

\[
\Psi_{\mathrm{Li}}
\]

are exactly

\[
c_0,c_1,c_2,\ldots.
\]

Therefore

\[
\Psi_{\mathrm{Li}}
\left(
\frac{c_k}{a}
\right)
=
0
\]

if and only if

\[
\frac{c_k}{a}
=
c_m
\]

for some

\[
m\ge0.
\]

Equivalently,

\[
\boxed{
a
=
\frac{c_k}{c_m}.
}
\]

Define the blind-scale ratio resonance set

\[
\boxed{
\mathcal R
=
\left\{
\frac{c_k}{c_m}:
k,m\ge0
\right\}.
}
\]

For the equal-weight two-orbit model, the individual blind coordinate

\[
c_k
\]

survives aggregation if and only if

\[
a\in\mathcal R
\]

with

\[
a=c_k/c_m
\]

for some \(m\).

Thus single-orbit blind-scale survival is non-generic with respect to the relative height ratio.

---

# 6. Resonant fourth-order coefficient

Suppose

\[
a
=
\frac{c_k}{c_m}
\]

and choose the exact common path

\[
n/\Gamma=c_k.
\]

Then

\[
n/(a\Gamma)=c_m.
\]

Both individual leading profiles vanish.

The aggregate response satisfies

\[
\boxed{
\mathcal X_n^{(2)}(\Gamma)
=
\Gamma^{-4}
K_{k,m}^{(2)}
+
O(\Gamma^{-6}),
}
\]

where

\[
\boxed{
K_{k,m}^{(2)}
=
K_{\mathrm{Li}}(c_k)
+
\left(
\frac{c_m}{c_k}
\right)^4
K_{\mathrm{Li}}(c_m).
}
\]

If

\[
K_{k,m}^{(2)}
\ne0,
\]

then

\[
\boxed{
\Gamma^4
\mathcal X_n^{(2)}(\Gamma)
\to
K_{k,m}^{(2)}.
}
\]

---

# 7. Parity obstruction to fourth-order cancellation

At a blind scale,

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

Since

\[
c_k
\in
\left(
\left(k+\frac12\right)\pi,
(k+1)\pi
\right),
\]

one has

\[
\boxed{
\operatorname{sgn}
K_{\mathrm{Li}}(c_k)
=
(-1)^{k+1}.
}
\]

The positive prefactor

\[
(c_m/c_k)^4
\]

does not change sign.

Therefore, if

\[
k\equiv m\pmod2,
\]

the two terms in

\[
K_{k,m}^{(2)}
\]

have the same sign.

Hence

\[
\boxed{
K_{k,m}^{(2)}
\ne0
}
\]

for every same-parity resonant pair.

Thus every same-parity two-orbit resonance has exact leading aggregate exponent

\[
4.
\]

For opposite-parity pairs, the correction terms have opposite signs and further cancellation is not excluded by sign alone.

---

# 8. General fully aligned finite resonance

Fix a reference blind scale

\[
c_{k_1}.
\]

Choose relative heights

\[
\boxed{
a_j
=
\frac{
c_{k_1}
}{
c_{k_j}
}
}
\]

for indices

\[
k_1,\ldots,k_J.
\]

Then at the common coordinate

\[
c=c_{k_1},
\]

one has

\[
\frac c{a_j}
=
c_{k_j}.
\]

Therefore every individual leading profile vanishes:

\[
\Psi_{\mathrm{Li}}
\left(
\frac c{a_j}
\right)
=
0.
\]

Hence

\[
\boxed{
\Psi_{\mathbf a,\mathbf w}^{\mathrm{agg}}
(c_{k_1})
=
0.
}
\]

The fourth-order aggregate coefficient is

\[
\boxed{
\sum_{j=1}^J
w_j
\left(
\frac{
c_{k_j}
}{
c_{k_1}
}
\right)^4
K_{\mathrm{Li}}(c_{k_j}).
}
\]

If this coefficient is nonzero, the fully aligned finite aggregate response has exponent \(4\).

---

# 9. Interpretation

The individual Li zero-kernel blind-scale phenomenon is generically unstable under addition of a nonresonant second orbit.

A second orbit restores a generic

\[
\Gamma^{-2}
\]

response at the first orbit's blind coordinate unless its relative height lies in the blind-scale ratio resonance set.

Exact simultaneous leading-order blindness is possible in finite synthetic orbit families whose relative heights are coordinated by ratios of profile zeros.

---

# 10. What is not proved

The actual Riemann zeta zero heights have not been shown to satisfy blind-scale ratio resonances.

No infinite zero sum is analyzed.

No statement about global Li coefficient blindness is made.

No result in this phase proves or supports RH.

---

# 11. Candidate status

The finite aggregate profile, two-orbit resonance condition, and same-parity fourth-order noncancellation have direct analytic derivations.

They require independent symbolic and arbitrary-precision validation in Phase 4D.

Originality remains unresolved.
