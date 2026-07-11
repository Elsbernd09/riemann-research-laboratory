# Phase 5T — Hermitian Symmetrization and Weil-Rank Obstruction

## Status

PROVED IN PROJECT — SYMMETRY-CLASS OBSTRUCTION.

CORRECTED INDEFINITE-SIGNATURE TARGET IDENTIFIED.

## Objective

Test whether the one-sided second log-moment Li test function

\[
G_n^{(2)}(y)
=
y^2G_n(y)
\]

admits a finite signed Hermitian convolution-square decomposition.

The answer is no.

The obstruction is exact and follows from reflection symmetry.

The correct Weil-side object corresponding to the real Li susceptibility is instead the Hermitian symmetrization of \(G_n^{(2)}\).

---

# 1. Hermitian reflection

For a complex-valued function \(u\) on the additive logarithmic line, define

\[
\widetilde u(y)
=
\overline{u(-y)}.
\]

Define the Hermitian autocorrelation

\[
h
=
u*\widetilde u.
\]

Then

\[
h(y)
=
\int_{\mathbb R}
u(x)
\overline{u(x-y)}
\,dx.
\]

Taking the complex conjugate gives

\[
\overline{h(y)}
=
\int_{\mathbb R}
\overline{u(x)}
u(x-y)
\,dx.
\]

After the change of variable

\[
z=x-y,
\]

we obtain

\[
\overline{h(y)}
=
\int_{\mathbb R}
u(z)
\overline{u(z+y)}
\,dz
=
h(-y).
\]

Therefore

\[
\boxed{
h(-y)
=
\overline{h(y)}.
}
\]

If \(u\) is real-valued, then

\[
\boxed{
h(-y)=h(y).
}
\]

Thus every real autocorrelation is even.

---

# 2. Signed sums preserve Hermitian symmetry

Let

\[
H(y)
=
\sum_{j=1}^r
\sigma_j
u_j*\widetilde u_j,
\]

where

\[
\sigma_j\in\{-1,+1\}.
\]

Each summand satisfies

\[
h_j(-y)
=
\overline{h_j(y)}.
\]

Because each \(\sigma_j\) is real,

\[
\boxed{
H(-y)
=
\overline{H(y)}.
}
\]

Hence every finite real signed sum of Hermitian convolution squares remains in the Hermitian reflection class.

The signs do not alter this constraint.

The rank does not alter this constraint.

---

# 3. One-sided second log-moment Li function

The Phase 5S test function is

\[
G_n^{(2)}(y)
=
y^2G_n(y),
\]

where

\[
G_n(y)
=
e^{-y/2}
\sum_{\ell=1}^n
\binom n\ell
\frac{(-1)^{\ell-1}y^{\ell-1}}
{(\ell-1)!}
\]

for

\[
y>0,
\]

and

\[
G_n(y)=0
\]

for

\[
y<0.
\]

Therefore

\[
G_n^{(2)}(y)=0
\]

for

\[
y<0.
\]

For every positive integer \(n\),

\[
G_n^{(2)}
\not\equiv0.
\]

Indeed, the polynomial-exponential formula contains the nonzero \(\ell=1\) term

\[
n y^2e^{-y/2}.
\]

Thus \(G_n^{(2)}\) is a nonzero real one-sided function.

---

# 4. Finite signed Weil-rank obstruction

Suppose, for contradiction, that

\[
G_n^{(2)}
=
\sum_{j=1}^r
\sigma_j
u_j*\widetilde u_j
\]

for a finite collection of functions \(u_j\) and real signs

\[
\sigma_j\in\{-1,+1\}.
\]

The right-hand side is Hermitian under reflection.

Since the left-hand side is real-valued, equality would imply

\[
G_n^{(2)}(-y)
=
G_n^{(2)}(y)
\]

for every \(y\) at which the equality is interpreted pointwise, or almost everywhere in an \(L^1/L^2\) interpretation.

Take

\[
y>0.
\]

Because \(G_n^{(2)}\) is one-sided,

\[
G_n^{(2)}(-y)=0.
\]

Hence Hermitian symmetry would require

\[
G_n^{(2)}(y)=0.
\]

This would hold for almost every positive \(y\), contradicting

\[
G_n^{(2)}
\not\equiv0.
\]

Therefore

\[
\boxed{
G_n^{(2)}
\text{ cannot be represented as a finite real signed sum of }
u_j*\widetilde u_j.
}
\]

The obstruction is purely symmetry-theoretic.

It is independent of basis choice and independent of numerical rank.

---

# 5. Correction to the Phase 5S target

The finite signed Weil-rank question posed directly for

\[
G_n^{(2)}
\]

was formulated in the wrong symmetry class.

The classical Weil quadratic architecture uses Hermitian convolution structure.

A nonzero real one-sided function cannot itself belong to the finite real signed span of Hermitian autocorrelations.

Thus the direct Phase 5S finite signed rank target is rejected.

---

# 6. Hermitian symmetrization

Define

\[
\boxed{
H_n^{(2)}(y)
=
G_n^{(2)}(y)
+
G_n^{(2)}(-y).
}
\]

Because \(G_n^{(2)}\) is real,

\[
H_n^{(2)}(-y)
=
H_n^{(2)}(y).
\]

Therefore

\[
\boxed{
H_n^{(2)}
\text{ is real and even.}
}
\]

It lies in the correct reflection symmetry class for comparison with real Hermitian Weil test functions.

---

# 7. Exact susceptibility Fourier identity

