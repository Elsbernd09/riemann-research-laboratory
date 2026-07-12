# Phase 8R — Log-Coordinate Bridge to Fourier Side

## Purpose

Phase 8Q recorded the source evidence chain for Bombieri's Fourier-side program.

Phase 8R builds the algebraic bridge from the multiplicative \(x\)-variable to the additive log-coordinate.

This phase does not implement a matrix.

This phase does not compute eigenvalues.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. Change of variables

Let

\[
x=e^u.
\]

Given a multiplicative test function

\[
f(x),
\]

define the additive half-density

\[
F(u)=e^{u/2}f(e^u).
\]

Equivalently,

\[
f(e^u)=e^{-u/2}F(u).
\]

This is the natural log-coordinate normalization because it converts the mass terms in Bombieri's \(T[f]\) formula into symmetric hyperbolic weights.

---

# 2. Involution in log coordinates

Bombieri's algebraic involution is

\[
f^*(x)=x^{-1}f(1/x).
\]

Evaluate at \(x=e^u\):

\[
f^*(e^u)=e^{-u}f(e^{-u}).
\]

Since

\[
f(e^{-u})=e^{u/2}F(-u),
\]

we get

\[
f^*(e^u)=e^{-u/2}F(-u).
\]

Thus the additive half-density of \(f^*\) is

\[
F^*(u)=F(-u).
\]

So the multiplicative involution becomes ordinary reflection in log coordinates.

---

# 3. Mass terms

Using

\[
dx=e^u\,du,
\]

we have

\[
\int_0^\infty f(x)\,dx
=
\int_{-\infty}^{\infty} e^{u/2}F(u)\,du.
\]

Similarly,

\[
\int_0^\infty f^*(x)\,dx
=
\int_{-\infty}^{\infty} e^{-u/2}F(u)\,du.
\]

Therefore,

\[
\int_0^\infty f(x)\,dx
+
\int_0^\infty f^*(x)\,dx
=
\int_{-\infty}^{\infty}2\cosh(u/2)F(u)\,du.
\]

---

# 4. Prime-side term

For \(n\ge1\),

\[
f(n)=n^{-1/2}F(\log n).
\]

Also,

\[
f^*(n)=n^{-1/2}F(-\log n).
\]

Therefore Bombieri's prime-side term becomes

\[
-\sum_{n=1}^{\infty}
\frac{\Lambda(n)}{\sqrt n}
\left(
F(\log n)+F(-\log n)
\right).
\]

---

# 5. Multiplicative convolution becomes additive convolution

Let \(h=f*g\), where

\[
(f*g)(x)=\int_0^\infty f(x/y)g(y)\frac{dy}{y}.
\]

Let

\[
F(u)=e^{u/2}f(e^u),
\qquad
G(u)=e^{u/2}g(e^u),
\qquad
H(u)=e^{u/2}h(e^u).
\]

Put \(y=e^v\), so \(dy/y=dv\). Then

\[
h(e^u)
=
\int_{-\infty}^{\infty}
f(e^{u-v})g(e^v)\,dv.
\]

Using the half-density normalization,

\[
f(e^{u-v})=e^{-(u-v)/2}F(u-v),
\]

and

\[
g(e^v)=e^{-v/2}G(v).
\]

Thus

\[
h(e^u)
=
e^{-u/2}
\int_{-\infty}^{\infty}
F(u-v)G(v)\,dv.
\]

Multiplying by \(e^{u/2}\), we obtain

\[
H(u)=\int_{-\infty}^{\infty}F(u-v)G(v)\,dv.
\]

Therefore,

\[
\boxed{
\text{multiplicative convolution becomes additive convolution.}
}
\]

---

# 6. Positivity convolution in log coordinates

For the Hermitian positivity adjoint, log coordinates convert the reflected-conjugate operation into

\[
G^*_{\mathrm{pos}}(u)=\overline{G(-u)}.
\]

Thus the positivity convolution becomes

\[
F*F^*_{\mathrm{pos}}.
\]

This is the additive convolution form needed before Fourier-side analysis.

---

# 7. What this phase locks

The following algebraic bridge is now locked:

\[
x=e^u,
\qquad
F(u)=e^{u/2}f(e^u).
\]

Under this bridge:

1. algebraic involution becomes reflection;
2. Hermitian positivity adjoint becomes reflected conjugation;
3. multiplicative convolution becomes additive convolution;
4. mass terms become a \(2\cosh(u/2)\) integral;
5. prime terms occur at \(u=\pm\log n\).

---

# 8. What remains unlocked

The following remain unlocked:

1. Bombieri's exact Fourier transform sign convention;
2. Bombieri's exact Fourier-side infinite quadratic form;
3. exact Hilbert space;
4. exact matrix entries;
5. exact finite truncation model;
6. exact eigenvalue theorem.

---

# 9. Boundary

No Fourier-side implementation.

No finite matrix implementation.

No eigenvalue computation.

No RH proof.

No novelty claim.

