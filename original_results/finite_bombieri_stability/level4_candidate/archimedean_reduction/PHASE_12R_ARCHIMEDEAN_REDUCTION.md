# Phase 12R — Archimedean Integral Reduction

## Purpose

Phase 12Q proved that the prime sum is finite on the compactly supported finite test class.

The next major arithmetic-side obstacle is the archimedean integral:

\[
A[F]
=
\int_1^\infty
\left(
F(x)+F^*(x)-\frac{2F(1)}{x}
\right)
\frac{x\,dx}{x^2-1}.
\]

Phase 12R reduces this term into:

1. a finite compact-support integral;
2. an explicit analytic tail;
3. a removable-singularity treatment near \(x=1\).

---

# 1. Compact support setup

From Phase 12Q, for every \(g\in\mathcal F_R^{(m)}\),

\[
F_g=g*g^*
\]

and

\[
F_g^*
\]

are supported in

\[
[e^{-2B},e^{2B}].
\]

Let

\[
M=e^{2B}.
\]

Then for

\[
x>M,
\]

we have

\[
F_g(x)=0,
\qquad
F_g^*(x)=0.
\]

---

# 2. Archimedean integral

Define

\[
A[F_g]
=
\int_1^\infty
\left(
F_g(x)+F_g^*(x)-\frac{2F_g(1)}{x}
\right)
\frac{x\,dx}{x^2-1}.
\]

Because \(F_g\) and \(F_g^*\) vanish for \(x>M\), the integral splits as

\[
A[F_g]
=
\int_1^M
\left(
F_g(x)+F_g^*(x)-\frac{2F_g(1)}{x}
\right)
\frac{x\,dx}{x^2-1}
+
\int_M^\infty
\left(
-\frac{2F_g(1)}{x}
\right)
\frac{x\,dx}{x^2-1}.
\]

The second integral is explicit.

---

# Theorem 12R.1 — Explicit archimedean tail

For

\[
M>1,
\]

\[
\int_M^\infty
\left(
-\frac{2F_g(1)}{x}
\right)
\frac{x\,dx}{x^2-1}
=
-F_g(1)\log\left(\frac{M+1}{M-1}\right).
\]

## Proof

The tail is

\[
-2F_g(1)\int_M^\infty \frac{dx}{x^2-1}.
\]

Since

\[
\int \frac{dx}{x^2-1}
=
\frac12\log\left(\frac{x-1}{x+1}\right),
\]

we get

\[
\int_M^\infty \frac{dx}{x^2-1}
=
\lim_{R\to\infty}
\frac12
\left[
\log\left(\frac{R-1}{R+1}\right)
-
\log\left(\frac{M-1}{M+1}\right)
\right].
\]

The first logarithm tends to \(0\). Therefore

\[
\int_M^\infty \frac{dx}{x^2-1}
=
\frac12
\log\left(\frac{M+1}{M-1}\right).
\]

Multiplying by \(-2F_g(1)\) gives

\[
-F_g(1)\log\left(\frac{M+1}{M-1}\right).
\]

\[
\square
\]

---

# 3. Reduced archimedean formula

Thus

\[
A[F_g]
=
\int_1^M
\left(
F_g(x)+F_g^*(x)-\frac{2F_g(1)}{x}
\right)
\frac{x\,dx}{x^2-1}
-
F_g(1)\log\left(\frac{M+1}{M-1}\right).
\]

This reduces the infinite integral to a finite integral plus an explicit analytic term.

---

# 4. Removable singularity near \(x=1\)

The integrand has apparent denominator

\[
x^2-1=(x-1)(x+1).
\]

At \(x=1\), the numerator is

\[
F_g(1)+F_g^*(1)-2F_g(1).
\]

If

\[
F_g^*(1)=F_g(1),
\]

then the numerator vanishes at \(x=1\).

Since

\[
F_g^*(1)=1^{-1}\overline{F_g(1)}
=
\overline{F_g(1)},
\]

we need

\[
F_g(1)\in\mathbb R.
\]

For \(F_g=g*g^*\), the value \(F_g(1)\) is expected to be real and nonnegative under the convolution-star structure.

This must be proved.

---

# Theorem 12R.2 — \(F_g(1)\) is real and nonnegative

Let

\[
F_g=g*g^*
\]

with

\[
g^*(x)=x^{-1}\overline{g(1/x)}.
\]

Then

\[
F_g(1)=\int_0^\infty |g(y)|^2\,dy.
\]

In particular,

\[
F_g(1)\in\mathbb R_{\ge0}.
\]

## Proof

By definition,

\[
F_g(1)=\int_0^\infty g(y)g^*(1/y)\frac{dy}{y}.
\]

Now

\[
g^*(1/y)
=
(1/y)^{-1}\overline{g(y)}
=
y\overline{g(y)}.
\]

Therefore,

\[
F_g(1)
=
\int_0^\infty g(y)y\overline{g(y)}\frac{dy}{y}
=
\int_0^\infty |g(y)|^2\,dy.
\]

This is real and nonnegative.

\[
\square
\]

---

# 5. Numerator cancellation

Define

\[
N_g(x)=F_g(x)+F_g^*(x)-\frac{2F_g(1)}{x}.
\]

At \(x=1\),

\[
N_g(1)=F_g(1)+F_g^*(1)-2F_g(1).
\]

Since

\[
F_g^*(1)=\overline{F_g(1)}=F_g(1),
\]

Theorem 12R.2 gives

\[
N_g(1)=0.
\]

Thus the singularity at \(x=1\) is removable if \(N_g\) is differentiable.

---

# Theorem 12R.3 — Removable singularity criterion

Assume \(N_g\) is differentiable near \(x=1\) and

\[
N_g(1)=0.
\]

Then

\[
\frac{N_g(x)x}{x^2-1}
\]

has a finite limit as

\[
x\to1.
\]

The limit is

\[
\frac{N_g'(1)}{2}.
\]

## Proof

Since

\[
x^2-1=(x-1)(x+1),
\]

we have

\[
\frac{N_g(x)x}{x^2-1}
=
\frac{N_g(x)}{x-1}
\cdot
\frac{x}{x+1}.
\]

Because

\[
N_g(1)=0
\]

and \(N_g\) is differentiable,

\[
\lim_{x\to1}\frac{N_g(x)}{x-1}=N_g'(1).
\]

Also,

\[
\lim_{x\to1}\frac{x}{x+1}=\frac12.
\]

Therefore,

\[
\lim_{x\to1}
\frac{N_g(x)x}{x^2-1}
=
\frac{N_g'(1)}2.
\]

\[
\square
\]

---

# 6. Reduced certified integral target

The archimedean term can now be evaluated as:

\[
A[F_g]
=
\operatorname{PV/rem}
\int_1^M
N_g(x)\frac{x\,dx}{x^2-1}
-
F_g(1)\log\left(\frac{M+1}{M-1}\right),
\]

where the integral over \([1,M]\) is interpreted with the removable value

\[
\frac{N_g'(1)}2
\]

at \(x=1\).

For certified computation, one can split:

\[
[1,M]=[1,1+\epsilon]\cup[1+\epsilon,M].
\]

The near interval uses Taylor bounds for \(N_g\).

The far interval uses standard interval quadrature.

---

# 7. Matrix-entry version

For basis-pair entries, define

\[
F_{ij}=\phi_i*\phi_j^*.
\]

Then the same reduction applies:

\[
A[F_{ij}]
=
\int_1^M
\left(
F_{ij}(x)+F_{ij}^*(x)-\frac{2F_{ij}(1)}{x}
\right)
\frac{x\,dx}{x^2-1}
-
F_{ij}(1)\log\left(\frac{M+1}{M-1}\right).
\]

For diagonal entries \(i=j\), the same nonnegativity proof gives

\[
F_{ii}(1)=\int_0^\infty|\phi_i(y)|^2\,dy.
\]

For off-diagonal entries, \(F_{ij}(1)\) is an inner product:

\[
F_{ij}(1)=\int_0^\infty \phi_i(y)\overline{\phi_j(y)}\,dy.
\]

The removable-singularity condition becomes a Hermitian compatibility condition and must be handled entrywise.

---

# 8. What this proves

Phase 12R proves:

1. the archimedean infinite tail is explicit;
2. the remaining integral is finite over \([1,M]\);
3. \(F_g(1)\) is real and nonnegative;
4. the apparent singularity at \(x=1\) is removable under differentiability;
5. the certificate problem reduces to finite interval integration plus an analytic logarithmic term.

This is a major arithmetic-side reduction.

---

# 9. What remains

Still needed:

1. certified interval quadrature;
2. derivative/Taylor bounds near \(x=1\);
3. off-diagonal matrix-entry removable singularity handling;
4. implementation;
5. primary-source convention validation;
6. full arithmetic matrix assembly.

---

# 10. Next target

Phase 12S should define arithmetic matrix entries:

\[
M_{ij}^{arith}=T[\phi_i*\phi_j^*]
\]

using:

1. finite prime sums;
2. central integrals;
3. constant term;
4. reduced archimedean term;
5. certified integral placeholders.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove a complete arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

ARCHIMEDEAN_REDUCTION_COMPLETE

ARCHIMEDEAN_TAIL_EXPLICIT_PROVED

FINITE_ARCHIMEDEAN_INTERVAL_REDUCTION_PROVED

F_G_ONE_REAL_NONNEGATIVE_PROVED

REMOVABLE_SINGULARITY_CRITERION_PROVED

ARCHIMEDEAN_CERTIFICATION_REDUCED_TO_FINITE_INTERVAL

CERTIFIED_QUADRATURE_STILL_REQUIRED

ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE

LEVEL4_BREAKTHROUGH_CANDIDATE_STILL_CONDITIONAL

