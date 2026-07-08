# Reflection-Invariant Finite Li Response

## Phase 1C

This document addresses whether the project's finite signed zero response is compatible with a Li-type derivative functional.

---

# 1. Zero-side kernel

For integers \(n\ge1\), define

\[
f_n(z)
=
1-
\left(
1-\frac1z
\right)^n.
\]

The project previously studied the signed response

\[
\int f_n(z)\,d\nu_{\delta,\gamma}(z).
\]

---

# 2. Finite-factor Li-type functional

For a function \(F\) analytic and nonzero in a neighborhood of \(s=1\), define

\[
\mathscr L_n[F]
=
\frac1{(n-1)!}
\left.
\frac{d^n}{ds^n}
\left[
s^{n-1}\log F(s)
\right]
\right|_{s=1}.
\]

The value is independent of the additive branch constant in a local logarithm because

\[
s^{n-1}C
\]

has degree \(n-1\) and therefore has vanishing \(n\)-th derivative.

---

# 3. Single-factor calculation

Let

\[
F_\rho(s)
=
1-\frac{s}{\rho},
\]

where

\[
\rho\ne0,1.
\]

Set

\[
u=s-1.
\]

Then

\[
1-\frac{1+u}{\rho}
=
\left(
1-\frac1\rho
\right)
\left(
1-\frac{u}{\rho-1}
\right).
\]

The locally constant logarithmic term does not contribute to the \(n\)-th derivative after multiplication by \(s^{n-1}\).

Using

\[
\log(1-x)
=
-\sum_{k\ge1}\frac{x^k}{k}
\]

locally near \(x=0\), the coefficient of \(u^n\) in

\[
(1+u)^{n-1}
\log\left(
1-\frac{u}{\rho-1}
\right)
\]

is

\[
-\sum_{k=1}^n
\binom{n-1}{k-1}
\frac1{k(\rho-1)^k}.
\]

Using

\[
\frac1k
\binom{n-1}{k-1}
=
\frac1n
\binom nk,
\]

this becomes

\[
-\frac1n
\sum_{k=1}^n
\binom nk
\frac1{(\rho-1)^k}.
\]

Therefore

\[
\mathscr L_n[F_\rho]
=
1-
\left(
\frac{\rho}{\rho-1}
\right)^n.
\]

Define

\[
g_n(\rho)
=
1-
\left(
1-\frac1\rho
\right)^{-n}.
\]

Then

\[
\boxed{
\mathscr L_n[F_\rho]
=
g_n(\rho).
}
\]

---

# 4. Reflection identity

Since

\[
1-\frac1{1-\rho}
=
\frac{\rho}{\rho-1},
\]

one has

\[
\boxed{
g_n(\rho)
=
f_n(1-\rho).
}
\]

Thus the finite-factor derivative functional does not equal the project zero kernel term-by-term at the same zero.

Instead, it equals the zero kernel at the reflected point.

---

# 5. Reflection-invariant signed measures

Let \(\sigma\) denote the reflection

\[
\sigma(z)=1-z.
\]

Let

\[
\nu
=
\sum_{j=1}^m a_j\mathfrak d_{z_j}
\]

be a finite signed point measure.

Say that \(\nu\) is reflection invariant if

\[
\sigma_*\nu=\nu.
\]

Equivalently, for every function \(h\) defined on the finite support,

\[
\int h(1-z)\,d\nu(z)
=
\int h(z)\,d\nu(z).
\]

Using

\[
g_n(z)=f_n(1-z),
\]

it follows that

\[
\int g_n(z)\,d\nu(z)
=
\int f_n(1-z)\,d\nu(z)
=
\int f_n(z)\,d\nu(z).
\]

Hence

\[
\boxed{
\int g_n\,d\nu
=
\int f_n\,d\nu
}
\]

for every finite reflection-invariant signed point measure \(\nu\) whose support avoids \(0\) and \(1\).

---

# 6. Orbit-splitting measure

Define

\[
\nu_{\delta,\gamma}
=
\sum_{\epsilon=\pm1}
\sum_{\eta=\pm1}
\mathfrak d_{
\frac12+\epsilon\delta+i\eta\gamma
}
-
2\mathfrak d_{\frac12+i\gamma}
-
2\mathfrak d_{\frac12-i\gamma}.
\]

Under

\[
z\mapsto1-z,
\]

the quartet support is permuted.

The doubled critical-line pair is also permuted.

Therefore

\[
\sigma_*\nu_{\delta,\gamma}
=
\nu_{\delta,\gamma}.
\]

Thus

\[
\boxed{
\int g_n(z)\,d\nu_{\delta,\gamma}(z)
=
\int f_n(z)\,d\nu_{\delta,\gamma}(z).
}
\]

The right side is the project's signed Li-kernel response

\[
\mathcal R_n^{\mathrm{Li}}(\delta,\gamma).
\]

---

# 7. Finite factor ratio

For a finite signed point measure with integer weights

\[
\nu
=
\sum_j a_j\mathfrak d_{\rho_j},
\]

define locally

\[
R_\nu(s)
=
\prod_j
\left(
1-\frac{s}{\rho_j}
\right)^{a_j},
\]

provided the support avoids \(s=1\).

Negative weights make \(R_\nu\) rational rather than necessarily entire.

Logarithmic additivity gives

\[
\mathscr L_n[R_\nu]
=
\sum_j a_j g_n(\rho_j)
=
\int g_n\,d\nu.
\]

If \(\nu\) is reflection invariant,

\[
\mathscr L_n[R_\nu]
=
\int f_n\,d\nu.
\]

Therefore, for the orbit-splitting measure,

\[
\boxed{
\mathscr L_n[R_{\nu_{\delta,\gamma}}]
=
\mathcal R_n^{\mathrm{Li}}(\delta,\gamma).
}
\]

---

# 8. Interpretation

The equality is an orbit-level reflection-symmetry statement.

It is not a termwise identity at an individual zero.

Indeed,

\[
g_n(\rho)
\ne
f_n(\rho)
\]

in general.

The agreement arises because

\[
g_n(\rho)=f_n(1-\rho)
\]

and the signed perturbation measure is invariant under

\[
\rho\mapsto1-\rho.
\]

Thus functional-equation-type reflection symmetry is essential to the bridge between the project's zero-kernel response and the finite-factor Li-type derivative functional.

---

# 9. Limit of a fixed finite signed perturbation

Suppose a chosen zero-sum truncation gives

\[
S_T(f_n)\to S(f_n).
\]

Let \(\nu\) be a fixed finite signed point measure.

Once the truncation contains the finite support relevant to the perturbation convention,

\[
S_T^\nu(f_n)
=
S_T(f_n)
+
\int f_n\,d\nu.
\]

Therefore

\[
\boxed{
S_T^\nu(f_n)
\to
S(f_n)+\int f_n\,d\nu.
}
\]

This does not require rearranging infinitely many zero terms.

The finite correction is eventually constant in \(T\).

---

# 10. What is not proved

The factor ratio

\[
R_{\nu_{\delta,\gamma}}
\]

is generally rational because the signed measure has negative weights.

The project has not shown that multiplying the actual Riemann xi-function by this ratio produces an entire function.

In particular, the baseline subtraction uses multiplicity two at the critical-line pair.

No such multiplicity-two zeta zero is assumed.

Therefore the project does not identify the synthetic response with the Li coefficients of a modified zeta function.

The result is a finite signed response identity and a finite-factor Li-type functional identity.

---

# 11. Candidate proposition status

The reflection-invariant finite response identity is supported by direct algebra.

It must undergo independent symbolic and arbitrary-precision numerical validation before promotion to PROVED IN PROJECT.

No originality claim is made.