From Phase 5S,

\[
\chi_n^{Li}(\gamma)
=
2
\int_0^\infty
G_n^{(2)}(y)
\cos(\gamma y)
\,dy.
\]

The Fourier transform of the symmetrized function is

\[
\begin{aligned}
\widehat H_n^{(2)}(\gamma)
&=
\int_{-\infty}^{\infty}
H_n^{(2)}(y)
e^{-i\gamma y}
\,dy
\\
&=
\int_0^\infty
G_n^{(2)}(y)e^{-i\gamma y}
\,dy
+
\int_{-\infty}^0
G_n^{(2)}(-y)e^{-i\gamma y}
\,dy.
\end{aligned}
\]

Changing variables in the second integral gives

\[
\widehat H_n^{(2)}(\gamma)
=
\int_0^\infty
G_n^{(2)}(y)
\left(
e^{-i\gamma y}
+
e^{i\gamma y}
\right)
dy.
\]

Therefore

\[
\boxed{
\widehat H_n^{(2)}(\gamma)
=
2
\int_0^\infty
G_n^{(2)}(y)\cos(\gamma y)\,dy
=
\chi_n^{Li}(\gamma).
}
\]

Thus the real Li susceptibility is exactly the Fourier transform of the Hermitian symmetrization of the second log-moment Li test function.

---

# 8. Single positive-square obstruction

Suppose

\[
H_n^{(2)}
=
u*\widetilde u.
\]

Fourier transformation gives

\[
\widehat H_n^{(2)}(\gamma)
=
|\widehat u(\gamma)|^2
\ge0.
\]

But

\[
\widehat H_n^{(2)}(\gamma)
=
\chi_n^{Li}(\gamma).
\]

The Li susceptibility is sign-changing.

Its matched-scale profile is

\[
\Psi_{Li}(c)
=
-2c
\left(
c\cos c
+
2\sin c
\right),
\]

which takes both positive and negative values.

Therefore

\[
\boxed{
H_n^{(2)}
\text{ is not a single positive Hermitian convolution square.}
}
\]

The susceptibility cannot be represented by one positive Weil-energy channel.

---

# 9. Correct indefinite-signature problem

The surviving structural question is whether

\[
H_n^{(2)}
\]

admits a finite indefinite Hermitian decomposition

\[
\boxed{
H_n^{(2)}
=
\sum_{j=1}^{r_+(n)}
u_{n,j}*\widetilde u_{n,j}
-
\sum_{k=1}^{r_-(n)}
v_{n,k}*\widetilde v_{n,k}.
}
\]

The associated signature is

\[
\boxed{
\operatorname{sig}_W(H_n^{(2)})
=
\left(
r_+(n),
r_-(n)
\right).
}
\]

A meaningful finite-rank theorem requires a specified admissible function class and a specified basis or minimality notion.

Without those choices, arbitrary spectral positive-negative decomposition can obscure the algebraic structure.

The next target is therefore the natural polynomial-exponential Hardy/Mellin basis inherited from

\[
G_n^{(2)}.
\]

---

# 10. Natural rational transform basis

Define

\[
\phi_k(y)
=
\frac{y^k}{k!}
e^{-y/2}
\mathbf 1_{y>0},
\qquad
k\ge0.
\]

With Fourier convention

\[
\widehat f(\gamma)
=
\int_{\mathbb R}
f(y)e^{-i\gamma y}\,dy,
\]

we have

\[
\boxed{
\widehat\phi_k(\gamma)
=
\frac1{(1/2+i\gamma)^{k+1}}.
}
\]

The one-sided second log-moment Li function lies in

\[
\operatorname{span}
\{
\phi_2,\phi_3,\ldots,\phi_{n+1}
\}.
\]

Its Hermitian symmetrization has Fourier transform

\[
\chi_n^{Li}(\gamma)
=
f_n''
\left(
\frac12+i\gamma
\right)
+
f_n''
\left(
\frac12-i\gamma
\right).
\]

Thus the corrected finite-signature problem can be formulated algebraically in the rational basis generated by

\[
\left\{
(1/2+i\gamma)^{-k}
\right\}.
\]

The next phase must determine whether the susceptibility rational function admits a finite Hermitian Gram representation

\[
\chi_n^{Li}(\gamma)
=
V_n(\gamma)^*
A_n
V_n(\gamma),
\]

for a natural finite vector \(V_n\) of rational basis functions and a real Hermitian matrix \(A_n\).

If such a representation exists, the inertia of \(A_n\) gives a basis-relative signed Weil signature.

The distinction between basis-relative inertia and an intrinsic minimal signature must be maintained.

---

# 11. Prior-art boundary

Bombieri's Weil quadratic functional explicitly uses Hermitian convolution structure and studies its Fourier-side quadratic-form and eigenvalue representation.

Therefore no originality claim is made for convolution-square positivity, Fourier quadratic forms, finite matrix truncations, or signature analysis in general.

The project-specific question is the algebraic Gram representation of the Hermitian Li susceptibility kernel

\[
H_n^{(2)}
\]

and the behavior of its signature in the natural Li polynomial-exponential basis.

No subsuming source identified in the current audit.

This is not a novelty claim.

---

# 12. Restrictions

This phase does not prove RH.

The direct finite signed Weil-rank target for the one-sided function \(G_n^{(2)}\) has failed.

The symmetrized kernel \(H_n^{(2)}\) is the corrected object.

No finite Gram representation has yet been proved.

No signature law has yet been proved.

No RH implication has been established.

