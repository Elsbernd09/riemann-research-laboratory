# Phase 12D — External Source Review Package

## Purpose

Phase 12C identified the current Level 4 blocker:

\[
F_g \text{ is missing.}
\]

The project has a source-extracted Bombieri explicit formula functional:

\[
T[f].
\]

But the project has not yet imported the exact classical construction:

\[
Q_W(g)=T[F_g].
\]

Phase 12D creates the professor/source-review package needed to resolve that missing object.

---

# 1. Central question

Given the Bombieri explicit formula functional

\[
T[f]
=
\int_0^\infty f(x)\,dx
+
\int_0^\infty f^*(x)\,dx
-
\sum_{n=1}^{\infty}\Lambda(n)\{f(n)+f^*(n)\}
-
(\log 4\pi+\gamma_E)f(1)
-
\int_1^\infty
\left(
f(x)+f^*(x)-\frac{2f(1)}{x}
\right)
\frac{x\,dx}{x^2-1},
\]

with

\[
f^*(x)=x^{-1}f(1/x),
\]

what is the exact classical construction \(F_g\) used to define the Weil positivity quadratic form

\[
Q_W(g)=T[F_g]?
\]

---

# 2. Required missing objects

The project needs exact source-grounded definitions of:

\[
F_g,
\quad
Q_W,
\quad
B_W,
\quad
\mathcal D_W,
\quad
P_N.
\]

Specifically:

## Object 1 — \(F_g\)

Question:

What exact function \(F_g\) is built from \(g\)?

Possible shapes to clarify:

1. convolution;
2. autocorrelation;
3. Mellin convolution;
4. involution product;
5. Fourier-side square;
6. another classical construction.

No guessing is allowed.

---

## Object 2 — \(Q_W\)

Question:

Is the quadratic Weil form exactly

\[
Q_W(g)=T[F_g],
\]

or is there a sign convention such as

\[
Q_W(g)=-T[F_g]?
\]

The sign convention must be locked.

---

## Object 3 — \(B_W\)

Question:

What is the corresponding bilinear or Hermitian form

\[
B_W(g,h)
\]

whose diagonal gives

\[
Q_W(g)=B_W(g,g)?
\]

---

## Object 4 — \(\mathcal D_W\)

Question:

What exact admissible function class does \(g\) belong to?

Needed properties may include:

1. smoothness;
2. compact support;
3. decay;
4. Mellin transform conditions;
5. symmetry under star/involution;
6. support away from singularities;
7. positivity-domain restrictions.

The exact source-level hypotheses are required.

---

## Object 5 — RH positivity theorem

Question:

What is the exact theorem statement relating RH to positivity?

Target shape:

\[
\mathrm{RH}
\Longleftrightarrow
Q_W(g)\geq0
\quad
\forall g\in\mathcal D_W.
\]

But the exact theorem, sign, and domain must be source-grounded.

---

## Object 6 — finite approximation map \(P_N\)

Question:

For a finite approximation theorem, what is the correct map

\[
P_N:\mathcal D_W\to V_N?
\]

Is \(P_N\):

1. a finite zero-support projection;
2. a finite-dimensional test-function projection;
3. a spectral truncation;
4. a sampling map;
5. something else?

---

# 3. Why this matters

The Level 4 target is:

\[
Q_W(g)<0
\Longrightarrow
Q_N(P_Ng)<0
\]

for sufficiently large \(N\), with explicit error control.

But this cannot be attempted honestly until \(Q_W\) and \(P_N\) are defined from real classical sources.

---

# 4. Current project result before source review

The project currently has:

\[
T[f]
\]

and a finite extracted Bombieri-style \(H\)-kernel.

It also has a conditional finite transfer framework.

But it does not yet have the exact source-grounded quadratic Weil positivity object.

Therefore the current status is:

\[
\boxed{\text{source review required before Level 4 theorem attempt}}
\]

---

# 5. Suggested professor question

Dear Professor,

I am working through a finite-dimensional Bombieri/Weil-style positivity framework related to the Riemann Hypothesis. I am not claiming a proof or breakthrough. I am trying to correctly identify the classical objects before going further.

I have reconstructed the following explicit-formula functional:

\[
T[f]
=
\int_0^\infty f(x)\,dx
+
\int_0^\infty f^*(x)\,dx
-
\sum_{n=1}^{\infty}\Lambda(n)\{f(n)+f^*(n)\}
-
(\log 4\pi+\gamma_E)f(1)
-
\int_1^\infty
\left(
f(x)+f^*(x)-\frac{2f(1)}{x}
\right)
\frac{x\,dx}{x^2-1},
\]

with \(f^*(x)=x^{-1}f(1/x)\), and zero-side expression \(T[f]=\sum_\rho f(\rho)\).

My question is: in the classical Weil positivity criterion, what exact function \(F_g\) is inserted into \(T\) to define the quadratic form \(Q_W(g)=T[F_g]\)? I want to avoid guessing the wrong convolution/involution convention.

Could you point me to the exact definition of \(F_g\), the admissible test-function space, and the precise sign convention in the RH positivity theorem?

My current goal is modest: to see whether a finite-dimensional approximation \(Q_N(P_Ng)\) can be shown to converge to the true \(Q_W(g)\) on a controlled finite test class. I am not claiming this has been achieved.

Thank you.

---

# 6. Source-review checklist

A valid answer must provide:

1. exact definition of \(F_g\);
2. exact definition of \(Q_W\);
3. exact definition of \(B_W\), if applicable;
4. exact admissible domain \(\mathcal D_W\);
5. exact RH positivity theorem;
6. exact sign convention;
7. exact source citation;
8. implications for finite approximation \(P_N\).

---

# 7. Next after source review

Once \(F_g\) and \(Q_W\) are imported, the next theorem attempt will be:

\[
|Q_N(P_Ng)-Q_W(g)|
\leq
\varepsilon_N(g),
\]

with

\[
\varepsilon_N(g)\to0.
\]

Only then can the Level 4 obstruction-detection theorem be attempted.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove Level 4 contribution.

This phase does not import the missing \(F_g\).

This phase does not establish novelty.

Exact audit strings:

EXTERNAL_SOURCE_REVIEW_PACKAGE_CREATED

F_G_SOURCE_REQUEST_CREATED

TRUE_Q_W_SOURCE_REQUEST_CREATED

ADMISSIBLE_DOMAIN_SOURCE_REQUEST_CREATED

SIGN_CONVENTION_SOURCE_REQUEST_CREATED

FINITE_APPROXIMATION_MAP_REQUEST_CREATED

SOURCE_REVIEW_REQUIRED_BEFORE_LEVEL4

LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED

