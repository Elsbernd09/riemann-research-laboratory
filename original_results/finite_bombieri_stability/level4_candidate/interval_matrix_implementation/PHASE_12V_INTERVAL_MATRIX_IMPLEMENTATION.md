# Phase 12V — Interval Arithmetic Matrix Implementation Skeleton

## Purpose

Phase 12U identified two safe routes:

1. conditional Hermitian route;
2. direct certified Hermitian residual route.

Phase 12V builds the implementation skeleton needed for certified arithmetic matrix entries, Hermitian residual checks, Rayleigh quotient interval checks, and negative-direction certificate logic.

This phase does not yet compute the true arithmetic entries.

It creates the certificate infrastructure.

---

# 1. Certified matrix goal

The target object is an interval arithmetic matrix

\[
\mathbf M^{arith}
\]

where each entry is enclosed by an interval:

\[
M_{ij}^{arith}\in [\ell_{ij},u_{ij}].
\]

For complex Hermitian entries, this eventually requires rectangular complex intervals, but Phase 12V starts with real interval infrastructure and a real symmetric certificate skeleton.

---

# 2. Hermitian residual interval

Given interval entries for \(M_{ij}\) and \(M_{ji}\), define the Hermitian residual

\[
R_{ij}=M_{ij}-\overline{M_{ji}}.
\]

In the real skeleton, this becomes

\[
R_{ij}=M_{ij}-M_{ji}.
\]

If

\[
0\in R_{ij}
\]

for all \(i,j\), symmetry is not disproved.

If

\[
R_{ij}=[0,0]
\]

for all \(i,j\), exact interval symmetry is certified.

---

# 3. Rayleigh quotient interval

For a real vector \(v\), the Rayleigh quotient is

\[
v^TMv.
\]

If each matrix entry is interval-valued, then the Rayleigh quotient is interval-valued:

\[
v^T\mathbf Mv\subset [L,U].
\]

If

\[
U<0,
\]

then every real matrix inside the interval matrix has negative Rayleigh quotient along \(v\).

This gives a certified negative-direction test.

---

# Theorem 12V.1 — Interval Rayleigh negative-direction certificate

Let \(\mathbf M\) be an interval matrix enclosing exact matrices \(M\).

Let \(v\neq0\) be a real vector.

If the interval evaluation satisfies

\[
v^T\mathbf Mv\subset (-\infty,0),
\]

then every exact matrix \(M\in\mathbf M\) satisfies

\[
v^TMv<0.
\]

## Proof

The interval evaluation contains every possible value of \(v^TMv\) for matrices \(M\) whose entries lie inside the interval entries.

If the upper endpoint of the interval is negative, then every possible value is negative.

Therefore

\[
v^TMv<0
\]

for every exact matrix enclosed by \(\mathbf M\).

\[
\square
\]

---

# 4. Margin version

If

\[
v^T\mathbf Mv\subset (-\infty,-\eta],
\]

then the negative direction has certified margin \(\eta\).

This is the finite arithmetic analogue of the negative-obstruction detection logic from earlier phases.

---

# 5. What this implementation does

The Phase 12V implementation includes:

1. real interval arithmetic;
2. interval addition, subtraction, multiplication;
3. interval matrix storage;
4. Hermitian/symmetry residual intervals;
5. Rayleigh quotient interval evaluation;
6. negative-direction certificate verdicts;
7. JSON certificate output.

It uses placeholder interval entries.

It does not yet compute true \(T[\phi_j*\phi_i^*]\) entries.

---

# 6. What remains

Still needed:

1. complex interval arithmetic;
2. true basis function representation;
3. certified convolution evaluation;
4. finite prime-sum evaluation;
5. certified archimedean quadrature;
6. \(T\)-star source validation;
7. true arithmetic matrix construction.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove a complete arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

INTERVAL_MATRIX_IMPLEMENTATION_COMPLETE

REAL_INTERVAL_CLASS_IMPLEMENTED

INTERVAL_MATRIX_CLASS_IMPLEMENTED

HERMITIAN_RESIDUAL_INTERVAL_IMPLEMENTED

RAYLEIGH_INTERVAL_IMPLEMENTED

NEGATIVE_DIRECTION_CERTIFICATE_LOGIC_IMPLEMENTED

PLACEHOLDER_ENTRIES_ONLY

TRUE_ARITHMETIC_ENTRIES_NOT_YET_COMPUTED

ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_COMPLETE

