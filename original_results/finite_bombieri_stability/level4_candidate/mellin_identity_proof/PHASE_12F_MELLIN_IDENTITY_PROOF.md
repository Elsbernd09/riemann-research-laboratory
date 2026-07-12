# Phase 12F — Mellin Identity Proof

## Purpose

Phase 12E provisionally imported

\[
F_g=g*g^*
\]

with

\[
g^*(x)=x^{-1}\overline{g(1/x)}
\]

and multiplicative convolution

\[
(a*b)(x)=\int_0^\infty a(y)b(x/y)\frac{dy}{y}.
\]

Phase 12F proves the formal Mellin identities:

\[
\widehat{g^*}(s)=\overline{\widehat g(1-\bar s)}
\]

and

\[
\widehat{g*g^*}(s)=\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

These identities explain why \(g*g^*\) becomes a square on the critical line.

---

# 1. Mellin transform convention

For a suitable function \(g:(0,\infty)\to\mathbb C\), define

\[
\widehat g(s)=\int_0^\infty g(x)x^{s-1}\,dx.
\]

The function class is provisionally taken to be smooth and compactly supported on \((0,\infty)\), so all substitutions below are justified.

---

# 2. Involution

Define

\[
g^*(x)=x^{-1}\overline{g(1/x)}.
\]

---

# Theorem 12F.1 — Mellin transform of the involution

For suitable \(g\),

\[
\widehat{g^*}(s)
=
\overline{\widehat g(1-\bar s)}.
\]

## Proof

By definition,

\[
\widehat{g^*}(s)
=
\int_0^\infty g^*(x)x^{s-1}\,dx.
\]

Using

\[
g^*(x)=x^{-1}\overline{g(1/x)},
\]

we get

\[
\widehat{g^*}(s)
=
\int_0^\infty x^{-1}\overline{g(1/x)}x^{s-1}\,dx
=
\int_0^\infty \overline{g(1/x)}x^{s-2}\,dx.
\]

Set

\[
u=1/x.
\]

Then

\[
x=1/u,
\qquad
dx=-u^{-2}\,du.
\]

As \(x\) runs from \(0\) to \(\infty\), \(u\) runs from \(\infty\) to \(0\). Therefore,

\[
\widehat{g^*}(s)
=
\int_\infty^0
\overline{g(u)}
(1/u)^{s-2}
(-u^{-2})\,du.
\]

Thus

\[
\widehat{g^*}(s)
=
\int_0^\infty
\overline{g(u)}
u^{-s}\,du.
\]

Now

\[
\overline{\widehat g(1-\bar s)}
=
\overline{
\int_0^\infty g(u)u^{(1-\bar s)-1}\,du
}
=
\overline{
\int_0^\infty g(u)u^{-\bar s}\,du
}.
\]

Since \(u>0\),

\[
\overline{u^{-\bar s}}=u^{-s}.
\]

Hence

\[
\overline{\widehat g(1-\bar s)}
=
\int_0^\infty \overline{g(u)}u^{-s}\,du.
\]

Therefore,

\[
\widehat{g^*}(s)
=
\overline{\widehat g(1-\bar s)}.
\]

\[
\square
\]

---

# 3. Multiplicative convolution

Define

\[
(a*b)(x)=\int_0^\infty a(y)b(x/y)\frac{dy}{y}.
\]

---

# Theorem 12F.2 — Mellin convolution theorem

For suitable \(a,b\),

\[
\widehat{a*b}(s)=\widehat a(s)\widehat b(s).
\]

## Proof

By definition,

\[
\widehat{a*b}(s)
=
\int_0^\infty
(a*b)(x)x^{s-1}\,dx.
\]

Substitute the convolution:

\[
\widehat{a*b}(s)
=
\int_0^\infty
\left(
\int_0^\infty a(y)b(x/y)\frac{dy}{y}
\right)
x^{s-1}\,dx.
\]

Assuming the justified Fubini interchange,

\[
\widehat{a*b}(s)
=
\int_0^\infty
a(y)
\left(
\int_0^\infty b(x/y)x^{s-1}\,dx
\right)
\frac{dy}{y}.
\]

Set

\[
u=x/y.
\]

Then

\[
x=yu,
\qquad
dx=y\,du.
\]

The inner integral becomes

\[
\int_0^\infty b(u)(yu)^{s-1}y\,du
=
y^s
\int_0^\infty b(u)u^{s-1}\,du
=
y^s\widehat b(s).
\]

Therefore,

\[
\widehat{a*b}(s)
=
\int_0^\infty
a(y)y^s\widehat b(s)\frac{dy}{y}
=
\widehat b(s)
\int_0^\infty a(y)y^{s-1}\,dy.
\]

Thus

\[
\widehat{a*b}(s)
=
\widehat a(s)\widehat b(s).
\]

\[
\square
\]

---

# Theorem 12F.3 — Mellin product for \(F_g=g*g^*\)

Let

\[
F_g=g*g^*.
\]

Then

\[
\widehat{F_g}(s)
=
\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

## Proof

By Theorem 12F.2,

\[
\widehat{g*g^*}(s)
=
\widehat g(s)\widehat{g^*}(s).
\]

By Theorem 12F.1,

\[
\widehat{g^*}(s)
=
\overline{\widehat g(1-\bar s)}.
\]

Therefore,

\[
\widehat{F_g}(s)
=
\widehat g(s)\overline{\widehat g(1-\bar s)}.
\]

\[
\square
\]

---

# Corollary 12F.4 — Square structure on the critical line

If

\[
s=\frac12+i\gamma,
\]

then

\[
1-\bar s=s.
\]

Therefore,

\[
\widehat{F_g}(s)
=
\widehat g(s)\overline{\widehat g(s)}
=
|\widehat g(s)|^2.
\]

Thus, on the critical line,

\[
\widehat{g*g^*}(s)=|\widehat g(s)|^2\ge0.
\]

---

# 4. Why this matters

The formal Mellin identity proves that the provisional construction

\[
F_g=g*g^*
\]

has the correct square-producing structure on the critical line.

This supports the provisional definition

\[
Q_W(g)=T[g*g^*].
\]

It does not prove RH.

It does not prove the full Weil criterion.

It only proves the algebraic Mellin identities needed for the positivity mechanism.

---

# 5. Remaining unresolved issues

Still unresolved:

1. primary-source confirmation of \(F_g\);
2. exact admissible domain \(\mathcal D_W\);
3. sign convention for \(Q_W\);
4. compatibility with the project’s extracted \(T[f]\);
5. finite approximation map \(P_N\);
6. truncation and projection error bounds.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove Level 4 contribution.

This phase does not establish novelty.

Exact audit strings:

MELLIN_IDENTITY_PROOF_COMPLETE

G_STAR_MELLIN_IDENTITY_PROVED

MELLIN_CONVOLUTION_THEOREM_PROVED

F_G_MELLIN_PRODUCT_PROVED

CRITICAL_LINE_SQUARE_STRUCTURE_PROVED

PRIMARY_SOURCE_CONFIRMATION_STILL_REQUIRED

SIGN_CONVENTION_STILL_UNCONFIRMED

LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED

