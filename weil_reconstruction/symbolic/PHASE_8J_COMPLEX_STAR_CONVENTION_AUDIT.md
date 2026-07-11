# Phase 8J — Complex Star Convention Audit

## Purpose

Phase 8I recorded the algebraic identity

\[
f^*(s)=f(1-s)
\]

under the source-extracted involution

\[
f^*(x)=x^{-1}f(1/x).
\]

However, Bombieri's positivity statements involve complex-valued test functions.

For complex-valued functions, there is a major convention risk:

\[
f^*(x)=x^{-1}f(1/x)
\]

and

\[
f^\dagger(x)=x^{-1}\overline{f(1/x)}
\]

are different operations.

This phase audits that distinction.

This is not a proof of RH.

This is not a new Weil criterion.

This phase blocks finite-rank positivity code until the source convention is fully locked.

---

# 1. Algebraic star

The algebraic star operation recorded from the extracted formula is

\[
f^*(x)=x^{-1}f(1/x).
\]

Under the Mellin transform convention

\[
f(s)=\int_0^\infty f(x)x^{s-1}\,dx,
\]

this gives

\[
f^*(s)=f(1-s).
\]

This identity is algebraic.

It does not by itself create Hermitian positivity for complex functions.

---

# 2. Hermitian adjoint candidate

For complex-valued positivity, the natural Hermitian candidate is

\[
f^\dagger(x)=x^{-1}\overline{f(1/x)}.
\]

Under the same Mellin convention,

\[
f^\dagger(s)=\overline{f(1-\overline{s})}.
\]

In particular, on RH where

\[
1-\rho=\overline{\rho},
\]

one obtains

\[
f^\dagger(\rho)=\overline{f(\rho)}.
\]

Then products become

\[
f(\rho)f^\dagger(\rho)=|f(\rho)|^2.
\]

This is the Hermitian mechanism behind positivity.

---

# 3. Convention danger

The expressions

\[
g(\rho)g(1-\rho)
\]

and

\[
g(\rho)\overline{g(\rho)}
\]

coincide under RH only if the test-function convention connects

\[
g(1-\rho)
\]

with

\[
\overline{g(\rho)}.
\]

That connection depends on source conventions.

Therefore, the project must not assume Hermitian positivity from the algebraic star alone.

---

# 4. Source-lock requirement

Before any positivity computation, the repository must source-lock:

1. whether Bombieri's \(g^*\) includes complex conjugation;
2. whether \(f^*\) in \(T[f]=T[f^*]\) is the same operation as the positivity adjoint;
3. whether convolution \(f*f^*\) is algebraic, Hermitian, or context-dependent;
4. how complex-valued test functions are paired;
5. which formula yields the nonnegative sum under RH.

---

# 5. Current status

## LOCKED

Algebraic identity:

\[
f^*(x)=x^{-1}f(1/x)
\Rightarrow
f^*(s)=f(1-s).
\]

Multiplicative convolution identity:

\[
(f*g)(s)=f(s)g(s).
\]

## PARTIAL

Bombieri theorem statement involving

\[
g(\rho)g(1-\rho).
\]

## UNLOCKED

Hermitian positivity convention for complex-valued test functions.

Exact role of complex conjugation in Bombieri's \(g^*\).

Exact role of complex conjugation in Bombieri's \(f*f^*\).

Finite-rank positivity implementation.

---

# 6. Consequence for future phases

No finite-rank Weil positivity code may be written yet.

No matrix entries may be called Hermitian Weil entries yet.

No eigenvalue computation may be described as a classical Weil truncation yet.

The next phase must extract the relevant source lines around complex-valued functions, transpose conjugation, and the \(g^*\) convention.

---

# 7. Boundary

No RH proof.

No new Weil criterion.

No novelty claim.

This is a convention-safety audit.

