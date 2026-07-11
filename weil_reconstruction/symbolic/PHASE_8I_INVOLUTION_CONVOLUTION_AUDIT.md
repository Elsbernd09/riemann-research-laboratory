# Phase 8I — Involution and Convolution Identity Audit

## Purpose

Phase 8H locked Bombieri's full linear functional

\[
T[f].
\]

Phase 8I audits the symbolic identities surrounding the involution

\[
f^*(x)=x^{-1}f(1/x)
\]

and multiplicative convolution.

This phase does not prove RH.

This phase does not create a new Weil criterion.

This phase does not implement finite-rank Weil matrices.

---

# 1. Current locked convention

From the Phase 8H extraction, the project currently records Bombieri's involution as

\[
f^*(x)=x^{-1}f(1/x).
\]

The Mellin transform convention is recorded as

\[
f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
\]

The multiplicative convolution is

\[
(f*g)(x)
=
\int_0^\infty f(x/y)g(y)\frac{dy}{y}.
\]

---

# 2. Mellin transform of the involution

Let

\[
f^*(x)=x^{-1}f(1/x).
\]

Then

\[
f^*(s)
=
\int_0^\infty f^*(x)x^{s-1}\,dx.
\]

Substitute the definition:

\[
f^*(s)
=
\int_0^\infty x^{-1}f(1/x)x^{s-1}\,dx
=
\int_0^\infty f(1/x)x^{s-2}\,dx.
\]

Let

\[
u=1/x.
\]

Then

\[
x=1/u,
\qquad
dx=-u^{-2}du.
\]

Thus

\[
x^{s-2}dx
=
(1/u)^{s-2}(-u^{-2})du
=
-u^{-s}du.
\]

Changing limits gives

\[
f^*(s)
=
\int_0^\infty f(u)u^{-s}\,du
=
\int_0^\infty f(u)u^{(1-s)-1}\,du
=
f(1-s).
\]

Therefore

\[
\boxed{
f^*(s)=f(1-s).
}
\]

---

# 3. Multiplicative convolution Mellin identity

For

\[
(f*g)(x)=\int_0^\infty f(x/y)g(y)\frac{dy}{y},
\]

the Mellin transform satisfies

\[
(f*g)(s)=f(s)g(s),
\]

whenever the integrals are justified.

Proof:

\[
(f*g)(s)
=
\int_0^\infty
\left[
\int_0^\infty f(x/y)g(y)\frac{dy}{y}
\right]
x^{s-1}dx.
\]

Let

\[
u=x/y.
\]

Then

\[
x=uy,
\qquad
dx=y\,du.
\]

For fixed \(y\),

\[
x^{s-1}dx
=
(uy)^{s-1}y\,du
=
u^{s-1}y^sdu.
\]

Including \(dy/y\), the \(y\)-factor becomes

\[
y^{s-1}dy.
\]

Therefore

\[
(f*g)(s)
=
\left(\int_0^\infty f(u)u^{s-1}du\right)
\left(\int_0^\infty g(y)y^{s-1}dy\right)
=
f(s)g(s).
\]

---

# 4. Bombieri product identity

If

\[
F=f*f^*,
\]

then the Mellin transform satisfies

\[
F(s)=f(s)f^*(s)=f(s)f(1-s).
\]

This is the symbolic origin of the Bombieri zero-side product

\[
g(\rho)g(1-\rho).
\]

---

# 5. Complex-valued caution

The source theorem is stated for complex-valued test functions.

In positivity contexts, conjugation conventions are delicate.

The repository currently has the source-extracted involution

\[
f^*(x)=x^{-1}f(1/x).
\]

However, before implementing positivity or finite matrices, the exact role of complex conjugation must be source-audited.

Possible conventions include:

\[
f^*(x)=x^{-1}f(1/x)
\]

or a conjugate-involving version such as

\[
f^*(x)=x^{-1}\overline{f(1/x)}.
\]

The project must not silently switch between these conventions.

---

# 6. Locked result of this phase

The following algebraic identities are verified under the non-conjugated involution convention:

\[
f^*(s)=f(1-s),
\]

\[
(f*g)(s)=f(s)g(s),
\]

\[
(f*f^*)(s)=f(s)f(1-s).
\]

---

# 7. Boundary

No finite-rank Weil implementation.

No positivity code.

No RH proof.

No new Weil criterion.

The next source-grounded task is to audit the complex conjugation convention in Bombieri's \(g^*\), \(f^*\), and positivity statements.

