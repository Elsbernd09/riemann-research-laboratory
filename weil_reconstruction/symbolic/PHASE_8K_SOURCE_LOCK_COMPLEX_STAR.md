# Phase 8K — Source-Lock Complex Star Convention

## Purpose

Phase 8J distinguished two operations:

\[
f^*(x)=x^{-1}f(1/x)
\]

and

\[
f^\dagger(x)=x^{-1}\overline{f(1/x)}.
\]

Phase 8K source-locks the convention needed for Bombieri's positivity theorem.

This is not a proof of RH.

This is not a new Weil criterion.

This is a source-grounded convention-lock phase.

---

# 1. Source-grounded observation

Bombieri Section 3 says that the test function \(f\) is the multiplicative convolution of a function \(g\) and its transpose conjugate \(g^*\).

The source then records

\[
f(s)=g(s)g(1-s)
\]

in its notation.

In the proof under RH, Bombieri uses

\[
1-\rho=\overline{\rho}
\]

and obtains a nonnegative expression

\[
g(\rho)g(1-\rho)=|g(\rho)|^2.
\]

Therefore, in the positivity context, the star operation must be understood as a transpose-conjugate/Hermitian operation, not merely as the non-conjugated algebraic involution.

---

# 2. Two star conventions

## Algebraic star

The algebraic involution from the explicit formula is

\[
f^*(x)=x^{-1}f(1/x).
\]

Under the Mellin transform convention,

\[
f^*(s)=f(1-s).
\]

This is useful for explicit formula symmetry.

## Hermitian transpose-conjugate star

For complex-valued positivity, the relevant adjoint convention is

\[
g^\dagger(x)=x^{-1}\overline{g(1/x)}.
\]

Under the Mellin transform,

\[
g^\dagger(s)=\overline{g(1-\overline{s})}.
\]

If RH holds and

\[
1-\rho=\overline{\rho},
\]

then

\[
g^\dagger(\rho)
=
\overline{g(\rho)}.
\]

Thus the product becomes

\[
g(\rho)g^\dagger(\rho)=|g(\rho)|^2.
\]

---

# 3. Source-lock decision

The repository now distinguishes:

## Explicit-formula algebraic involution

\[
f^*_{\mathrm{alg}}(x)=x^{-1}f(1/x).
\]

Status: LOCKED.

## Positivity adjoint / transpose conjugate

\[
g^*_{\mathrm{pos}}(x)=x^{-1}\overline{g(1/x)}.
\]

Status: LOCKED for the positivity mechanism.

## Warning

The same star symbol may appear in source notation for related but context-sensitive operations.

The repository must disambiguate internally using:

\[
*_{\mathrm{alg}}
\]

and

\[
*_{\mathrm{pos}}.
\]

---

# 4. Corrected Bombieri product identity

For positivity work, write

\[
F=g*g^*_{\mathrm{pos}}.
\]

Then the Mellin transform has the Hermitian form

\[
F(s)=g(s)\overline{g(1-\overline{s})}.
\]

At a zero \(\rho\), this is

\[
F(\rho)=g(\rho)\overline{g(1-\overline{\rho})}.
\]

Under RH,

\[
1-\overline{\rho}=\rho,
\]

so

\[
F(\rho)=g(\rho)\overline{g(\rho)}=|g(\rho)|^2.
\]

This is the positivity mechanism.

---

# 5. Repair to previous notation

Previous phases recorded the algebraic identity

\[
(f*f^*)(s)=f(s)f(1-s).
\]

That identity remains valid for the non-conjugated algebraic star.

But for complex-valued positivity, the repository must use the Hermitian form

\[
(g*g^*_{\mathrm{pos}})(s)
=
g(s)\overline{g(1-\overline{s})}.
\]

Thus:

- algebraic symbolic identities remain valid;
- positivity interpretations must use the transpose-conjugate convention.

---

# 6. Implementation status

Symbolic algebra with both conventions is now allowed.

Finite-rank Weil matrix implementation is still blocked because Bombieri's finite truncation model, matrix entries, and eigenvalue construction remain unlocked.

However, future symbolic positivity notes may now use the source-locked Hermitian convention.

---

# 7. Boundary

No RH proof.

No new Weil criterion.

No novelty claim.

No finite-rank Weil matrix yet.

